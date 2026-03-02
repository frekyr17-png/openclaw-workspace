#!/usr/bin/env python3
"""
Security Skill Scanner for ClawdHub Skills
Scans installed skills for suspicious patterns.
"""

import os
import json
import re
import argparse
from pathlib import Path
from datetime import datetime

SKILLS_DIR = os.environ.get('CLAWDHUB_SKILLS', '/home/linuxbrew/.linuxbrew/lib/node_modules/clawdbot/skills')
OUTPUT_DIR = '/tmp/security-scanner'
SKILL_PATH = os.path.dirname(os.path.abspath(__file__))

# Load whitelist from skill data
def load_whitelist():
    whitelist_file = Path(f'{SKILL_PATH}/data/whitelist.json')
    if whitelist_file.exists():
        with open(whitelist_file, 'r') as f:
            data = json.load(f)
            return set(data.keys())
    return set()

WHITELISTED_SKILLS = load_whitelist()

# Security patterns to detect
SUSPICIOUS_PATTERNS = {
    'credential_theft': [
        (r'\.env', 'Access to .env file'),
        (r'webhook\.site', 'External webhook'),
        (r'curl.*http', 'HTTP curl request'),
        (r'POST.*json', 'JSON POST request'),
        (r'read.*api.*key', 'API key access'),
        (r'steal|exfil|secret', 'Secret exfiltration keywords'),
        (r'ship.*credential', 'Credential shipping'),
    ],
    'command_injection': [
        (r'os\.system', 'System command execution'),
        (r'eval\(', 'Eval execution'),
        (r'shell=True', 'Shell execution enabled'),
        (r'subprocess', 'Subprocess spawning'),
        (r'\|\s*\$', 'Pipe to shell variable'),
    ],
    'network_exfil': [
        (r'requests\.(post|get)', 'HTTP requests library'),
        (r'Authorization.*Bearer', 'Bearer token header'),
        (r'header.*secret', 'Secret in headers'),
        (r'httpx\.Client', 'HTTPX client'),
    ],
    'suspicious_downloads': [
        (r'wget|curl.*-O', 'Download utility'),
        (r'remote.*script', 'Remote script execution'),
    ],
    'filesystem_access': [
        (r'open\(.*w', 'File write access'),
        (r'writefile', 'File writing'),
        (r'readfile', 'File reading'),
    ]
}

class RegexScanner:
    def __init__(self):
        self.findings = []
        self.stats = {'scanned': 0, 'threats': 0, 'warnings': 0}
    
    def scan_file(self, file_path: str) -> dict:
        """Scan a single file for suspicious patterns."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
        except Exception as e:
            return {'error': str(e)}
        
        results = {'file': file_path, 'threats': [], 'warnings': []}
        
        for category, patterns in SUSPICIOUS_PATTERNS.items():
            for pattern, description in patterns:
                matches = re.findall(pattern, content, re.IGNORECASE)
                if matches:
                    if category == 'credential_theft':
                        results['threats'].append({
                            'category': category,
                            'description': description,
                            'matches': len(matches)
                        })
                    else:
                        results['warnings'].append({
                            'category': category,
                            'description': description,
                            'matches': len(matches)
                        })
        
        return results
    
    def scan_skill(self, skill_path: str) -> dict:
        """Scan entire skill directory."""
        skill_name = Path(skill_path).name
        
        # Check whitelist first
        if skill_name in WHITELISTED_SKILLS:
            return {
                'skill': skill_name,
                'path': skill_path,
                'status': 'whitelisted',
                'note': 'Known legitimate skill - API integrations expected'
            }
        
        all_results = {
            'skill': skill_name,
            'path': skill_path,
            'threats': [],
            'warnings': [],
            'files_scanned': 0
        }
        
        for ext in ['*.md', '*.py', '*.js', '*.json']:
            for file_path in Path(skill_path).glob(ext):
                all_results['files_scanned'] += 1
                result = self.scan_file(str(file_path))
                if 'threats' in result:
                    all_results['threats'].extend(result['threats'])
                if 'warnings' in result:
                    all_results['warnings'].extend(result['warnings'])
        
        return all_results
    
    def scan_specific(self, skill_name: str) -> dict:
        """Scan a specific skill by name."""
        skill_path = Path(SKILLS_DIR) / skill_name
        if not skill_path.exists():
            return {'error': f'Skill not found: {skill_name}'}
        return self.scan_skill(str(skill_path))
    
    def scan_all_skills(self):
        """Scan all installed skills."""
        results = {
            'timestamp': datetime.now().isoformat(),
            'skills_scanned': 0,
            'threats_found': 0,
            'warnings_found': 0,
            'findings': [],
            'clean_skills': [],
            'whitelisted_skills': [],
            'unknown_skills': []
        }
        
        if not Path(SKILLS_DIR).exists():
            print(f"⚠️ Skills directory not found: {SKILLS_DIR}")
            return results
        
        for skill_path in sorted(Path(SKILLS_DIR).iterdir()):
            if skill_path.is_dir():
                results['skills_scanned'] += 1
                skill_result = self.scan_skill(str(skill_path))
                
                status = skill_result.get('status', 'unknown')
                
                if status == 'whitelisted':
                    results['whitelisted_skills'].append(skill_result['skill'])
                elif skill_result.get('threats') or skill_result.get('warnings'):
                    results['threats_found'] += len(skill_result.get('threats', []))
                    results['warnings_found'] += len(skill_result.get('warnings', []))
                    results['unknown_skills'].append(skill_result)
                else:
                    results['clean_skills'].append(skill_result['skill'])
        
        return results
    
    def generate_report(self, results: dict) -> str:
        """Generate markdown report."""
        report = f"""# Skill Security Scan Report
