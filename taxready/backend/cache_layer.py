"""
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
