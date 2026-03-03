# Project Management Hub Skill

**Purpose:** Central coordination for all agents to track work, prevent duplicate effort, and keep Arjuna informed.

**For Agents:** Use this to stay synced with the team.  
**For Rahul:** See PROJECT_TRACKER.md for the single source of truth.

---

## Quick Commands

```bash
# Update your status (run this daily)
pmt status richie "ETA-001 bot: 55.6% win rate, running 24/7"

# Log a blocker
pmt blocker "LinkedIn visuals not sourced - waiting on Rahul"

# Check project health
pmt health  # Shows all active projects, blockers, next actions

# Report to Arjuna
pmt report  # Generates daily digest for Arjuna
```

---

## Files Used

- **PROJECT_TRACKER.md** — Master task list (single source of truth)
- **memory/YYYY-MM-DD-standup.md** — Daily agent reports
- **memory/YYYY-MM-DD.md** — Session work logs

---

## For Each Agent

**Every 24 hours, report to Aria:**

1. What you completed yesterday
2. What you're working on today
3. Any blockers or decisions needed
4. Recommendations for Rahul

**Format:**
```
@aria status

Yesterday: Completed X, Y, Z
Today: Working on A, B, C
Blockers: None / List them
Recommendations: Rahul should do X by date
```

---

## For Aria (Project Manager)

**Daily duties:**
1. Collect stand-ups from all agents
2. Update PROJECT_TRACKER.md
3. Flag blockers to Arjuna
4. Report health to Rahul (if needed)

---

## Why This Matters

**Without tracking:**
- Work gets duplicated
- Decisions are forgotten
- Agents work in isolation
- Rahul can't see progress

**With tracking:**
- All work visible
- Decisions logged
- Team coordination
- One page status = clarity

---

## File Locations

```
/root/.openclaw/workspace/
├── PROJECT_TRACKER.md          ← MASTER TRACKER (read daily)
├── memory/
│   ├── YYYY-MM-DD-standup.md   ← Agent daily reports
│   └── YYYY-MM-DD.md           ← Session logs
└── skills/project-management-hub/
    └── SKILL.md                ← This file
```

---

## Integration with Memory

**MEMORY.md** = Long-term strategic notes (updated weekly)  
**PROJECT_TRACKER.md** = Live project status (updated daily)  
**memory/YYYY-MM-DD.md** = Session work logs (updated per session)

All three work together. None replace the other.

---

**The goal: No agent forgets what they're doing. No duplicate work. Rahul always knows status.**
