# 🔐 CREDENTIALS & SERVICES NEEDED FOR LEADFLOW AI

**Project:** LeadFlow AI Launch  
**Timeline:** Start tomorrow when credentials provided  
**Access Method:** Master email + password (you provide, we signup everywhere)

---

## 📋 **PRIORITY 1: MUST HAVE (Day 1)**

These are required to build and test the system.

---

### **1. LinkedIn Account**
**What we need:** Login credentials (email + password)  
**Used for:** Scraping B2B leads, automation  
**Options:**
- **Option A:** Your existing LinkedIn account (safest but may get restricted)
- **Option B:** Create new "agency" LinkedIn account (recommended)
  - Sign up: https://www.linkedin.com/signup
  - Name: "Ingversions Digital" or similar
  - Use your master email

**Cost:** Free  
**Risk:** LinkedIn may flag automation (we'll be careful, use slow scraping)

**What we'll do:**
- Sonic builds n8n workflow to scrape profiles
- Extract: Name, Title, Company, Email (if available)
- Target: 50 leads/day (conservative to avoid flags)

---

### **2. Email Service (for sending/receiving)**
**What we need:** SMTP credentials OR API key  
**Used for:** Sending leads to clients, automated emails  

**Recommended: SendGrid (Best for automation)**
- Sign up: https://sendgrid.com/pricing/ 
- **Free tier:** 100 emails/day (enough for testing)
- **Paid:** $19.95/month for 50,000 emails
- Use your master email to signup

**Alternative: Gmail SMTP**
- Use your master email's Gmail account
- Enable "App Passwords": https://myaccount.google.com/apppasswords
- Free but limited (500 emails/day)

**What we need from you:**
- If SendGrid: API Key (we'll get after signup)
- If Gmail: Email + App Password

**What we'll do:**
- Dexter configures agentmail-integration
- Automated lead delivery emails
- Client onboarding emails

---

### **3. Google Account (Sheets + Drive)**
**What we need:** Google login credentials  
**Used for:** Storing leads, client data, dashboards  

**Sign up:** https://accounts.google.com/signup (use your master email)

**Cost:** Free (15GB storage included)

**What we'll do:**
- Sonic creates Google Sheets for lead storage
- Automated CSV exports for clients
- Dashboard data (until we build proper database)

---

## 📋 **PRIORITY 2: NICE TO HAVE (Week 1)**

These unlock full automation but we can build without them initially.

---

### **4. Stripe (Payment Processing)**
**What we need:** Stripe account access  
**Used for:** Client payments ($297-1,997/month subscriptions)

**Sign up:** https://dashboard.stripe.com/register  
- Use your master email
- Requires: Business info, bank account for payouts

**Cost:** Free to setup, 2.9% + $0.30 per transaction

**Alternative:** Start without payments (manual invoicing), add later

**What we'll do:**
- Phineas integrates Stripe subscriptions
- Automatic billing every month
- Failed payment handling

---

### **5. Domain/Hosting Access**
**What we need:** Access to ingversionsdigital.com  
**Used for:** Landing page, client dashboard  

**What we need from you:**
- **Option A:** cPanel/FTP credentials (we upload files)
- **Option B:** Cloudflare/DNS access (we create subdomain)
- **Option C:** GitHub repo access (we push code, you deploy)

**If domain is on:**
- **Namecheap:** Dashboard login
- **GoDaddy:** Account access
- **Cloudflare:** Account login
- **Other:** Let us know provider

**What we'll do:**
- Henry uploads landing page
- Phineas deploys client dashboard
- Full site at: leadflow.ingversionsdigital.com (or /leadflow)

---

### **6. Airtable (Optional - Better than Google Sheets)**
**What we need:** Airtable account  
**Used for:** Lead database, client management, dashboards  

**Sign up:** https://airtable.com/signup  
- Use your master email
- **Free tier:** Unlimited bases, 1,200 records

**Cost:** Free tier enough for 10-15 clients, then $20/month

**Why use it:**
- Better than Google Sheets for dashboards
- Has API (easier integrations)
- Client-friendly interface

**What we'll do:**
- Phineas builds lead database
- Client self-service portal
- Real-time dashboard

---

## 📋 **PRIORITY 3: FUTURE SCALING (Month 2+)**

These are for when we have 10+ clients and need to scale.

---

### **7. Phantombuster (Advanced LinkedIn Scraping)**
**What we need:** Account + API key  
**Used for:** Higher volume LinkedIn scraping (more reliable than manual)

**Sign up:** https://phantombuster.com/pricing  
- **Free tier:** 2 hours/month execution time
- **Paid:** $59/month for 20 hours (enough for 500+ leads/day)

**What we'll do:**
- Sonic replaces basic scraper with Phantombuster
- Scale to 200+ leads/day per client
- More reliable, less likely to get flagged

---

### **8. Make.com (Alternative to n8n)**
**What we need:** Account  
**Used for:** Backup automation platform (if n8n limitations hit)

**Sign up:** https://www.make.com/en/register  
- **Free tier:** 1,000 operations/month
- **Paid:** $9/month for 10,000 operations

**When we use it:**
- If n8n becomes limiting
- For specific integrations n8n doesn't support

---

### **9. Zapier (Another automation option)**
**Sign up:** https://zapier.com/sign-up  
- Most expensive option
- Only if n8n + Make.com don't work

**We probably won't need this** (n8n is better and free)

---

## 🎯 **RECOMMENDED SETUP TOMORROW**

### **When you give us master email + password, we'll:**

**Immediately sign up for:**
1. ✅ LinkedIn (new agency account recommended)
2. ✅ SendGrid (free tier for email)
3. ✅ Google Account (Sheets, Drive)
4. ✅ Airtable (lead database)

**Week 1:**
5. ✅ Stripe (when ready to accept payments)

**Later (if needed):**
6. ✅ Phantombuster (for scaling)

---

## 📊 **COST BREAKDOWN**

### **Month 1 (Testing Phase):**
- LinkedIn: **$0** (free account)
- SendGrid: **$0** (free tier - 100 emails/day)
- Google: **$0** (free tier)
- Airtable: **$0** (free tier)
- **Total: $0**

### **Month 1 (Production - First Clients):**
- SendGrid: **$19.95** (50,000 emails/month)
- Airtable: **$0** (free tier enough for ~10 clients)
- Stripe: **$0** (just transaction fees: 2.9%)
- **Total: ~$20/month**

### **Month 2+ (Scaling to 20+ clients):**
- SendGrid: **$19.95**
- Airtable: **$20** (if we exceed free tier)
- Phantombuster: **$59** (optional, for higher volume)
- **Total: ~$40-100/month**

**ROI:** With just 1 client at $497/month, we're profitable immediately.

---

## 🔐 **SECURITY NOTES**

**Master Email + Password Approach:**
- ✅ **Good:** Fast signup, we handle everything
- ⚠️ **Risk:** All services use same credentials (if leaked, all compromised)

**Recommendations:**
1. **Use a NEW email** just for these services (not your main email)
2. **Use a STRONG password** (we'll never expose it)
3. **Enable 2FA later** (after we set everything up)
4. **Share via secure method** (Telegram is fine, or encrypted paste)

**What we'll do:**
- Store credentials in `~/.openclaw/workspace/agents/.credentials` (encrypted)
- Never expose in code or logs
- Only agents who need them get access

---

## 📝 **SIMPLE CREDENTIAL TEMPLATE**

**When you're ready tomorrow, just send this:**

```
MASTER EMAIL: your-email@example.com
MASTER PASSWORD: YourStrongPassword123!

OPTIONAL (if you want to provide separately):
LINKEDIN EMAIL: (if different from master)
LINKEDIN PASSWORD: (if different from master)

DOMAIN ACCESS:
- Provider: (Namecheap/GoDaddy/Cloudflare/Other)
- Login: (if different from master email)
```

**That's it. We handle the rest.**

---

## ⚡ **TIMELINE AFTER WE GET CREDENTIALS**

**Day 1 (Tomorrow):**
- Volt: Secure all credentials, store encrypted
- Sonic + Phineas: Sign up for all Priority 1 services
- Henry: Create agency LinkedIn profile (professional setup)

**Day 2-3:**
- Sonic: Build n8n lead gen workflow
- Test with real LinkedIn scraping
- Generate first 50 leads

**Day 4-7:**
- Full system build continues
- Landing page, payments, dashboard

**Day 8:**
- System ready for first client

---

## 🚀 **READY TO START**

**Tomorrow, just send:**
1. Master email
2. Master password
3. (Optional) Any specific requirements

**We'll:**
- Sign up for everything
- Update you with progress
- Show you first 50 leads by Day 3

**No more questions. Just execute.**

---

**Saved as:** `agents/CREDENTIALS_NEEDED.md`

📋 **Quick Reference Links:**

**Priority 1 (Sign up tomorrow):**
- LinkedIn: https://www.linkedin.com/signup
- SendGrid: https://sendgrid.com/pricing/
- Google: https://accounts.google.com/signup
- Airtable: https://airtable.com/signup

**Priority 2 (Week 1):**
- Stripe: https://dashboard.stripe.com/register

**Priority 3 (Later):**
- Phantombuster: https://phantombuster.com/pricing

---

⚡ **Volt** + 🎼 **Aria** + 💨 **Sonic** + 😈 **Henry** + 🔧 **Phineas**  
_"Credentials → Execution. We'll take it from there."_
