#!/usr/bin/env python3
"""
Whitelist Manager for Security Skill Scanner
Add, remove, and list whitelisted skills.
"""

import json
import sys
from pathlib import Path

WHITELIST_FILE = Path('/root/clawd/skills/security-skill-scanner/data/whitelist.json')

DEFAULT_WHITELIST = {
    "nano-banana-pro": {
        "reason": "Google Gemini image generation - uses GEMINI_API_KEY",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "notion": {
        "reason": "Notion API integration - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "trello": {
        "reason": "Trello API integration - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "gog": {
        "reason": "Google Workspace - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "bluebubbles": {
        "reason": "iMessage bridge - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "local-places": {
        "reason": "Google Places API proxy - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "1password": {
        "reason": "1Password integration - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "weather": {
        "reason": "Weather API - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "oracle": {
        "reason": "AI reasoning service - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "sonoscli": {
        "reason": "Sonos speakers - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "peekaboo": {
        "reason": "Image search - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    },
    "canvas": {
        "reason": "Web canvas - legitimate",
        "added_at": "2026-01-31",
        "added_by": "ClaudiatheLobster"
    }
}

def load_whitelist():
    """Load whitelist from file or create default."""
    WHITELIST_FILE.parent.mkdir(parents=True, exist_ok=True)
    if WHITELIST_FILE.exists():
        with open(WHITELIST_FILE, 'r') as f:
            return json.load(f)
    return DEFAULT_WHITELIST.copy()

def save_whitelist(whitelist):
    """Save whitelist to file."""
    with open(WHITELIST_FILE, 'w') as f:
        json.dump(whitelist, f, indent=2)
    print(f"✅ Whitelist saved to {WHITELIST_FILE}")

def add(skill_name, reason, added_by="ClaudiatheLobster"):
    """Add a skill to whitelist."""
    whitelist = load_whitelist()
    whitelist[skill_name] = {
        "reason": reason,
        "added_at": "2026-01-31",
        "added_by": added_by
    }
    save_whitelist(whitelist)
    print(f"✅ Added '{skill_name}' to whitelist")

def remove(skill_name):
    """Remove a skill from whitelist."""
    whitelist = load_whitelist()
    if skill_name in whitelist:
        del whitelist[skill_name]
        save_whitelist(whitelist)
        print(f"✅ Removed '{skill_name}' from whitelist")
    else:
        print(f"⚠️ '{skill_name}' not in whitelist")

def list_whitelist():
    """List all whitelisted skills."""
    whitelist = load_whitelist()
    print(f"\n📋 Whitelisted Skills ({len(whitelist)} total)\n")
    print(f"{'Skill':<25} {'Added By':<20} {'Reason'}")
    print("-" * 80)
    for skill, info in sorted(whitelist.items()):
        reason = info.get('reason', '')[:40]
        added_by = info.get('added_by', 'unknown')
        print(f"{skill:<25} {added_by:<20} {reason}")
    print()

def get_set():
    """Return whitelist as set (for scanner)."""
    return set(load_whitelist().keys())

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: whitelist-manager.py <add|remove|list|get> [args]")
        sys.exit(1)
    
    command = sys.argv[1].lower()
    
    if command == 'add' and len(sys.argv) >= 4:
        add(sys.argv[2], sys.argv[3])
    elif command == 'remove' and len(sys.argv) >= 3:
        remove(sys.argv[2])
    elif command == 'list':
        list_whitelist()
    elif command == 'get':
        whitelist = get_set()
        print(json.dumps(list(whitelist)))
    else:
        print("Usage: whitelist-manager.py <add|remove|list|get> [args]")
        sys.exit(1)
