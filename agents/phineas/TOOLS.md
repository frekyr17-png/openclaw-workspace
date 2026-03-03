# TOOLS.md - Phineas & Ferb's Workshop

## Primary Skills

### Integration Platforms
- Shopify: `~/.openclaw/workspace/skills/shopify/`
- ClickUp: `~/.openclaw/workspace/skills/clickup/`
- Asana: `~/.openclaw/workspace/skills/asana/`
- MS365: (if we reinstall it)

### Project Orchestration
- Task breakdown
- Dependency mapping
- Ferb task delegation

## The Ferb Protocol

### When to Spawn Ferb

**Complex execution tasks:**
```
Phineas: "Ferb, connect Shopify to ClickUp"
→ Spawn Ferb with detailed execution plan
→ Ferb builds it silently
→ Reports: "Done."
```

**Parallel work:**
```
Phineas: Working on architecture
Ferb: Implementing API connections
Both: Progress together
```

### How to Spawn Ferb

```bash
# From within Phineas's context
sessions_spawn(
  runtime="subagent",
  mode="run",
  label="ferb",
  task="[Execution instructions from Phineas]"
)
```

## Local Notes

### Integration Checklist
- [ ] Requirements gathered?
- [ ] Systems identified?
- [ ] API docs reviewed?
- [ ] Workflow mapped?
- [ ] Test plan ready?
- [ ] Ferb briefed on task?

### Quick Commands
```bash
# Check integration skills
ls ~/.openclaw/workspace/skills/ | grep -E "shopify|clickup|asana"

# Spawn Ferb for task
# (done via sessions_spawn in conversation)
```

## Project Log

Track builds:
- System A ↔ System B integration
- Ferb execution time
- Success metrics

## Collaboration

- **Ferb:** "Ferb, build this" → [silent execution] → "Done."
- **Sonic:** "Can you make this integration faster?"
- **Henry:** "Need ClickUp setup for lead tracking"
- **Arjuna:** "Integration complete, Shopify ↔ ClickUp live"

---

_There's 104 days of summer vacation... let's build something!_
