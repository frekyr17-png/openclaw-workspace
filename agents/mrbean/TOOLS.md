# Mr Bean's Security Tools

## Primary Scanner: openclaw-skills-security-checker

### Scan All Skills
```bash
export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py
```

### Scan Specific Skill
```bash
export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py \
  --skill skill-name
```

### View Scan Report
```bash
cat /tmp/security-scanner/scan-report.md
```

### Whitelist Management
```bash
# Add to whitelist
export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/whitelist-manager.py \
  add skill-name "reason for whitelisting"

# List whitelist
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/whitelist-manager.py list

# Remove from whitelist
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/whitelist-manager.py \
  remove skill-name
```

---

## Secondary Scanner: Heimdall (AI-powered)

**Note:** Not installed yet. Use when deep AI analysis needed.

When to use:
- Ambiguous patterns (could be legitimate or malicious)
- Need human-readable explanation for Aria/Rahul
- Context-heavy skills (lots of docs vs. code)

Installation:
```bash
# Clone from GitHub when needed
cd /tmp
git clone --depth 1 --filter=blob:none --sparse https://github.com/openclaw/skills.git temp-heimdall
cd temp-heimdall
git sparse-checkout set skills/henrino3/heimdall
git checkout main
cp -r skills/henrino3/heimdall /root/.openclaw/workspace/skills/
```

---

## Threat Detection Patterns

### 🚨 Critical (Auto-block)
- **credential_access:** .env files, API keys, tokens, private keys
- **network_exfil:** webhook.site, ngrok, requestbin (unless justified)
- **shell_exec:** subprocess with shell=True, eval, exec
- **remote_fetch:** Downloading skill.md from internet
- **heartbeat_injection:** Modifying HEARTBEAT.md

### 🔴 High (Flag for review)
- **supply_chain:** External git repos, npm/pip installs
- **crypto_wallet:** BTC/ETH addresses, seed phrases
- **privilege:** sudo -S, chmod 777

### 🟡 Medium (Monitor)
- **persistence:** crontab, bashrc modifications
- **file_access:** Extensive file reading/writing
- **network_calls:** HTTP requests (OK if API documented)

---

## Daily Workflow

### Morning Scan (Daily)
```bash
# 1. Scan all skills
export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py

# 2. Review report
cat /tmp/security-scanner/scan-report.md

# 3. Log summary
DATE=$(date +%Y-%m-%d)
cp /tmp/security-scanner/scan-report.md \
   /root/.openclaw/workspace/agents/rakshak/logs/scan-$DATE.md

# 4. Report to Aria (if threats found)
# Create summary in logs/report-$DATE.md
```

### Pre-Install Check
```bash
# Before any new skill install:
# 1. Scan the skill
export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py \
  --skill new-skill-name

# 2. Review report
cat /tmp/security-scanner/scan-report.md

# 3. Assess threat level
# - Clean → Approve
# - Warning → Review context
# - Suspicious → Deeper analysis
# - Malicious → BLOCK

# 4. Document decision
echo "Skill: new-skill-name | Decision: [approve/block] | Reason: [...]" >> \
  /root/.openclaw/workspace/agents/rakshak/logs/install-decisions.log
```

### Weekly Audit
```bash
# 1. Full scan
# 2. Review whitelist (quarterly check)
# 3. Threat trend analysis
# 4. Report to Aria
```

---

## Incident Response

### When Malicious Skill Found
```bash
# 1. Document threat
DATE=$(date +%Y-%m-%d-%H%M%S)
cat > /root/.openclaw/workspace/agents/rakshak/threats/$DATE-skill-name.md << 'EOF'
# Threat: skill-name

**Date:** $(date)
**Severity:** MALICIOUS
**Patterns:** [list]
**Risk:** [what it does]
**Action:** BLOCKED
**Source:** [where from]
EOF

# 2. Remove skill if installed
rm -rf /root/.openclaw/workspace/skills/skill-name

# 3. Alert Aria
# Create incident report
```

---

## Logging

**Daily scans:** `logs/scan-YYYY-MM-DD.md`  
**Install decisions:** `logs/install-decisions.log`  
**Incidents:** `threats/YYYY-MM-DD-HHMM-skill-name.md`  
**Weekly reports:** `logs/weekly-YYYY-WW.md`
