#!/usr/bin/env python3
"""
Create task orchestration manifest from GitHub issues.
"""

import json
import os
import sys
from datetime import datetime, timezone

def create_manifest(project, repo, workdir, issues=None):
    """Create orchestration manifest template."""
    
    manifest = {
        "project": project,
        "repo": repo,
        "workdir": workdir,
        "socket": f"{workdir}/orchestrator.sock",
        "created": datetime.now(timezone.utc).isoformat(),
        "model": "copilot-proxy/gpt-5.2-codex",
        "modelTier": "high",
        "phases": []
    }
    
    if issues:
        # Parse issues and create phases
        # For now, create a simple phase template
        phase = {
            "name": "Phase 1: Initial Tasks",
            "tasks": []
        }
        
        for i, issue in enumerate(issues, 1):
            task = {
                "id": f"t{i}",
                "issue": issue.get("number", i),
                "title": issue.get("title", f"Task {i}"),
                "files": issue.get("files", []),
                "dependsOn": [],
                "status": "pending",
                "worktree": None,
                "tmuxSession": None,
                "startedAt": None,
                "lastProgress": None,
                "completedAt": None,
                "prNumber": None
            }
            phase["tasks"].append(task)
        
        manifest["phases"].append(phase)
    
    return manifest

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: create-manifest.py PROJECT OWNER/REPO WORKDIR [issues.json]")
        print("Example: create-manifest.py my-project owner/repo /tmp/orch-123")
        sys.exit(1)
    
    project = sys.argv[1]
    repo = sys.argv[2]
    workdir = sys.argv[3]
    
    issues = None
    if len(sys.argv) > 4:
        with open(sys.argv[4], 'r') as f:
            issues = json.load(f)
    
    manifest = create_manifest(project, repo, workdir, issues)
    
    # Create workdir if it doesn't exist
    os.makedirs(workdir, exist_ok=True)
    
    output_file = f"{workdir}/manifest.json"
    with open(output_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"✅ Manifest created: {output_file}")
    print(f"📝 Project: {project}")
    print(f"📁 Workdir: {workdir}")
    print(f"🔧 Edit manifest to add tasks and dependencies")
