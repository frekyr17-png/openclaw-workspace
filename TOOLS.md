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
