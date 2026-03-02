#!/bin/bash
# Skill Installation Wrapper
# Wraps molthub install with pre-install security scanning

# Usage: ./install-skill.sh <skill-name> [--force]

SKILL_NAME="${1:-}"
FORCE_FLAG="${2:-}"

if [ -z "$SKILL_NAME" ]; then
    echo "Usage: ./install-skill.sh <skill-name> [--force]"
    echo ""
    echo "This wrapper scans skills for suspicious patterns before installation."
    echo "Suspicious skills will be BLOCKED unless --force is specified."
    exit 1
fi

SKILL_SCANNER="/root/clawd/skills/security-skill-scanner/install-hook.py"
MOLTHUB_BIN="/home/linuxbrew/.linuxbrew/bin/molthub"

echo "🔒 Pre-Install Security Scan: $SKILL_NAME"
echo "============================================"

# Run the pre-install scanner
SCAN_RESULT=$(python3 "$SKILL_SCANNER" "$SKILL_NAME" --scan-only 2>&1)

echo "$SCAN_RESULT"

# Check if blocked
if echo "$SCAN_RESULT" | grep -q "INSTALLATION BLOCKED"; then
    if [ "$FORCE_FLAG" = "--force" ] || [ "$FORCE_FLAG" = "-f" ]; then
        echo ""
        echo "⚠️  WARNING: Installing despite security concerns!"
        echo "Continuing with --force..."
    else
        echo ""
        echo "❌ Installation blocked for security reasons."
        echo ""
        echo "To override and install anyway, run:"
        echo "   ./install-skill.sh $SKILL_NAME --force"
        exit 1
    fi
fi

# Check if already installed
if [ -d "/home/linuxbrew/.linuxbrew/lib/node_modules/clawdbot/skills/$SKILL_NAME" ]; then
    echo ""
    echo "ℹ️  Skill '$SKILL_NAME' is already installed."
    echo "   Use 'molthub update $SKILL_NAME' to update."
    exit 0
fi

# Install the skill
echo ""
echo "🚀 Installing $SKELL_NAME..."

if [ -x "$MOLTHUB_BIN" ]; then
    $MOLTHUB_BIN install "$SKILL_NAME"
else
    echo "⚠️  molthub not found at $MOLTHUB_BIN"
    echo "   Manual installation required."
    echo ""
    echo "   To install manually:"
    echo "   npx molthub@latest install $SKILL_NAME"
fi

echo ""
echo "✅ Installation complete!"
echo ""
echo "📝 Post-install actions:"
echo "   - Run: python3 $SKILL_SCANNER $SKILL_NAME --scan-only"
echo "   - Add to whitelist if legitimate: python3 /root/clawd/skills/security-skill-scanner/whitelist-manager.py add $SKILL_NAME 'reason'"
