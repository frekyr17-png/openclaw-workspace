# TaxReady - Project Status

**Owner:** Volt (execution) | Aria (oversight)  
**Started:** 2025-02-22  
**Status:** 🟡 Running - No active development  
**Goal:** Tax prep SaaS prototype (currently demo/internal tool)

---

## Current State

### What It Is
Full-stack tax preparation tool:
- **Backend:** FastAPI (Python) on port 8000
- **Frontend:** Next.js on port 3003 (moved from 3000 due to conflict)
- **Deployment:** Docker Compose
- **Data:** Local storage in `./data`

### Infrastructure
- Running via Docker Compose at `/root/.openclaw/workspace/taxready/`
- Backend: http://localhost:8000
- Frontend: http://localhost:3003
- Both containers healthy and auto-restart

---

## Next Steps

- [ ] **Audit:** Review current features, decide if worth productizing
- [ ] **Decision:** Keep as internal tool vs. build for revenue?
- [ ] **If revenue:** Define MVP, pricing, target market
- [ ] **If internal:** Document and maintain minimally

---

## Metrics to Track

- Currently none (not revenue-generating)

---

## Decisions Needed

**Priority call:** Is TaxReady a revenue opportunity or just a side project?
- If revenue → Aria to scope MVP, timeline, market fit
- If side project → keep running, minimal maintenance

---

## Notes

- Port changed to 3003 on 2026-02-28 (3000 conflicted with copilot-proxy attempts)
- No active users, no traffic data
- Code quality unknown (needs review)
