# Ollama Fix - VPS CPU-Only Limitation (2026-03-03)

## Problem
Ollama was running but local CPU models (qwen2.5:7b, mistral:7b, deepseek-coder) were timing out on the VPS (no GPU). This made heartbeats and some tasks hang.

## Solution Implemented
1. ✅ Exposed Ollama on all interfaces: `OLLAMA_HOST=0.0.0.0:11434` in systemd service
2. ✅ Restarted ollama service (PID 562482, active now)
3. ✅ Verified cloud models work fast (kimi-k2.5:cloud: 0.87s, gpt-oss:120b-cloud: 0.82s)
4. ✅ Verified local CPU models timeout (qwen2.5:7b: >30s, won't work)

## What's Working Now
- **Cloud models** in Ollama (via ollama.com proxy):
  - kimi-k2.5:cloud ✅ 0.87s
  - minimax-m2.5:cloud ✅ 2.90s
  - gpt-oss:120b-cloud ✅ 0.82s
  - glm-5:cloud (untested but should work)

- **Ollama service**: Running, fully functional, listening on :11434

## What Won't Work
- Local CPU models: qwen2.5:7b, mistral:7b, deepseek-coder:6.7b (7B+ models need GPU)

## Recommendation
1. Keep Ollama running for cloud models (free via ollama.com)
2. Use cloud models in heartbeats/cheap tasks (0.87s response, $0 cost)
3. Use OpenRouter or Anthropic for heavy work (already configured)
4. **Optional**: Install a small 1B-2B quantized model if needed for ultra-light tasks (but not recommended on CPU)

## Test Results
```
✅ kimi-k2.5:cloud           | 0.87s | Working
✅ minimax-m2.5:cloud        | 2.90s | Working
✅ gpt-oss:120b-cloud        | 0.82s | Working
⏱️  qwen2.5:7b                | TIMEOUT (>10s) | CPU too slow
```

## Service Status
- Ollama version: 0.16.1
- Service: active (running) since 2026-03-03 12:00:09 UTC
- Memory: ~4.3GB
- Port: 0.0.0.0:11434 (all interfaces)

---
Next steps: Monitor trading lab performance with cloud models in heartbeat, consider GPU for production.
