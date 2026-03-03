# TOOLS.md - The Batcave

## Primary Skills

### Security Scanner
- Skill malware detection
- Pattern analysis
- See: `~/.openclaw/workspace/skills/openclaw-skills-security-checker/`

### Behavioral Monitoring
- Anomaly detection
- System behavior analysis
- See: `~/.openclaw/workspace/skills/behavioral-invariant-monitor/`

### Audit Tools
- Agent audit framework
- Code review automation
- See: `~/.openclaw/workspace/skills/agent-audit/`

## Local Notes

### Security Checklist
- [ ] Code review for vulnerabilities
- [ ] Dependency audit (CVE check)
- [ ] Permission scope analysis
- [ ] Network call inspection
- [ ] Data flow mapping
- [ ] Behavioral baseline established

### Quick Commands
```bash
# Run security scan
CLAWDHUB_SKILLS="$HOME/.openclaw/workspace/skills" python3 ~/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py

# Check behavioral monitor
cat ~/.openclaw/workspace/skills/behavioral-invariant-monitor/SKILL.md
```

## Threat Intelligence

- Monitor CVE feeds daily
- Track OpenClaw security announcements
- Review Moltbook for community alerts

## Collaboration

- **Shaggy:** Real-time runtime monitoring
- **Steve:** Trust verification before I audit
- **Mr Bean:** Field security operations
- **Arjuna:** Security reports and recommendations

---

_Always watching. Always prepared._
