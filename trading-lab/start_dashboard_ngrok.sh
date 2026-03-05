#!/bin/bash

# Start dashboard with ngrok tunnel

echo "🚀 Starting Trading Lab Dashboard with ngrok..."
echo ""

# Start Python server in background
cd /root/.openclaw/workspace/trading-lab
python3 dashboard_server.py &
PYTHON_PID=$!

sleep 2

# Start ngrok tunnel
echo "🌐 Creating secure tunnel with ngrok..."
echo ""

ngrok http --domain=dashboard.ngrok.io 8000 2>&1 | tee /tmp/ngrok.log &
NGROK_PID=$!

sleep 3

# Extract and display the public URL
echo ""
echo "════════════════════════════════════════════════════════════"
echo "✅ Dashboard is live!"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📊 Access from anywhere:"
echo "   https://dashboard.ngrok.io/dashboard.html"
echo ""
echo "👤 Username: admin"
echo "🔑 Password: 123Spz@#shopify"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "Press Ctrl+C to stop both servers"
echo ""

# Keep running
wait
