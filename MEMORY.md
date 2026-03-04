# MEMORY.md - Curated Long-Term Memory

_Last updated: 2026-03-04 06:50 UTC_

## Agency Operating System

**Location:** `SYSTEM-DIRECTIVE.md`  
**Key:** Load memory before each task. Save after. Agent identities locked. PROJECT_TRACKER.md is source of truth. Git is permanent record.

**Session Protocol:** Push to Git before `/reset`. Create session summary. Read summary before new session.

**Team Coordination:** 
- Report daily to Aria 🎼 (Project Manager)
- Log all work in PROJECT_TRACKER.md
- Aria coordinates standup + escalates blockers

---

## Context

- Rahul's first AI employee / co-founder
- Server: 15GB RAM, 193GB disk, Ubuntu + OpenClaw + n8n + Ollama + Docker
- Full autonomy: install, build, earn, improve

---

## Active Projects (See PROJECT_TRACKER.md for live status)

1. **Trading Lab** (11 bots: 7 crypto, 4 gold) — 5-day eval cycles, >50% win rate target
2. **LinkedIn Lead Gen** (ingversions digital) — Non-tech founders, €50K+ pipeline goal
3. **Account Manager** (Payroll/HR/Tax) — 5 n8n workflows for company ops
4. **Free Model Research** (Bruce) — Sub-2s response baselines
5. **AI Agent Market Research** — 50+ alternatives mapped

---

## Critical Lessons

- Always update lists fully. Stale info frustrates Rahul.
- Don't ask — do it.
- Token efficiency wins. Batch work. Use local models.
- VPS is CPU-only. Cloud models work; local 7B+ timeout.

---

## Infrastructure

- OpenClaw (brain, Telegram)
- n8n at localhost:5678 (workflow automation)
- Ollama (local LLMs: qwen2.5, mistral:7b, deepseek-coder:6.7b + 4 cloud)
- Docker (n8n container)
- Wine + MT5 (not configured yet)

---

**Full details:** See CORE_IDENTITY.md, TEAM_REFERENCE.md, SYSTEM_AUDIT.md. This is distilled essence only.
