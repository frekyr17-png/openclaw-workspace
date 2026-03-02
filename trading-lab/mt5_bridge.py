#!/usr/bin/env python3
"""
MT5 Bridge - File-based signal bridge
Python writes trade signals → MT5 EA reads and executes → Writes results back
This avoids complex RPC setup on Linux+Wine environment
"""
import json
import os
from datetime import datetime, timezone
from pathlib import Path

# Signal file paths (MT5 EA will monitor these)
BRIDGE_DIR = Path.home() / ".openclaw/workspace/trading-lab/mt5_bridge"
SIGNALS_FILE = BRIDGE_DIR / "signals.json"
RESULTS_FILE = BRIDGE_DIR / "results.json"
STATUS_FILE = BRIDGE_DIR / "status.json"

def ensure_bridge_dir():
    """Create bridge directory if it doesn't exist"""
    BRIDGE_DIR.mkdir(parents=True, exist_ok=True)

def write_signal(strategy_id, action, symbol, stop_loss=None, take_profit=None, lot_size=0.01):
    """
    Write a trade signal for MT5 EA to execute
    
    Args:
        strategy_id: Bot ID (e.g., 'OMEGA-001')
        action: 'BUY' or 'SELL'
        symbol: MT5 symbol (e.g., 'XAUUSD')
        stop_loss: Optional SL price
        take_profit: Optional TP price
        lot_size: Position size in lots (default 0.01 = micro lot)
    """
    ensure_bridge_dir()
    
    signal = {
        'strategy_id': strategy_id,
        'action': action,
        'symbol': symbol,
        'lot_size': lot_size,
        'stop_loss': stop_loss,
        'take_profit': take_profit,
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'status': 'pending'  # pending, executed, failed
    }
    
    # Append to signals file (MT5 EA will process and mark as executed)
    signals = []
    if SIGNALS_FILE.exists():
        with open(SIGNALS_FILE) as f:
            signals = json.load(f)
    
    signals.append(signal)
    
    with open(SIGNALS_FILE, 'w') as f:
        json.dump(signals, f, indent=2)
    
    return signal

def read_results():
    """Read execution results from MT5 EA"""
    if not RESULTS_FILE.exists():
        return []
    
    with open(RESULTS_FILE) as f:
        return json.load(f)

def get_mt5_status():
    """Check if MT5 EA is running and connected"""
    if not STATUS_FILE.exists():
        return {'connected': False, 'last_heartbeat': None}
    
    with open(STATUS_FILE) as f:
        status = json.load(f)
    
    # Check if heartbeat is recent (within last 60 seconds)
    if status.get('last_heartbeat'):
        last_beat = datetime.fromisoformat(status['last_heartbeat'])
        age = (datetime.now(timezone.utc) - last_beat).total_seconds()
        status['connected'] = age < 60
    
    return status

def clear_executed_signals():
    """Remove executed signals from queue"""
    if not SIGNALS_FILE.exists():
        return
    
    with open(SIGNALS_FILE) as f:
        signals = json.load(f)
    
    # Keep only pending signals
    pending = [s for s in signals if s.get('status') == 'pending']
    
    with open(SIGNALS_FILE, 'w') as f:
        json.dump(pending, f, indent=2)

if __name__ == '__main__':
    # Test bridge
    ensure_bridge_dir()
    print(f"✅ Bridge directory created: {BRIDGE_DIR}")
    print(f"Signal file: {SIGNALS_FILE}")
    print(f"Status: {get_mt5_status()}")
