# Richie's Trading Tools

## Trading Lab Commands

### Check Current State
```bash
cd ~/.openclaw/workspace/trading-lab
cat state.json | jq '.'
```

### View Recent Trades
```bash
tail -50 ~/.openclaw/workspace/trading-lab/trader.log
```

### Run Trader Manually
```bash
cd ~/.openclaw/workspace/trading-lab
python3 trader.py
```

### Check Bot Status
```bash
cd ~/.openclaw/workspace/trading-lab
python3 trader.py --status
```

### Check Cron Jobs
```bash
crontab -l | grep trader
```

---

## Performance Analysis

### Calculate Daily P&L
```bash
# Parse today's trades from state.json
cd ~/.openclaw/workspace/trading-lab
cat state.json | jq '[.[] | select(.status == "closed") | .pnl] | add'
```

### Bot Win Rates
```bash
# Count wins vs losses per bot
cd ~/.openclaw/workspace/trading-lab
grep "CLOSED" trader.log | tail -100
```

### Identify Inactive Bots
```bash
# Bots with no trades in 24h
cd ~/.openclaw/workspace/trading-lab
cat state.json | jq '.[] | select(.last_trade_time < (now - 86400))'
```

---

## Strategy Optimization

### Adjust Bot Thresholds
Edit `trader.py` strategy parameters:
```python
# In trader.py, find the bot config:
"ALPHA-001": {
    "strategy": "trend",
    "timeframe": "4h",
    "trend_threshold": 0.1,  # Adjust this
    ...
}
```

### Kill Underperforming Bot
```bash
# Remove from state.json and trader.py
# Document in decisions.md
```

### Switch Bot Strategy
```python
# Change strategy type in trader.py
"BOT-NAME": {
    "strategy": "meanrev",  # was "trend"
    ...
}
```

---

## Reporting Templates

### Daily P&L Report
```bash
cat > ~/agents/richie/logs/daily-$(date +%Y-%m-%d).md << 'EOF'
# Richie's Daily P&L - $(date +%Y-%m-%d)

**Total P&L:** +$XX.XX (+X.X%)
**Winning bots:** X/12
**Trades today:** XX

## Top Performers
- BOT-NAME: +$XX (+X trades, X% win rate)

## Underperformers
- BOT-NAME: -$XX or no trades

## Actions Taken
- [list any adjustments]

## Next Steps
- [plan for tomorrow]
EOF
```

### Weekly Strategy Review
```bash
cat > ~/agents/richie/logs/weekly-$(date +%Y-W%W).md << 'EOF'
# Weekly Strategy Review - Week $(date +%W)

## Performance Summary
- Total P&L: $XXX
- Average win rate: XX%
- Best bot: BOT-NAME (XX%)
- Worst bot: BOT-NAME (XX%)

## Strategy Adjustments
- [list changes made]

## Go-Live Candidates
- [bots ready for real money]

## Next Week Focus
- [priorities]
EOF
```

---

## Key Files

### Trading Lab Files
- `~/.openclaw/workspace/trading-lab/trader.py` - Main bot script
- `~/.openclaw/workspace/trading-lab/state.json` - Current positions & P&L
- `~/.openclaw/workspace/trading-lab/trader.log` - All trade history
- `~/.openclaw/workspace/trading-lab/credentials.env` - Binance API keys

### Richie's Files
- `logs/daily-YYYY-MM-DD.md` - Daily P&L reports
- `logs/weekly-YYYY-WW.md` - Weekly strategy reviews
- `performance/bot-analytics.json` - Historical bot performance
- `decisions.md` - Major decisions log (go-live, kills, pivots)

---

## Daily Workflow

### Morning Routine (Every Day)
```bash
# 1. Check overnight performance
cd ~/.openclaw/workspace/trading-lab
tail -100 trader.log

# 2. Review state.json
cat state.json | jq '.'

# 3. Calculate P&L
# [manual for now, automate later]

# 4. Identify issues
# - Bots with no trades
# - Bots with >20% drawdown
# - Errors in logs

# 5. Create daily report
# Use template above

# 6. Report to Aria
# Post in team channel or Aria's session
```

### Before Evaluation Gates
**March 7 (ZETA, ETA):**
```bash
# Pull all trades for these bots since Feb 21
grep -E "(ZETA-001|ETA-001)" trader.log > evaluation-mar7.log

# Calculate metrics
# - Win rate
# - Total P&L
# - Trade frequency
# - Max drawdown

# Make decision: Keep, Optimize, or Replace
```

**March 23 (5 standard bots):**
```bash
# Same process for ALPHA, BETA, GAMMA, DELTA, EPSILON
```

---

## Go-Live Checklist

Before deploying real money:
- [ ] 1 month consistent paper profit
- [ ] Win rate >55%
- [ ] Max drawdown <15%
- [ ] Daily trades (no 24h silence)
- [ ] Aria approval obtained
- [ ] Start with $100 (not full capital)
- [ ] Real-money credentials configured
- [ ] Stop-loss configured
- [ ] Alert system ready

---

## Emergency Procedures

### Bot Stuck/Error
```bash
# 1. Check logs
tail -50 trader.log

# 2. Check process
ps aux | grep trader

# 3. Restart if needed
cd ~/.openclaw/workspace/trading-lab
python3 trader.py

# 4. Document incident
```

### Unusual Losses
```bash
# If bot loses >20% in single day:
# 1. STOP the bot immediately
# 2. Alert Aria
# 3. Analyze what happened
# 4. Adjust or kill
```

---

## Automation Goals

**Phase 1 (Manual):**
- Daily log review
- Manual P&L calculation
- Manual reporting

**Phase 2 (Semi-automated):**
- Python script to calculate P&L
- Automated daily report generation
- Alert on 24h silence

**Phase 3 (Fully automated):**
- Real-time dashboard
- Automatic strategy adjustments
- Auto-reporting to Aria
