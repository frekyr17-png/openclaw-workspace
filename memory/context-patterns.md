# context-patterns.md — Repeated Errors & Solutions

**Purpose:** Track patterns of repeated mistakes and proven solutions.

**Last updated:** 2026-03-04 06:50 UTC

---

## Pattern Tracking Format

```
## Pattern: [Category]

**Instances:** [When/how often it happens]

**Root cause:** [Why it keeps happening]

**Solution:** [What fixes it reliably]

**Confidence:** ⭐⭐⭐⭐⭐ (1-5 stars)
```

---

## Patterns Identified

### Pattern: Stale Workspace Lists

**Instances:** 
- 2026-03-03: Ollama model list not refreshed after pull
- 2026-02-25: Trading strategy list outdated after restart
- Multiple mentions from Rahul

**Root cause:** Lazy file reads. Assuming cache is current instead of refreshing.

**Solution:** 
1. Always run `git status` before reading lists
2. Check timestamps on state files (git log)
3. Refresh before any agent report

**Confidence:** ⭐⭐⭐⭐⭐ (100% proven)

---

### Pattern: Token Bloat on Main Session Load

**Instances:**
- 2026-03-03: 2,600 tokens for simple startup
- Complaint: "This is too much context"

**Root cause:** Loading full AGENTS.md, MEMORY.md, plus consolidated docs without consolidation.

**Solution:**
1. Quarterly consolidation audit (COMPONENT 1 did this)
2. Keep cross-references instead of duplication
3. Archive old memory to memory/archive/

**Confidence:** ⭐⭐⭐⭐⭐ (Fixed via CORE_IDENTITY consolidation)

---

## Auto-Escalation Rules

If a pattern appears 3+ times in 30 days: Flag for Aria/Arjuna review.

If blocking revenue: Immediate escalation to Rahul.

---

_Maintained by Bruce 🔒. Cross-referenced with corrections.md._
