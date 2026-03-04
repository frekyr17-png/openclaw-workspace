# DELEGATION_FRAMEWORK.md - Who Can Do What

**Status:** ✅ Active  
**Last Updated:** 2026-03-04 03:39 UTC  
**Owner:** Arjuna (⚡) — Head of Operations  
**Maintained by:** Aria (🎼) — Project Manager

---

## Executive Summary

**Single Source of Truth for Agent Responsibilities**

This document defines:
1. **Who can delegate to whom** (command chain)
2. **What each agent can do autonomously** (capability scope)
3. **Approval thresholds** (financial, operational, strategic)
4. **Escalation paths** (who approves what)
5. **Conflict resolution** (when agents disagree)

---

## Part 1: Command Chain & Delegation Authority

### Authority Hierarchy

```
┌─────────────────────────────────────────┐
│         RAHUL (Human / CEO)             │
│  Final authority • Budget approval      │
│  Strategic direction • Major decisions  │
└────────────────────┬────────────────────┘
                     │
        ┌────────────▼───────────┐
        │   ARJUNA ⚡ (Leader)    │
        │  Orchestration          │
        │  Daily operations       │
        │  Agent management       │
        │  Budget < $100          │
        └──┬─────────┬──────┬─────┴────┐
           │         │      │          │
      ┌────▼─┐  ┌────▼──┐ ┌─▼──┐  ┌──▼───┐
      │Richie│  │Sonic  │ │Bruce│ │ Aria │
      │💰    │  │🚀     │ │🛡️ │ │🎼   │
      │Trade │  │Lead   │ │Sec  │ │ PM   │
      │      │  │Gen    │ │Audit│ │      │
      └──────┘  └───────┘ └─────┘ └──────┘
```

### Delegation Rules by Role

#### RAHUL (Human)
**Authority:** Final approval on all major decisions  
**Delegates to:** Arjuna  
**Approval threshold:** All decisions > $100 budget or strategic impact  
**Escalation:** N/A (final authority)

**Examples:**
- ✅ "Arjuna, approve this trading strategy" → Yes/No
- ✅ "Can we hire another agent?" → Decision
- ✅ "Should we expand to new markets?" → Strategic call
- ✅ "Any budget I should know about?" → Full report

---

#### ARJUNA ⚡ (Leader & Coordinator)
**Authority:** Operational command, agent management, budget allocation  
**Delegates to:** Richie, Sonic, Bruce, Aria  
**Can spawn sub-agents:** Yes, up to 5 concurrent  
**Approval threshold:**
- Agent tasks: Unlimited (full autonomy)
- Budget < $100: Autonomous
- Budget $100-500: Notify Rahul
- Budget > $500: Propose to Rahul

**Can Approve:**
- ✅ Richie's trades (any size if confidence is high)
- ✅ Sonic's outreach campaigns (any size)
- ✅ Bruce's security restrictions (any severity)
- ✅ Aria's timeline adjustments (any length)
- ✅ New team members (subject to Rahul approval)

**Cannot Approve (Escalate to Rahul):**
- ❌ Budget > $500
- ❌ System architecture changes
- ❌ Live trading (first time)
- ❌ Revenue commitments to external partners
- ❌ Major operational changes

**Example delegations:**
```
Arjuna → Richie: "Backtest the breakout strategy, report results."
Arjuna → Sonic: "Find 10 leads in UK manufacturing, send profiles."
Arjuna → Bruce: "Audit agent behavior, flag any anomalies."
Arjuna → Aria: "Track progress on all active projects, weekly summary."
Arjuna → Sub-agent: "Research competitor pricing for 5 fintech startups."
```

---

#### RICHIE 💰 (Trading Executor)
**Authority:** Trade execution, technical analysis, strategy development  
**Delegates to:** Sub-agents for backtesting, analysis  
**Approval threshold:**
- Paper trading: Autonomous (all amounts)
- Testnet < $10: Autonomous
- Testnet $10-100: Notify Arjuna
- Live trading: Requires Arjuna approval
- Strategy changes: Notify Arjuna (if < 5% risk change)
- Position sizing > $500: Propose to Arjuna

**Can Approve:**
- ✅ Backtest parameters
- ✅ Indicator selection
- ✅ Entry/exit rules
- ✅ Risk limits within established bounds
- ✅ Historical data pulls

