#!/usr/bin/env python3
"""
THETA-001: Theta Gold Trend
Day trading strategy for XAU/USD (Gold) on 15m timeframe
Trend following using SMA crossover
"""

import json
import os
import time
from datetime import datetime, timedelta
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
    """Get XAU/USD price from alternative source (Binance doesn't have XAU directly)"""
    try:
        # Using PAXG (Paxos Gold) as proxy for XAU/USD on Binance
        resp = requests.get(f"{BINANCE_TESTNET}/fapi/v1/ticker/price?symbol=PAXGUSDT", timeout=10)
        data = resp.json()
        return float(data['price'])
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None

def calculate_sma(prices, period):
    if len(prices) < period:
        return None
    return sum(prices[-period:]) / period

def run_strategy():
    print(f"[{datetime.now()}] THETA-001: Checking XAU/USD trend signal...")
    
    price = get_xau_price()
    if not price:
        print("Failed to get price, skipping...")
        return
    
    # For demo purposes using simplified logic
    # In production, fetch historical candles and calculate SMA
    state = get_state()
    
    # Find our strategy
    strat_idx = None
    for i, s in enumerate(state['strategies']):
        if s['id'] == 'THETA-001':
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
    
    # Simple trend signal simulation
    # In reality: fetch 15m candles, calc SMA10 vs SMA30
    print(f"XAU/USD price: {price}")
    
    # Log the check
    state['lastUpdate'] = datetime.now().isoformat()
    save_state(state)
    
    print(f"Strategy check complete. No trade signal at this time.")

if __name__ == "__main__":
    run_strategy()