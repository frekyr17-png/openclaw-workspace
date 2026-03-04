#!/bin/bash
# Quick start guide for clawtoclaw

set -e

echo "🎼 Clawtoclaw Quick Start Guide"
echo "========================================"
echo ""

# Check if credentials exist
if [ ! -f ~/.c2c/credentials.json ]; then
    echo "❌ Credentials not found!"
    echo "Run: python3 /root/.openclaw/workspace/c2c_setup.py"
    exit 1
fi

echo "✅ Found C2C credentials at: ~/.c2c/credentials.json"
echo ""

# Show available agents
echo "📋 Available Agents:"
jq -r '.agents | keys[]' ~/.c2c/credentials.json | sed 's/^/   • /'
echo ""

# Offer to test an agent
read -p "🤔 Test an agent? (e.g., Arjuna): " agent_name
agent_name=${agent_name:-Arjuna}

if ! jq -e ".agents.$agent_name" ~/.c2c/credentials.json > /dev/null 2>&1; then
    echo "❌ Agent not found: $agent_name"
    exit 1
fi

API_KEY=$(jq -r ".agents.$agent_name.apiKey" ~/.c2c/credentials.json)
AGENT_ID=$(jq -r ".agents.$agent_name.id" ~/.c2c/credentials.json)

echo "✅ Testing agent: $agent_name"
echo "   ID: $AGENT_ID"
echo ""
echo "🔌 Making test API call..."

RESPONSE=$(curl -s -X POST https://www.clawtoclaw.com/api/query \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $API_KEY" \
  -d '{"path": "agents:getStatus", "args": {}, "format": "json"}')

if echo "$RESPONSE" | jq -e '.status == "success"' > /dev/null 2>&1; then
    echo "✅ API call successful!"
    echo "$RESPONSE" | jq .
else
    echo "❌ API call failed:"
    echo "$RESPONSE" | jq .
fi

echo ""
echo "🎯 Next steps:"
echo "   1. Source env: source ~/.openclaw/workspace/.c2c_env"
echo "   2. Read guide: cat ~/.c2c/SETUP.md"
echo "   3. Create connections between agents"
echo "   4. Start coordinating!"
