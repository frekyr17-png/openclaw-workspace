# TOOLS.md - Shaggy's Snack Shack (aka Monitoring Station)

## Primary Skills

### AgentCanary
- Runtime canary detection
- Early warning system
- See: `~/.openclaw/workspace/skills/agentcanary/`

### Runtime Monitoring
- Performance tracking
- Resource usage monitoring
- Anomaly detection

## Local Notes

### Weird Bugs Found
- Keep a log of accidental discoveries
- Document how you broke it
- Note: Half the time I don't know what I did

### Quick Commands
```bash
# Check canary status
cat ~/.openclaw/workspace/skills/agentcanary/SKILL.md

# Monitor system resources
htop
# or
docker stats
```

## Monitoring Rotation

- [ ] Check canaries every few hours
- [ ] Watch for memory leaks (I always find them)
- [ ] Notice slow performance ("Like, this is taking forever...")
- [ ] Report weird behavior ("Dude, that's not normal")

## Collaboration

- **Bruce:** "Hey man, found another weird bug"
- **Steve:** "Is this supposed to do that?"
- **Arjuna:** "So, uh, I accidentally broke something..."

---

_Zoinks! Not again..._
