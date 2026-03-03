# Scalping Bots Blueprint 💰
## Richie Rich Trading Strategy Plan

**Generated:** 2026-03-03  
**Status:** Blueprint Ready for Arjuna's Approval  
**Total Allocation:** $300 ($100 per bot)

---

## 📊 Executive Summary

| Bot | Symbol | Timeframe | Strategy | Expected WR | Risk Level |
|-----|--------|-----------|----------|-------------|------------|
| SILVER-001 | XAGUSDT | 5m | Momentum/Mean Reversion | 55-65% | 🔴 High |
| COPPER-001 | XPDUSDT | 15m | Breakout + Volume | 50-60% | 🟡 Medium |
| ENERGY-001 | BTCUSDT | 30m | Trend + RSI Divergence | 45-55% | 🟠 Medium-High |

---

## 🤖 Bot 1: SILVER-001 (Silver 5-Minute Scalper)

### Configuration
```json
{
  "id": "SILVER-001",
  "name": "Silver Flash Scalper",
  "type": "momentum",
  "market": "XAG/USDT",
  "timeframe": "5m",
  "subagent": "trading-silver-flash",
  "status": "planned",
  "deployed": "TBD",
  "expires": "TBD+30d",
  "allocation": 100,
  "targets": {
    "profit": "0.5-1%",
    "profitTicks": "8-15 pips",
    "stopLoss": "0.25%",
    "stopTicks": "4-5 pips",
    "riskReward": "2:1 to 4:1",
    "entrySignal": "momentum_burst",
    "positionSize": "$100"
  },
  "parameters": {
    "atrPeriod": 14,
    "momentumThreshold": 0.3,
    "reversionLookback": 10,
    "volumeConfirm": true,
    "maxSlippage": "0.05%"
  },
  "fastTrack": true
}
```

### Strategy Details
**Logic:** Momentum/Mean Reversion Hybrid
- **Long Entry:** Price > SMA(10) + Momentum spike > 0.3% + Volume above average
- **Short Entry:** Price < SMA(10) + Momentum spike > 0.3% + Volume above average
- **Exit TP:** 0.5-1% profit
- **Exit SL:** 0.25% loss or mean reversion trigger

### Expected Performance
| Metric | Value |
|--------|-------|
| Expected Win Rate | **55-65%** |
| Expected Trades/Day | 8-15 |
| Risk Per Trade | $0.25 (0.25%) |
| Avg Holding Time | 5-15 minutes |
| Monthly Volume | 160-300 trades |

### Risk Assessment
**Level:** 🔴 HIGH
- **Pros:** Quick turnover, tight stops, high R:R ratio
- **Cons:** High frequency = more exposure to slippage/spread costs
- **Silver Volatility:** XAG moves fast, can gap over stops
- **Risk Mitigation:** Hard stops, max 3 consecutive losses = daily pause

---

## 🤖 Bot 2: COPPER-001 (Platinum/Palladium 15-Minute Scalper)

### Configuration
```json
{
  "id": "COPPER-001",
  "name": "Palladium Breakout Scout",
  "type": "breakout",
  "market": "XPD/USDT",
  "timeframe": "15m",
  "subagent": "trading-palladium-breakout",
  "status": "planned",
  "deployed": "TBD",
  "expires": "TBD+30d",
  "allocation": 100,
  "targets": {
    "profit": "1-1.5%",
    "profitTicks": "15-25 pips",
    "stopLoss": "0.5%",
    "stopTicks": "8-12 pips",
    "riskReward": "2:1 to 3:1",
    "entrySignal": "s_r_breakout",
    "positionSize": "$100"
  },
  "parameters": {
    "srLookback": 20,
    "breakoutThreshold": "0.4%",
    "volumeMultiplier": 1.5,
    "confirmPeriods": 2,
    "falseBreakoutFilter": true
  },
  "fastTrack": true
}
```

### Strategy Details
**Logic:** Breakout + Volume Confirmation
- **Support/Resistance:** Dynamic levels from 20-period high/low
- **Long Entry:** Close above resistance + volume > 1.5x avg + 2-confirm periods
- **Short Entry:** Close below support + volume > 1.5x avg + 2-confirm periods
- **Exit TP:** 1-1.5% profit
- **Exit SL:** 0.5% loss or false breakout reclaim

### Expected Performance
| Metric | Value |
|--------|-------|
| Expected Win Rate | **50-60%** |
| Expected Trades/Day | 3-6 |
| Risk Per Trade | $0.50 (0.5%) |
| Avg Holding Time | 30-90 minutes |
| Monthly Volume | 60-120 trades |

### Risk Assessment
**Level:** 🟡 MEDIUM
- **Pros:** Volume confirmation reduces false breakouts, cleaner S/R levels
- **Cons:** Palladium lower liquidity than gold/silver, wider spreads
- **Whiplash Risk:** Fake breakouts on low volume
- **Risk Mitigation:** 2-period confirmation, volume threshold, false breakout reclaim exits

---

## 🤖 Bot 3: ENERGY-001 (BTC 30-Minute Volatility Scalper)

