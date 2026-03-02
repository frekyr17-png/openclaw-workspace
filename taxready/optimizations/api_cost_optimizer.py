#!/usr/bin/env python3
"""
API Cost Optimizer for TaxReady
Daily script to monitor and optimize API usage
"""

import json
import os
from datetime import datetime

LOGS_DIR = "/root/.openclaw/workspace/taxready/logs"
OPTIMIZATIONS_DIR = "/root/.openclaw/workspace/taxready/optimizations"

def ensure_dirs():
    os.makedirs(LOGS_DIR, exist_ok=True)
    os.makedirs(OPTIMIZATIONS_DIR, exist_ok=True)

def log_audit():
    """Audit current API usage in TaxReady"""
    timestamp = datetime.now().isoformat()
    
    # Read current state
    audit = {
        "timestamp": timestamp,
        "check_type": "daily_audit",
        "findings": []
    }
    
    # Check if backend exists and analyze it
    backend_path = "/root/.openclaw/workspace/taxready/backend"
    if os.path.exists(backend_path):
        main_file = os.path.join(backend_path, "main.py")
        if os.path.exists(main_file):
            with open(main_file, 'r') as f:
                content = f.read()
            
            findings = []
            
            # Check for external API calls
            if "requests.get" in content or "requests.post" in content:
                findings.append("External API calls detected in main.py - consider caching")
            
            # Check if Ollama is used (it should be for local AI)
            if "ollama" not in content.lower():
                findings.append("Ollama not integrated - high priority to add for document extraction")
            
            # Check for caching
            if "cache" not in content.lower():
                findings.append("No caching mechanism detected - should add response caching")
            
            audit["findings"] = findings
    
    # Log to audit file
    audit_file = os.path.join(LOGS_DIR, "api-audit.jsonl")
    with open(audit_file, 'a') as f:
        f.write(json.dumps(audit) + "\n")
    
    return audit

def create_cost_tracker():
    """Initialize cost tracking"""
    tracker_file = os.path.join(LOGS_DIR, "api-cost-tracker.json")
    
    tracker = {
        "created": datetime.now().isoformat(),
        "daily_stats": [],
        "optimization_suggestions": [
            "Replace regex extraction with Ollama local model",
            "Add @lru_cache to expensive functions",
            "Implement document type cache (same type = same parsing)",
            "Batch similar document processing jobs",
            "Add API call middleware to track every external request"
        ],
        "current_cost_estimate_usd": 0.0,
        "potential_savings_usd": 0.0
    }
    
    with open(tracker_file, 'w') as f:
        json.dump(tracker, f, indent=2)
    
    print(f"Cost tracker created at {tracker_file}")
    return tracker

def create_ollama_integration():
    """Create Ollama integration module for TaxReady"""
    
    ollama_code = '''"""
Ollama AI Integration for TaxReady
Replaces cloud API calls with local Ollama models
"""

import requests
import json
from typing import Dict, Any

OLLAMA_HOST = "http://localhost:11434"

def extract_with_ollama(text: str, doc_type: str) -> Dict[str, Any]:
    """
    Use local Ollama model for intelligent document extraction
    Much cheaper than cloud APIs (free after setup)
    """
    
    prompts = {
        "form16": """You are a tax document parser. Extract these fields from Form 16:
- Employer name
- Employee PAN
- Gross salary
- TDS deducted
- Section 80C deductions
- Section 80D deductions
- Any other deductions

Return ONLY valid JSON format:
{
  "employer_name": "...",
  "pan": "...",
  "gross_salary": number,
  "tds_deducted": number,
  "deductions_80c": number,
  "deductions_80d": number,
  "other_deductions": number
}

Document text:
{text}""",
        
        "bank_statement": """Extract bank interest income from this statement.
Return JSON with:
{
  "total_interest": number,
  "tcs_collected": number
}

Document:
{text}""",
        
        "mf_statement": """Extract mutual fund details:
- Total investment
- Current value
- Realized gains (STCG/LTCG)
- Unrealized gains

Return JSON format.

Document:
{text}"""
    }
    
    prompt = prompts.get(doc_type, prompts["form16"]).format(text=text[:4000])
    
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": "qwen2.5",
                "prompt": prompt,
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        result = response.json()
        
        # Parse the response text as JSON
        try:
            extracted = json.loads(result.get("response", "{}"))
            return extracted
        except json.JSONDecodeError:
            # If not valid JSON, return raw text
            return {"raw_response": result.get("response", ""), "parsed": False}
            
    except Exception as e:
        return {"error": str(e), "parsed": False}


def check_ollama_available() -> bool:
    """Check if Ollama is running locally"""
    try:
        response = requests.get(f"{OLLAMA_HOST}/api/tags", timeout=5)
        return response.status_code == 200
    except:
        return False
'''
    
    backend_path = "/root/.openclaw/workspace/taxready/backend"
    ollama_file = os.path.join(backend_path, "ollama_integration.py")
    
    with open(ollama_file, 'w') as f:
        f.write(ollama_code)
    
    print(f"Ollama integration created at {ollama_file}")
    return ollama_file

