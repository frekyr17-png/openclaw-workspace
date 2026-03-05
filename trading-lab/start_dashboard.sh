#!/bin/bash

# Start simple HTTP server for dashboard
PORT=8000
WORKSPACE="/root/.openclaw/workspace/trading-lab"

echo "🚀 Starting Trading Lab Dashboard..."
echo "📊 Open your browser: http://localhost:8000/dashboard.html"
echo "📍 Or access remotely: http://[YOUR_VPS_IP]:8000/dashboard.html"
echo ""
echo "Press Ctrl+C to stop"
echo ""

cd "$WORKSPACE"
python3 -m http.server $PORT
