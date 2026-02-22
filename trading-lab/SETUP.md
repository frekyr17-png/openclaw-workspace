# Trading Lab Setup

## Step 1: API Credentials

1. Copy the template:
   ```bash
   cp credentials.env.template credentials.env
   ```

2. Edit `credentials.env` with your real credentials

3. Fill in:
   - **Binance:** API Key + Secret (from Profile → API Management)
   - **Exness:** MT5 Login + Password + Server (from Personal Area)

## Step 2: Trading Preferences

1. Copy the template:
   ```bash
   cp preferences.json.template preferences.json
   ```

2. Edit `preferences.json`:
   - `markets` - What you want to trade
   - `timeframes` - Chart timeframes (e.g., 4h, 1d)
   - `riskPerTrade` - % risk per trade (1 = 1%)
   - `positionSize` - How much per position

## Step 3: Tell Me When Ready

Just say: **"credentials added"**

I'll verify the setup and launch the first 5 strategies.

---

## File Locations

```
trading-lab/
├── credentials.env      ← Your API keys (NEVER share this)
├── preferences.json     ← Your trading settings
├── state.json           ← Strategy tracking (auto-managed)
└── SETUP.md             ← This file
```

## Security

- `credentials.env` should NEVER be shared or committed to git
- I read it locally, it never leaves your machine
- Your chat history has NO credentials