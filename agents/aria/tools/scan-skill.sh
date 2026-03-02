#!/bin/bash
# Wrapper for security skill scanner

export CLAWDHUB_SKILLS=/root/.openclaw/workspace/skills

python3 /root/.openclaw/workspace/skills/openclaw-skills-security-checker/skill-scanner.py "$@"
