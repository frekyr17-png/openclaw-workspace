# GOLD-001 Demo Setup Report

## ✅ XAUUSDT Futures Availability: CONFIRMED

XAUUSDT (Gold/USD futures) is **available on Binance Futures testnet**.
Current price: **$5,248.88**

---

## 🤖 Bot Configuration: GOLD-001

| Parameter | Value |
|-----------|-------|
| **Bot ID** | GOLD-001 |
| **Strategy Name** | Gold Momentum Hunter |
| **Type** | Momentum (trend-following) |
| **Market** | XAUUSDT (Gold/USD Futures) |
| **Timeframe** | 1H |
| **Status** | Active |
| **Deployed** | 2026-03-03 |
| **Expires** | 2026-04-03 |

---

## 📊 Trade Parameters

| Setting | Value | Notes |
|---------|-------|-------|
| **Entry Signal** | Momentum trigger | ROC(5) > 2% + volume confirmation |
| **Profit Target** | 2-3% | Custom (vs standard 5%) |
| **Stop Loss** | 1% below entry | Tighter risk management |
| **Position Size** | $100 allocation | Demo size |
| **Network** | Binance Testnet | Paper trading only |

---

## 🎯 First Trade Signals

**Current Status:** `HOLD` - No entry yet

**Market Conditions:**
- ROC(5): -1.11% (slight downtrend)
- ROC(10): -1.81% (medium-term weak)
- Momentum strength: 2.92 (below 4% threshold)

**Entry Criteria:**
- BUY signal: ROC(5) > 2.0% + volume > 1.0
- SELL signal: ROC(5) < -2.0% + volume < 1.0

---

## ⚙️ Cron Job Setup

Scanning: **Every 5 minutes** (Mon-Fri)

```
*/5 * * * 1-5 /usr/bin/python3 /root/.openclaw/workspace/trading-lab/trader.py >> /root/.openclaw/workspace/trading-lab/trader.log 2>&1
```

All 8 active strategies are scanned together (including GOLD-001).

---

## 📈 Current Portfolio Status

| Bot | Market | Type | Status | Trades |
|-----|--------|------|--------|--------|
| ALPHA-001 | BTC/USDT | Trend | Active | 2 (1 win, 1 loss) |
| BETA-001 | ETH/USDT | MeanRev | Active | 1 (pending) |
| GAMMA-001 | BTC/USDT | Breakout | Active | 0 |
| DELTA-001 | ETH/USDT | Momentum | Active | 1 (pending) |
| EPSILON-001 | BTC/USDT | Swing | Active | 1 (pending) |
| ZETA-001 | SOL/USDT | Momentum | Active | 1 (pending) |
| ETA-001 | XRP/USDT | Trend | Active | 3 (1 win, 1 loss, 1 pending) |
| **GOLD-001** | **XAUUSDT** | **Momentum** | **Active** | **0** |

---

## ⚠️ Issues / Notes

1. **No immediate signal** - Gold is in slight consolidation, waiting for momentum breakout
2. **Testnet only** - Paper trading, no real funds at risk
3. **Custom targets** - Modified trader.py to handle 2.5% target / 1% stop loss (vs standard 5%)
4. **Fast-track enabled** - GOLD-001 will get evaluated after 1 month with accelerated feedback

---

## 📋 Next Steps

1. **Monitor cron** - Auto-scan every 5 min will catch momentum signals
2. **Review daily** - Check daily reports for trade activity
3. **Extend to live** - After demo success, can connect to Binance live with real funds

---

*Report generated: 2026-03-03*
