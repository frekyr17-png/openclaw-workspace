# TOOLS.md - Local Notes

## Infrastructure

### Server
- Ubuntu 6.8.0, 15GB RAM, 193GB disk
- IP: VPS (Contabo or similar based on IP range)

### n8n (Workflow Automation)
- URL: http://localhost:5678
- Docker container: `n8n`
- Data volume: `n8n_data`
- Status: Running, needs initial setup (create admin account)

### Ollama (Local LLMs)
- Models: qwen2.5 (7b), mistral:7b, deepseek-coder:6.7b + 4 cloud models
- Storage: /usr/share/ollama/.ollama/models (12GB)
- Use for: cheap tasks, local processing, avoid API costs

### Trading Lab
- Trader script: ~/.openclaw/workspace/trading-lab/trader.py
- State: ~/.openclaw/workspace/trading-lab/state.json
- Credentials: ~/.openclaw/workspace/trading-lab/credentials.env
- Log: ~/.openclaw/workspace/trading-lab/trader.log
- Cron: every 4h (all bots) + every 1h (ZETA, ETA fast track) Mon-Fri

### MetaTrader 5
- Installed via Wine 11.2
- Path: /root/.wine/drive_c/Program Files/MetaTrader 5/
- Server: Exness-MT5Trial6
- Login: 413408643
- Status: Not running, Python MT5 package not installed
- TODO: Set up later per Rahul's request

### Docker
- Running: n8n
- Available for: more services as needed

## Token Efficiency Rules
- Use Ollama for simple text processing, summaries, classification
- Use main model (Claude) for complex reasoning, coding, decisions
- Batch heartbeat checks
- Cache frequently accessed data in memory files
- Build skills for repeated tasks

## Model Selection (Updated 2026-03-03)
- **Main/Default:** `anthropic/claude-haiku-4-5` (switched from ollama/kimi-k2.5:cloud due to rate limits)
- **Reason:** Ollama free tier hit weekly limit, Haiku is reliable + cheap ($0.25-1.25/M tokens)
- **Heartbeat:** 30 min interval - use free models (OR-Free, Qwen3-80B) per HEARTBEAT.md
- **Cron jobs:** Direct Python scripts, no LLM involved
- **Trading bot:** Technical analysis (SMA, RSI) - no LLM, just ccxt library
- **Fallback:** Still have kimi-k2.5:cloud available when Haiku is needed elsewhere

## LinkedIn Lead Gen (ingversions digital)
- Target: Europe (UK, Germany, France, Netherlands) + USA
- Industries: Manufacturing, Healthcare, Real Estate, D2C, Agriculture
- Exclude: IT, Software, Digital Agencies

## Phineas & Ferb - 1% Daily Learning Plan

**Program:** Figma MCP + Shopify Liquid Development
**Pace:** 1% daily (sustainable, no API burn)
**Duration:** 5 weeks to production-ready

### Daily Tasks (Mon-Fri)

**Phineas 🔧 (Figma MCP):**
- 1 small project or learning module
- Document findings in /root/.openclaw/workspace/agents/phineas/
- Create 1 reusable code snippet
- Test 1 integration pattern

**Ferb 🔩 (Shopify Liquid):**
- 1 Liquid template exercise
- Build 1 component/snippet
- Test on Shopify dev store
- Document in /root/.openclaw/workspace/agents/ferb/

### Weekly Deliverables
- 5 working Figma MCP examples
- 5 working Liquid templates
- 1 combined integration demo

### Timeline
- Week 1: Fundamentals
- Week 2-3: Intermediate patterns
- Week 4: Advanced integrations
- Week 5: Production-ready systems

### Progress Tracking
- Daily standup (brief status)
- Weekly demos for Rahul
- Monthly milestone review
