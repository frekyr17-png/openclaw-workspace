# HEARTBEAT.md

**MODEL:** Use OpenRouter free models ONLY (OR-Free, Qwen3-80B, etc.)  
**NO OPUS/SONNET for heartbeats - costs too much**

## Every Heartbeat (rotate, don't do all at once)

### Priority 1: Revenue Check
- [ ] Check trading lab state.json — any completed trades? Run trader.py if needed
- [ ] Check trader.log for errors

### Priority 2: Infrastructure Health
- [ ] n8n running? `docker ps --filter name=n8n`
- [ ] Ollama running? `ollama ps`
- [ ] Disk usage still healthy? `df -h / | tail -1`
- [ ] RAM not full? `free -h`

### Priority 3: Self-Improvement (every few heartbeats)
- [ ] Review recent memory files, update MEMORY.md
- [ ] Check if any skills can be created from repeated tasks
- [ ] Look for new revenue opportunities

## Rules
- Keep it fast. Don't scan everything every time.
- Rotate through priorities. Priority 1 every time, others on rotation.
- If trading bot errors: fix and log.
- If infra down: restart and notify Rahul.
- Late night (23:00-08:00 UTC): HEARTBEAT_OK unless urgent.
