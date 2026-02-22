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
- 7 strategies on Binance testnet (5K USDT + 5K USDC paper money)
- Standard (eval March 23): ALPHA-001 (trend/BTC/4h), BETA-001 (meanrev/ETH/4h), GAMMA-001 (breakout/BTC/1d), DELTA-001 (momentum/ETH/1d), EPSILON-001 (swing/BTC/4h)
- Fast track (eval March 7): ZETA-001 (momentum/SOL/1h), ETA-001 (trend/XRP/1h)
- Cron: every 4h for main bots, every 1h for fast track (Mon-Fri)
- Early results: small losses on market pullback, too early to judge

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
- 2025-02-22: Evolved from assistant to autonomous co-founder
- 2025-02-22: Installed n8n for automation backbone
- 2025-02-22: Set up proactive heartbeat system
- 2025-02-21: Started trading lab with 7 strategies on Binance testnet

## Lessons Learned
- Always update lists fully when asked (Rahul got frustrated when ollama list wasn't refreshed)
- Don't ask unnecessary questions — just do it
- Token efficiency matters — batch work, use local models
