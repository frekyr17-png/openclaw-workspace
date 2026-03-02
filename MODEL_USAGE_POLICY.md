# MODEL USAGE POLICY

**Updated:** 2026-03-02 19:48 UTC  
**Goal:** Save costs while maintaining quality

---

## **TIER 1: FREE MODELS** ($0/use)

### **For routine tasks, heartbeats, simple work:**

**Best general free model:**
- `OR-Free` - Auto-routes to best available free model
- `openrouter/free`

**Best for coding:**
- `Qwen3-Coder` - Free, good for code generation/review
- `openrouter/qwen/qwen3-coder:free`

**Best for speed:**
- `StepFun-Flash` - Fast responses
- `openrouter/stepfun/step-3.5-flash:free`

**Best for quality (free):**
- `Qwen3-80B` - High quality, still free
- `openrouter/qwen/qwen3-next-80b-a3b-instruct:free`

---

## **TIER 2: CHEAP CLAUDE** (~$0.25-1 per million tokens)

### **Claude Haiku 4** - When free isn't enough but don't need Opus

**Use for:**
- ✅ Chat/conversation
- ✅ Code reviews
- ✅ Documentation writing
- ✅ Medium complexity tasks
- ✅ Quick debugging

**Model:** `anthropic/claude-haiku-4`

**Cost:** ~90% cheaper than Opus

---

## **TIER 3: MID-TIER CLAUDE** (~$3-5 per million tokens)

### **Claude Sonnet 4.5** - Balanced quality/cost

**Use for:**
- ✅ Complex coding
- ✅ Architecture decisions
- ✅ Client-facing work
- ✅ Revenue-generating tasks

**Model:** `anthropic/claude-sonnet-4-5`

**Cost:** ~60% cheaper than Opus

---

## **TIER 4: PREMIUM** (~$15 per million tokens)

### **Claude Opus 4** - ONLY for critical work

**Use ONLY for:**
- ❌ Extremely complex problems
- ❌ Critical strategic decisions
- ❌ When free/cheap models fail

**Model:** `anthropic/claude-opus-4`

**Cost:** Most expensive

**NOTE:** `copilot-proxy/*` models REMOVED (not working)

---

## **USAGE RULES BY TASK**

### **Heartbeats:**
→ **OR-Free** or **StepFun-Flash** (free)

### **Simple chat/questions:**
→ **Claude Haiku 4.5** (cheap)

### **Code generation:**
→ **Qwen3-Coder** (free) or **Claude Haiku** (cheap)

### **Complex coding:**
→ **Claude Sonnet 4.5** (mid-tier)

### **Documentation:**
→ **Claude Haiku 4.5** (cheap)

### **Strategic decisions:**
→ **Claude Sonnet 4.5** (mid-tier)

### **Client deliverables:**
→ **Claude Sonnet 4.5** (mid-tier)

### **Last resort only:**
→ **Claude Opus 4.6** (premium)

---

## **COST COMPARISON**

**Daily usage estimate (200k tokens):**

| Task Mix | Old (Opus) | New (Smart) | Savings |
|----------|------------|-------------|---------|
| Heartbeats (50k) | $0.75 | $0.00 (free) | $0.75 |
| Chat (50k) | $0.75 | $0.15 (Haiku) | $0.60 |
| Coding (50k) | $0.75 | $0.00 (free) | $0.75 |
| Complex (50k) | $0.75 | $0.25 (Sonnet) | $0.50 |
| **TOTAL/day** | **$3.00** | **$0.40** | **$2.60** |
| **TOTAL/month** | **$90** | **$12** | **$78** |

**Yearly savings: ~$940**

---

## **DEFAULT MODEL OVERRIDE**

**Current default:** Claude Opus 4.6 (expensive)

**Recommended new default:** Claude Haiku 4.5 (cheap, good quality)

**To override for specific sessions:**
```bash
# Use Haiku for this session
/model copilot-proxy/claude-haiku-4.5

# Use free for heartbeats
/model OR-Free
```

---

## **TEAM ENFORCEMENT**

**All agents must:**
1. Start with free models
2. Escalate to Haiku if free isn't enough
3. Only use Sonnet for complex/revenue work
4. Never use Opus without Arjuna approval

**Richie must:** Generate enough revenue to cover API costs within 7 days

---

⚡ **Arjuna**  
_"Smart model selection = 87% cost savings"_
