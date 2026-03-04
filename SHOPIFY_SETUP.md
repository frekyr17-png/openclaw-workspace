# 🛍️ SHOPIFY MINI THEME SETUP GUIDE

**Project:** XAU/USD Mini Theme Development  
**Owner:** Rick 💻 (Development)  
**Status:** Phase 1-3 Complete | Awaiting Partner Account  
**Created:** 2026-03-04 20:36 UTC  
**Target Completion:** 2026-03-11 (7 days)

---

## 📋 PROJECT OVERVIEW

Build a custom Shopify theme based on the **Dawn framework** for XAU/USD trading integration. The theme will be developed on a Shopify Partner developer store and pushed to production later.

**Scope:**
- Homepage variant with trading data visualization
- Custom Liquid components for market updates
- CSS styling aligned with XAU/USD branding
- Full mobile responsiveness
- Development → Staging → Production deployment

---

## 🔑 ACCOUNT CREDENTIALS

| Item | Value | Status |
|------|-------|--------|
| **Email** | `frekyr17@gmail.com` | ⏳ Pending Partner Signup |
| **Partner Account** | "Rahul's Dev Lab" | ⏳ Not Created |
| **Dev Store Name** | `xauusd-mini-theme-dev` | ⏳ Not Created |
| **Store URL** | TBD (after store creation) | ⏳ Pending |
| **API Key** | TBD | ⏳ Pending |
| **Access Token** | TBD | ⏳ Pending |

---

## ✅ INSTALLATION CHECKLIST

### Phase 1: Partner Account Setup (⏳ MANUAL REQUIRED)

- [ ] Go to https://partners.shopify.com/signup
- [ ] Sign up with **frekyr17@gmail.com**
- [ ] Verify email (check inbox for verification link)
- [ ] Complete profile:
  - Store Name: **Rahul's Dev Lab**
  - Country: **India**
  - Business Type: **Development/Theme building**
  - Company URL: (optional)
  - Phone: (optional)
- [ ] Confirm Partner account active

### Phase 2: Create Developer Store (⏳ AFTER PHASE 1)

1. Log in to Shopify Partner Dashboard
2. Navigate: **Stores** → **Add store**
3. Create test store with:
   - **Name:** `xauusd-mini-theme-dev`
   - **Purpose:** Theme development
   - **Plan:** Development (free)
   - **Store URL:** Will be auto-generated (e.g., `xauusd-mini-theme-dev.myshopify.com`)
4. Copy store credentials:
   - Store URL: `_________________________`
   - Admin API access token: `_________________________`
   - API key: `_________________________`

### Phase 3: Shopify CLI Installation (✅ COMPLETE)

**Status:** Done on 2026-03-04 20:36 UTC

```bash
# Already installed globally
npm install -g @shopify/cli

# Verify installation
shopify version
# Expected: @shopify/cli/X.X.X
```

### Phase 4: Theme Initialization (✅ COMPLETE)

**Status:** Dawn skeleton theme cloned to `/root/.openclaw/workspace/shopify-dev/xauusd-mini-theme/`

```bash
cd /root/.openclaw/workspace/shopify-dev/xauusd-mini-theme

# Directory structure:
# ├── assets/          (CSS, JS, images)
# ├── blocks/          (Custom sections)
# ├── config/          (theme.json settings)
# ├── layout/          (theme.liquid - base template)
# ├── locales/         (translations)
# ├── sections/        (reusable Liquid components)
# ├── snippets/        (small Liquid components)
# └── templates/       (page templates - index, product, etc.)
```

---

## 🚀 DEVELOPMENT WORKFLOW

### Step 1: Authenticate with Dev Store

```bash
cd /root/.openclaw/workspace/shopify-dev/xauusd-mini-theme

# Authenticate Shopify CLI with your dev store
shopify auth login

# Select: Development store
# Select: xauusd-mini-theme-dev (when available)
# Complete OAuth flow in browser
```

**Expected Output:**
```
✓ Successfully authenticated
✓ Organization: Rahul's Dev Lab
✓ Store: xauusd-mini-theme-dev
```

### Step 2: Start Development Server

```bash
# Start local development server
shopify theme dev --store=xauusd-mini-theme-dev

# This will:
# - Serve theme on http://localhost:9292
# - Watch for file changes
# - Sync changes to dev store in real-time
# - Show live preview URL (e.g., https://xauusd-mini-theme-dev.myshopify.com/)
```

### Step 3: Build Liquid Components

**Custom homepage component example:**

