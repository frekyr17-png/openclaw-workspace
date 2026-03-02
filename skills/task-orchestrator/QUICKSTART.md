# Task Orchestrator - Quick Start

## Overview

Orchestrate multiple parallel tasks using tmux + Codex with dependency analysis and self-healing.

## Setup

### 1. Create Working Directory

```bash
WORKDIR="${TMPDIR:-/tmp}/orchestrator-$(date +%s)"
mkdir -p "$WORKDIR"
echo "Workdir: $WORKDIR"
```

### 2. Clone Repository

```bash
cd "$WORKDIR"
git clone https://github.com/OWNER/REPO.git repo
cd repo
```

### 3. Create Manifest

```bash
# Using helper script
python3 ~/.openclaw/workspace/skills/task-orchestrator/scripts/create-manifest.py \
  "my-project" "owner/repo" "$WORKDIR"

# Or manually create manifest.json in $WORKDIR
```

### 4. Edit Manifest

Add tasks with dependencies:

```json
{
  "project": "my-project",
  "phases": [
    {
      "name": "Phase 1",
      "tasks": [
        {
          "id": "t1",
          "title": "Update bot ALPHA",
          "files": ["alpha.py"],
          "dependsOn": []
        },
        {
          "id": "t2",
          "title": "Update bot BETA",
          "files": ["beta.py"],
          "dependsOn": []
        }
      ]
    }
  ]
}
```

## Execution

### Launch Tasks

```bash
SOCKET="$WORKDIR/orchestrator.sock"

# Create worktrees
cd "$WORKDIR/repo"
git worktree add -b task/t1 "$WORKDIR/task-t1" main
git worktree add -b task/t2 "$WORKDIR/task-t2" main

# Launch tmux sessions
tmux -S "$SOCKET" new-session -d -s "task-t1"
tmux -S "$SOCKET" send-keys -t "task-t1" \
  "cd $WORKDIR/task-t1 && codex --yolo 'Update bot ALPHA. Run tests, commit, push.'" Enter

tmux -S "$SOCKET" new-session -d -s "task-t2"
tmux -S "$SOCKET" send-keys -t "task-t2" \
  "cd $WORKDIR/task-t2 && codex --yolo 'Update bot BETA. Run tests, commit, push.'" Enter
```

### Monitor Progress

```bash
# Check all sessions
~/.openclaw/workspace/skills/task-orchestrator/scripts/check-progress.sh "$WORKDIR"

# Attach to specific session
tmux -S "$SOCKET" attach -t "task-t1"
# Detach: Ctrl+B, D
```

## Best Practices

1. **Use GPT-5.2-codex-high** for complex work
2. **Clear prompts** - Include expected outcome, test instructions
3. **Atomic commits** - Tell Codex to commit after each logical change
4. **Push early** - Push to remote branch so progress isn't lost
5. **Phase gates** - Don't start Phase N+1 until Phase N is 100% complete

## Dependency Rules

- **Same file = sequential** — Tasks touching same file must run in order
- **Different files = parallel** — Independent tasks can run simultaneously
- **Explicit depends = wait** — `dependsOn` array enforces ordering

## Cleanup

```bash
# Kill all sessions
tmux -S "$SOCKET" kill-server

# Remove worktrees
cd "$WORKDIR/repo"
git worktree remove "$WORKDIR/task-t1" --force
git worktree remove "$WORKDIR/task-t2" --force

# Optional: Remove workdir
rm -rf "$WORKDIR"
```

## For Aria

This skill is perfect for:
- Updating 12 trading bots in parallel
- Multi-file refactoring projects
- Complex builds with dependency chains
- Any project where tasks can be split and parallelized

See SKILL.md for full documentation.
