# Trusted Skills Whitelist

_Last updated: 2026-03-02_

## 🟢 Whitelisted Skills

### openclaw-skills-security-checker
- **Source:** digitaladaption via ClawHub + GitHub
- **Purpose:** Security scanner (this is what I use!)
- **Why trusted:** Official security tool. Patterns detected are for scanning, not exploitation.
- **Flagged patterns:** credential_theft, command_injection (expected for security tools)
- **Whitelisted:** 2026-03-02
- **Review:** Quarterly

### agent-lifecycle
- **Source:** trypto1019 via GitHub
- **Purpose:** Track agent evolution, snapshots, rollback
- **Why trusted:** Clean scan, documentation-focused, no network calls
- **Flagged patterns:** None
- **Whitelisted:** 2026-03-02
- **Review:** Quarterly

### task-orchestrator
- **Source:** henrino3 via GitHub
- **Purpose:** Multi-agent parallel task orchestration
- **Why trusted:** Documentation/methodology skill, creates tmux sessions (expected)
- **Flagged patterns:** subprocess (expected for tmux management)
- **Whitelisted:** 2026-03-02
- **Review:** Quarterly

### trading-lab
- **Source:** Internal (Volt-built)
- **Purpose:** Trading bot system
- **Why trusted:** Built by our team, reviewed code
- **Flagged patterns:** None
- **Whitelisted:** 2026-03-02
- **Review:** Monthly (active development)

---

## Review Schedule

- **Monthly:** Internal/active development skills (trading-lab)
- **Quarterly:** External stable skills (security tools, lifecycle)
- **On update:** Any skill that receives updates gets re-scanned

## Whitelist Criteria

✅ **Auto-whitelist:**
- Official OpenClaw skills
- Skills from verified developers
- Clean security scan + clear purpose

⚠️ **Review required:**
- Network access (APIs are OK if documented)
- File system write (OK if purpose is clear)
- Subprocess spawning (OK for tooling)

🚨 **Never whitelist:**
- Credential theft patterns
- External webhook calls without justification
- Shell injection / eval without sandboxing
- Undocumented network exfil
