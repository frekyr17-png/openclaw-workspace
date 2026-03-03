#!/bin/bash
# Weekly Team Learning Digest
# Runs every Sunday at 00:00 UTC

WEEK=$(date +%Y-W%V)
DIGEST_FILE="agents/shared-learnings/weekly-digests/$WEEK.md"

cat > "$DIGEST_FILE" << 'EOF'
# Team Learning Digest - Week $(date +%Y-W%V)

**Generated:** $(date +"%Y-%m-%d %H:%M UTC")

## This Week's Insights

### Arjuna (Head of Operations)
Check daily-reflections/ for key lessons

### Aria (Project Manager)
Check daily-reflections/ for key lessons

### Richie (Trading Specialist)
Check daily-reflections/ for key lessons

### Mr Bean (Security Guardian)
Check daily-reflections/ for key lessons

## Promoted Patterns

Review each agent's memory.md for new HOT tier entries.

## Cross-Pollination Opportunities

[To be filled by agents during weekly review]

## Action Items

- [ ] Review team insights
- [ ] Apply relevant patterns to your domain
- [ ] Update shared-learnings/patterns/ if you have proven wins
EOF

echo "✅ Weekly digest created: $DIGEST_FILE"
