# Trading Lab - Project Status

**Owner:** Volt (execution) | Aria (oversight)  
**Started:** 2025-02-21  
**Status:** 🟢 Active - Cycle 1  
**Goal:** Prove paper trading strategies → go live with winners

---

## Current State

### Objective
- **Daily target:** 10% profit per bot = $10/day per $100 allocation
- **Monthly target:** $200/month per bot
- **Phase:** Paper trading on Binance testnet (5K USDT + 5K USDC)

### Active Strategies (12 bots)

**5-minute scalping** (eval: continuous)
- KAPPA-001 (BTC)
- LAMBDA-001 (ETH)
- MU-001 (SOL)
- THETA-001 (XAU)
- IOTA-001 (XAU)

**1-hour fast track** (eval: March 7)
- ZETA-001 (SOL)
- ETA-001 (XRP) → **Leading at 55.6% win rate**

**4-hour standard** (eval: March 23)
- ALPHA-001 (BTC)
- BETA-001 (ETH)
- GAMMA-001 (BTC)
- DELTA-001 (ETH)
- EPSILON-001 (BTC)

### Rules
- **No trade in 24h** = adjust timeframe/strategy or kill the bot
- **Target:** 5-10% profit per trade
- **Method:** Trade frequency doesn't matter, hit the 10% daily target

---

## Next Milestones

- **Mar 7:** Evaluate ZETA & ETA (1-hour bots) - promote winners, adjust/kill losers
- **Mar 23:** Evaluate 5 standard bots (4-hour) - same criteria
- **End of Cycle 1:** Decide which strategies go live with real money

---

## Metrics to Track

- [ ] Daily: Bot trade activity (flag 24h silence)
- [ ] Weekly: Win rate, profit %, drawdown per bot
- [ ] Monthly: Total paper profit, best/worst performers

---

## Decisions Needed

- None currently. Volt monitoring daily, Aria reviewing weekly.

---

## Notes

- Switched to AGGRESSIVE mode 2026-02-23 (lower thresholds, faster execution)
- Cron running: every 4h (all bots) + every 1h (ZETA, ETA fast track) Mon-Fri
- Logs: `~/.openclaw/workspace/trading-lab/trader.log`
- State: `~/.openclaw/workspace/trading-lab/state.json`
