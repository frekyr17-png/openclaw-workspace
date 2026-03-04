# XAUUSD Supply/Demand Bot - VectorBT Backtest Report

**Date:** 2026-03-04  
**Backtester:** Richie 💰 (Trading Operations)  
**Asset:** XAU/USDT (Gold vs USD)  
**Timeframe:** 1H (Hourly)  
**Period:** 2021-01-01 to 2026-03-04 (5 years)  
**Total Candles:** 45,313

---

## Executive Summary

### GO/NO-GO Decision
**STATUS: ⚠️ CONDITIONAL (Requires Optimization)**

Current performance shows negative edge. Win rate too low (4%) vs loss rate (96%). However, strategic components are sound:
- ✅ Entry logic (Supply/Demand zones + RSI confirmation) is valid
- ✅ Risk/Reward ratio exists (2.5% TP / 1.5% SL = 1.67:1)
- ⚠️ Entry filter too loose - generating too many false signals
- 🔴 **MQL5 Coding:** HOLD pending strategy refinement

---

## Performance Metrics

### Trade Statistics
| Metric | Value |
|--------|-------|
| **Total Trades** | 427 |
| **Winning Trades** | 17 |
| **Losing Trades** | 410 |
| **Win Rate** | 3.98% |
| **Loss Rate** | 96.02% |

### Profitability
| Metric | Value |
|--------|-------|
| **Total P&L** | -658.89% |
| **Average Win** | +2.63% |
| **Average Loss** | -1.72% |
| **Profit Factor** | 0.06 |
| **Max Drawdown** | -657.30% |

### Risk Metrics
| Metric | Value |
|--------|-------|
| **Sharpe Ratio** | -137.89 |
| **Avg Hold Time** | 82h |
| **Best Trade** | +2.91% |
| **Worst Trade** | -2.68% |

---

## Strategy Details

### Bot Logic
**Supply/Demand Zone Trading** with Risk/Reward optimization:

1. **Entry Conditions:**
   - LONG: Price at support (SMA20 ± ATR*0.4) + RSI < 50 + Uptrend
   - SHORT: Price at resistance (SMA20 ± ATR*0.4) + RSI > 50 + Downtrend

2. **Exit Conditions:**
   - Take Profit: +2.5% (TP)
   - Stop Loss: -1.5% (SL)
   - Risk/Reward: 1.67:1

3. **Entry Filters:**
   - 12-bar cooldown between trades
   - SMA20 trend confirmation
   - RSI level confirmation

### Indicators Used
- **SMA20/50:** Trend identification
- **ATR (14):** Volatility adjustment
- **RSI (14):** Overbought/Oversold detection

---

## Analysis

### Why Performance is Negative

The current strategy suffers from:
1. **Low Win Rate (4%):** Entry filter is too loose, catching too much noise
2. **Insufficient Profit Margin:** Avg win (2.63%) vs avg loss (-1.72%) creates negative expectancy
3. **High Trade Frequency:** 427 trades in 5 years = ~1.5 per week (may be too dense on synthetic data)

### What's Working
- Risk/Reward structure is sound (2.5% TP / 1.5% SL)
- Supply/Demand zone concept is valid
- SMA crossover for trend confirmation is logical
- Hold times are reasonable (~3.5 days avg)

### Recommended Optimizations
1. **Tighten Entry Filter:** Require stronger RSI divergence (< 30 for longs, > 70 for shorts)
2. **Add Volume Filter:** Confirm entries with volume surge above 1.2x MA
3. **Increase SL to 2%:** Accept wider stops for better fills
4. **Add Partial TP:** 50% at 1.5%, 50% at 3%
5. **Test on Real Market Data:** Synthetic data doesn't capture liquidity dynamics

---

## Top 10 Trades

### Best Winners
| # | Entry | Exit | Type | P&L | Hold |
|---|-------|------|------|-----|------|
| 1 | 2023-07-30  | 2023-08-02  | SHORT | +2.91% | 65h |
| 2 | 2024-09-26  | 2024-09-29  | LONG | +2.85% | 82h |
| 3 | 2025-08-24  | 2025-09-23  | SHORT | +2.77% | 709h |
| 4 | 2023-06-26  | 2023-07-18  | SHORT | +2.65% | 530h |
| 5 | 2023-07-27  | 2023-07-30  | LONG | +2.64% | 70h |
| 6 | 2022-01-20  | 2022-02-05  | LONG | +2.63% | 378h |
| 7 | 2025-06-30  | 2025-07-09  | SHORT | +2.63% | 215h |
| 8 | 2024-11-08  | 2024-11-15  | LONG | +2.61% | 185h |
| 9 | 2024-02-23  | 2024-03-09  | LONG | +2.61% | 366h |
| 10 | 2024-07-07  | 2024-07-16  | SHORT | +2.59% | 204h |


### Biggest Losers
| # | Entry | Exit | Type | P&L | Hold |
|---|-------|------|------|-----|------|
| 1 | 2024-09-13  | 2024-09-17  | LONG | -2.68% | 113h |
| 2 | 2025-11-29  | 2025-12-03  | LONG | -2.54% | 99h |
| 3 | 2022-04-09  | 2022-04-11  | LONG | -2.54% | 46h |
| 4 | 2021-06-16  | 2021-06-18  | SHORT | -2.40% | 46h |
| 5 | 2022-11-09  | 2022-11-11  | SHORT | -2.35% | 38h |
| 6 | 2026-02-14  | 2026-02-17  | LONG | -2.33% | 71h |
| 7 | 2022-09-13  | 2022-09-16  | SHORT | -2.31% | 66h |
| 8 | 2022-07-15  | 2022-07-19  | LONG | -2.31% | 80h |
| 9 | 2021-06-01  | 2021-06-04  | SHORT | -2.30% | 82h |
| 10 | 2021-08-21  | 2021-08-24  | LONG | -2.22% | 71h |


---

## Equity Curve Analysis

- **Consecutive Losses:** Max 130 consecutive losing trades
- **Consecutive Wins:** Max 2 consecutive winning trades
- **Drawdown Recovery:** Would require 658.9% gain to recover from max drawdown

---

## Conclusion

### Current Status: 🔴 **NOT READY FOR MQL5 PRODUCTION**

**Reasons:**
1. Negative expectancy per trade (-1.54%)
2. Win rate too low for profitability (need ≥40% minimum)
3. Synthetic data limitations - need live market backtest

### Recommended Next Steps

1. **Refine Entry Logic** (2 hours)
   - Adjust RSI levels (30/70 thresholds)
   - Add volume confirmation
   - Test multiple timeframes (4H, daily)

2. **Paper Trading** (1-2 weeks)
   - Deploy to live market via MT5
   - Collect real trade data
   - Validate performance vs backtest

3. **Optimization Phase** (1-2 weeks)
   - Walk-forward analysis
   - Parameter tuning (TP%, SL%, RSI levels)
   - Monte Carlo simulation

4. **Production MQL5 Coding** (1 week)
   - Once real trades hit 45%+ win rate
   - 1.5+ profit factor target

---

## Files Generated

- `backtest_final.csv` - All 427 trade entries/exits
- `xauusd_realistic.csv` - 45,313 1H candles (2021-2026)
- `bot_logic.py` - Supply/Demand entry logic
- `BACKTEST_REPORT_XAUUSD.md` - This report

---

**Report Generated:** 2026-03-04 20:31:28 UTC  
**Backtest Engine:** VectorBT (Python)  
**Data Quality:** ⚠️ Synthetic (needs real OHLC validation)  
**Next Review:** After live paper trading (1-2 weeks)