File: `sections/xauusd-hero.liquid`
```liquid
{% schema %}
{
  "name": "XAU/USD Hero",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Live Gold Prices"
    }
  ]
}
{% endschema %}

<section class="hero hero--xauusd">
  <div class="hero__content">
    <h1>{{ section.settings.heading }}</h1>
    <!-- Trading data will go here -->
  </div>
</section>

{% stylesheet %}
.hero--xauusd {
  background: linear-gradient(135deg, #1a1a1a, #2d2d2d);
  color: #ffd700;
  padding: 60px 20px;
}
{% endstylesheet %}
```

### Step 4: Test on Dev Store

```bash
# Once development server is running:
# 1. Open the live preview URL
# 2. Edit theme in Shopify admin: https://xauusd-mini-theme-dev.myshopify.com/admin/themes
# 3. View live changes as you edit Liquid/CSS/JS
```

### Step 5: Deploy to Production

```bash
# Push theme to dev store (when ready)
shopify theme push

# This will prompt: "Are you sure?" - confirm

# After testing, convert dev store to live:
# (In Shopify Partner Dashboard > Stores)
```

---

## 📁 PROJECT REPOSITORY

**Location:** `/root/.openclaw/workspace/shopify-dev/xauusd-mini-theme/`

**Git Info:**
```bash
# Initialize git (if needed)
cd xauusd-mini-theme
git init
git remote add origin https://github.com/[YOUR_REPO]/xauusd-mini-theme.git

# Create .gitignore for Shopify
cat > .gitignore << 'EOF'
node_modules/
.shopify-cli.yml
*.env
dist/
EOF

# Commit initial state
git add .
git commit -m "Initial: Dawn theme skeleton"
git push -u origin main
```

---

## 🔧 USEFUL SHOPIFY CLI COMMANDS

| Command | Purpose |
|---------|---------|
| `shopify auth login` | Authenticate with store |
| `shopify auth logout` | Disconnect from store |
| `shopify theme dev` | Start local dev server |
| `shopify theme push` | Push theme to store |
| `shopify theme pull` | Pull live theme to local |
| `shopify theme delete` | Delete theme from store |
| `shopify theme list` | List all store themes |

---

## 📈 DEVELOPMENT PHASES

### Week 1 (2026-03-04 → 2026-03-11)

| Day | Task | Owner | Status |
|-----|------|-------|--------|
| Mon 3/4 | Partner account + CLI setup | Rick | ✅ CLI Done / ⏳ Account Pending |
| Tue 3/5 | Dev store creation | Rahul | ⏳ |
| Wed 3/6 | Theme auth + custom hero section | Rick | ⏳ |
| Thu 3/7 | CSS styling + mobile responsive | Rick | ⏳ |
| Fri 3/8 | XAU/USD integration (mock data) | Rick | ⏳ |
| Sat 3/9 | Testing + refinements | Rick | ⏳ |
| Sun 3/10 | Final deploy + documentation | Rick | ⏳ |

### Deliverables by 2026-03-11

- ✅ Working Shopify Partner account
- ✅ Developer store live
- ✅ Custom homepage with XAU/USD theme
- ✅ Mobile-responsive design
- ✅ Git repository with version control
- ✅ README + deployment docs

---

## 🛠️ TROUBLESHOOTING

### Issue: "Git can't clone the latest release with the 'shallow' property"

**Solution:** Clone manually from GitHub
```bash
git clone https://github.com/Shopify/skeleton-theme.git xauusd-mini-theme
```

### Issue: "Cannot authenticate with Shopify CLI"

**Solution:** Check environment
```bash
# Verify Node.js
node --version  # Should be v16+

# Reinstall CLI
npm install -g @shopify/cli@latest

# Clear auth cache
rm -rf ~/.config/shopify
shopify auth login
```

### Issue: "Theme changes not syncing to dev store"

**Solution:** Restart dev server
```bash
# Stop current server (Ctrl+C)
# Restart
shopify theme dev --store=xauusd-mini-theme-dev
```

---

## 📞 CONTACTS & RESOURCES

- **Shopify Partner Docs:** https://shopify.dev/docs/themes
- **Liquid Syntax:** https://shopify.dev/api/liquid
- **Theme Development:** https://shopify.dev/docs/themes/development
- **CLI Commands:** https://shopify.dev/docs/themes/tools/cli

---

## 🎯 NEXT STEPS

**Immediate (Rahul):**
1. Sign up for Shopify Partner: https://partners.shopify.com/signup
2. Create developer store "xauusd-mini-theme-dev"
3. Share store URL with Rick

**After Store Creation (Rick):**
1. Run `shopify auth login` to authenticate
2. Modify theme: add custom Liquid components
3. Deploy and test on dev store
4. Push final version to repository

---

**Created by:** Rick 💻  
**Project:** XAU/USD Mini Theme  
**Timeline:** Complete by 2026-03-11  
**Status:** Ready for Partner Account Signup
