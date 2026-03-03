# TOOLS.md - Sonic's Speed Lab

## Primary Skills

### n8n Workflow Automation
- Rapid workflow building
- Performance-optimized pipelines
- See: `~/.openclaw/workspace/skills/n8n-workflow-automation/`

### n8n Instance
- URL: http://localhost:5678
- Docker container running
- Admin access ready

### Speed Tools
- Performance profiling
- Latency monitoring
- Parallel execution frameworks

## Local Notes

### Speed Checklist
- [ ] Can this run in parallel?
- [ ] Can this be cached?
- [ ] Is there unnecessary latency?
- [ ] Are we waiting when we don't need to?
- [ ] Can we pre-compute this?

### Quick Commands
```bash
# Check n8n status
docker ps --filter name=n8n

# Access n8n
# Browser: http://localhost:5678

# Check workflow skill
cat ~/.openclaw/workspace/skills/n8n-workflow-automation/SKILL.md
```

## Performance Philosophy

- Measure first (no guessing)
- Optimize hot paths
- Parallel everything possible
- Cache aggressively (but safely)
- Never block when you can async

## Collaboration

- **Henry:** "Built your lead gen workflow—runs in 2 seconds"
- **Phineas:** "Optimized your integration—50% faster"
- **Arjuna:** "Workflow deployed, zero latency added"

---

_You're too slow! Let's speed this up!_
