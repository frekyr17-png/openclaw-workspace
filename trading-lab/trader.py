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

def fetch_ohlcv(exchange, symbol, timeframe, limit=100):
    return exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

def get_balance(exchange):
    bal = exchange.fetch_balance()
    usdt = float(bal.get('USDT', {}).get('free', 0))
    return usdt

def scan_strategy(exchange, strategy_id, strategy_type, market, timeframe):
    """Analyze market and return a signal: 'buy', 'sell', or 'hold'"""
    candles = fetch_ohlcv(exchange, market, timeframe, limit=50)
    if len(candles) < 20:
        return 'hold', {}

    closes = [c[4] for c in candles]
    current = closes[-1]

    if strategy_type == 'trend':
        sma_fast = sum(closes[-7:]) / 7
        sma_slow = sum(closes[-21:]) / 21
        if sma_fast > sma_slow * 1.002:
            return 'buy', {'sma_fast': sma_fast, 'sma_slow': sma_slow}
        elif sma_fast < sma_slow * 0.998:
            return 'sell', {'sma_fast': sma_fast, 'sma_slow': sma_slow}

    elif strategy_type == 'meanrev':
        sma20 = sum(closes[-20:]) / 20
        std = (sum((c - sma20)**2 for c in closes[-20:]) / 20) ** 0.5
        if std == 0:
            return 'hold', {}
        z_score = (current - sma20) / std
        if z_score < -1.5:
            return 'buy', {'z_score': z_score, 'sma20': sma20}
        elif z_score > 1.5:
            return 'sell', {'z_score': z_score, 'sma20': sma20}

    elif strategy_type == 'breakout':
        high_20 = max(closes[-20:])
        low_20 = min(closes[-20:])
        if current > high_20 * 0.998:
            return 'buy', {'high_20': high_20}
        elif current < low_20 * 1.002:
            return 'sell', {'low_20': low_20}

    elif strategy_type == 'momentum':
        roc = (current - closes[-10]) / closes[-10] * 100
        if roc > 3:
            return 'buy', {'roc': roc}
        elif roc < -3:
            return 'sell', {'roc': roc}

    elif strategy_type == 'swing':
        sma10 = sum(closes[-10:]) / 10
        sma30 = sum(closes[-30:]) / 30
        highs = [c[2] for c in candles[-10:]]
        lows = [c[3] for c in candles[-10:]]
        if current > sma10 and sma10 > sma30 and current <= min(highs) * 1.01:
            return 'buy', {'sma10': sma10, 'sma30': sma30}
        elif current < sma10 and sma10 < sma30:
            return 'sell', {'sma10': sma10, 'sma30': sma30}

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
            signal, meta = scan_strategy(
                exchange, strat['id'], strat['type'], strat['market'], strat['timeframe']
            )

            ticker = exchange.fetch_ticker(strat['market'])
            price = ticker['last']

            print(f"  {strat['id']} ({strat['type']}/{strat['market']}/{strat['timeframe']}): {signal} @ {price}")

            if signal in ('buy', 'sell'):
                trade = {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "action": signal.upper(),
                    "market": strat['market'],
                    "price": price,
                    "signal_meta": meta,
                    "result": "pending"
                }
                strat['trades'].append(trade)
                print(f"    → Logged {signal.upper()} trade")

                # Evaluate previous pending trades
                for t in strat['trades']:
                    if t['result'] == 'pending' and t != trade:
                        if t['action'] == 'BUY':
                            pnl_pct = (price - t['price']) / t['price'] * 100
                        else:
                            pnl_pct = (t['price'] - price) / t['price'] * 100

                        t['exit'] = price
                        t['pnl'] = round(pnl_pct, 2)
                        t['result'] = 'win' if pnl_pct > 0 else 'loss'
                        t['closed'] = datetime.now(timezone.utc).isoformat()

                        if t['result'] == 'win':
                            strat['stats']['wins'] += 1
                        else:
                            strat['stats']['losses'] += 1

                        total = strat['stats']['wins'] + strat['stats']['losses']
                        strat['stats']['winRate'] = round(strat['stats']['wins'] / total * 100, 1) if total > 0 else 0
                        print(f"    → Closed previous trade: {t['result']} ({t['pnl']}%)")

        except Exception as e:
            print(f"  {strat['id']}: ERROR - {e}")

    state['lastUpdate'] = datetime.now(timezone.utc).isoformat()
    save_state(state)
    print(f"State saved. Done.")

if __name__ == '__main__':
    main()
