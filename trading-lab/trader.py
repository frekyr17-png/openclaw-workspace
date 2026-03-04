#!/usr/bin/env python3
"""Trading Lab - Strategy Executor
Reads credentials, connects to Binance testnet via ccxt, executes strategy logic, logs trades to state.json.
"""
import ccxt
import json
import os
import time
import sys
from datetime import datetime, timezone

STATE_PATH = os.path.expanduser("~/.openclaw/workspace/trading-lab/state.json")
CRED_PATH = os.path.expanduser("~/.openclaw/workspace/trading-lab/credentials.env")

def load_creds():
    creds = {}
    with open(CRED_PATH) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                creds[key.strip()] = val.strip()
    return creds

def get_exchange(creds):
    use_testnet = creds.get('BINANCE_USE_TESTNET', 'false').lower() == 'true'
    exchange = ccxt.binance({
        'apiKey': creds['BINANCE_API_KEY'],
        'secret': creds['BINANCE_SECRET_KEY'],
        'sandbox': use_testnet,
        'enableRateLimit': True,
    })
    return exchange

def load_state():
    with open(STATE_PATH) as f:
        return json.load(f)

def save_state(state):
    with open(STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def update_markdown_reports(state):
    """Auto-generate markdown trade reports after every cycle"""
    from datetime import datetime, timezone
    
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    
    # --- OPEN POSITIONS (always current) ---
    open_positions = []
    for strat in state['strategies']:
        for trade in strat['trades']:
            if trade['result'] == 'pending':
                open_positions.append({
                    'bot': strat['id'],
                    'market': trade['market'],
                    'action': trade['action'],
                    'entry': trade['price'],
                    'opened': trade['timestamp'][:16].replace('T', ' '),
                    'type': strat['type']
                })
    
    open_md = f"""# 🟡 OPEN POSITIONS — LIVE
**Last Updated:** {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}

| Bot | Market | Action | Entry Price | Opened | Status |
|-----|--------|--------|-------------|--------|--------|
"""
    for pos in open_positions:
        open_md += f"| **{pos['bot']}** | {pos['market']} | {pos['action']} | ${pos['entry']:,.2f} | {pos['opened']} | ⏳ OPEN |\n"
    
    open_md += f"\n**Total Open:** {len(open_positions)} positions\n"
    
    # Alert if any position >24h
    from datetime import datetime, timezone
    for pos in open_positions:
        opened_dt = datetime.fromisoformat(pos['opened'].replace(' ', 'T') + ':00+00:00')
        hours_open = (datetime.now(timezone.utc) - opened_dt).total_seconds() / 3600
        if hours_open > 24:
            open_md += f"\n⚠️ **{pos['bot']}** open {hours_open:.0f}h — consider review"
    
    with open(os.path.expanduser("~/.openclaw/workspace/trading-lab/OPEN-POSITIONS.md"), 'w') as f:
        f.write(open_md)
    
    # --- DAILY REPORT (if not exists, create; if exists, update) ---
    daily_path = os.path.expanduser(f"~/.openclaw/workspace/trading-lab/trades-daily-{today}.md")
    
    # Closed trades today
    closed_today = []
    for strat in state['strategies']:
        for trade in strat['trades']:
            if trade['result'] != 'pending' and trade.get('closed', '').startswith(today):
                closed_today.append({
                    'bot': strat['id'],
                    'market': trade['market'],
                    'action': trade['action'],
                    'entry': trade['price'],
                    'exit': trade.get('exit', 0),
                    'result': trade['result'],
                    'pnl': trade.get('pnl', 0)
                })
    
    # Bot performance summary
    perf_rows = []
    for strat in state['strategies']:
        wins = strat['stats']['wins']
        losses = strat['stats']['losses']
        total = wins + losses
        wr = strat['stats']['winRate']
        # Calculate net P/L
        net_pnl = sum(t.get('pnl', 0) for t in strat['trades'] if t['result'] != 'pending')
        perf_rows.append({
            'bot': strat['id'],
            'type': strat['type'],
            'market': strat['market'],
            'tf': strat['timeframe'],
            'wins': wins,
            'losses': losses,
            'wr': wr,
            'pnl': net_pnl
        })
    
    daily_md = f"""# Trading Lab — Daily Report
**Date:** {today} · **Updated:** {datetime.now(timezone.utc).strftime("%H:%M UTC")}

---

## 🟢 CLOSED TRADES TODAY ({len(closed_today)})

| Bot | Market | Action | Entry | Exit | Result | P/L % |
|-----|--------|--------|-------|------|--------|-------|
"""
    
    total_pnl = 0
    for t in closed_today:
        emoji = "🟢" if t['result'] == 'win' else "🔴"
        sign = "+" if t['pnl'] > 0 else ""
        daily_md += f"| **{t['bot']}** | {t['market']} | {t['action']} | ${t['entry']:,.4f} | ${t['exit']:,.4f} | {emoji} {t['result'].upper()} | {sign}{t['pnl']:.2f}% |\n"
        total_pnl += t['pnl']
    
    if not closed_today:
        daily_md += "| — | — | — | — | — | — | — |\n"
    
    daily_md += f"\n**Today's Net P/L:** {('+' if total_pnl >= 0 else '')}{total_pnl:.2f}%\n\n---\n\n## 🟡 OPEN POSITIONS ({len(open_positions)})\n"
    
    daily_md += "| Bot | Market | Action | Entry | Opened | Status |\n|-----|--------|--------|-------|--------|--------|\n"
    for pos in open_positions:
        daily_md += f"| **{pos['bot']}** | {pos['market']} | {pos['action']} | ${pos['entry']:,.4f} | {pos['opened']} | ⏳ HOLDING |\n"
    
    daily_md += f"""\n---\n\n## 📊 BOT PERFORMANCE\n\n| Bot | Type | Market | TF | Wins | Losses | Win Rate | Net P/L |
|-----|------|--------|----|------|--------|----------|---------|
"""
    
    for row in perf_rows:
        pnl_str = f"+{row['pnl']:.2f}%" if row['pnl'] >= 0 else f"{row['pnl']:.2f}%"
        daily_md += f"| **{row['bot']}** | {row['type']} | {row['market']} | {row['tf']} | {row['wins']} | {row['losses']} | {row['wr']}% | {pnl_str} |\n"
    
    daily_md += "\n---\n\n*Auto-generated by Trading Lab*\n"
    
    with open(daily_path, 'w') as f:
        f.write(daily_md)

def fetch_ohlcv(exchange, symbol, timeframe, limit=100):
    return exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

def get_balance(exchange):
    bal = exchange.fetch_balance()
    usdt = float(bal.get('USDT', {}).get('free', 0))
    return usdt

def calc_atr(candles, period=14):
    """Calculate Average True Range for stop loss placement"""
    if len(candles) < period + 1:
        return None
    trs = []
    for i in range(1, period + 1):
        high = candles[-i][2]
        low = candles[-i][3]
        close_prev = candles[-i-1][4]
        tr = max(high - low, abs(high - close_prev), abs(low - close_prev))
        trs.append(tr)
    return sum(trs) / len(trs)

def find_support_resistance(candles, window=10):
    """Find recent support/resistance levels"""
    if len(candles) < window * 2:
        return None, None
    highs = [c[2] for c in candles[-window*2:-window]]
    lows = [c[3] for c in candles[-window*2:-window]]
    return max(highs), min(lows)

def detect_engulfing(candles):
    """Detect bullish/bearish engulfing patterns"""
    if len(candles) < 3:
        return None
    prev = candles[-2]
    curr = candles[-1]
    
    prev_body = abs(prev[4] - prev[1])
    curr_body = abs(curr[4] - curr[1])
    prev_bullish = prev[4] > prev[1]
    curr_bullish = curr[4] > curr[1]
    
    # Bullish engulfing: current bullish, previous bearish, body engulfs
    if curr_bullish and not prev_bullish and curr_body > prev_body * 1.2:
        if curr[1] <= prev[4] and curr[4] >= prev[1]:
            return 'bullish_engulfing'
    
    # Bearish engulfing: current bearish, previous bullish, body engulfs
    if not curr_bullish and prev_bullish and curr_body > prev_body * 1.2:
        if curr[1] >= prev[4] and curr[4] <= prev[1]:
            return 'bearish_engulfing'
    
    return None

def calc_atr(candles, period=14):
    """Calculate Average True Range for stop loss placement"""
    if len(candles) < period + 1:
        return None
    trs = []
    for i in range(1, period + 1):
        high = candles[-i][2]
        low = candles[-i][3]
        close_prev = candles[-i-1][4]
        tr = max(high - low, abs(high - close_prev), abs(low - close_prev))
        trs.append(tr)
    return sum(trs) / len(trs)

def find_support_resistance(candles, window=10):
    """Find recent support/resistance levels"""
    if len(candles) < window * 2:
        return None, None
    highs = [c[2] for c in candles[-window*2:-window]]
    lows = [c[3] for c in candles[-window*2:-window]]
    return max(highs), min(lows)

def detect_engulfing(candles):
    """Detect bullish/bearish engulfing patterns"""
    if len(candles) < 3:
        return None
    prev = candles[-2]
    curr = candles[-1]
    
    prev_body = abs(prev[4] - prev[1])
    curr_body = abs(curr[4] - curr[1])
    prev_bullish = prev[4] > prev[1]
    curr_bullish = curr[4] > curr[1]
    
    # Bullish engulfing: current bullish, previous bearish, body engulfs
    if curr_bullish and not prev_bullish and curr_body > prev_body * 1.2:
        if curr[1] <= prev[4] and curr[4] >= prev[1]:
            return 'bullish_engulfing'
    
    # Bearish engulfing: current bearish, previous bullish, body engulfs
    if not curr_bullish and prev_bullish and curr_body > prev_body * 1.2:
        if curr[1] >= prev[4] and curr[4] <= prev[1]:
            return 'bearish_engulfing'
    
    return None

def scan_mtf_strategy(exchange, market, strat_config):
    """
    Multi-timeframe strategy:
    - 1H: Higher timeframe trend (EMA alignment)
    - 30M: Structure confirmation   
    - 5M: Pattern entry + ATR stop loss
    """
    # Fetch all three timeframes
    candles_1h = fetch_ohlcv(exchange, market, '1h', limit=50)
    candles_30m = fetch_ohlcv(exchange, market, '30m', limit=50)
    candles_5m = fetch_ohlcv(exchange, market, '5m', limit=50)
    
    if len(candles_1h) < 30 or len(candles_30m) < 20 or len(candles_5m) < 20:
        return 'hold', {'reason': 'insufficient data'}
    
    # 1H Trend Analysis (Higher timeframe)
    closes_1h = [c[4] for c in candles_1h]
    ema50_1h = sum(closes_1h[-50:]) / 50
    ema20_1h = sum(closes_1h[-20:]) / 20
    current_1h = closes_1h[-1]
    
    # Bullish trend: price > EMA20 > EMA50
    # Bearish trend: price < EMA20 < EMA50
    trend_bullish = current_1h > ema20_1h > ema50_1h
    trend_bearish = current_1h < ema20_1h < ema50_1h
    
    if not trend_bullish and not trend_bearish:
        return 'hold', {'reason': 'no clear 1H trend', 'ema20': ema20_1h, 'ema50': ema50_1h}
    
    # 30M Structure Confirmation
    closes_30m = [c[4] for c in candles_30m]
    highs_30m = [c[2] for c in candles_30m[-10:]]
    lows_30m = [c[3] for c in candles_30m[-10:]]
    
    higher_highs = highs_30m[-1] > max(highs_30m[:-1]) if trend_bullish else False
    lower_lows = lows_30m[-1] < min(lows_30m[:-1]) if trend_bearish else False
    
    structure_confirmed = (trend_bullish and higher_highs) or (trend_bearish and lower_lows)
    
    if not structure_confirmed:
        return 'hold', {'reason': '30M structure not confirming', 'trend': 'bullish' if trend_bullish else 'bearish'}
    
    # 5M Pattern Detection for Entry
    closes_5m = [c[4] for c in candles_5m]
    current_5m = closes_5m[-1]
    
    # Detect patterns
    pattern = detect_engulfing(candles_5m)
    resistance, support = find_support_resistance(candles_5m)
    atr = calc_atr(candles_5m, 14)
    
    signal = 'hold'
    stop_loss = None
    take_profit = None
    reason = 'no entry pattern'
    
    # Entry logic
    if trend_bullish and structure_confirmed:
        # Look for long entries on 5M
        if pattern == 'bullish_engulfing':
            signal = 'buy'
            stop_loss = current_5m - (atr * 2 if atr else current_5m * 0.002)
            take_profit = current_5m + (atr * 4 if atr else current_5m * 0.01)
            reason = 'bullish engulfing on 5M'
        elif support and current_5m <= support * 1.001:  # Near support
            signal = 'buy'
            stop_loss = support - (atr if atr else current_5m * 0.001)
            take_profit = current_5m + (current_5m - stop_loss) * 2  # 1:2 RR
            reason = 'support bounce on 5M'
            
    elif trend_bearish and structure_confirmed:
        # Look for short entries on 5M
        if pattern == 'bearish_engulfing':
            signal = 'sell'
            stop_loss = current_5m + (atr * 2 if atr else current_5m * 0.002)
            take_profit = current_5m - (atr * 4 if atr else current_5m * 0.01)
            reason = 'bearish engulfing on 5M'
        elif resistance and current_5m >= resistance * 0.999:  # Near resistance
            signal = 'sell'
            stop_loss = resistance + (atr if atr else current_5m * 0.001)
            take_profit = current_5m - (stop_loss - current_5m) * 2  # 1:2 RR
            reason = 'resistance rejection on 5M'
    
    meta = {
        'trend': 'bullish' if trend_bullish else 'bearish',
        'pattern': pattern,
        'structure_confirmed': structure_confirmed,
        'reason': reason,
        'stop_loss': round(stop_loss, 4) if stop_loss else None,
        'take_profit': round(take_profit, 4) if take_profit else None,
        'atr_5m': round(atr, 4) if atr else None,
        'support_5m': round(support, 4) if support else None,
        'resistance_5m': round(resistance, 4) if resistance else None
    }
    
    return signal, meta

def scan_strategy(exchange, strategy_id, strategy_type, market, timeframe, has_open_trade=False, strat_config=None):
    """Analyze market and return a signal: 'buy', 'sell', or 'hold'"""
    
    # Multi-timeframe strategy (NU-001 style)
    if strategy_type == 'mtf':
        return scan_mtf_strategy(exchange, market, strat_config)
    
    # Standard single-timeframe strategies
    candles = fetch_ohlcv(exchange, market, timeframe, limit=100)

    closes = [c[4] for c in candles]
    current = closes[-1]

    # TARGET: 10% daily profit per bot
    # Strategy: Enter on strong signals, hold until profit target or end of day

    if strategy_type == 'trend':
        sma_fast = sum(closes[-5:]) / 5
        sma_slow = sum(closes[-15:]) / 15
        # ALPHA-001 (BTC/5m): 0.5% → 0.15% (0.005 → 0.0015)
        # ETA-001 (XRP/15m): 0.6% → 0.2% (0.006 → 0.002)
        # GOLD-30M (trend/30m): 0.2% → 0.08% (0.002 → 0.0008)
        if 'GOLD-30M' in strategy_id:
            threshold = 0.0008  # Aggressive trend catch
        elif 'ETA-001' in strategy_id:
            threshold = 0.002   # Lower from 0.006 to 0.002
        else:  # ALPHA-001 and others default to 0.0015
            threshold = 0.0015  # Aggressive momentum detection
        if sma_fast > sma_slow * (1 + threshold):  # Adjustable momentum for entry
            return 'buy', {'sma_fast': sma_fast, 'sma_slow': sma_slow, 'momentum': (sma_fast/sma_slow-1)*100}
        elif sma_fast < sma_slow * (1 - threshold):
            return 'sell', {'sma_fast': sma_fast, 'sma_slow': sma_slow, 'momentum': (1-sma_fast/sma_slow)*100}

    elif strategy_type == 'meanrev':
        sma20 = sum(closes[-20:]) / 20
        std = (sum((c - sma20)**2 for c in closes[-20:]) / 20) ** 0.5
        if std == 0:
            return 'hold', {}
        z_score = (current - sma20) / std
        # BETA-001 (ETH/15m): z-score -1.5 → -0.8 (more aggressive)
        # GOLD-15M (meanrev/15m): z-score aggressive (use -1.0)
        z_threshold = -0.8 if 'BETA-001' in strategy_id else (-1.0 if 'GOLD-15M' in strategy_id else -1.5)
        if z_score < z_threshold:  # Oversold - buy for bounce
            return 'buy', {'z_score': z_score, 'sma20': sma20, 'target_revert': 3.0}
        elif z_score > -z_threshold:  # Overbought - sell for pullback
            return 'sell', {'z_score': z_score, 'sma20': sma20, 'target_revert': 3.0}

    elif strategy_type == 'breakout':
        # GOLD-15M: Switch from breakout to mean reversion (z-score)
        if 'GOLD-15M' in strategy_id:
            sma20 = sum(closes[-20:]) / 20
            std = (sum((c - sma20)**2 for c in closes[-20:]) / 20) ** 0.5
            if std == 0:
                return 'hold', {}
            z_score = (current - sma20) / std
            # GOLD-15M: z-score aggressive (use -1.0)
            z_threshold = -1.0
            if z_score < z_threshold:  # Oversold - buy for bounce
                return 'buy', {'z_score': z_score, 'sma20': sma20, 'strategy': 'mean_reversion_oversold'}
            elif z_score > -z_threshold:  # Overbought - sell for pullback
                return 'sell', {'z_score': z_score, 'sma20': sma20, 'strategy': 'mean_reversion_overbought'}
        else:
            # Standard breakout for other strategies
            # GAMMA-001 (BTC/30m): breakout threshold 0.4% → 0.15% (0.004 → 0.0015)
            high_20 = max(closes[-20:])
            low_20 = min(closes[-20:])
            breakout_threshold = 0.0015 if 'GAMMA-001' in strategy_id else 0.002
            # Breakout entry for momentum moves
            if current > high_20 * (1 + breakout_threshold):
                return 'buy', {'high_20': high_20, 'breakout_pct': (current/high_20-1)*100}
            elif current < low_20 * (1 - breakout_threshold):
                return 'sell', {'low_20': low_20, 'breakout_pct': (1-current/low_20)*100}

    elif strategy_type == 'momentum':
        roc5 = (current - closes[-5]) / closes[-5] * 100
        roc10 = (current - closes[-10]) / closes[-10] * 100
        volumetric = sum(closes[-3:]) / sum(closes[-6:-3])  # Volume proxy
        
        # DELTA-001 (ETH/5m): ROC 1.5% → 0.4%
        # ZETA-001 (SOL/5m): ROC 1.5% → 0.4%
        # GOLD-001 (1h): ROC 1.0% → 0.4%
        # GOLD-5M (5m): ROC 0.3% → 0.1%
        if 'DELTA-001' in strategy_id or 'ZETA-001' in strategy_id:
            roc_threshold = 0.4  # Lower from 1.5% → 0.4%
            volume_check = False
        elif 'GOLD-001' in strategy_id:
            roc_threshold = 0.4  # Lower from 1.0% → 0.4%
            volume_check = False
        elif 'GOLD-5M' in strategy_id:
            roc_threshold = 0.1  # Lower from 0.3% → 0.1%
            volume_check = False
        else:
            roc_threshold = 2.0  # Default for other momentum strategies
            volume_check = True
        
        # Momentum entry with adjusted thresholds
        if 'GOLD' in strategy_id or 'DELTA-001' in strategy_id or 'ZETA-001' in strategy_id:
            # For GOLD and aggressive crypto: ignore volume requirement, just use ROC
            if abs(roc5) > roc_threshold:
                if roc5 > roc_threshold:
                    return 'buy', {'roc5': roc5, 'roc10': roc10, 'momentum_strength': roc5 + roc10}
                else:
                    return 'sell', {'roc5': roc5, 'roc10': roc10, 'momentum_strength': abs(roc5) + abs(roc10)}
        else:
            # For non-GOLD: use original volume check
            if roc5 > roc_threshold and volumetric > 1.0:
                return 'buy', {'roc5': roc5, 'roc10': roc10, 'momentum_strength': roc5 + roc10}
            elif roc5 < -roc_threshold and volumetric < 1.0:
                return 'sell', {'roc5': roc5, 'roc10': roc10, 'momentum_strength': abs(roc5) + abs(roc10)}

    elif strategy_type == 'swing':
        sma10 = sum(closes[-10:]) / 10
        sma30 = sum(closes[-30:]) / 30
        # EPSILON-001 (BTC/15m): trend strength 0.4 → 0.15 (0.003 → 0.0015)
        trend_strength_threshold = 0.0015 if 'EPSILON-001' in strategy_id else 0.003
        # Swing entry on confirmed direction
        if current > sma10 and sma10 > sma30 * (1 + trend_strength_threshold):  # Strong uptrend
            return 'buy', {'sma10': sma10, 'sma30': sma30, 'trend_strength': (current/sma10-1)*100}
        elif current < sma10 and sma30 > sma10 * (1 + trend_strength_threshold):  # Strong downtrend
            return 'sell', {'sma10': sma10, 'sma30': sma30, 'trend_strength': (1-current/sma10)*100}

    return 'hold', {}

def main():
    strategy_id = sys.argv[1] if len(sys.argv) > 1 else None

    creds = load_creds()
    exchange = get_exchange(creds)
    state = load_state()

    if strategy_id:
        strategies = [s for s in state['strategies'] if s['id'] == strategy_id]
    else:
        strategies = [s for s in state['strategies'] if s['status'] == 'active']

    print(f"[{datetime.now(timezone.utc).isoformat()}] Scanning {len(strategies)} strategies...")

    for strat in strategies:
        try:
            # Check if we have an open trade
            has_open = any(t['result'] == 'pending' for t in strat['trades'])
            
            signal, meta = scan_strategy(
                exchange, strat['id'], strat['type'], strat['market'], strat['timeframe'], has_open, strat
            )

            ticker = exchange.fetch_ticker(strat['market'])
            price = ticker['last']

            print(f"  {strat['id']} ({strat['type']}/{strat['market']}/{strat['timeframe']}): {signal} @ {price}")

            if signal in ('buy', 'sell'):
                # Check existing trades - evaluate profit target
                for t in strat['trades']:
                    if t['result'] == 'pending':
                        entry_price = t['price']
                        signal_meta = t.get('signal_meta', {})
                        
                        # Get custom targets from strategy config
                        targets = strat.get('targets', {})
                        profit_target = 5.0  # default
                        loss_limit = -5.0   # default
                        
                        if strat['id'] == 'GOLD-001':
                            profit_target = 2.5  # 2-3% target
                            loss_limit = -1.0  # 1% stop loss
                        
                        # For MTF strategy, use preset stop/target from entry signal
                        if strat['type'] == 'mtf' and 'stop_loss' in signal_meta and 'take_profit' in signal_meta:
                            sl = signal_meta['stop_loss']
                            tp = signal_meta['take_profit']
                            
                            if t['action'] == 'BUY':
                                if price <= sl:  # Hit stop loss
                                    pnl_pct = (price - entry_price) / entry_price * 100
                                    t['exit'] = price
                                    t['pnl'] = round(pnl_pct, 2)
                                    t['result'] = 'loss'
                                    t['closed'] = datetime.now(timezone.utc).isoformat()
                                    strat['stats']['losses'] += 1
                                    print(f"    → CLOSED LOSS: {pnl_pct:.2f}% (MTF stop loss hit @{sl:.2f})")
                                elif price >= tp:  # Hit take profit
                                    pnl_pct = (price - entry_price) / entry_price * 100
                                    t['exit'] = price
                                    t['pnl'] = round(pnl_pct, 2)
                                    t['result'] = 'win'
                                    t['closed'] = datetime.now(timezone.utc).isoformat()
                                    strat['stats']['wins'] += 1
                                    print(f"    → CLOSED WIN: +{pnl_pct:.2f}% (MTF take profit hit @{tp:.2f})")
                            else:  # SELL
                                if price >= sl:  # Hit stop loss
                                    pnl_pct = (entry_price - price) / entry_price * 100
                                    t['exit'] = price
                                    t['pnl'] = round(pnl_pct, 2)
                                    t['result'] = 'loss'
                                    t['closed'] = datetime.now(timezone.utc).isoformat()
                                    strat['stats']['losses'] += 1
                                    print(f"    → CLOSED LOSS: {pnl_pct:.2f}% (MTF stop loss hit @{sl:.2f})")
                                elif price <= tp:  # Hit take profit
                                    pnl_pct = (entry_price - price) / entry_price * 100
                                    t['exit'] = price
                                    t['pnl'] = round(pnl_pct, 2)
                                    t['result'] = 'win'
                                    t['closed'] = datetime.now(timezone.utc).isoformat()
                                    strat['stats']['wins'] += 1
                                    print(f"    → CLOSED WIN: +{pnl_pct:.2f}% (MTF take profit hit @{tp:.2f})")
                        else:
                            # Standard strategies: use profit/loss targets
                            if t['action'] == 'BUY':
                                pnl_pct = (price - entry_price) / entry_price * 100
                            else:
                                pnl_pct = (entry_price - price) / entry_price * 100

                            # Close if we hit profit target
                            if pnl_pct >= profit_target:  
                                t['exit'] = price
                                t['pnl'] = round(pnl_pct, 2)
                                t['result'] = 'win'
                                t['closed'] = datetime.now(timezone.utc).isoformat()
                                strat['stats']['wins'] += 1
                                print(f"    → CLOSED WIN: +{pnl_pct:.2f}% (profit target hit)")
                            elif pnl_pct < loss_limit:  # Cut losses
                                t['exit'] = price
                                t['pnl'] = round(pnl_pct, 2)
                                t['result'] = 'loss'
                                t['closed'] = datetime.now(timezone.utc).isoformat()
                                strat['stats']['losses'] += 1
                                print(f"    → CLOSED LOSS: {pnl_pct:.2f}% (loss limit hit)")

                # Only enter new trade if we don't have one open
                if not has_open:
                    trade = {
                        "timestamp": datetime.now(timezone.utc).isoformat(),
                        "action": signal.upper(),
                        "market": strat['market'],
                        "price": price,
                        "signal_meta": meta,
                        "result": "pending"
                    }
                    strat['trades'].append(trade)
                    print(f"    → OPENED {signal.upper()} @ {price}")

                # Update stats
                total = strat['stats']['wins'] + strat['stats']['losses']
                strat['stats']['winRate'] = round(strat['stats']['wins'] / total * 100, 1) if total > 0 else 0

        except Exception as e:
            print(f"  {strat['id']}: ERROR - {e}")

    state['lastUpdate'] = datetime.now(timezone.utc).isoformat()
    save_state(state)
    update_markdown_reports(state)
    print(f"State saved. Reports updated. Done.")

if __name__ == '__main__':
    main()
