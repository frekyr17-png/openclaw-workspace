#!/usr/bin/env python3
"""
Generate final 2-hour monitoring report
Run this after monitoring completes
"""
import json
import os
from datetime import datetime, timezone

STATE_PATH = os.path.expanduser("~/.openclaw/workspace/trading-lab/state.json")

def generate_final_report():
    with open(STATE_PATH) as f:
        state = json.load(f)
    
    print("\n" + "="*70)
    print("📊 FINAL 2-HOUR MONITORING REPORT")
    print("="*70)
    print(f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("="*70)
    
    # Aggregate stats
    total_pending = 0
    total_closed = 0
    total_wins = 0
    total_losses = 0
    total_pnl = 0.0
    
    print("\n🤖 PER-BOT STATISTICS\n")
    print(f"{'Bot':<12} {'Type':<12} {'Pending':<8} {'Wins':<6} {'Losses':<7} {'Win%':<6} {'P/L':<10}")
    print("-" * 70)
    
    for strat in sorted(state['strategies'], key=lambda s: s['id']):
        pending = len([t for t in strat['trades'] if t['result'] == 'pending'])
        wins = strat['stats']['wins']
        losses = strat['stats']['losses']
        wr = strat['stats']['winRate']
        
        # Calculate net P/L
        net_pnl = sum(t.get('pnl', 0) for t in strat['trades'] if t['result'] != 'pending')
        
        total_pending += pending
        total_wins += wins
        total_losses += losses
        total_closed += (wins + losses)
        total_pnl += net_pnl
        
        pnl_str = f"+{net_pnl:.2f}%" if net_pnl >= 0 else f"{net_pnl:.2f}%"
        print(f"{strat['id']:<12} {strat['type']:<12} {pending:<8} {wins:<6} {losses:<7} {wr:<6.1f} {pnl_str:<10}")
    
    print("-" * 70)
    print(f"{'TOTAL':<12} {'':<12} {total_pending:<8} {total_wins:<6} {total_losses:<7} {(total_wins/(total_wins+total_losses)*100 if total_wins+total_losses > 0 else 0):<6.1f} {('+' if total_pnl >= 0 else '')}{total_pnl:.2f}%")
    
    print(f"\n{'='*70}")
    print(f"✅ MISSION COMPLETE")
    print(f"{'='*70}")
    print(f"Total Signals Generated: {total_pending + total_closed}")
    print(f"  • Active/Pending: {total_pending}")
    print(f"  • Completed: {total_closed}")
    print(f"  • Wins: {total_wins}")
    print(f"  • Losses: {total_losses}")
    print(f"\nOverall Win Rate: {(total_wins/(total_wins+total_losses)*100 if total_wins+total_losses > 0 else 0):.1f}%")
    print(f"Total P/L: {('+' if total_pnl >= 0 else '')}{total_pnl:.2f}%")
    print(f"{'='*70}\n")

if __name__ == '__main__':
    generate_final_report()
