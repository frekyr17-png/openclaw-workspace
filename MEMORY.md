# MEMORY.md - Long-Term Memory

_Last updated: 2026-03-03_

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

### Trading Lab (Cycle 1, started 2025-02-21)
**Updated 2026-02-23: Switched to aggressive mode**
- **GOAL:** 10% daily profit per bot = $10/day per $100 allocation = $200/month per bot
- **12 strategies** on Binance testnet (5K USDT + 5K USDC paper)
- **5-minute scalping** (runs every 5 min): KAPPA-001 (BTC), LAMBDA-001 (ETH), MU-001 (SOL), THETA-001 (XAU), IOTA-001 (XAU)
- **1-hour fast track** (eval March 7): ZETA-001 (SOL), ETA-001 (XRP) → ETA leading at 55.6% win rate
- **4-hour standard** (eval March 23): ALPHA-001 (BTC), BETA-001 (ETH), GAMMA-001 (BTC), DELTA-001 (ETH), EPSILON-001 (BTC)
- **Rule:** No trade in 24h = adjust timeframe/strategy/kill the bot
- **Strategy updated:** 
  - Lowered thresholds (trend: 0.1%, meanrev: 1.0 z-score, momentum: 1.5% ROC)
  - **Trade management:** Target 5-10% profit per trade, exit when hit
  - **Daily target:** 10% gain per bot portfolio ($10 on $100 allocation)
  - **Method:** 1 trade or 100 trades — doesn't matter, just hit the 10%

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
