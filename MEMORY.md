# MEMORY.md - Long-Term Memory

_Last updated: 2025-02-22_

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

## Lessons Learned
- Always update lists fully when asked (Rahul got frustrated when ollama list wasn't refreshed)
- Don't ask unnecessary questions — just do it
- Token efficiency matters — batch work, use local models
