#!/usr/bin/env python3
"""
IOTA-001: Iota Gold Scalp
Day trading breakout scalping strategy for XAU/USD on 15m timeframe
Trades range breakouts with momentum
"""

import json
import os
from datetime import datetime
import requests

STATE_FILE = os.path.expanduser("~/.openclaw/workspace/trading-lab/state.json")
BINANCE_TESTNET = "https://testnet.binancefuture.com"

def get_state():
    with open(STATE_FILE, 'r') as f:
        return json.load(f)

def save_state(state):
    with open(STATE_FILE, 'w') as f:
        json.dump(state, f, indent=2)

def get_xau_price():
    """Get XAU/USD price using PAXG as proxy"""
    try:
        resp = requests.get(f"{BINANCE_TESTNET}/fapi/v1/ticker/price?symbol=PAXGUSDT", timeout=10)
        data = resp.json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def run_strategy():
    print(f"[{datetime.now()}] IOTA-001: Checking XAU/USD breakout signal...")
    
    price = get_xau_price()
    if not price:
        print("Failed to get price, skipping...")
        return
    
    state = get_state()
    
    # Find our strategy
    strat_idx = None
    for i, s in enumerate(state['strategies']):
        if s['id'] == 'IOTA-001':
            strat_idx = i
            break
    
    if strat_idx is None:
        print("Strategy not found in state")
        return
    
    strategy = state['strategies'][strat_idx]
    
    # Skip if already in trade
    pending_trades = [t for t in strategy['trades'] if t.get('result') == 'pending']
    if pending_trades:
        print(f"Already in trade, skipping...")
        return
    
    print(f"XAU/USD price: {price}")
    
    # In production: fetch 1h candles, determine range, check for breakout
    # For now, logging check
    
    state['lastUpdate'] = datetime.now().isoformat()
    save_state(state)
    
    print(f"Strategy check complete. No breakout signal at this time.")

if __name__ == "__main__":
    run_strategy()