Generated: {results['timestamp']}

## Summary
- **Skills Scanned**: {results['skills_scanned']}
- **Threats Found**: {results['threats_found']}
- **Warnings Found**: {results['warnings_found']}
- **Clean Skills**: {len(results['clean_skills'])}
- **Whitelisted (Legitimate)**: {len(results['whitelisted_skills'])}
- **Unknown (Needs Review)**: {len(results['unknown_skills'])}

## 🟢 Whitelisted Skills (Known Legitimate)
These skills have API integrations that are expected and verified:
"""
        for skill in sorted(results['whitelisted_skills']):
            report += f"- {skill}\n"
        
        report += f"""
## ✅ Clean Skills (No Suspicious Patterns)
"""
        for skill in results['clean_skills'][:25]:
            report += f"- {skill}\n"
        
        if len(results['clean_skills']) > 25:
            report += f"\n... and {len(results['clean_skills']) - 25} more\n"
        
        report += "\n## ⚠️ Unknown Skills (Needs Manual Review)\n"
        if results['unknown_skills']:
            report += "These skills have patterns that warrant investigation:\n\n"
            for skill_result in results['unknown_skills']:
                report += f"### {skill_result['skill']}\n"
                report += f"- Files scanned: {skill_result.get('files_scanned', 'N/A')}\n"
                
                if skill_result.get('threats'):
                    report += "\n🔴 **POTENTIAL THREATS**:\n"
                    for t in skill_result['threats']:
                        report += f"  - `{t['category']}`: {t['description']} ({t['matches']} matches)\n"
                
                if skill_result.get('warnings'):
                    report += "\n🟡 **WARNINGS**:\n"
                    for w in skill_result['warnings']:
                        report += f"  - `{w['category']}`: {w['description']} ({w['matches']} matches)\n"
        else:
            report += "No unknown skills detected. ✅\n"
        
        return report

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Security Skill Scanner')
    parser.add_argument('--skill', '-s', help='Scan specific skill by name')
    parser.add_argument('--output', '-o', default=OUTPUT_DIR, help='Output directory')
    args = parser.parse_args()
    
    os.makedirs(args.output, exist_ok=True)
    
    scanner = RegexScanner()
    
    if args.skill:
        log(f"Scanning skill: {args.skill}")
        result = scanner.scan_specific(args.skill)
        print(json.dumps(result, indent=2))
    else:
        log("Starting skill security scan...")
        results = scanner.scan_all_skills()
        
        # Save JSON
        json_path = f'{args.output}/scan-results.json'
        with open(json_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        # Save markdown report
        md_path = f'{args.output}/scan-report.md'
        with open(md_path, 'w') as f:
            f.write(scanner.generate_report(results))
        
        log(f"✅ Scanned {results['skills_scanned']} skills")
        log(f"⚠️ Found {results['threats_found']} threats, {results['warnings_found']} warnings")
        log(f"📄 Report: {md_path}")
