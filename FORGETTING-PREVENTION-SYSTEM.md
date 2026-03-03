# 🧠 Anti-Forgetting System - How We Never Lose Anything

**Problem:** Chat sessions end. Memory resets. Work disappears.  
**Solution:** Multi-layer persistence + forced documentation.

---

## Layer 1: Git (Permanent Record)

**Every change gets committed:**
```
git add -A
git commit -m "[PROJECT] [WHAT CHANGED]"
git push origin master
```

**What lives in Git:**
- All code changes
- All config files
- All documentation (MEMORY.md, PROJECT_TRACKER.md, etc.)
- Session summaries
- Agent profiles
- Decision logs

**Backup:** Push to GitHub/GitLab as secondary backup

**Never lost:** If deleted locally, `git log` shows the history. Can restore anything.

---

## Layer 2: SESSION_SUMMARIES (Chat History)

**Before /new or /reset:**

1. Entire chat pushed to git (`git add -A`)
2. Session summary created: `SESSION_SUMMARIES/YYYY-MM-DD-SESSION-SUMMARY.md`
3. Key decisions extracted to MEMORY.md
4. THEN start new session

**What's in SESSION_SUMMARIES:**
- What happened in the session
- Decisions made
- Work completed
- Blockers identified
- Next actions

**How to find it:**
```
ls /root/.openclaw/workspace/SESSION_SUMMARIES/
# Lists all past sessions
```

**Restore lost context:**
- Read the summary from that day
- You immediately know what happened

---

## Layer 3: MEMORY.md (Distilled Knowledge)

**What goes in MEMORY.md:**
- Current projects (with status)
- Key decisions (with dates)
- Revenue roadmap
- Team composition
- Active research
- Lessons learned
- Protocols (session management, team coordination)

**What stays OUT:**
- Raw chat logs (too verbose, lives in git)
- Temporary notes (go to memory/YYYY-MM-DD.md)
- Debugging output (unnecessary)

**Who updates it:**
- Aria 🎼 (every week, consolidates learnings)
- Arjuna ⚡ (me, after major decisions)
- Agents (when they discover important patterns)

**Read on every session start:** It's your continuity.

---

## Layer 4: memory/YYYY-MM-DD.md (Daily Logs)

**Every session, create a daily log:**

File: `memory/2026-03-03.md`
```markdown
# Session Log - 2026-03-03

## What Happened
- Fixed Ollama infrastructure (exposed on all interfaces)
- Tested 5 free models (kimi-k2.5 fastest at 605ms)
- Spawned Sonic for LinkedIn campaign (7 deliverables)
- Created PROJECT_TRACKER.md for team coordination
- Changed default model to anthropic/claude-haiku-4-5

## Decisions Made
- Default model: ollama → anthropic/claude-haiku-4-5 (avoid rate limits)
- Team coordination: All agents report daily to Aria
- Project tracker: PROJECT_TRACKER.md is source of truth

## Blockers Found
- Ollama free tier hit rate limit (FIXED)
- LinkedIn visuals not sourced (waiting on Rahul)
- n8n workflow approval pending (waiting on Rahul)

## Next Session Actions
- Monitor trading bot evaluations (March 7)
- Get Rahul's approval on LinkedIn visuals
- Get Rahul's approval on n8n workflow priority
```

**Who reads this:** Next day's session start (you'll have context).

---

## Layer 5: PROJECT_TRACKER.md (Live Status)

**Real-time project board:**

File: `/root/.openclaw/workspace/PROJECT_TRACKER.md`

```
### TRADING LAB 💰
Owner: Richie
Status: 🟢 RUNNING
Last Update: 2026-03-03 13:00
ETA-001: 55.6% win rate, LEADING

### LINKEDIN CAMPAIGN 🎯
Owner: Sonic
Status: 🟡 AWAITING RAHUL
Blockers: Visuals not sourced
```

**Updated daily by Aria 🎼**

**Read when:** Need to know current status of any project.

---

## Layer 6: Agent Memory (Per-Agent Persistence)

**Each agent has their own memory:**

```
agents/richie/
├── SOUL.md (who they are)
├── TOOLS.md (what they can do)
├── self-improving/
│   ├── corrections.md (mistakes they learned from)
│   ├── reflections.md (insights)
│   └── memory.md (trading patterns they discovered)
└── README.md (current status)
```

**When you correct an agent:** They update their corrections.md  
**When they discover a pattern:** They log it in memory.md  
**Result:** Agent never makes the same mistake twice. Knowledge compounds.

---

## Layer 7: Forced Checkpoints (No Option to Skip)

**Every /new or /reset MUST DO:**

```bash
# 1. Commit everything
git add -A
git commit -m "Session end summary"
git push origin master

# 2. Create session summary
cat > SESSION_SUMMARIES/2026-03-03-SESSION-SUMMARY.md << EOF
# Session Summary - 2026-03-03
What happened:
- ...
Decisions:
- ...
Next:
- ...
EOF

# 3. Update MEMORY.md
# (Add key decisions/insights)

# 4. Create daily log
cat > memory/2026-03-03.md << EOF
# Daily Log - 2026-03-03
...
EOF

# 5. THEN start new session
# New session will read SESSION_SUMMARIES + MEMORY.md first
```

