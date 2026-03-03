# COST OPTIMIZATION - API Usage Rules

**Updated:** 2026-03-02 19:39 UTC

---

## **MODEL USAGE POLICY**

**Full details:** See `MODEL_USAGE_POLICY.md`

**Quick reference:**
- Heartbeats → OR-Free (free)
- Chat → Claude Haiku 4.5 (cheap)
- Coding → Qwen3-Coder (free) or Haiku (cheap)
- Complex → Claude Sonnet 4.5 (mid)
- Emergency only → Claude Opus 4.6 (expensive)

---

### **FREE MODELS (OpenRouter) - Use for:**
- ✅ **Heartbeats** (routine checks)
- ✅ **Simple tasks** (file organization, status checks)
- ✅ **Draft work** (initial code, rough summaries)
- ✅ **Memory searches** (local files first anyway)
- ✅ **Logs parsing**
- ✅ **Simple QA checks**

### **PAID MODELS (Claude Opus/Sonnet) - Use ONLY for:**
- ❌ **Strategic decisions**
- ❌ **Complex code generation**
- ❌ **Client-facing work**
- ❌ **Critical debugging**
- ❌ **Revenue-generating tasks**

---

## **FREE MODEL RECOMMENDATIONS**

**Best for heartbeats:**
- **Qwen3-80B** (`openrouter/qwen/qwen3-next-80b-a3b-instruct:free`)
- **Trinity-Large** (`openrouter/arcee-ai/trinity-large-preview:free`)
- **OR-Free** (`openrouter/free`) - auto-routes to best available

**Best for coding:**
- **Qwen3-Coder** (`openrouter/qwen/qwen3-coder:free`)

**Best for quick tasks:**
- **StepFun-Flash** (`openrouter/stepfun/step-3.5-flash:free`)

---

## **HEARTBEAT CONFIGURATION**

**Current:** Uses default model (expensive)  
**New:** Use `OR-Free` or `Qwen3-80B`

**How to override for heartbeats:**
Set in heartbeat spawn or session config to use free model.

---

## **LOCAL MODELS (Ollama) - Use for:**
- ✅ **Text summarization**
- ✅ **Simple classifications**
- ✅ **Data extraction**
- ✅ **Template filling**

**Available locally:**
- qwen2.5 (7b)
- mistral:7b
- deepseek-coder:6.7b

**Cost:** $0 (runs on server)

---

## **COST TARGETS**

**Daily budget:** <$5/day until revenue covers it

**Priority order:**
1. Local (Ollama) - $0
2. OpenRouter Free - $0
3. Paid APIs - Only when necessary

**Goal:** Trading revenue ($50-100/day) covers all API costs within 7 days.

---

## **TEAM ENFORCEMENT**

**All agents must:**
- Check if task can use free model first
- Default to OR-Free for routine work
- Only use paid models for revenue-critical work
- Report daily API spend to Arjuna

**Richie's responsibility:** Generate revenue to cover costs.

---

**⚡ Arjuna**  
_"Free first. Paid only when worth it."_