def create_cache_module():
    """Create caching module for TaxReady"""
    
    cache_code = '''"""
Caching layer for TaxReady API calls
Prevents redundant expensive operations
"""

import hashlib
import json
import os
from functools import lru_cache
from typing import Optional, Any

CACHE_DIR = "/root/.openclaw/workspace/taxready/data/cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_key(*args, **kwargs) -> str:
    """Generate cache key from function arguments"""
    key_data = json.dumps({"args": args, "kwargs": kwargs}, sort_keys=True)
    return hashlib.md5(key_data.encode()).hexdigest()

def cache_result(ttl_hours: int = 24):
    """Decorator to cache function results to file"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            cache_key = f"{func.__name__}_{get_cache_key(*args, **kwargs)}"
            cache_file = os.path.join(CACHE_DIR, f"{cache_key}.json")
            
            # Check if cache exists and is valid
            if os.path.exists(cache_file):
                import time
                file_age = time.time() - os.path.getmtime(cache_file)
                if file_age < (ttl_hours * 3600):
                    with open(cache_file, 'r') as f:
                        cached = json.load(f)
                        print(f"[CACHE HIT] {func.__name__}")
                        return cached["result"]
            
            # Call function and cache result
            result = func(*args, **kwargs)
            with open(cache_file, 'w') as f:
                json.dump({"result": result, "cached_at": datetime.now().isoformat()}, f)
            
            print(f"[CACHE SET] {func.__name__}")
            return result
        
        return wrapper
    return decorator


# Document type cache - same type = similar parsing
document_cache = {}

def get_document_parser_cache(doc_type: str):
    """Get cached parser hints for document type"""
    return document_cache.get(doc_type, {})

def set_document_parser_cache(doc_type: str, hints: dict):
    """Cache parser hints for document type"""
    document_cache[doc_type] = hints
'''
    
    backend_path = "/root/.openclaw/workspace/taxready/backend"
    cache_file = os.path.join(backend_path, "cache_layer.py")
    
    with open(cache_file, 'w') as f:
        f.write(cache_code)
    
    print(f"Cache module created at {cache_file}")
    return cache_file

