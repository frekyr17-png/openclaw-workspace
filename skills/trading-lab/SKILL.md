---
name: trading-lab
description: "Autonomous crypto/metal forex trading strategy lab. Spawns subagents for paper trading on TradingView, evaluates win rates over 1-month periods, keeps winners, replaces losers. Runs 24/7 Mon-Fri. Use when: managing trading strategies, spawning strategy subagents, evaluating paper trading results, iterating trading systems."
---

# Trading Lab

Autonomous strategy evolution system. Deploys strategies → paper trades → evaluates → iterates.

## Core Loop

```
DEPLOY (5 strategies) → EVALUATE (1 month) → EVOLVE (replace losers) → REPEAT
```

## Tracking File

**Path:** `~/.openclaw/workspace/trading-lab/state.json`

Structure:
```json
{
  "strategies": [
    {
      "id": "ALPHA-001",
      "name": "Alpha Trend Rider",
      "type": "trend",
      "market": "BTC/USDT",
      "timeframe": "4h",
      "subagent": "trading-alpha-trend",
      "status": "active",
      "deployed": "2024-01-15",
      "expires": "2024-02-15",
      "trades": [],
      "stats": { "wins": 0, "losses": 0, "winRate": 0 }
    }
  ],
  "history": []
}
```

## Subagent Naming

Pattern: `trading-<strategy-tag>`

Examples:
- `trading-alpha-trend`
- `trading-beta-meanrev`
- `trading-gamma-breakout`
- `trading-delta-momentum`
- `trading-epsilon-swing`

## Strategy Types

| Type | Code | Description |
|------|------|-------------|
| Trend | `trend` | Follow momentum, moving average crossovers |
| Mean Reversion | `meanrev` | Buy oversold, sell overbought |
| Breakout | `breakout` | Trade range expansions |
| Momentum | `momentum` | Ride strong directional moves |
| Swing | `swing` | Multi-day position trades |

## Markets

Primary: BTC/USDT, ETH/USDT, XAU/USD
Secondary: Altcoins, EUR/USD, other metals

## Evaluation

**Primary metric:** Win rate
**Period:** 30 days (1 month)
**Threshold:** Strategies below 50% win rate after evaluation period → replace

### At Evaluation Time

1. Calculate each strategy's win rate
2. Mark losers for replacement
3. Generate new strategies informed by winners' patterns
4. Deploy replacements
5. Archive losers to history

## Daily Operations

**Morning briefing** (check state.json):
- Active strategies count
- Pending evaluations
- Any subagent issues

**During trading hours:**
- Subagents run autonomously
- Log trades to state.json

**End of evaluation period:**
- Run evaluation cycle
- Generate replacement strategies

## Commands

- Start new cycle: Deploy 5 fresh strategies
- Status check: Read state.json, summarize
- Evaluate now: Run evaluation on expired strategies
- Clean slate: Reset state.json, start fresh

## Workflow Reference

See [workflows.md](references/workflows.md) for detailed procedures.