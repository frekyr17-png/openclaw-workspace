# Trading Lab Workflows

## Deployment Workflow

1. Generate 5 diverse strategies (vary type, market, timeframe)
2. For each strategy:
   - Create subagent with proper naming
   - Log to state.json with deployment date + expiration (30 days)
3. Update phase to "trading"

```bash
# Spawn strategy subagent
sessions_spawn agentId="trading-strategy" task="Paper trade BTC/USDT using trend following on 4h timeframe. Log all trades to trading-lab/state.json. Run M-F during market hours."
```

## Evaluation Workflow

Run when any strategy has expired (30 days):

1. Load state.json
2. For each expired strategy:
   - Calculate: wins / (wins + losses) = winRate
   - If winRate < 0.50: mark REPLACE
   - If winRate >= 0.50: mark KEEP
3. Generate replacement strategies inspired by winners
4. Archive REPLACE strategies to history
5. Deploy replacements
6. Increment cycle counter

## Trade Logging Format

Each trade logged to strategy's `trades` array:

```json
{
  "timestamp": "2024-01-20T14:30:00Z",
  "action": "BUY",
  "market": "BTC/USDT",
  "entry": 42500,
  "exit": 43100,
  "result": "win",
  "pnl": 1.41
}
```

## Status Check

Quick status for heartbeats:

```
Cycle: 1 | Active: 5 | Next Eval: 2024-02-15
Alpha: 62% | Beta: 45% | Gamma: 58% | Delta: 51% | Epsilon: 39%
```

## Strategy Generation Prompts

When creating new strategies, draw from:

- **Winner patterns:** What's working? Similar types, timeframes, markets
- **Loser lessons:** What failed? Avoid similar setups
- **Diversity:** Mix types, vary timeframes, spread across markets

## Token Efficiency

- Brief subagent task prompts (they have trading context)
- Log trades as JSON (minimal parsing)
- Status checks: numbers only, no prose
- Batch evaluations at month-end, not daily