def create_middleware():
    """Create API tracking middleware for FastAPI"""
    
    middleware_code = '''"""
API Cost Tracking Middleware for TaxReady
Monitors all external API calls
"""

import json
import os
from datetime import datetime
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

LOGS_DIR = "/root/.openclaw/workspace/taxready/logs"
os.makedirs(LOGS_DIR, exist_ok=True)

class APICostMiddleware(BaseHTTPMiddleware):
    """Track all API calls and costs"""
    
    async def dispatch(self, request: Request, call_next):
        import time
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        
        # Log the request
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "method": request.method,
            "path": request.url.path,
            "duration_ms": round(duration * 1000, 2),
            "status": response.status_code
        }
        
        # Append to daily log
        log_file = os.path.join(LOGS_DIR, f"api-requests-{datetime.now().strftime('%Y-%m-%d')}.jsonl")
        with open(log_file, 'a') as f:
            f.write(json.dumps(log_entry) + "\\n")
        
        return response


def log_external_api_call(service: str, endpoint: str, tokens_used: int = 0, cost_usd: float = 0.0):
    """Log external API call (OpenAI, etc.)"""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "type": "external_api",
        "service": service,
        "endpoint": endpoint,
        "tokens_used": tokens_used,
        "estimated_cost_usd": cost_usd
    }
    
    log_file = os.path.join(LOGS_DIR, f"api-costs-{datetime.now().strftime('%Y-%m-%d')}.jsonl")
    with open(log_file, 'a') as f:
        f.write(json.dumps(log_entry) + "\\n")
'''
    
    backend_path = "/root/.openclaw/workspace/taxready/backend"
    middleware_file = os.path.join(backend_path, "api_middleware.py")
    
    with open(middleware_file, 'w') as f:
        f.write(middleware_code)
    
    print(f"API tracking middleware created at {middleware_file}")
    return middleware_file

def update_main_py():
    """Update main.py to include optimizations"""
    
    backend_path = "/root/.openclaw/workspace/taxready/backend"
    main_file = os.path.join(backend_path, "main.py")
    
    if not os.path.exists(main_file):
        print("main.py not found, skipping update")
        return False
    
    with open(main_file, 'r') as f:
        content = f.read()
    
    # Check if already updated
    if "APICostMiddleware" in content:
        print("main.py already has optimizations")
        return True
    
    # Add imports at the top
    import_section = '''from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import os
import uuid
import json
from datetime import datetime
import shutil

# API Cost Optimization imports
from api_middleware import APICostMiddleware, log_external_api_call
from cache_layer import cache_result
from ollama_integration import extract_with_ollama, check_ollama_available
'''
    
    # Find where to insert middleware
    content = content.replace(
        'app.add_middleware(\n    CORSMiddleware,',
        'app.add_middleware(APICostMiddleware)\n\napp.add_middleware(\n    CORSMiddleware,'
    )
    
    # Add Ollama check on startup
    startup_check = '''
# Check Ollama availability on startup
ollama_available = check_ollama_available()
if ollama_available:
    print("✓ Ollama is available - will use local AI for extraction")
else:
    print("⚠ Ollama not available - falling back to regex extraction")
'''
    
    # Insert after CORS middleware setup
    content = content.replace(
        'allow_headers=["*"],\n)',
        'allow_headers=["*"],\n)\n' + startup_check
    )
    
    with open(main_file, 'w') as f:
        f.write(content)
    
    print(f"Updated {main_file} with optimizations")
    return True

def main():
    print("=" * 60)
    print("TaxReady API Cost Optimizer - Daily Run")
    print("=" * 60)
    print(f"Started: {datetime.now().isoformat()}")
    
    ensure_dirs()
    
    # Run audit
    audit = log_audit()
    print(f"\n📊 Audit Findings: {len(audit['findings'])}")
    for finding in audit['findings']:
        print(f"  - {finding}")
    
    # Create cost tracker if not exists
    tracker_file = os.path.join(LOGS_DIR, "api-cost-tracker.json")
    if not os.path.exists(tracker_file):
        create_cost_tracker()
    else:
        print(f"\n✓ Cost tracker exists")
    
    # Create optimization modules
    print("\n🔧 Creating optimization modules...")
    create_ollama_integration()
    create_cache_module()
    create_middleware()
    
    # Update main.py
    print("\n📝 Updating main.py...")
    update_main_py()
    
    print("\n" + "=" * 60)
    print("✅ API Cost Optimizer run complete")
    print("Next steps:")
    print("1. Restart TaxReady containers to load new modules")
    print("2. Monitor /logs/api-cost-tracker.json for savings")
    print("=" * 60)

if __name__ == "__main__":
    main()
