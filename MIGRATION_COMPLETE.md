# ⚡ Volt Migration Package - Ready

## 📦 Backup Complete

**File:** `volt_backup_20260225_053809.tar.gz`  
**Size:** 251 MB  
**Created:** Feb 25, 2026 05:38 UTC

---

## 📥 Download Options

### Option 1: Direct HTTP Download (Easiest)
```bash
# On your laptop:
wget http://72.62.226.183:8000/volt_backup_20260225_053809.tar.gz
# Or open in browser:
# http://72.62.226.183:8000/volt_backup_20260225_053809.tar.gz
```

### Option 2: SCP (Secure)
```bash
# On your laptop:
scp root@72.62.226.183:/tmp/volt_backup_20260225_053809.tar.gz ~/Downloads/
```

### Option 3: SFTP Client
- Host: `72.62.226.183`
- User: `root`
- File: `/tmp/volt_backup_20260225_053809.tar.gz`

---

## 📋 What's Included

✅ **Complete workspace** (~/.openclaw/workspace)
- Trading Lab: state.json, trader.py, credentials.env, all 13 bot configs
- Memory files: MEMORY.md, daily logs, heartbeat state
- Agent configs: SOUL.md, USER.md, IDENTITY.md, AGENTS.md, TOOLS.md
- Skills: trading-lab skill + all references
- All projects: taxready, research files, etc.

✅ **OpenClaw configuration**
- API keys (Telegram, OpenRouter, etc.)
- Model configs
- Channel settings

✅ **System state**
- Crontab (trading bots schedule)
- Python packages list
- Docker state (n8n config)
- Environment details

✅ **Migration tools**
- RESTORE_ON_LAPTOP.sh (automated restore script)
- MANIFEST.md (full documentation)
- requirements.txt (exact Python environment)

---

## 🚀 Restore on Your Laptop

### Prerequisites
1. **Install OpenClaw:**
   ```bash
   npm install -g openclaw
   ```

2. **Install Python 3.10+** (if not already installed)

### Restore Steps

1. **Extract backup:**
   ```bash
   cd ~/Downloads  # or wherever you downloaded
   tar -xzf volt_backup_20260225_053809.tar.gz
   cd volt_backup_20260225_053809
   ```

2. **Run restore script:**
   ```bash
   bash RESTORE_ON_LAPTOP.sh
   ```

3. **Start OpenClaw:**
   ```bash
   openclaw gateway start
   ```

4. **Verify everything works:**
   ```bash
   # Test trading lab
   cd ~/.openclaw/workspace/trading-lab
   python3 trader.py
   
   # Should see: "Scanning 13 strategies..."
   ```

---

## ⚙️ Post-Migration Setup

### 1. Review Cron Jobs
Cron jobs from server are saved but NOT auto-installed.

**Current schedule (from server):**
- Every 4h: Full trading lab scan (all bots)
- Every 1h: Fast-track bots (ZETA, ETA)
- Every 5m: 5-minute scalpers (KAPPA, LAMBDA, MU, THETA, IOTA)

**On laptop:** You probably want different timing (e.g., only when laptop is awake).

```bash
# View saved cron:
cat crontab.txt

# Install (optional, review first):
crontab crontab.txt
```

### 2. Network Differences

**Server (Docker):**
- Always-on, 24/7 trading
- n8n on localhost:5678
- Public IP for webhooks

**Laptop:**
- Intermittent (sleep/wake cycles)
- Consider disabling always-on services (n8n Docker)
- VPN might affect API connections

### 3. Optional: Install n8n (if you want workflow automation)
```bash
docker run -d \
  --name n8n \
  -p 5678:5678 \
  -v ~/.openclaw/n8n_data:/home/node/.n8n \
  n8nio/n8n
```

### 4. Credentials Check

All credentials are preserved:
- **Binance testnet:** API keys in `trading-lab/credentials.env`
- **Telegram:** Configured in OpenClaw
- **OpenRouter API:** Configured in OpenClaw
- **Exness MT5:** Login/password in credentials.env

⚠️ **Important:** If laptop has different IP/network, you may need to:
- Re-whitelist IP on Binance (if using IP restrictions)
- Test Telegram connection: `openclaw chat`

---

## 🔍 Verify Migration Success

**Checklist:**
- [ ] OpenClaw gateway starts: `openclaw status`
- [ ] Trading lab runs: `python3 ~/.openclaw/workspace/trading-lab/trader.py`
- [ ] State file exists: `cat ~/.openclaw/workspace/trading-lab/state.json`
- [ ] Memory intact: `cat ~/.openclaw/workspace/MEMORY.md`
- [ ] Telegram works: Send message via OpenClaw
- [ ] Bots show correct stats (13 bots, recent trades)

---

## 🗑️ Clean Up Server (After Successful Migration)

Once everything works on laptop:

```bash
# On server:
openclaw gateway stop
docker stop n8n
# Optional: Remove OpenClaw
# npm uninstall -g openclaw
```

---

## 📊 Current Trading Lab State (Snapshot at Backup)

**13 bots running:**
- **Standard track (4h/1d):** ALPHA, BETA, GAMMA, DELTA, EPSILON
- **Fast track (1h):** ZETA (SOL), ETA (XRP)
- **5m scalpers:** KAPPA (BTC), LAMBDA (ETH), MU (SOL), THETA/IOTA (Gold), NU (Gold MTF)

**Recent performance:**
- ETA-001: 55.6% win rate, +2.82% net
- BETA-001: 100% win rate, +5.29% net
- EPSILON-001: Hit -8.16% loss, re-entered

**All state preserved** → You can continue exactly where you left off.

---

## 🆘 Troubleshooting

**"OpenClaw not found"**
→ `npm install -g openclaw`

**"ModuleNotFoundError: ccxt"**
→ `pip3 install ccxt oandapyV20`

**"Permission denied"**
→ `chmod +x RESTORE_ON_LAPTOP.sh`

**Trading bots not running**
→ Check credentials: `cat ~/.openclaw/workspace/trading-lab/credentials.env`

**Need help?**
→ Telegram: Message Volt (me) once OpenClaw is running

---

## ⚡ Status

✅ Backup created  
✅ HTTP server running on port 8000  
✅ Ready for download  
✅ Restore script included  
✅ Full migration guide prepared  

**Next:** Download backup to your laptop and run `RESTORE_ON_LAPTOP.sh`

---

_Generated: 2026-02-25 05:40 UTC_  
_Volt → Laptop Migration_
