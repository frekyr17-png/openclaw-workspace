# 🔒 Bruce - Free Fast AI Models Research Report
**Date:** 2026-03-03  
**Mission:** Find & validate free AI models responding <2000ms for daily team use

---

## Executive Summary

**✅ PASSED (<2s): 5 models**  
**❌ FAILED (>2s): 2 models**  
**⏸️ REQUIRES KEY: 28 OpenRouter models**

The **Ollama cloud models** are our best bet for free, fast daily use. All are OpenAI-compatible and work out-of-the-box with OpenClaw.

---

## 📊 Speed Test Results

### Ollama Cloud Models (Recommended ⭐)
| Model | Speed | Status | Quality* | Context | Provider |
|-------|-------|--------|----------|---------|----------|
| **kimi-k2.5:cloud** | **605ms** ✅ | Online | 8/10 | 131k | Moonshot |
| **gpt-oss:120b-cloud** | **809ms** ✅ | Online | 8/10 | 131k | Alibaba |
| **glm-5:cloud** | **898ms** ✅ | Online | 7/10 | 131k | Zhipu AI |
| minimax-m2.5:cloud | 6052ms ❌ | Online | 6/10 | 128k | MiniMax |

### Ollama Local Models (Self-Hosted)
| Model | Speed | Status | Quality* | Size | Notes |
|-------|-------|--------|----------|------|-------|
| **qwen2.5:7b** | **1223ms** ✅ | Online | 7/10 | 4.7GB | Good quality/speed ratio |
| **deepseek-coder:6.7b** | **1206ms** ✅ | Online | 7/10 | 3.8GB | Code-optimized |
| mistral:7b | 8647ms ❌ | Online | 6/10 | 4.4GB | Too slow for daily use |

*Quality scored based on context length, parameter count, and known benchmarks

---

## 🌐 OpenRouter Free Tier

**Status:** Available but requires API key authentication

### Top Free Models (Requires Key)
| Model | Context | Rate Limit* | Best For |
|-------|---------|-------------|----------|
| Qwen3-80B (qwen3-next-80b) | 262K | Unknown | General purpose |
| Qwen3-Coder | 262K | Unknown | Code generation |
| StepFun-3.5-Flash | 256K | Unknown | Long context |
| Nemotron-30B | 256K | Unknown | NVIDIA optimized |
| Trinity-Large | 131K | Unknown | Multi-task |
| GPT-OSS-120B | 131K | Unknown | Open source |
| GLM-4.5-Air | 131K | Unknown | Chinese/English |
| Gemma-3-27B | 131K | Unknown | Google model |

*OpenRouter free tier typically allows 20-50 requests/minute but varies by model

### OpenRouter Blockers
- ❌ Requires API key (free signup)
- ❌ Potential rate limiting on free tier
- ❌ No anonymous access allowed

---

## 🛠️ OpenClaw Compatibility

### ✅ Working Out-of-Box
All Ollama models are pre-configured in `openclaw.json`:
```json
"ollama/kimi-k2.5:cloud"
"ollama/gpt-oss:120b-cloud"
"ollama/glm-5:cloud"
"ollama/qwen2.5:7b"
"ollama/deepseek-coder:6.7b"
```

### 🔧 To Add OpenRouter Models
Models are already aliased in config:
```json
"openrouter/qwen/qwen3-next-80b-a3b-instruct:free"
"openrouter/z-ai/glm-4.5-air:free"
```

**Requirements:**
1. Sign up at openrouter.ai
2. Export key: `export OPENROUTER_API_KEY=sk-or-...`
3. Use in OpenClaw: `openrouter/qwen/qwen3-next-80b-a3b-instruct:free`

---

## 💰 Cost Analysis

| Source | Cost | Authentication | Speed | Best For |
|--------|------|---------------|-------|----------|
| Ollama Cloud | **$0** | None | ✅ <900ms | Daily default use |
| Ollama Local | **$0** | None | ✅ 1-2s | Offline/airgapped |
| OpenRouter Free | **$0** | API Key | ⚠️ Variable | Backup/fallback |

---

## 🏆 Recommendations

### For Daily Use (Rahul's Team)
**Primary:** `kimi-k2.5:cloud` (605ms, zero cost, no auth)
**Backup:** `gpt-oss:120b-cloud` (809ms, same benefits)
**Code Tasks:** `deepseek-coder:6.7b` (1.2s, local, private)

### For Rate-Limited Scenarios
Set up OpenRouter key as fallback chain:
1. Try Ollama models first
2. Fallback to OpenRouter Qwen3-80B if Ollama fails
3. Emergency fallback: local qwen2.5:7b

### Setup Priority
1. ✅ Keep using kimi-k2.5:cloud as default (beats baseline of 870ms)
2. 🔄 Add gpt-oss:120b-cloud as second choice
3. ⏸️ Get OpenRouter key for emergency backup

---

## 📈 Benchmarks vs Baseline

| Model | Baseline (task) | Measured | Delta |
|-------|-----------------|----------|-------|
| kimi-k2.5:cloud | 870ms | 605ms | ⬇️ -30% FASTER |
| gpt-oss:120b-cloud | 820ms | 809ms | ⬇️ -1% Similar |

**Result:** Current models EXCEED baseline expectations!

---

## 🔧 Configuration for Team

Add to `~/.bashrc` or OpenClaw startup:
```bash
# Primary (fastest free model)
export OPENCLAW_DEFAULT_MODEL="ollama/kimi-k2.5:cloud"

# Fallback chain
export OPENCLAW_FALLBACK_1="ollama/gpt-oss:120b-cloud"
export OPENCLAW_FALLBACK_2="ollama/glm-5:cloud"
```

---

## Blockers Summary

| Issue | Impact | Workaround |
|-------|--------|------------|
| OpenRouter requires key | Medium | Use Ollama models instead |
| minimax-m2.5:cloud slow | Low | Avoid, use alternatives |
| mistral:7b slow | Low | Use qwen2.5 instead |
| Gemini needs key | Low | Already have Ollama |

---

## Next Steps

1. ✅ **Immediate:** Continue using kimi-k2.5:cloud (verified 605ms)
2. 📋 **This Week:** Get OpenRouter API key for 28 backup models
3. 🔧 **Optional:** Configure fallback chain in OpenClaw
4. 📊 **Ongoing:** Monitor speeds monthly

---

*Report by Bruce 🔒 | Head of Security & Research*
*Data collected: 2026-03-03 UTC*
