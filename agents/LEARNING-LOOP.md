# Team Learning Loop Architecture

**Owner:** Arjuna (Head of Operations)  
**Created:** 2026-03-02  
**Purpose:** Continuous self-improvement for all agents

## Vision

Every agent learns from their work, shares insights with the team, and compounds knowledge over time. No manual intervention required.

## Architecture

```
Individual Learning (per agent)
    ↓
Team Knowledge Base (shared)
    ↓
Cross-Pollination (insights → actions)
    ↓
Feedback Loop (results → learning)
```

## Individual Agent Structure

Each agent maintains their own learning memory:

```
~/agents/{name}/self-improving/
├── memory.md          # HOT: ≤100 lines, always loaded
├── index.md           # Topic index
├── corrections.md     # Last 50 corrections
├── reflections.md     # Self-reflection log
├── projects/          # Project-specific learnings
├── domains/           # Domain knowledge (trading, security, etc.)
└── archive/           # Cold storage

~/agents/{name}/daily-reflections/
└── YYYY-MM-DD.md      # Daily reflection outputs
```

## Team Knowledge Base

Shared learnings across all agents:

```
~/agents/shared-learnings/
├── README.md          # How to use shared knowledge
├── patterns/          # Proven patterns any agent can use
│   ├── trading.md     # Richie's winning strategies
│   ├── security.md    # Mr Bean's threat patterns
│   ├── project-mgmt.md # Aria's coordination tactics
│   └── operations.md  # Arjuna's execution patterns
├── decisions/         # Major decisions and rationale
└── weekly-digests/    # Weekly team learning summaries
    └── YYYY-WW.md
```

## Learning Triggers

### Immediate (as they happen)
- **Corrections from Rahul** → log to corrections.md
- **Mistakes caught** → self-reflection entry
- **Positive feedback** → pattern candidate
- **Repeated instruction** → track, promote after 3x

### Scheduled Reflection

**Daily (via heartbeat, 23:00 UTC):**
- Review today's work
- Log 3-5 key reflections
- Identify patterns worth sharing
- Update personal memory.md if needed

**Weekly (Sundays, 00:00 UTC via cron):**
- Deep reflection: What worked? What didn't?
- Promote strong patterns to HOT tier
- Archive unused patterns to COLD
- Contribute to team digest
- Cross-pollinate: Read other agents' weekly insights

**Monthly (1st of month, 01:00 UTC):**
- Memory compaction (merge similar rules)
- Archive old patterns
- Export full memory snapshot
- Team retrospective

## Cross-Agent Learning Flow

1. **Richie discovers:** "BTC trend-following works better in Asian hours"
2. **Richie logs:** `domains/trading.md` + contributes to `shared-learnings/patterns/trading.md`
3. **Weekly digest:** All agents see: "Richie: BTC Asian hours trend edge confirmed"
4. **Arjuna applies:** Adjusts trading lab cron timing
5. **Results feed back:** Better P&L → reinforces pattern → promotes to HOT

## Automation Setup

### Heartbeat Integration
Add to each agent's HEARTBEAT.md:

```markdown
## Self-Improvement Check (rotate, 1x per day)

- [ ] Review today's actions — any mistakes or wins?
- [ ] Log 1-3 reflections to reflections.md
- [ ] Check for repeated patterns (3x = candidate for memory.md)
- [ ] Read shared-learnings/patterns/ for new team insights
```

### Cron Jobs

**Daily Reflection (all agents):**
```bash
0 23 * * * /usr/local/bin/openclaw run --label arjuna-reflection "Read your work from memory/$(date +\%Y-\%m-\%d).md. Write 3-5 key reflections to agents/arjuna/daily-reflections/$(date +\%Y-\%m-\%d).md. Identify patterns worth sharing."
0 23 * * * /usr/local/bin/openclaw run --label aria-reflection ...
0 23 * * * /usr/local/bin/openclaw run --label richie-reflection ...
0 23 * * * /usr/local/bin/openclaw run --label mrbean-reflection ...
```

**Weekly Team Digest (Sundays):**
```bash
0 0 * * 0 /usr/local/bin/openclaw run --label team-digest "Aggregate all agents' weekly reflections. Create shared-learnings/weekly-digests/$(date +\%Y-W\%V).md with key insights, patterns, and cross-pollination opportunities."
```

**Monthly Compaction:**
```bash
0 1 1 * * /usr/local/bin/openclaw run --label memory-compaction "Compact all agents' memory.md files. Merge similar rules, archive cold patterns, export snapshots."
```

## Learning Metrics

Track in `agents/shared-learnings/metrics.json`:

```json
{
  "arjuna": {
    "corrections_logged": 12,
    "reflections_written": 45,
    "patterns_promoted": 3,
    "patterns_archived": 7,
    "team_contributions": 5
  },
  "aria": { ... },
  "richie": { ... },
  "mrbean": { ... }
}
```

## Knowledge Sharing Protocol

**When to share:**
- Pattern used successfully 3+ times
- Major insight that affects team operations
- Security finding (Mr Bean → all)
- Revenue optimization (Richie → Arjuna)
- Process improvement (Aria → all)

**How to share:**
1. Write to personal memory first
2. Add summary to `shared-learnings/patterns/{domain}.md`
3. Mention in weekly digest
4. Tag for relevant agents (e.g., "[Arjuna] [Richie]")

## Rules

1. **Individual first, team second:** Log to personal memory, then share proven patterns
2. **No spam:** Only share patterns with 3+ confirmations
3. **Cite sources:** "Using X (from Richie's trading.md:42)"
4. **Conflicts = ask Arjuna:** If agents learn contradictory patterns, Arjuna decides
5. **Privacy:** Don't share Rahul's personal info across agents
6. **Compounding:** Old patterns don't disappear, they archive. Always recoverable.

## Success Criteria

- ✅ Agents stop making the same mistake twice
- ✅ Successful patterns spread across team automatically
- ✅ Weekly digests show compounding knowledge
- ✅ Rahul sees measurable improvement (fewer corrections, better results)
- ✅ Team autonomy increases (less hand-holding needed)

## Implementation Phases

**Phase 1 (Week 1):** Individual learning
- Set up self-improving directories for all 4 agents
- Enable heartbeat-based daily reflection
- Manual weekly reviews

**Phase 2 (Week 2):** Team knowledge base
- Create shared-learnings structure
- First weekly digest
- Cross-agent pattern reading

**Phase 3 (Week 3):** Automation
- Deploy cron jobs for automated reflection
- Memory compaction system
- Metrics tracking

**Phase 4 (Ongoing):** Optimization
- Tune reflection frequency based on value
- Prune low-signal patterns
- Increase cross-pollination

---

**Next steps:** Start Phase 1 — create self-improving directories for all agents.