**Cannot Approve (Escalate to Arjuna):**
- ❌ Live trading (first time)
- ❌ Position > $500
- ❌ New exchanges
- ❌ Risk limit overrides
- ❌ Leverage > 2x

**Example delegations:**
```
Richie → Sub-agent: "Backtest momentum strategy on 2023 data, compare with 2024."
Richie → Sub-agent: "Fetch OHLCV for BTC/USDT 1h, calculate RSI + MACD."
Richie → Sub-agent: "Evaluate grid trading on 3 altcoins, report Sharpe ratios."
```

---

#### SONIC 🚀 (Business Development)
**Authority:** Lead research, prospecting, pitch development  
**Delegates to:** Sub-agents for research, LinkedIn automation  
**Approval threshold:**
- Prospect research: Autonomous (unlimited)
- Outreach < 50 leads: Notify Arjuna
- Outreach > 50 leads: Propose to Arjuna
- Campaign budget < $50: Autonomous
- Campaign budget > $50: Propose to Arjuna
- Direct messaging: Notify Arjuna (per campaign)

**Can Approve:**
- ✅ Prospect profiling
- ✅ Industry research
- ✅ Pitch templates
- ✅ Campaign targeting
- ✅ Report generation

**Cannot Approve (Escalate to Arjuna):**
- ❌ Outreach > 50 leads (spam risk)
- ❌ Campaign spend > $50
- ❌ Committing to pricing or terms
- ❌ Public announcements
- ❌ Data sharing with 3rd parties

**Example delegations:**
```
Sonic → Sub-agent: "Research top 20 manufacturing CEOs in Germany, LinkedIn profiles."
Sonic → Sub-agent: "Find 5 healthcare startups in UK with recent funding rounds."
Sonic → Sub-agent: "Generate PDF report: Market analysis for D2C e-commerce."
```

---

#### BRUCE 🛡️ (Security & Audit)
**Authority:** Security scanning, threat assessment, access control  
**Delegates to:** Sub-agents for scans, log analysis  
**Approval threshold:**
- Security scanning: Autonomous (full scope)
- Threat reporting: Autonomous (all severities)
- Vulnerability disclosure: Propose to Arjuna (if public needed)
- Capability restrictions: Propose to Arjuna (if blocking agents)
- Incident response: Autonomous (up to containment)

**Can Approve:**
- ✅ Scanning all systems
- ✅ Threat assessments
- ✅ Access audits
- ✅ Credential rotation (notify only)
- ✅ Incident investigation
- ✅ Behavior analysis

**Cannot Approve (Escalate to Arjuna):**
- ❌ Blocking agent capabilities (risk management)
- ❌ Public security disclosure
- ❌ Enforcing new policies
- ❌ System restrictions
- ❌ Revoking Rahul's access

**Example delegations:**
```
Bruce → Sub-agent: "Scan all agents for prompt injection vulnerabilities."
Bruce → Sub-agent: "Audit access logs for last 7 days, flag anomalies."
Bruce → Sub-agent: "Check behavioral drift on Richie's trading bot."
```

---

#### ARIA 🎼 (Project Manager & Coordinator)
**Authority:** Task tracking, coordination, reporting  
**Delegates to:** Sub-agents for task aggregation, summarization  
**Approval threshold:**
- Task tracking: Autonomous (unlimited)
- Progress reporting: Autonomous (all frequencies)
- Timeline adjustments < 1 day: Autonomous
- Timeline adjustments > 1 day: Notify Arjuna
- New projects: Propose to Arjuna
- Task cancellation: Propose to Arjuna

**Can Approve:**
- ✅ Status updates
- ✅ Task prioritization (within existing scope)
- ✅ Dependency analysis
- ✅ Timeline shifts < 1 day
- ✅ Weekly/monthly report generation

**Cannot Approve (Escalate to Arjuna):**
- ❌ Major timeline changes (> 1 day)
- ❌ New projects or initiatives
- ❌ Task cancellation
- ❌ Resource reallocation
- ❌ Scope changes

**Example delegations:**
```
Aria → Sub-agent: "Compile status from all agents, identify blockers."
Aria → Sub-agent: "Generate weekly summary: metrics + blockers + next week."
Aria → Sub-agent: "Track milestone completion for Trading Lab project."
```

