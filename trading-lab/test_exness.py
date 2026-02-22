#!/usr/bin/env python3
"""Test MT5 connection for Exness"""
import subprocess
import sys

# Check if MetaTrader5 package is available
try:
    import MetaTrader5 as mt5
    HAS_MT5 = True
except ImportError:
    HAS_MT5 = False
    print("⚠️ MetaTrader5 Python package not installed")
    print("   This is needed for Exness/MT5 trading")

if HAS_MT5:
    # Load credentials
    import os
    cred_path = os.path.expanduser("~/.openclaw/workspace/trading-lab/credentials.env")
    creds = {}
    with open(cred_path) as f:
        for line in f:
            line = line.strip()
            if '=' in line and not line.startswith('#'):
                key, val = line.split('=', 1)
                creds[key.strip()] = val.strip()

    login = int(creds.get('EXNESS_MT5_LOGIN', '0'))
    password = creds.get('EXNESS_MT5_PASSWORD', '')
    server = creds.get('EXNESS_MT5_SERVER', '').strip()

    print(f"Testing MT5 connection to {server}...")
    print(f"Login: {login}")

    # Initialize MT5
    if not mt5.initialize():
        print(f"❌ MT5 initialize() failed: {mt5.last_error()}")
        sys.exit()

    # Login
    authorized = mt5.login(login, password, server)
    if authorized:
        print(f"✅ MT5 Connected to {server}")
        account_info = mt5.account_info()
        if account_info:
            print(f"   Balance: {account_info.balance} {account_info.currency}")
            print(f"   Equity: {account_info.equity}")
            print(f"   Margin free: {account_info.margin_free}")
    else:
        print(f"❌ MT5 login failed: {mt5.last_error()}")

    mt5.shutdown()
else:
    print("\nTo enable MT5 trading, install:")
    print("  pip install MetaTrader5")
    print("\nNote: MT5 terminal must also be installed and running")