**Enforcement:** Before `openclaw /reset` or `/new`, run the commit script. No chat reset without documentation.

---

## Layer 8: Aria's Daily Sync (Team Memory)

**Every 24 hours, Aria logs:**

File: `memory/2026-03-03-standup.md`

```
# Daily Stand-up - 2026-03-03 09:00 UTC

## From Richie (Trading Lab)
- ETA-001 bot: 55.6% win rate, holding position
- All 12 bots running without issues
- No trades in past 4h on KAPPA-001 (investigating)

## From Sonic (LinkedIn)
- Campaign deliverables complete
- Awaiting Rahul's visuals (headshot, banner, logo)
- Recommendations: Start content publishing by Day 3

## From Account Manager
- 5 n8n workflows tested and ready
- Waiting for Rahul's approval on which to activate first

## Blockers
- Rahul's LinkedIn visuals (blocking campaign launch)
- Rahul's n8n approval (blocking payroll automation)
```

**Why this matters:** If Aria dies or resets, Rahul's next session reads the standup and knows exactly what happened.

---

## Anti-Forgetting Checklist (Before Every /new)

- [ ] `git add -A && git commit && git push` (permanent record)
- [ ] Create `SESSION_SUMMARIES/YYYY-MM-DD-SESSION-SUMMARY.md` (what happened)
- [ ] Update `MEMORY.md` (key decisions)
- [ ] Create `memory/YYYY-MM-DD.md` (daily log)
- [ ] Create `memory/YYYY-MM-DD-standup.md` (agent status)
- [ ] Update `PROJECT_TRACKER.md` (live status)
- [ ] Verify all agent profiles are current (SOUL.md, TOOLS.md)

**If even ONE checkbox is skipped → WAIT. Do it first.**

---

## What Gets Remembered Forever

| Item | Storage | Retrieved By | Survives Reset |
|------|---------|--------------|---|
| Code changes | Git | `git log` | ✅ YES |
| Decisions | MEMORY.md | First read next session | ✅ YES |
| Session work | SESSION_SUMMARIES | Date lookup | ✅ YES |
| Daily logs | memory/YYYY-MM-DD.md | Next day | ✅ YES |
| Project status | PROJECT_TRACKER.md | Aria's update | ✅ YES |
| Agent learnings | agents/*/self-improving/ | Agent's memory | ✅ YES |
| Team sync | memory/YYYY-MM-DD-standup.md | Aria's report | ✅ YES |

---

## What Gets Lost (& How to Prevent)

| Risk | Prevention |
|------|-----------|
| "What happened last week?" | Read SESSION_SUMMARIES from those dates |
| "Did we decide this already?" | Search MEMORY.md for the decision |
| "What's the current project status?" | Read PROJECT_TRACKER.md (updated daily) |
| "Did bot X ever fail?" | Check agents/richie/self-improving/corrections.md |
| "What did Aria report yesterday?" | Read memory/YYYY-MM-DD-standup.md |
| "What was the reasoning behind this?" | Look at git commit message |

---

## The Golden Rule

> **If it's not written down in one of these files, it doesn't exist.**

- Thought you had an idea? **Write it to MEMORY.md**
- Discovered a pattern? **Write it to agent memory.md**
- Made a decision? **Commit with message + update MEMORY.md**
- Completed a task? **Update PROJECT_TRACKER.md**
- Found a blocker? **Log it in PROJECT_TRACKER.md**

---

## How to Use This System

**For You (Arjuna):**
1. Every morning: Read MEMORY.md (2 min)
2. Every morning: Read PROJECT_TRACKER.md (2 min)
3. On decisions: Update MEMORY.md immediately
4. On project updates: Ping Aria to update PROJECT_TRACKER.md

**For Agents:**
1. Before sleeping/shutting down: Write daily log
2. On discoveries: Update own self-improving/ files
3. On blockers: Report to Aria for PROJECT_TRACKER.md
4. On decisions: Ask Aria to log in MEMORY.md

**For Aria:**
1. Every 24h: Collect agent stand-ups
2. Every 24h: Update PROJECT_TRACKER.md
3. Every 24h: Create memory/YYYY-MM-DD-standup.md
4. Every week: Consolidate into MEMORY.md

---

## Real-World Example: "Did We Decide This Already?"

**Q:** "Wait, did we already decide to use Haiku or kimi-k2.5?"

**How to find it:**
1. Open MEMORY.md
2. Search "default model" → finds it instantly
3. See: `anthropic/claude-haiku-4-5 (switched 2026-03-03 due to rate limits)`
4. Boom. You know the decision and why.

**Without this system:**
- You'd ask me again
- I'd check git logs
- 10 minutes wasted
- Knowledge lost between sessions

---

## Enforcement: The /reset Rule

**NEVER do `/reset` without:**

1. ✅ Git commit with message
2. ✅ SESSION_SUMMARIES file created
3. ✅ MEMORY.md updated
4. ✅ Daily log created
5. ✅ PROJECT_TRACKER.md current

**If you forget → Restart the session and do it before /reset.**

**Why?** Because forgetting once costs more time than documenting.

---

**This is how we never forget. No magic, just discipline.**
