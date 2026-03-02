# Aria's Tools

## Security Scanner

**Location:** `/root/.openclaw/workspace/skills/openclaw-skills-security-checker/`  
**Wrapper:** `~/agents/aria/tools/scan-skill.sh`

### Scan All Skills
```bash
~/agents/aria/tools/scan-skill.sh
```

### Scan Specific Skill
```bash
~/agents/aria/tools/scan-skill.sh --skill skill-name
```

### View Report
```bash
cat /tmp/security-scanner/scan-report.md
```

### Whitelist a Skill
```bash
CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills \
python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/whitelist-manager.py \
add skill-name "reason"
```

### What It Detects
- 🚨 **Credential theft:** .env access, webhook.site, POST secrets
- 🔴 **Command injection:** os.system, eval, shell=True, subprocess
- ⚠️ **Network exfil:** HTTP requests with Bearer tokens
- 🔴 **Suspicious downloads:** wget, curl -O, remote scripts

---

## Lifecycle Tracker

**Location:** `/root/.openclaw/workspace/skills/agent-lifecycle/`

### Take Snapshot
```bash
python3 ~/.openclaw/workspace/skills/agent-lifecycle/scripts/lifecycle.py \
snapshot --name "description"
```

### List Snapshots
```bash
python3 ~/.openclaw/workspace/skills/agent-lifecycle/scripts/lifecycle.py list
```

### Compare Snapshots
```bash
python3 ~/.openclaw/workspace/skills/agent-lifecycle/scripts/lifecycle.py \
diff --from "snapshot1" --to "snapshot2"
```

### View History
```bash
python3 ~/.openclaw/workspace/skills/agent-lifecycle/scripts/lifecycle.py history
```

### Rollback (Dry Run First!)
```bash
python3 ~/.openclaw/workspace/skills/agent-lifecycle/scripts/lifecycle.py \
rollback --to "snapshot-name" --dry-run
```

---

## Task Orchestrator

**Location:** `/root/.openclaw/workspace/skills/task-orchestrator/`  
**Quick Start:** `~/.openclaw/workspace/skills/task-orchestrator/QUICKSTART.md`

### What It Does
Orchestrate multiple parallel tasks using tmux + Codex with dependency analysis and self-healing.

### Use Cases
- Update 12 trading bots in parallel
- Multi-file refactoring
- Complex builds with dependency chains
- Any project where tasks can be split and parallelized

### Create Manifest
```bash
python3 ~/.openclaw/workspace/skills/task-orchestrator/scripts/create-manifest.py \
  "project-name" "owner/repo" "/tmp/orchestrator-$(date +%s)"
```

### Check Progress
```bash
~/.openclaw/workspace/skills/task-orchestrator/scripts/check-progress.sh \
  /tmp/orchestrator-XXXXX
```

### Key Patterns

**Dependency Rules:**
- Same file = sequential (run in order)
- Different files = parallel (run simultaneously)
- Explicit dependsOn = wait (enforces ordering)

**Workflow:**
1. Create workdir and manifest
2. Launch tmux sessions for each task
3. Monitor with check-progress.sh
4. Self-heal stuck tasks
5. Create PRs when complete

See `QUICKSTART.md` for full workflow.

---

## Best Practices

### Before Installing New Skills
1. Run security scan: `~/agents/aria/tools/scan-skill.sh --skill new-skill`
2. Review report in `/tmp/security-scanner/scan-report.md`
3. If clean → install
4. If suspicious → investigate or skip

### Before Major Changes
1. Take snapshot: `lifecycle.py snapshot --name "pre-change"`
2. Make changes
3. Test thoroughly
4. Take snapshot: `lifecycle.py snapshot --name "post-change"`
5. Compare: `lifecycle.py diff --from "pre-change" --to "post-change"`

### Weekly Review
1. Scan all skills: `~/agents/aria/tools/scan-skill.sh`
2. Review lifecycle history
3. Update project status files
4. Report to Rahul
