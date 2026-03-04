# corrections.md — Logged Mistakes & Lessons

**Purpose:** Every mistake logged with lesson learned. Nothing repeated twice.

**Last updated:** 2026-03-04 06:50 UTC

---

## Format

```
### [Date] - [Mistake Category]

**What happened:** 
[What went wrong?]

**Why it happened:**
[Root cause]

**Lesson learned:**
[What to do differently next time]

**Status:** ✅ Fixed / 🔄 In Progress / ⏳ Pending Review
```

---

## Log

### 2026-03-04 - System File Redundancy

**What happened:** SOUL.md, IDENTITY.md, and AGENTS.md contained overlapping instructions, bloating token usage to 2,600 per session.

**Why it happened:** Files evolved organically without consolidation pass.

**Lesson learned:** Quarterly consolidation audit prevents bloat. Merge files when >30% overlap detected. Cross-reference via links instead of duplication.

**Status:** ✅ Fixed (COMPONENT 1 complete)

---

## Guidelines for Auto-Logging

**Trigger points:**
- Rahul corrects you
- You realize a repeated mistake
- A workflow fails twice
- Token usage spikes unexpectedly
- A task takes longer than estimated

**Do NOT log:**
- Normal edge cases (expected)
- One-time external API failures
- Routine debugging

---

_Maintained by Aria 🎼 with Bruce 🔒 oversight. Reviewed nightly at 23:00 UTC._
