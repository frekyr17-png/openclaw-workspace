#!/bin/bash
# Check orchestration progress and self-heal stuck tasks

WORKDIR="${1:-}"
if [ -z "$WORKDIR" ] || [ ! -d "$WORKDIR" ]; then
    echo "Usage: $0 WORKDIR"
    echo "Example: $0 /tmp/orchestrator-123456"
    exit 1
fi

SOCKET="$WORKDIR/orchestrator.sock"
MANIFEST="$WORKDIR/manifest.json"
STALL_THRESHOLD_MINS=20

if [ ! -f "$MANIFEST" ]; then
    echo "❌ Manifest not found: $MANIFEST"
    exit 1
fi

echo "🔍 Checking orchestration progress..."
echo "📁 Workdir: $WORKDIR"
echo "📄 Manifest: $MANIFEST"
echo ""

check_session() {
    local session="$1"
    local task_id="$2"
    
    # Check if session exists
    if ! tmux -S "$SOCKET" has-session -t "$session" 2>/dev/null; then
        echo "DEAD:$task_id"
        return 3
    fi
    
    # Capture recent output
    local output=$(tmux -S "$SOCKET" capture-pane -p -t "$session" -S -50 2>/dev/null)
    
    # Check for completion indicators
    if echo "$output" | grep -qE "(All tests passed|Successfully pushed|❯ $|% $)"; then
        echo "DONE:$task_id"
        return 0
    fi
    
    # Check for errors
    if echo "$output" | grep -qiE "(error:|failed:|FATAL|panic|Command.*failed)"; then
        echo "ERROR:$task_id"
        return 1
    fi
    
    # Check for stall (prompt waiting for input)
    if echo "$output" | grep -qE "(\? |Continue\?|y/n|Press any key|\[Y/n\])"; then
        echo "STUCK:$task_id:waiting_for_input"
        return 2
    fi
    
    echo "RUNNING:$task_id"
    return 0
}

# Get list of sessions
sessions=$(tmux -S "$SOCKET" list-sessions -F "#{session_name}" 2>/dev/null)

if [ -z "$sessions" ]; then
    echo "⚠️  No active tmux sessions found"
    echo "   Socket: $SOCKET"
    exit 0
fi

echo "Active sessions:"
for session in $sessions; do
    status=$(check_session "$session" "$session")
    state=$(echo "$status" | cut -d: -f1)
    task=$(echo "$status" | cut -d: -f2)
    
    case "$state" in
        DONE)
            echo "  ✅ $session: Complete"
            ;;
        RUNNING)
            echo "  🔄 $session: Running"
            ;;
        ERROR)
            echo "  ❌ $session: Error detected"
            ;;
        STUCK)
            echo "  ⚠️  $session: Stuck (waiting for input)"
            ;;
        DEAD)
            echo "  💀 $session: Session dead"
            ;;
    esac
done

echo ""
echo "💡 Use 'tmux -S $SOCKET attach -t SESSION_NAME' to inspect"
