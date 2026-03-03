# 🚀 QUICK REFERENCE - Master Directive

**What is this?** The operating system for your autonomous AI agency. Read this if you need quick answers.

---

## 📋 Files You Need to Know

| File | What It Does | When to Read |
|------|-------------|-------------|
| `MEMORY.md` | Strategic knowledge + decisions | Every session start |
| `PROJECT_TRACKER.md` | Live status of all projects | When you need to know what's happening |
| `SYSTEM-DIRECTIVE.md` | How the agency operates | When you need to understand the rules |
| `SESSION_SUMMARIES/YYYY-MM-DD-SESSION-SUMMARY.md` | What happened that day | Before starting a new session |
| `memory/YYYY-MM-DD.md` | Daily work log | End of each session |
| `agents/{agent}/SOUL.md` | Agent's identity + role | When spawning an agent |
| `PROJECT_TRACKER.md` | All 5 active projects | Every 24h (updated by Aria) |

---

## ⏰ Daily Routine (Copy This)

### Morning (09:00 UTC):
```
1. Read MEMORY.md (2 min)
2. Read PROJECT_TRACKER.md (2 min)
3. Check blockers section
4. Know what's happening
```

### When Assigning Task:
```
1. Load agent's SOUL.md
2. Load relevant memory
3. Assign task with full context
4. Specify what memory to update
```

### When Task Completes:
```
1. Verify memory was updated
2. Verify git commit made
3. Verify PROJECT_TRACKER.md updated
4. Mark as complete
```

### End of Session (Before /new or /reset):
```
1. git add -A && git commit && git push
2. Create SESSION_SUMMARIES/YYYY-MM-DD-SESSION-SUMMARY.md
3. Update MEMORY.md
4. Create memory/YYYY-MM-DD.md
5. ./pre-reset-checklist.sh
6. THEN /new or /reset
```

---

## 🎯 The 7 Rules (Never Break These)

1. **Load memory first** — Every task starts with memory load
2. **Save memory last** — Every task ends with git commit
3. **Identity lock** — Agents don't change their own SOUL.md
4. **PROJECT_TRACKER is truth** — One source of truth for projects
5. **Aria coordinates** — She owns daily sync
6. **Git is permanent** — All changes committed
7. **Sessions are documented** — Summaries before /new

---

## 🚨 If You Forget Something

**Q: "Did we already decide this?"**  
→ Search `MEMORY.md` for the decision

**Q: "What's the project status?"**  
→ Read `PROJECT_TRACKER.md`

**Q: "What did we do yesterday?"**  
→ Read `memory/YYYY-MM-DD.md` from yesterday

**Q: "What happened in session X?"**  
→ Read `SESSION_SUMMARIES/YYYY-MM-DD-SESSION-SUMMARY.md`

**Q: "Did agent X fail before?"**  
→ Read `agents/X/self-improving/corrections.md`

---

## 📊 The 5 Active Projects (Right Now)

1. **Trading Lab** (Richie 💰) — 12 bots running, eval March 7/23
2. **LinkedIn Campaign** (Sonic 🎯) — Awaiting your visuals (headshot, banner, logo)
3. **n8n HR/Payroll** (Account Manager) — Awaiting your approval + employee data
4. **Infrastructure** (Arjuna ⚡) — Complete
5. **Free Models Research** (Bruce 🔒) — Complete

**Full details:** Read `PROJECT_TRACKER.md`

---

## 🔴 Current Blockers (Waiting on You)

1. LinkedIn visuals not sourced (blocks campaign launch)
2. n8n workflow approval needed (blocks payroll automation)
3. Employee data needed (blocks payroll setup)

**When you handle these → pipeline moves forward**

---

## 🧠 How We Never Forget

**8 Layers:**
1. Git (permanent code archive)
2. MEMORY.md (strategic knowledge)
3. PROJECT_TRACKER.md (live status board)
4. memory/YYYY-MM-DD.md (daily work logs)
5. SESSION_SUMMARIES/ (chat history before resets)
6. Agent self-improving/ (per-agent learning)
7. Aria's stand-ups (daily team sync logs)
8. pre-reset-checklist.sh (enforces documentation)

**Result:** Nothing gets lost, nothing gets forgotten.

---

## 🎯 Agency KPIs (What We're Measuring)

| Metric | Target | Current |
|--------|--------|---------|
| Trading bot win rate | >50% | ETA-001: 55.6% |
| LinkedIn pipeline value | €50K+ by Month 1 | In progress |
| n8n automation efficiency | TBD | Ready to activate |
| Memory persistence | 100% | 100% (via 8 layers) |
| Agent availability | 24/7 | ✅ 24/7 |

---

## 🚀 Next 3 Actions (For You)

1. **Source LinkedIn visuals** (2 hours)
   - Headshot (professional photo)
   - Banner (1200x627 or custom)
   - Company logo

2. **Approve n8n workflow priority** (30 min)
   - Which HR process first? (payroll recommended)
   - Provide employee data

3. **Monitor trading bots** (passive)
   - March 7: 1-hour bot evaluation
   - March 23: 4-hour bot evaluation

---

## 📞 How to Communicate

**To Arjuna:** Direct message (I read all context first)  
**To Team:** `@aria` for coordination  
**To Individual Agent:** `@{agent-name}` (e.g., `@richie`)  

**Format:** Just tell me what you want, I'll read memory and execute.

---

## 🔒 What's Protected

- Agent identities (only Arjuna updates)
- Git history (permanent record)
- MEMORY.md (decisions are final)
- PROJECT_TRACKER.md (truth source)

---

## ✅ When You See This

✅ **Memory loaded** — Agent has full context  
✅ **Task complete** — Memory was persisted  
✅ **Git synced** — Changes are permanent  
✅ **Directive active** — System is operating correctly  

---

**Read full details:** `SYSTEM-DIRECTIVE.md`

**Questions?** They're probably answered in `MEMORY.md` or `PROJECT_TRACKER.md`.

---

*Last updated: 2026-03-03*
