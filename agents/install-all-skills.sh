#!/bin/bash

# MEGA-SKILL INSTALLATION SCRIPT
# Installs all 67 skills organized by mega-skill category
# Created: 2026-03-02 by Volt

set -e  # Exit on error

SKILLS_DIR="$HOME/.openclaw/workspace/skills"
TEMP_REPO="/tmp/openclaw-skills-repo"
LOG_FILE="$HOME/.openclaw/workspace/agents/skill-installation.log"

echo "=== MEGA-SKILL INSTALLATION STARTED ===" | tee -a "$LOG_FILE"
echo "Time: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"

cd "$SKILLS_DIR"

# Function to install from ClawHub
install_clawhub() {
    local skill_name=$1
    echo "  📦 Installing $skill_name from ClawHub..." | tee -a "$LOG_FILE"
    if clawhub install "$skill_name" --force 2>&1 | tee -a "$LOG_FILE"; then
        echo "  ✅ $skill_name installed" | tee -a "$LOG_FILE"
    else
        echo "  ⚠️  $skill_name failed (might not exist in ClawHub)" | tee -a "$LOG_FILE"
    fi
}

# Function to install from GitHub
install_github() {
    local skill_path=$1
    local skill_name=$(basename "$skill_path")
    local author=$(echo "$skill_path" | cut -d'/' -f6)
    
    echo "  🐙 Installing $skill_name from GitHub ($author)..." | tee -a "$LOG_FILE"
    
    # Clone if repo doesn't exist
    if [ ! -d "$TEMP_REPO" ]; then
        echo "  📥 Cloning openclaw/skills repository..." | tee -a "$LOG_FILE"
        git clone https://github.com/openclaw/skills.git "$TEMP_REPO" 2>&1 | tee -a "$LOG_FILE"
    fi
    
    # Copy skill
    local source_path="$TEMP_REPO/skills/$author/$skill_name"
    if [ -d "$source_path" ]; then
        cp -r "$source_path" "$SKILLS_DIR/$skill_name" 2>&1 | tee -a "$LOG_FILE"
        echo "  ✅ $skill_name installed from GitHub" | tee -a "$LOG_FILE"
    else
        echo "  ⚠️  $skill_name not found at $source_path" | tee -a "$LOG_FILE"
    fi
}

#=====================================================
# BATCH 1: SELF-EVOLVING INTELLIGENCE CORE (Volt ⚡)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🧠 BATCH 1: Self-Evolving Intelligence Core (8 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "self-improving"
install_clawhub "memory-setup"
install_clawhub "memory-manager"
install_clawhub "self-evolving-skill"
install_clawhub "tokenoptimizer"
install_github "roosch269/agent-self-assessment"
install_github "rushant-123/session-cost-tracker"

#=====================================================
# BATCH 2: SECURITY COMMAND CENTER (Mr Bean + QA)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🛡️ BATCH 2: Security Command Center (9 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "moltguard"
install_clawhub "clawrouter"
install_github "trypto1019/arc-trust-verifier"
install_github "fatfingererr/azhua-skill-vetter"
install_github "sharbelayy/agent-audit"
install_github "sanguineseal/aegis-audit"
install_github "mrcerq/agentcanary"
install_github "nukewire/clawdefender"
install_github "andyxinweiminicloud/behavioral-invariant-monitor"

#=====================================================
# BATCH 3: TRADING INTELLIGENCE PLATFORM (Richie 💰)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "💰 BATCH 3: Trading Intelligence Platform (8 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "stock-market-pro"
install_clawhub "crypto"
install_clawhub "self-learning-base-trader"
install_clawhub "trading-coach"
install_clawhub "trading-token-profiler"
install_clawhub "gold-trading-skill"
install_clawhub "mt5-httpapi"
install_github "amitabhainarunachala/agentic-ai-gold"

#=====================================================
# BATCH 4: DEVELOPER TOOLKIT (Rick/Tony/Hiro)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "💻 BATCH 4: Developer Toolkit (6 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "api-gateway"
install_clawhub "playwright-mcp"
install_clawhub "debug-pro"
install_github "0xbreadguy/megaeth-ai-developer-skills"
install_github "enderfga/claude-code-skill"
install_github "chris6970barbarian-hue/acp"