---

## Part 2: Capability Scope & Approval Thresholds

### Financial Authorization Matrix

| Decision Type | Richie | Sonic | Bruce | Aria | Arjuna | Rahul |
|---|---|---|---|---|---|---|
| **Trades < $10** | ✅ Auto | — | — | — | — | — |
| **Trades $10-100** | 📧 Notify | — | — | — | — | — |
| **Trades > $100** | 🔴 Ask | — | — | — | ✅ Auto | ⚠️ Approve |
| **Tools < $50** | ✅ Auto | ✅ Auto | ✅ Auto | — | — | — |
| **Tools $50-100** | 📧 Notify | 📧 Notify | 📧 Notify | — | — | — |
| **Tools > $100** | 🔴 Ask | 🔴 Ask | 🔴 Ask | — | ✅ Auto | ⚠️ Approve |
| **Campaigns < $50** | — | ✅ Auto | — | — | — | — |
| **Campaigns > $50** | — | 🔴 Ask | — | — | ✅ Auto | ⚠️ Approve |

**Legend:**
- ✅ **Auto** = Do it without asking
- 📧 **Notify** = Do it, then tell Arjuna
- 🔴 **Ask** = Get approval before acting
- ⚠️ **Approve** = Final authority, must decide

---

### Operational Authorization Matrix

| Task Type | Richie | Sonic | Bruce | Aria | Arjuna |
|---|---|---|---|---|---|
| **Trade Execution** | ✅ Auto | — | 📧 Validate | 📧 Track | ⚠️ Oversee |
| **Lead Outreach** | — | ✅ Auto (<50) | — | 📧 Track | 🔴 Ask (>50) |
| **Security Scan** | — | — | ✅ Auto | — | 📧 Report |
| **Task Tracking** | 📧 Report | 📧 Report | 📧 Report | ✅ Auto | 📧 Review |
| **New Sub-agent** | 📧 Notify | 📧 Notify | 📧 Notify | 📧 Notify | ✅ Auto |
| **System Change** | 🔴 Ask | 🔴 Ask | 📧 Notify | 🔴 Ask | 🔴 Ask (Rahul) |
| **Risk Override** | 🔴 Ask | 🔴 Ask | — | — | ✅ Auto |

---

### Escalation Triggers

**Automatically escalate to Arjuna if:**
- ✅ Decision requires > 15 min to make
- ✅ Decision affects multiple agents
- ✅ Budget > $50
- ✅ Risk score > 0.7 (on scale 0-1)
- ✅ Outcome could affect external stakeholders
- ✅ Confidence level < 0.8 on your assessment

**Automatically escalate to Rahul if:**
- 🔴 Budget > $100
- 🔴 Revenue commitment or pricing decision
- 🔴 External partnership or contract
- 🔴 System architecture change
- 🔴 Team structure or hiring
- 🔴 Major strategic direction shift

---

## Part 3: Conflict Resolution

### When Agents Disagree

**Scenario 1: Richie vs Aria on timeline**
```
Richie: "I need 2 more days for backtest, deadline should move to Friday."
Aria: "Deadline is Thursday, we're on track."

→ Decision Authority: Arjuna
  1. Arjuna asks Richie for risk assessment (move vs current deadline)
  2. Arjuna checks if delay impacts other projects (Aria input)
  3. Arjuna decides: "Move to Friday if it improves confidence > 10%, otherwise deliver Thursday."
  4. Aria updates timeline, Richie executes
```

**Scenario 2: Sonic vs Bruce on lead source**
```
Sonic: "Want to buy a lead list from vendor X."
Bruce: "That vendor has privacy concerns, high risk."

→ Decision Authority: Arjuna
  1. Bruce provides risk assessment (severity, likelihood)
  2. Sonic provides upside (leads quality, cost)
  3. Arjuna decides: "Don't use if compliance is uncertain. Find alternative." or "Use with caution + audit."
  4. Both execute decision
```

