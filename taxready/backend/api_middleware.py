"""
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
            f.write(json.dumps(log_entry) + "\n")
        
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
        f.write(json.dumps(log_entry) + "\n")