#=====================================================
# BATCH 5: BUSINESS AUTOMATION HUB (Sonic/Henry/Phineas)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "⚡ BATCH 5: Business Automation Hub (10 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "automation-workflows"
install_clawhub "n8n-workflow-automation"
install_clawhub "shopify"
install_clawhub "clickup"
install_clawhub "asana"
install_clawhub "microsoft-365-mcp-server"
install_clawhub "accountant"
install_clawhub "linkedin-lead-generation"
install_github "highlander89/ai-lead-generator-skill"
install_github "lngdao/agenthire"

#=====================================================
# BATCH 6: MARKETING & DESIGN STUDIO (Henry 😈)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🎨 BATCH 6: Marketing & Design Studio (4 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "marketing-mode"
install_clawhub "superdesign"
install_github "blackshady1130-jpg/ai-review"
install_github "luruibu/beauty-generation-api"

#=====================================================
# BATCH 7: AGENT ORCHESTRATION LAYER (Aria 🎼)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🎼 BATCH 7: Agent Orchestration Layer (5 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "agent-directory"
install_clawhub "moltbook"
install_github "agentandbot-design/agents-manager"
install_github "thibautrey/agent-hq"
install_github "thesethrose/agent-browser"

#=====================================================
# BATCH 8: INTEGRATION TOOLS (Dexter 🔬)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🔬 BATCH 8: Integration Tools (11 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_clawhub "free-ride"
install_clawhub "find-skills"
install_github "adinvadim/2captcha"
install_github "fusionlabssource/captcha-ai"
install_github "synesthesia-wav/agentmail-integration"
install_github "swimmingkiim/ai-news-oracle"
install_github "rowbotik/adguard"
install_github "in-liberty420/0g-compute"
install_github "0isone/0protocol"
install_github "chunhualiao/add-top-openrouter-models"
install_github "mariusfit/bandwidth-income"

#=====================================================
# BATCH 9: PRODUCTIVITY TOOLS (Dexter 🔬)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "📅 BATCH 9: Productivity Tools (3 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_github "manantra/birthday-reminder"
install_github "shiv19/clawd-coach"
install_github "galizki/13-day-sprint-method"

#=====================================================
# BATCH 10: SYSTEM HEALTH (Dexter 🔬)
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "🏥 BATCH 10: System Health (2 skills)" | tee -a "$LOG_FILE"
echo "==========================================" | tee -a "$LOG_FILE"

install_github "hopyky/clawdbot-update-plus"
install_github "orlyjamie/badboi-1"

#=====================================================
# COMPLETION
#=====================================================
echo "" | tee -a "$LOG_FILE"
echo "=== INSTALLATION COMPLETE ===" | tee -a "$LOG_FILE"
echo "Time: $(date)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "📊 Summary:" | tee -a "$LOG_FILE"
echo "  Total skills targeted: 66" | tee -a "$LOG_FILE"
echo "  Skills installed: $(ls -1 $SKILLS_DIR | wc -l)" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "📝 Log saved to: $LOG_FILE" | tee -a "$LOG_FILE"
echo "" | tee -a "$LOG_FILE"
echo "🔍 Next Steps:" | tee -a "$LOG_FILE"
echo "  1. Security scan (Mr Bean): Review all installed skills" | tee -a "$LOG_FILE"
echo "  2. Agent assignment: Distribute skills to team members" | tee -a "$LOG_FILE"
echo "  3. Testing: Each agent tests their mega-skill" | tee -a "$LOG_FILE"
echo "  4. Integration: Connect to n8n, APIs, services" | tee -a "$LOG_FILE"
echo "  5. Report to Rahul: Full capability overview" | tee -a "$LOG_FILE"

# Cleanup
rm -rf "$TEMP_REPO"
echo "" | tee -a "$LOG_FILE"
echo "✅ Cleanup complete. Ready for security review." | tee -a "$LOG_FILE"
