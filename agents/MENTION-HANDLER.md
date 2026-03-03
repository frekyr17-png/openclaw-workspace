# Team @-Mention Handler

**Owner:** Arjuna  
**Purpose:** Direct @ access to team members

## How It Works

When Rahul messages starting with @, auto-spawn the agent:

```
@richie check the bots
@aria what's the status?
@mrbean scan the new skills
```

## Agent Mappings

| Mention | Agent | Role |
|---------|-------|------|
| @richie | Richie Rich | Trading Specialist |
| @aria | Aria | Project Manager |
| @mrbean | Mr Bean | Security Guardian |
| @tony, @arjuna | Arjuna (me) | Head of Operations |

## Detection Rules

**Pattern:** `^@(richie|aria|mrbean|tony|arjuna)\s+(.+)`

**Action:**
1. Detect @ mention at start of message
2. Extract agent name + message
3. Spawn agent with message as task
4. Return response directly to Rahul

**Model:** Use Claude Sonnet 4.5 for all spawns (reliable, fast)

## Implementation

Built into Arjuna's message processing. No user action needed.

---

**Status:** Active