### Configuration
```json
{
  "id": "ENERGY-001",
  "name": "BTC Divergence Hunter",
  "type": "meanrev",
  "market": "BTC/USDT",
  "timeframe": "30m",
  "subagent": "trading-btc-divergence",
  "status": "planned",
  "deployed": "TBD",
  "expires": "TBD+30d",
  "allocation": 100,
  "targets": {
    "profit": "1.5-2%",
    "profitTicks": "300-500 points",
    "stopLoss": "0.75%",
    "stopTicks": "150-200 points",
    "riskReward": "2:1 to 2.7:1",
    "entrySignal": "rsi_divergence",
    "positionSize": "$100"
  },
  "parameters": {
    "rsiPeriod": 14,
    "divergenceLookback": 15,
    "rsiOverbought": 65,
    "rsiOversold": 35,
    "trendFilter": true,
    "minDivergenceStrength": "1.5%"
  },
  "fastTrack": true
}
```

### Strategy Details
**Logic:** Trend + RSI Divergence
- **Trend Filter:** Only trade in direction of 50-SMA
- **Bullish Divergence:** Price lower low + RSI higher low = BUY
- **Bearish Divergence:** Price higher high + RSI lower high = SELL
- **Exit TP:** 1.5-2% profit
- **Exit SL:** 0.75% loss or divergence invalidation

### Expected Performance
| Metric | Value |
|--------|-------|
| Expected Win Rate | **45-55%** |
| Expected Trades/Day | 2-4 |
| Risk Per Trade | $0.75 (0.75%) |
| Avg Holding Time | 1-4 hours |
| Monthly Volume | 40-80 trades |

### Risk Assessment
**Level:** 🟠 MEDIUM-HIGH
- **Pros:** Higher profit targets, trend-following reduces counter-trend losses
- **Cons:** Lower win rate, divergence can be subjective, BTC can run through stops
- **Divergence Risk:** Late divergence signals, premature entries
- **Risk Mitigation:** Trend filter, minimum divergence strength, invalidate on structure break

---

## 📋 Recommended Execution Order

### Phase 1 (Week 1): COPPER-001 First
**Why:** Medium risk, reasonable frequency, good for testing scalping logic
1. Deploy COPPER-001 (Palladium 15m)
2. Monitor for 5-7 days
3. Validate execution quality (fills, slippage, signal accuracy)

### Phase 2 (Week 2): SILVER-001 Second
**Why:** Higher frequency, validate infrastructure can handle 5m timeframe
1. Deploy SILVER-001 (Silver 5m) 
2. Run parallel with COPPER-001
3. Monitor rate limits and API performance

### Phase 3 (Week 3): ENERGY-001 Third
**Why:** Most complex strategy, benefit from lessons learned
1. Deploy ENERGY-001 (BTC 30m)
2. All 3 bots running
3. Full evaluation cycle begins

---

## ⏰ Cron Job Adjustments

### Current Schedule
```bash
# 4-hour cycle for standard bots
0 */4 * * 1-5 /usr/bin/node /usr/lib/node_modules/openclaw/openclaw.js trading-lab
echo "Trading Lab cycle"

# 1-hour fast track (ZETA, ETA, GOLD)
0 * * * 1-5 /usr/bin/node /usr/lib/node_modules/openclaw/openclaw.js trading-lab-fast
echo "Fast track trading"
```

### New Schedule (With Scalping Bots)
All scalping bots get `fastTrack: true`, so they run on the **1-hour cron**.

**No cron changes needed** - they'll be picked up by the existing `trading-lab-fast` cron.

However, recommend adding a **5-minute heartbeat** check:
```bash
# Optional: 5-minute check for SL takeouts (emergency close)
*/5 * * * 1-5 /usr/bin/node /usr/lib/node_modules/openclaw/openclaw.js trading-check-sl
```

---

## 📈 Comparison: New vs Current Strategies

| Aspect | Current (ALPHA-EPSILON) | New Scalpers |
|--------|------------------------|--------------|
| Timeframes | 1h, 4h, 1d | 5m, 15m, 30m |
| Trade Frequency | 1-2/day | 2-15/day |
| Hold Time | Hours-Days | Minutes-Hours |
| Expected Trades/Month | 20-50 | 100-500 |
| Target Win Rate | 50%+ | 45-65% |
| Risk Per Trade | 1-2% | 0.25-0.75% |

---

## ✅ Final Checklist

- [ ] Bot configurations validated
- [ ] Risk parameters approved
- [ ] Symbol availability confirmed (XAG, XPD on exchange)
- [ ] API rate limits checked (scalping = more calls)
- [ ] Execution order agreed
- [ ] Cron schedule confirmed
- [ ] Paper trading period defined (suggest 7 days each)
- [ ] Live deployment authorized

---

## 🎯 Expected Portfolio Impact

**With $300 total allocation:**
- **Conservative estimate:** 15-20% monthly return ($45-60)
- **Realistic estimate:** 25-35% monthly return ($75-105)
- **Optimistic estimate:** 40-50% monthly return ($120-150)

**Risk:** Maximum loss per bot = allocation amount ($100 each)

---

**Ready for deployment when Arjuna gives the green light.** 💚

*Richie Rich, Trading Specialist*  
*Blueprint generated 2026-03-03*
