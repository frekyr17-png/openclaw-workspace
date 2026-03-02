# MT5 Setup Guide for Linux Gold Trading

## Architecture

**Python (Linux)** ↔ **File Bridge** ↔ **MT5 EA (Wine/Windows)**

- Python trader writes signals to `mt5_bridge/signals.json`
- MT5 Expert Advisor reads signals, executes trades, writes results
- Python reads results and updates state.json

## Current Status

✅ **Python bridge module created:** `mt5_bridge.py`
✅ **MT5 installed:** Via Wine at `/root/.wine/drive_c/Program Files/MetaTrader 5/`
✅ **Exness account:** Login 413408643, Server Exness-MT5Trial6
❌ **MT5 EA not installed yet** (needs MQL5 code + manual setup)

## Next Steps

### Option A: File-Based Bridge (Simpler, Manual Setup Required)

**Step 1:** Create MQL5 Expert Advisor
- File: `SignalBridge.mq5` (provided below)
- Compile in MetaEditor
- Attach to XAUUSD chart
- Enable AutoTrading

**Step 2:** EA monitors `signals.json` every second
- Reads pending signals
- Executes market orders
- Writes results to `results.json`
- Updates status heartbeat

**Step 3:** Python trader uses `mt5_bridge.py` to:
- Write trade signals
- Monitor execution status
- Update strategy state

### Option B: Native REST API (Complex but Better)

Use mt5linux RPC server (requires additional setup):
1. Install MQL5 RPC server EA
2. Configure port forwarding through Wine
3. Use `mt5linux.MetaTrader5()` Python client

**Recommendation:** Start with Option A (file bridge) for MVP, migrate to Option B later.

## MQL5 Expert Advisor Code

Save this as `SignalBridge.mq5` in MT5's `MQL5/Experts/` folder:

```mql5
//+------------------------------------------------------------------+
//| SignalBridge.mq5 - Python Signal Executor                         |
//| Reads JSON signals from Python, executes trades, writes results   |
//+------------------------------------------------------------------+
#property copyright "Trading Lab"
#property version   "1.00"
#property strict

#include <JAson.mqh>  // JSON parser (download from CodeBase)

string signalsPath = "C:\\users\\USERNAME\\.openclaw\\workspace\\trading-lab\\mt5_bridge\\signals.json";
string resultsPath = "C:\\users\\USERNAME\\.openclaw\\workspace\\trading-lab\\mt5_bridge\\results.json";
string statusPath  = "C:\\users\\USERNAME\\.openclaw\\workspace\\trading-lab\\mt5_bridge\\status.json";

int lastSignalCount = 0;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit() {
    Print("SignalBridge EA started");
    EventSetTimer(1);  // Check signals every 1 second
    UpdateStatus();
    return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Timer function - check for new signals                           |
//+------------------------------------------------------------------+
void OnTimer() {
    UpdateStatus();
    ProcessSignals();
}

//+------------------------------------------------------------------+
//| Update status heartbeat                                          |
//+------------------------------------------------------------------+
void UpdateStatus() {
    string status = "{";
    status += "\"connected\": true,";
    status += "\"account\": " + IntegerToString(AccountInfoInteger(ACCOUNT_LOGIN)) + ",";
    status += "\"balance\": " + DoubleToString(AccountInfoDouble(ACCOUNT_BALANCE), 2) + ",";
    status += "\"equity\": " + DoubleToString(AccountInfoDouble(ACCOUNT_EQUITY), 2) + ",";
    status += "\"last_heartbeat\": \"" + TimeToString(TimeCurrent(), TIME_DATE|TIME_SECONDS) + "\"";
    status += "}";
    
    int handle = FileOpen(statusPath, FILE_WRITE|FILE_TXT|FILE_ANSI);
    if(handle != INVALID_HANDLE) {
        FileWriteString(handle, status);
        FileClose(handle);
    }
}

//+------------------------------------------------------------------+
//| Process pending signals                                          |
//+------------------------------------------------------------------+
void ProcessSignals() {
    // Read signals.json
    int handle = FileOpen(signalsPath, FILE_READ|FILE_TXT|FILE_ANSI);
    if(handle == INVALID_HANDLE) return;
    
    string content = "";
    while(!FileIsEnding(handle)) {
        content += FileReadString(handle);
    }
    FileClose(handle);
    
    // Parse JSON and execute pending trades
    // (Full implementation requires JSON parser - simplified for now)
    
    // After execution, write results.json
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason) {
    EventKillTimer();
    Print("SignalBridge EA stopped");
}
```

**Note:** Full MQL5 implementation requires JSON parser library and error handling.

## Simpler Alternative: REST API Approach

Instead of file bridge, consider using a broker with Python REST API:
- **OANDA:** Native Python library, supports gold (XAU/USD)
- **Interactive Brokers:** `ib_insync` library
- **FXCM:** REST API available

These avoid Wine/MT5 complexity entirely.

## Current Decision Point

**Rahul:** Do you want me to:

1. **Continue with MT5 file bridge** (requires manual EA setup in MT5 GUI)
2. **Switch to OANDA/IB** for native Python gold trading (faster setup)
3. **Fix Binance PAXG thresholds first** (test strategies before going live)

All three can run in parallel, but (3) gives immediate data while (1)/(2) are production paths.
