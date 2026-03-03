# Inter-Agent Communication System

**Owner:** Arjuna  
**Purpose:** Enable agents to work together without Rahul managing each one

## Philosophy

**Rahul should talk to 2 agents:**
- Arjuna (operations/execution)
- Aria (strategy/planning)

**We coordinate the other 11.**

## How It Works

### Rahul's Interface (Simple)

```
Rahul: "Arjuna, improve the trading bots"
    ↓
Arjuna: [Analyzes what's needed]
    ↓
Arjuna → Richie: "Analyze current bot performance"
Arjuna → Bruce: "Security audit the trading code"
Arjuna → Sonic: "Optimize execution speed"
    ↓
[Agents work, collaborate if needed]
    ↓
Arjuna: "Done. Bots improved: +15% speed, security patched, win rate up 3%"
```

**Rahul sees:** One request → One response  
**Behind the scenes:** 3 agents coordinated by Arjuna

### Agent-to-Agent Communication

**Method 1: Direct Spawn (Cross-Agent Delegation)**

When one agent needs another:

```python
# Rick needs Tony to polish his prototype
sessions_spawn(
  runtime="subagent",
  mode="run",
  label="stark",
  task="Rick built a prototype at /tmp/rick-proto.py. Polish it for production."
)
```

**Method 2: Shared Workspace**

```
agents/shared/
├── handoffs/           # Work passed between agents
│   ├── rick-to-tony/   # Rick → Tony handoff
│   └── bruce-to-steve/ # Bruce → Steve handoff
├── collaboration/      # Joint work
└── comms/              # Inter-agent messages
```

**Method 3: Via Arjuna (Coordination)**

Agents report to Arjuna, Arjuna coordinates:

```
Bruce: "Found security issue in trading bot"
    ↓
Arjuna: [Delegates to Rick or Tony for fix]
    ↓
Tony: [Fixes issue]
    ↓
Arjuna: "Issue resolved, deploying"
```

## Delegation Rules

### When Rahul Makes a Request

**Arjuna's decision tree:**

1. **Can I do it myself?** → Do it, report back
2. **Need one specialist?** → Spawn them, coordinate, report back
3. **Need multiple specialists?** → Spawn all, coordinate, synthesize report
4. **Strategic question?** → Loop in Aria

**Rahul never sees the coordination complexity.**

### When Agents Need Each Other

**Example: Rick needs Tony**

```
Rick (to Arjuna via sessions_send):
"Prototype ready at /workspace/rick/prototypes/api-connector.py
Needs production polish. Assign to Tony?"

Arjuna:
[Spawns Tony with the task]
[Monitors completion]
[Confirms with Rick when done]

Rick: "Got it, thanks"
```

**Or direct (if authorized):**

```
Rick spawns Tony directly for known handoffs
Logs the delegation to shared workspace
```

## Communication Protocols

### Reporting Up (Agent → Arjuna)

**Format:**
```
**Status:** [done|blocked|in-progress]
**Task:** [what was requested]
**Result:** [outcome or blocker]
**Next:** [what's needed, if anything]
```

### Delegating Down (Arjuna → Agent)

**Format:**
```
**Agent:** {name}
**Task:** {clear instruction}
**Context:** {why this matters}
**Deadline:** {if time-sensitive}
**Handoff:** {who to pass work to next, if any}
```

### Peer Collaboration (Agent ↔ Agent)

**Format:**
```
**From:** {agent name}
**To:** {agent name}
**Need:** {what you need}
**Context:** {brief background}
**Files:** {if any}
```

## Coordination Workflows

### Standard Task Flow

```
1. Rahul → Arjuna: "Do X"
2. Arjuna analyzes:
   - What skills needed?
   - Which agents?
   - Dependencies?
3. Arjuna spawns agents (parallel if possible)
4. Agents execute (collaborate if needed)
5. Arjuna synthesizes results
6. Arjuna → Rahul: "X completed. Results: [summary]"
```

### Complex Project Flow

```
1. Rahul → Aria: "Build feature Y"
2. Aria breaks down:
   - Requirements
   - Agent assignments
   - Timeline
3. Aria → Arjuna: "Execute plan: [breakdown]"
4. Arjuna coordinates agents
5. Agents execute & collaborate
6. Arjuna → Aria: Progress updates
7. Aria → Rahul: "Feature Y: [status]"
```

### Emergency/Urgent Flow

```
1. Rahul → Arjuna: "Production down!"
2. Arjuna immediately:
   - Spawn Bruce (investigate)
   - Spawn Shaggy (monitor)
   - Spawn Tony/Rick (fix)
3. Real-time coordination
4. Arjuna → Rahul: Updates every 5 min
```

## Shared Workspace Structure

```
agents/shared/
├── handoffs/
│   ├── rick-to-tony/
│   │   └── api-connector-v1.py
│   └── bruce-to-steve/
│       └── security-audit-2026-03-02.md
├── collaboration/
│   ├── trading-bot-improvement/
│   │   ├── richie-analysis.md
│   │   ├── sonic-optimization.md
│   │   └── bruce-security-review.md
│   └── shopify-integration/
│       ├── phineas-design.md
│       └── ferb-implementation/
├── comms/
│   └── 2026-03-02/
│       ├── rick-to-arjuna.md
│       └── bruce-to-tony.md
└── README.md
```

## Key Principles

1. **Rahul's interface stays simple** (talk to me or Aria)
2. **Agents coordinate internally** (via spawning or shared workspace)
3. **Arjuna orchestrates** (delegates, monitors, synthesizes)
4. **Aria strategizes** (plans, tracks, reports)
5. **Results > process** (Rahul sees outcomes, not coordination)

## Implementation

**Phase 1 (Tonight):**
- Create shared workspace structure
- Update Arjuna's delegation logic
- Test: Rahul → Arjuna → multi-agent coordination

**Phase 2 (This Week):**
- Agent-to-agent direct spawning
- Collaboration templates
- Handoff protocols

**Phase 3 (Next Week):**
- Automated workflows (Aria assigns → Arjuna executes → agents collaborate)
- Progress dashboards
- Efficiency metrics

---

**Bottom line:** You talk to me or Aria. We handle the other 11. Simple interface, complex coordination hidden.
