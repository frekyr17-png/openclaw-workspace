# Trading Lab Instruction Guide

## Core Principles
- **Daily Target**: 10% profit per bot ($10 on $100 allocation)
- **Trade Philosophy**: Quantity + speed > perfection. Hit targets via 1 or 100 trades.
- **Strategy Rule**: No trades in 24h = kill/adjust bot immediately

## Quick Actions

### 🚨 Emergency Fixes
```bash
# Restart all bots
./trader.py reset

# Kill unresponsive bot (e.g. ALPHA-001)
./trader.py kill --id ALPHA-001

# Fix config errors
nano state.json  # Adjust thresholds/times
```

### 📊 Performance Checks
1. **Win rate leaderboards**: `grep -A5 'stats' state.json`
2. **Active trades**: `grep 'pending' state.json`
3. **Daily P&L**: `grep -E 'pnl|profit' trader.log | tail -20`

### ⚙️ Threshold Adjustments (Current)
```ini
[trend]
trend_threshold = 0.1%  # SMA crossover

[meanrev]
z_score_min = 1.0    # Entry signal

[momentum]
roc_threshold = 1.5%    # Rate of change
```

### 📈 Evaluation Criteria
| Status       | Action               |
|--------------|----------------------|
| >50% win rate| Scale position +50%  |
| <30% win rate| Kill after 3 trades  |
| No trades    | Adjust timeframe     |

## Critical Alerts
- If **trader.log** shows `ERROR: API rate limit` → throttle cron to 10m
- If `state.json` shows `pending` > 2h → increase exit thresholds
- If daily target not hit → switch to 1m scalping

> ⚡ *Pro Tip:* For ETA-001 (XRP 55.6% win rate), duplicate strategy with 2x position size.*

_Last updated: `date -u`_
