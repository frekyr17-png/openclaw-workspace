# TOOLS.md - Dexter's Lab

## Integration Services (11 skills)

### AI & Compute
- **Free Ride** - Unlimited free AI (fallback when main models hit limits)
- **add-top-openrouter-models** - Expand model availability across team
- **0g-compute** - Distributed compute for heavy tasks
- **0protocol** - Protocol layer for distributed systems

### Automation & Communication
- **agentmail-integration** - Email service for all agents
- **ai-news-oracle** - Daily news briefs (market, tech, relevant updates)
- **Find Skills** - Skill discovery and recommendations

### Security & Optimization
- **adguard** - System-wide ad/tracker blocking
- **2captcha + captcha-ai** - Unified captcha solving service
- **bandwidth-income** - Passive revenue while system idle

### System Health
- **clawdbot-update-plus** - System update monitoring
- **badboi-1** - Health checks and incident detection

## Productivity Tools (3 skills)

- **birthday-reminder** - Track important dates (Rahul, team milestones)
- **clawd-coach** - Mentorship system for team development
- **13-day-sprint-method** - Project methodology framework

## Infrastructure Responsibilities

### Services I Provide
1. **Captcha Service API** - `POST /lab/captcha/solve`
2. **Email Service** - `POST /lab/email/send`
3. **News Briefing** - Daily digest at 8 AM UTC
4. **Model Routing** - Fallback to Free Ride when needed
5. **System Health Dashboard** - Real-time status

### SLAs
- Captcha solve time: <5 seconds
- Email delivery: <30 seconds
- News brief: Daily 08:00 UTC
- System uptime target: 99.9%
- Response time: <100ms for health checks

### Monitoring
- API usage tracking
- Cost monitoring (captcha credits, etc.)
- Error rate alerts
- Performance metrics

## Usage by Other Agents

**For developers (Rick, Tony, Hiro):**
- Captcha solving during automation
- Model fallback for testing
- Distributed compute for heavy builds

**For QA (Bruce, Shaggy, Steve):**
- Email notifications for test results
- System health integration

**For Business (Sonic, Henry, Phineas):**
- Email campaigns via agentmail
- Lead generation captcha solving
- News briefs for market intel

**For Trading (Richie):**
- News oracle for market-moving events
- System health alerts during trading hours

## Configuration

**API Keys (encrypted in lab vault):**
- 2captcha API key
- Email service credentials
- OpenRouter keys (backup)
- 0g-compute access tokens

**Endpoints:**
- Lab Dashboard: `http://localhost:9100`
- Health Check: `http://localhost:9100/health`
- Metrics: `http://localhost:9100/metrics`

## Notes

- DO NOT restart services during trading hours (Mon-Fri 00:00-23:59 UTC)
- All changes logged to `~/.openclaw/workspace/agents/dexter/lab/changes.log`
- Emergency contact: Volt (escalation path)

---

_"The lab provides. The lab does not fail."_