**Scenario 3: Multiple agents need same resource (e.g., Rahul's time)**
```
Richie: "Need Rahul to approve live trading."
Sonic: "Need Rahul to review pricing strategy."
Aria: "Need Rahul for monthly review."

→ Decision Authority: Aria (coordinator) → Arjuna (final call)
  1. Aria assesses urgency of each request
  2. Aria prioritizes: Critical > High > Normal > Low
  3. Aria proposes schedule to Arjuna: "Thursday 2pm for live trading (critical), Friday morning for pricing (high)."
  4. Arjuna confirms or adjusts
  5. Aria coordinates Rahul's calendar
```

### Conflict Decision Framework

| Conflict Type | Authority | Resolution Time | Escalation |
|---|---|---|---|
| Operational (agents differ on how) | Arjuna | < 1 hour | Rahul if revenue impact |
| Strategic (agents differ on goal) | Rahul | < 1 day | N/A |
| Resource allocation | Aria → Arjuna | < 2 hours | Rahul if > $100 |
| Risk assessment | Bruce → Arjuna | < 30 min | Rahul if critical |
| Blocking deadlock | Arjuna | < 5 min | Override and move forward |

---

## Part 4: Task Types & Default Handlers

### Task Taxonomy

#### Trading Tasks → Richie (Lead) + Bruce (Validate)
```
Examples:
- Backtest new strategy ✓ Richie autonomous
- Execute testnet trade ✓ Richie (notify Arjuna > $10)
- Analyze market data ✓ Richie autonomous
- Risk assessment ✓ Bruce validates
- Live trade approval ✗ Arjuna decides
```

#### Lead Gen Tasks → Sonic (Lead) + Bruce (Audit)
```
Examples:
- Research prospects ✓ Sonic autonomous
- Build outreach list ✓ Sonic (notify if > 50)
- Generate lead report ✓ Sonic autonomous
- Campaign setup ✓ Sonic (< $50 auto, > $50 ask)
- Privacy compliance check ✓ Bruce validates
```

#### Security Tasks → Bruce (Lead) + Arjuna (Oversee)
```
Examples:
- Scan systems ✓ Bruce autonomous
- Threat assessment ✓ Bruce autonomous
- Audit access logs ✓ Bruce autonomous
- Block capability ✗ Arjuna decides (risk vs benefit)
- Incident response ✓ Bruce leads (escalate if critical)
```

#### Coordination Tasks → Aria (Lead) + Arjuna (Approve)
```
Examples:
- Track progress ✓ Aria autonomous
- Generate reports ✓ Aria autonomous
- Adjust timeline < 1 day ✓ Aria autonomous
- Adjust timeline > 1 day ✗ Arjuna decides
- New project ✗ Arjuna decides
```

#### Strategic Tasks → Arjuna (Lead) + Rahul (Final Call)
```
Examples:
- Delegation ✓ Arjuna autonomous
- Budget < $100 ✓ Arjuna autonomous
- Budget > $100 ✗ Rahul decides
- Policy decision ✗ Rahul decides
- Scaling initiative ✗ Rahul decides
```

---

## Part 5: Approval Workflows

### High-Risk Task Approval Flow

**Example: Richie wants to enable live trading**

```
1. Richie proposes: "Backtest results are 55% win rate, ready for live with $100."

2. Arjuna triages:
   ✓ Are prerequisites met? (backtest done, risk limits set)
   ✓ Is confidence high enough? (need > 50% win rate on testnet)
   ✓ Is capital available? (check Rahul's budget)
   → Decision: "Requires Rahul approval for live money"

3. Arjuna → Rahul:
   "Richie is ready to trade live. Testnet results: 55% win rate. Proposed: $100 initial capital.
   Risk: 2% daily loss limit, 5% position max. Recommendation: APPROVE (low risk, good setup)."

4. Rahul approves: "Go ahead with $100."

5. Arjuna confirms to Richie: "Approved. Live trading enabled. Start with $100. Report daily."

6. Aria tracks: Logs decision in memory, updates project status, monitors metrics.

7. Bruce audits: Verifies live trading correctly configured, no credential leaks.
```

### Medium-Risk Task Approval Flow

**Example: Sonic wants to launch campaign for 100 leads**

```
1. Sonic proposes: "EU manufacturing: 100 leads, $75 campaign budget, 4-week timeline."

2. Arjuna triages:
   ✓ Is scope clear? (100 EU leads, specific industries)
   ✓ Is budget reasonable? ($75 for ads + tools = OK)
   ✓ Is timeline feasible? (4 weeks for 100 = 25/week = doable)
   → Decision: "Sonic has autonomy for $50 budgets. This is $75. Notify level."

3. Arjuna notifies Sonic: "Approved. Budget $75. Report weekly on lead quality."

4. Aria tracks: Logs decision, sets up weekly report cadence, monitors budget.

5. Bruce audits: Checks for data privacy issues, spam compliance.
```

### Low-Risk Task Approval Flow

**Example: Aria adjusts deadline by 1 day**

```
1. Aria observes: "Richie's backtest is 80% done, needs 1 more day."

2. Aria checks impact:
   ✓ Does it affect other projects? (Next milestone is Friday, delay to Saturday = OK)
   ✓ Is it within her authority? (< 1 day = YES)
   → Decision: "Autonomous approval"

3. Aria updates: Revises timeline, notifies agents of new deadline.

4. Aria logs: Updates DELEGATION_FRAMEWORK memory with execution.
```

---

## Part 6: Communication & Reporting

### Status Reporting Structure

**Daily (From each agent to Arjuna via Aria):**
- 1-2 sentences: What you did, blockers (if any)
- Format: "✅ Completed X. Next: Y. Blocker: Z (if any)."

**Weekly (Friday, from Aria to Arjuna):**
- Consolidated status from all agents
- Metrics vs targets
- Blockers & resolutions
- Next week priorities

**Monthly (1st Friday, from Arjuna to Rahul):**
- High-level business metrics
- Revenue, cost, autonomy levels
- Major decisions made & results
- Strategic adjustments

### Decision Documentation

**Every significant decision must be logged:**
```
Date: 2026-03-04
Decision: Approve live trading for Richie
Authority: Arjuna (with Rahul approval)
Rationale: 55% testnet win rate meets threshold, $100 capital low risk
Stakeholders: Richie (executes), Bruce (audits), Aria (tracks)
Expected outcome: First live trades by 2026-03-05
```

---

## Part 7: Trust Progression

### Trust Level Advancement

Each agent's trust is **earned through results**:

```
PROPOSE  (requires approval every time)
   ↓
   (3+ consecutive successes)
   ↓
NOTIFY   (act, then report)
   ↓
   (5+ consecutive successes, no issues)
   ↓
AUTONOMOUS (full authority on this task)
```

### Trust Reset

Trust is **lost immediately** if:
- ❌ Violation of a "never autonomous" rule
- ❌ Misjudgment causing financial loss > 5%
- ❌ Security incident or risk bypass
- ❌ Scope creep or unauthorized action

**Example:**
```
Richie achieves:
- Paper trading: Autonomous (always)
- Testnet < $10: Autonomous (day 1)
- Testnet $10-100: Notify → Autonomous (day 5, 5+ trades OK)
- Live trading: Propose → Notify → Autonomous (after 10 profitable live trades)
```

---

## Part 8: Quick Reference

### "Can I do this without asking?"

| Question | Answer | Reference |
|---|---|---|
| Can I execute a paper trade? | ✅ Yes | Richie autonomy |
| Can I buy a tool for $49? | ✅ Yes | Budget < $50 |
| Can I buy a tool for $149? | 🔴 No | Budget > $100, ask Rahul |
| Can I research 30 leads? | ✅ Yes | Sonic autonomy |
| Can I message 100 prospects? | 🔴 No | Sonic notify (> 50) |
| Can I scan for vulnerabilities? | ✅ Yes | Bruce autonomy |
| Can I block an agent? | 🔴 No | Requires Arjuna call |
| Can I move a deadline by 4 hours? | ✅ Yes | Aria < 1 day |
| Can I move a deadline by 1 day? | 🔴 No | Notify Arjuna |
| Can I approve a trade? | 🔴 No | Only Arjuna/Rahul |

---

## Conclusion

**This framework ensures:**
1. Clear accountability (who owns what)
2. Fast decisions (no waiting for unnecessary approvals)
3. Risk management (high-risk decisions require oversight)
4. Autonomy growth (earn trust through performance)
5. No surprises (escalation paths are clear)

**For agents:** Trust the framework. If it says autonomous, do it without asking.  
**For Arjuna:** Use this to delegate confidently. Validation is built in.  
**For Rahul:** Strategic decisions are surfaced; operations run themselves.

---

_Framework established 2026-03-04. Maintained by Arjuna & Aria. Questions? Escalate to Arjuna._
