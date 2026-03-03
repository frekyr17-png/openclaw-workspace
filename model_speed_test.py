#!/usr/bin/env python3
"""Test AI model response speeds for OpenClaw compatibility"""
import requests
import time
import json

# Test prompt - simple and consistent
TEST_PROMPT = "What is 2+2? Answer with just the number."

# Models to test
MODELS = {
    # Ollama local/cloud models
    "ollama/kimi-k2.5:cloud": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/gpt-oss:120b-cloud": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/glm-5:cloud": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/minimax-m2.5:cloud": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/qwen2.5:7b": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/mistral:7b": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
    "ollama/deepseek-coder:6.7b": {"type": "ollama", "url": "http://127.0.0.1:11434/v1/chat/completions"},
}

def test_model(model_key, config):
    """Test a single model and return timing results"""
    model_name = model_key.split("/")[-1]
    
    payload = {
        "model": model_name,
        "messages": [{"role": "user", "content": TEST_PROMPT}],
        "max_tokens": 10,
        "temperature": 0.1
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        start = time.perf_counter()
        response = requests.post(
            config["url"], 
            json=payload, 
            headers=headers, 
            timeout=30
        )
        elapsed = (time.perf_counter() - start) * 1000  # Convert to ms
        
        if response.status_code == 200:
            data = response.json()
            content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
            return {
                "model": model_key,
                "speed_ms": round(elapsed, 2),
                "status": "OK",
                "response": content.strip()[:50],
                "error": None
            }
        else:
            return {
                "model": model_key,
                "speed_ms": None,
                "status": f"HTTP {response.status_code}",
                "response": None,
                "error": response.text[:200]
            }
    except Exception as e:
        return {
            "model": model_key,
            "speed_ms": None,
            "status": "ERROR",
            "response": None,
            "error": str(e)[:200]
        }

# Run tests
results = []
for model_key, config in MODELS.items():
    print(f"Testing {model_key}...", flush=True)
    result = test_model(model_key, config)
    results.append(result)
    print(f"  Result: {result['status']}, Speed: {result['speed_ms']}ms")

# Output JSON for parsing
print("\n" + "="*50)
print("RESULTS_JSON_START")
print(json.dumps(results, indent=2))
print("RESULTS_JSON_END")