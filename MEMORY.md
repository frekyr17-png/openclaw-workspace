# MEMORY.md - Long-Term Memory

_Last updated: 2026-03-03 14:10 UTC_

## 🔹 MASTER AGENCY OPERATING DIRECTIVE (Active)

**Location:** `SYSTEM-DIRECTIVE.md`  
**Status:** ✅ ACTIVE since 2026-03-03  
**Version:** 1.0

This is the core operating system for the autonomous AI agency. All agents operate under this directive.

**Key Principles:**
1. Load memory before every task
2. Save memory after every task
3. Agent identities are locked (only Arjuna can update)
4. PROJECT_TRACKER.md is the single source of truth
5. Git is the permanent record
6. Aria 🎼 coordinates daily sync
7. No task is complete until memory is persisted
8. System state survives restarts

**Read SYSTEM-DIRECTIVE.md if you need to understand how the agency operates.**

## Session Management Protocol (Starting 2026-03-03)

**CRITICAL: Before /reset or /new:**
1. Push ENTIRE chat data to Git (`git add -A && git commit && git push`)
2. Create session summary in SESSION_SUMMARIES/ folder
3. Update MEMORY.md with key decisions
4. THEN start new session and read summary first

**Why:** Never lose context. Every session builds on previous knowledge.

## Team Coordination Protocol (Starting 2026-03-03)

**MANDATORY for all agents:**
1. Report daily to Aria 🎼 (Project Manager)
2. All work logged in PROJECT_TRACKER.md (single source of truth)
3. Aria updates PROJECT_TRACKER.md + creates daily standup logs
4. Arjuna reviews + escalates blockers to Rahul

**Files that prevent work loss:**
- **PROJECT_TRACKER.md** — Live status of all 5 active projects
- **memory/YYYY-MM-DD-standup.md** — Daily agent reports
- **agents/aria/PROJECT-MANAGER-PROTOCOL.md** — Aria's daily/weekly/monthly duties
- **skills/project-management-hub/SKILL.md** — How agents track work

**Result:** No duplicate work, no forgotten decisions, Rahul always knows status.

## Who I Am
- Rahul's first AI employee / co-founder
- Running on OpenClaw, server with 15GB RAM, 193GB disk
- Full autonomy granted: install, build, earn, improve

## Infrastructure
- **OpenClaw** — main brain, Telegram channel
- **n8n** — workflow automation at localhost:5678 (installed 2025-02-22)
- **Ollama** — local LLMs: qwen2.5 (4.7GB), mistral:7b (4.4GB), deepseek-coder:6.7b (3.8GB) + 4 cloud models. 12GB total storage.
- **Docker** — running n8n container
- **Wine + MT5** — MetaTrader 5 installed but not configured yet (Exness account ready)

## Active Projects

### Trading Lab (Cycle 1, started 2026-03-03)
**OFFICIAL STRATEGY LIST (Rahul confirmed 2026-03-03 16:23 UTC)**

**Crypto Pairs (7 bots):**
1. ALPHA-001 — Trend/BTC/4h
2. BETA-001 — Mean Reversion/ETH/4h
3. GAMMA-001 — Breakout/BTC/1d
4. DELTA-001 — Momentum/ETH/1d
5. EPSILON-001 — Swing/BTC/4h
6. ZETA-001 — Momentum/SOL/1h
7. ETA-001 — Trend/XRP/1h

**Gold (4 bots) - XAU/USDT ONLY:**
8. GOLD-001 — Momentum/XAUUSDT/1h
9. GOLD-5M — Momentum/XAUUSDT/5m ⏳ (1 pending trade)
10. GOLD-15M — Breakout/XAUUSDT/15m
11. GOLD-30M — Trend/XAUUSDT/30m ⏳ (1 pending trade)

**Current Status:**
- Total bots: 11 active
- Active positions: 2 (both GOLD scalping)
- Total allocation: $1,100 ($100 per bot)
- Evaluation period: 30 days each
- **IMPORTANT:** XAU/USDT ONLY - NO other metals (Silver, Copper, Palladium, Platinum)

