#!/usr/bin/env python3
"""Test Binance API connectivity"""
import os
import hmac
import hashlib
import time
import urllib.request
import urllib.parse
import json

# Load credentials
cred_path = os.path.expanduser("~/.openclaw/workspace/trading-lab/credentials.env")
creds = {}
with open(cred_path) as f:
    for line in f:
        line = line.strip()
        if '=' in line and not line.startswith('#'):
            key, val = line.split('=', 1)
            creds[key.strip()] = val.strip()

api_key = creds.get('BINANCE_API_KEY', '')
secret_key = creds.get('BINANCE_SECRET_KEY', '')
use_testnet = creds.get('BINANCE_USE_TESTNET', 'false').lower() == 'true'

if use_testnet:
    base_url = "https://demo-api.binance.com"
else:
    base_url = "https://api.binance.com"

# Test connectivity
print(f"Testing Binance {'testnet' if use_testnet else 'mainnet'}...")

# Public endpoint test
try:
    req = urllib.request.Request(f"{base_url}/api/v3/ping")
    with urllib.request.urlopen(req, timeout=10) as resp:
        print(f"✅ Ping OK: {resp.read().decode()}")
except Exception as e:
    print(f"❌ Ping failed: {e}")

# Signed endpoint test (account info)
timestamp = int(time.time() * 1000)
query_string = f"timestamp={timestamp}"
signature = hmac.new(
    secret_key.encode(),
    query_string.encode(),
    hashlib.sha256
).hexdigest()
url = f"{base_url}/api/v3/account?{query_string}&signature={signature}"

try:
    req = urllib.request.Request(url)
    req.add_header("X-MBX-APIKEY", api_key)
    with urllib.request.urlopen(req, timeout=10) as resp:
        data = json.loads(resp.read().decode())
        print(f"✅ Account API OK")
        print(f"   Maker commission: {data.get('makerCommission', 'N/A')}")
        print(f"   Taker commission: {data.get('takerCommission', 'N/A')}")
        balances = [b for b in data.get('balances', []) if float(b['free']) > 0 or float(b['locked']) > 0]
        print(f"   Non-zero balances: {len(balances)}")
        if balances:
            for b in balances[:5]:
                print(f"      {b['asset']}: {b['free']} (free)")
except urllib.error.HTTPError as e:
    print(f"❌ Account API failed: {e.code}")
    print(f"   Response: {e.read().decode()}")
except Exception as e:
    print(f"❌ Account API error: {e}")