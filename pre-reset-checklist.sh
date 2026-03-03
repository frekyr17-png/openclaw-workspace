#!/bin/bash

# PRE-RESET CHECKLIST - Run this BEFORE /new or /reset
# This ensures nothing gets lost

echo "🧠 PRE-RESET VERIFICATION CHECKLIST"
echo "===================================="
echo ""

WORKSPACE="/root/.openclaw/workspace"
TODAY=$(date +%Y-%m-%d)

# Check 1: Git status
echo "✓ Checking git status..."
cd "$WORKSPACE"
if git status --porcelain | grep -q .; then
    echo "❌ FAIL: Uncommitted changes found!"
    echo "   Run: git add -A && git commit -m 'message' && git push"
    exit 1
else
    echo "✅ PASS: All changes committed"
fi

# Check 2: SESSION_SUMMARIES
echo ""
echo "✓ Checking SESSION_SUMMARIES..."
if [ -f "$WORKSPACE/SESSION_SUMMARIES/${TODAY}-SESSION-SUMMARY.md" ]; then
    echo "✅ PASS: Session summary created"
else
    echo "❌ FAIL: SESSION_SUMMARIES/${TODAY}-SESSION-SUMMARY.md missing!"
    echo "   Create it with key decisions and blockers"
    exit 1
fi

# Check 3: MEMORY.md updated
echo ""
echo "✓ Checking MEMORY.md..."
if grep -q "$(date +%Y-%m-%d)" "$WORKSPACE/MEMORY.md"; then
    echo "✅ PASS: MEMORY.md updated with today's date"
else
    echo "⚠️  WARNING: MEMORY.md may not be updated with today's date"
    echo "   Consider updating with key insights"
fi

# Check 4: Daily log
echo ""
echo "✓ Checking daily log..."
if [ -f "$WORKSPACE/memory/${TODAY}.md" ]; then
    echo "✅ PASS: Daily log exists"
else
    echo "❌ FAIL: memory/${TODAY}.md missing!"
    echo "   Create it with: What happened, Decisions, Blockers, Next actions"
    exit 1
fi

# Check 5: PROJECT_TRACKER.md
echo ""
echo "✓ Checking PROJECT_TRACKER.md..."
if [ -f "$WORKSPACE/PROJECT_TRACKER.md" ]; then
    LAST_UPDATE=$(grep "Updated" "$WORKSPACE/PROJECT_TRACKER.md" | head -1)
    echo "✅ PASS: PROJECT_TRACKER.md exists ($LAST_UPDATE)"
else
    echo "❌ FAIL: PROJECT_TRACKER.md missing!"
    exit 1
fi

# Check 6: Aria's standup
echo ""
echo "✓ Checking Aria's daily standup..."
if [ -f "$WORKSPACE/memory/${TODAY}-standup.md" ]; then
    echo "✅ PASS: Daily standup logged"
else
    echo "⚠️  WARNING: memory/${TODAY}-standup.md missing"
    echo "   Aria should log agent status reports"
fi

# Check 7: Git remote synced
echo ""
echo "✓ Checking git remote..."
REMOTE_STATUS=$(git status -sb | head -1)
if [[ $REMOTE_STATUS == *"up to date"* ]]; then
    echo "✅ PASS: Git synced with remote"
else
    echo "⚠️  WARNING: $REMOTE_STATUS"
    echo "   Run: git push origin master"
fi

echo ""
echo "===================================="
echo "✅ ALL CHECKS PASSED"
echo ""
echo "You can now safely run: /new or /reset"
echo ""
echo "Next session will read:"
echo "  1. MEMORY.md (strategic context)"
echo "  2. memory/${TODAY}.md (daily log)"
echo "  3. SESSION_SUMMARIES/${TODAY}-SESSION-SUMMARY.md (what happened)"
echo "  4. PROJECT_TRACKER.md (current status)"
echo ""
