# Learning Loop - Quick Start

**Status:** Phase 1 Complete ✅  
**For:** All agents (Arjuna, Aria, Richie, Mr Bean)

## What Is This?

A self-learning system where every agent:
1. **Learns from their work** (corrections, wins, mistakes)
2. **Shares insights with the team** (proven patterns)
3. **Compounds knowledge over time** (no forgetting)

## Your Learning Files

### Personal Memory (always check these)
```
~/agents/{yourname}/self-improving/
├── memory.md           ← HOT: Your core rules (≤100 lines)
├── corrections.md      ← Last 50 corrections from Rahul
├── reflections.md      ← Your daily self-reflections
└── domains/            ← Specialized knowledge
```

### Team Knowledge (check weekly)
```
~/agents/shared-learnings/
├── patterns/           ← Proven patterns from other agents
│   ├── trading.md      ← Richie's wins
│   ├── security.md     ← Mr Bean's threats
│   ├── project-mgmt.md ← Aria's tactics
│   └── operations.md   ← Arjuna's execution
└── weekly-digests/     ← Weekly team summaries
```

## Daily Routine (Built into Heartbeats)

**Once per day (rotate through your heartbeat checks):**

1. **Review today's work:**
   - Check `memory/YYYY-MM-DD.md` for what you did
   - Any mistakes? → Log to `reflections.md`
   - Any wins? → Log to `reflections.md`
   
2. **Log reflections (format):**
   ```
   CONTEXT: [what you were doing]
   REFLECTION: [what you noticed]
   LESSON: [what to do differently/keep doing]
   ```

3. **Check for patterns:**
   - Same lesson 3 times? → Promote to `memory.md`
   - Example: If you keep learning "check disk space before installs"
     → Add to memory.md after 3rd time

4. **Scan team insights (30 seconds):**
   - Quick read `shared-learnings/patterns/` for new entries
   - If relevant to you → apply it

## Weekly Routine (Sundays)

**Automated:**
- Weekly digest generated in `shared-learnings/weekly-digests/`
- All agents' top insights compiled

**Your job:**
1. Read the digest (5 min)
2. Pick 1-2 insights from other agents to try
3. If you have a proven pattern (used 3+ times successfully):
   - Add to `shared-learnings/patterns/{domain}.md`
   - Tag relevant agents: `[Arjuna] [Richie]`

## How to Log

### When Rahul corrects you:
```bash
echo "$(date +%Y-%m-%d): Rahul said: [correction]" >> corrections.md
echo "LESSON: [what to change]" >> corrections.md
```

### When you catch your own mistake:
```bash
cat >> reflections.md << EOF
CONTEXT: [what you were doing]
REFLECTION: Caught mistake before shipping - [what it was]
LESSON: [how to prevent next time]
EOF
```

### When something works really well:
```bash
cat >> reflections.md << EOF
CONTEXT: [what you were doing]
REFLECTION: This approach worked great - [what you did]
LESSON: Keep doing [pattern] for [situation]
EOF
```

## Promotion Rules

**Pattern becomes a rule after:**
1. ✅ Used successfully 3+ times
2. ✅ No contradicting feedback
3. ✅ Still relevant (not one-time context)

**Then:**
- Add to `memory.md` (HOT tier)
- Optionally share to `shared-learnings/patterns/`

## Example Learning Flow

**Day 1:**
- Richie tries "BTC trend-following in Asian hours"
- Works → logs to `reflections.md`

**Day 3:**
- Tries again → works again → 2nd reflection

**Day 7:**
- 3rd success → promotes to `memory.md`:
  ```
  ## Proven Patterns
  - BTC: Trend-following more reliable during Asian hours (12:00-20:00 UTC)
  ```

**Week 2:**
- Adds to `shared-learnings/patterns/trading.md`:
  ```
  [Richie] [Arjuna] BTC Asian hours edge: Trend strategies perform better 
  12:00-20:00 UTC vs US/EU hours. Confirmed 3+ weeks.
  ```

**Week 3:**
- Arjuna reads digest → adjusts trading cron timing
- Better results → pattern reinforced across team

## Memory Tiers Explained

| Tier | File | When to Use |
|------|------|-------------|
| HOT | memory.md | Always loaded, core rules (≤100 lines) |
| WARM | projects/*.md, domains/*.md | Load when context matches |
| COLD | archive/*.md | Old patterns, load on explicit query |

**Auto-promotion:** Pattern used 3x in 7 days → HOT  
**Auto-demotion:** Pattern unused 30 days → WARM, 90 days → COLD

## What NOT to Log

❌ One-time instructions ("do X now")  
❌ Context-specific ("in this file, change...")  
❌ Hypotheticals ("what if we...")  
❌ Rahul's personal info (keep private)  

✅ Repeated corrections  
✅ Proven patterns (3+ successes)  
✅ Mistakes you caught  
✅ Things that work really well  

## Quick Commands

**Check your memory size:**
```bash
wc -l self-improving/memory.md
```

**See last 10 reflections:**
```bash
tail -20 self-improving/reflections.md
```

**Check team insights:**
```bash
cat shared-learnings/patterns/*.md | grep "\[$(whoami)\]"
```

**Export your memory:**
```bash
tar -czf memory-backup-$(date +%Y%m%d).tar.gz self-improving/
```

## Success Metrics

You're doing it right when:
- ✅ You stop making the same mistake twice
- ✅ Your memory.md grows with proven patterns
- ✅ Team members use your insights
- ✅ Rahul corrects you less over time
- ✅ You catch mistakes before shipping

## Need Help?

- Read full docs: `~/agents/LEARNING-LOOP.md`
- Check skill docs: `~/.openclaw/workspace/skills/self-improving/SKILL.md`
- Ask Arjuna (he owns the learning loop)

---

**Last updated:** 2026-03-02
