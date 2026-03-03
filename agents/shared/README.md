# Shared Agent Workspace

**Purpose:** Inter-agent collaboration and coordination

## Structure

### handoffs/
Work passed from one agent to another.

**Example:** Rick builds prototype → hands off to Tony for polish

```
handoffs/rick-to-tony/
└── prototype-api.py
```

### collaboration/
Multiple agents working on the same project.

**Example:** Trading bot improvement (Richie + Sonic + Bruce)

```
collaboration/trading-bot-improvement/
├── richie-analysis.md
├── sonic-optimization.md
└── bruce-security.md
```

### comms/
Inter-agent messages and coordination notes.

**Example:** Agent status updates, requests, handoff notifications

```
comms/2026-03-02/
├── rick-to-arjuna.md (status update)
└── bruce-to-tony.md (fix request)
```

## Usage

**When handing off work:**
1. Create handoffs/{from}-to-{to}/ directory
2. Place files there
3. Notify via sessions_send or log to comms/

**When collaborating:**
1. Create collaboration/{project-name}/ directory
2. Each agent adds their piece
3. Coordinate via Arjuna or directly

**When communicating:**
1. Write to comms/{date}/{from}-to-{to}.md
2. Keep it brief and actionable
3. Use for coordination, not chat

## Principles

- Keep it organized (use directories)
- Name files clearly
- Document handoffs
- Clean up completed work (archive to history/)

---

**This is how the team works together without bothering Rahul.**
