# ⚡ SHOPIFY SETUP - QUICK REFERENCE CHECKLIST

## 🎯 FOR RAHUL (DO THIS NOW)

- [ ] Go to: https://partners.shopify.com/signup
- [ ] Email: `frekyr17@gmail.com`
- [ ] Verify email (check inbox)
- [ ] Complete profile:
  - Store name: `Rahul's Dev Lab`
  - Country: `India`
  - Business type: `Development/Theme building`
- [ ] In Partner Dashboard: **Stores → Add store**
- [ ] Create test store:
  - Name: `xauusd-mini-theme-dev`
  - Purpose: `Theme development`
  - Plan: `Development (free)`
- [ ] **Share store URL + API key with Rick**

**Time:** 20 minutes | **Impact:** Unblocks all development

---

## ✅ WHAT'S DONE (Rick)

- ✅ Shopify CLI installed
- ✅ Dawn theme cloned locally
- ✅ Documentation created
- ✅ Project tracked

---

## 🚀 FOR RICK (AFTER RAHUL CREATES STORE)

```bash
# 1. Authenticate
cd /root/.openclaw/workspace/shopify-dev/xauusd-mini-theme
shopify auth login
# Select: Development store
# Select: xauusd-mini-theme-dev

# 2. Start dev server
shopify theme dev --store=xauusd-mini-theme-dev

# 3. Open in browser
# http://localhost:9292 (local)
# https://xauusd-mini-theme-dev.myshopify.com (live)

# 4. Create custom sections
# Edit: sections/hero-xauusd.liquid
# Edit: assets/xauusd-theme.css

# 5. Deploy when ready
shopify theme push
```

---

## 📚 DOCUMENTATION

| File | Purpose |
|------|---------|
| `SHOPIFY_SETUP.md` | Full setup guide |
| `SHOPIFY_PHASE_STATUS.md` | Phase breakdown + status |
| `XAUUSD_CUSTOMIZATION.md` | Theme customization guide |
| `RICK_EXECUTION_REPORT.md` | Detailed execution report |
| `PROJECT_TRACKER.md` | Project tracking (entry #6) |

---

## 🎯 DEADLINE

**Complete by:** 2026-03-11 (7 days)  
**Status:** On track (awaiting Partner account signup only)

---

**Owner:** Rick 💻 | **Status:** Ready for Development