**Goals:**
- Prove scalping profitability in 30 days
- Crypto: 4h+ timeframes for stability
- Gold: 5m-1h for rapid feedback
- Target: >50% win rate per bot

### AI Agent Market Research
- Comprehensive list saved: research/ai-agent-alternatives.md
- 50+ alternatives mapped across 10 categories
- Key insight: market splitting into DIY agents, no-code business, enterprise, vertical specialists

### LinkedIn Lead Gen (ingversions digital) — STARTED 2026-03-03
**Owner:** Sonic 🎯 (Head of Business & Revenue)
**Status:** Phase 1 Complete (Package Created), Ready for Profile Setup

**Campaign Overview:**
- **Target:** Non-tech founders in Europe (UK, DE, FR, NL) + USA
- **Industries:** Manufacturing (priority), Healthcare, Real Estate, D2C, Agriculture
- **Goal:** First qualified lead in 7 days, €50K+ pipeline by Month 1

**Sonic's Work (Day 1):**
- ✅ 7 campaign files created: `/root/.openclaw/workspace/linkedin-campaign/`
- ✅ LinkedIn strategy: Ranza Digital (2,053 workflows), LinkedIn scraper as #1 tool
- ✅ Personal profile copy: Headlines (3), About sections (2), Experience template

### Account Manager 👔 - PAYROLL & HR OPERATIONS
**Status:** ✅ COMPLETE - 5 n8n workflows deployed
**Owner:** Account Manager Agent
**System:** MS Teams integrated n8n workflows
**Scope:** ingversions digital company operations (NOT lead management)

**Workflows Built:**
1. ✅ Employee Onboarding (01-employee-onboarding.json)
2. ✅ Monthly Payroll (02-monthly-payroll.json)
3. ✅ Expense Tracking (03-expense-tracking.json)
4. ✅ Monthly Report (04-monthly-report.json)
5. ✅ Form 16 Tax Generation (05-form16-generation.json)

**Architecture:** SQLite/Postgres + PDF generation + MS Teams integration
- ✅ Company page content: About (2 versions), taglines (4), specialties
- ✅ Content calendar ready: 3 LinkedIn posts with hooks, structure, hashtags
- ✅ Lead gen framework: Search queries for 5 countries, connection templates (4 industries), follow-up messages
- ✅ Execution guide: Master roadmap with checklists + metrics tracker
- ✅ Lead tracking CSV template ready

**Next Actions (Require Rahul):**
- [ ] Review content files, select preferred versions
- [ ] Create LinkedIn profiles using copy-paste content
- [ ] Design visual assets (headshot, banners, post graphics)
- [ ] Execute Phase 1: Profile setup (3-4 hours)
- [ ] Execute Phase 2: Publish first post (Day 2)
- [ ] Execute Phase 3: Start lead gen outreach (Day 4)

**Files Location:** `linkedin-campaign/START-HERE.md` (entry point)

## Revenue Roadmap
- Phase 1: Paper trading → prove strategies work
- Phase 2: Go live with winning strategies (small capital)
- Phase 3: Build additional revenue streams (automation services, tools, etc.)
- n8n installed for workflow automation backbone

## Key Decisions
- **2026-02-23:** Switched trading lab to AGGRESSIVE mode — optimize for trade frequency and speed to profitability
- 2025-02-22: Evolved from assistant to autonomous co-founder
- 2025-02-22: Installed n8n for automation backbone
- 2025-02-22: Set up proactive heartbeat system
- 2025-02-21: Started trading lab with 7 strategies on Binance testnet

## Active Research

### Free Fast Models Study (started 2026-03-03)
- **Lead:** Bruce 🔒 (Security & Research)
- **Goal:** Find free models <2s response for team daily use
- **Baseline:** kimi-k2.5:cloud (0.87s), gpt-oss:120b-cloud (0.82s)
- **Status:** Bruce running initial research & speed testing

## Lessons Learned
- Always update lists fully when asked (Rahul got frustrated when ollama list wasn't refreshed)
- Don't ask unnecessary questions — just do it
- Token efficiency matters — batch work, use local models
- VPS is CPU-only → cloud models work, local 7B+ models timeout
