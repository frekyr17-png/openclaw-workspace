#!/usr/bin/env python3
import requests
import json

# Test 1: API endpoint
try:
    resp = requests.get("http://127.0.0.1:11434/v1/models", timeout=5)
    print("✅ Ollama API responsive")
    print(f"   Models: {len(resp.json()['data'])} available")
except Exception as e:
    print(f"❌ API Error: {e}")

# Test 2: OpenClaw config
with open("openclaw.json") as f:
    config = json.load(f)
    ollama_baseurl = config["models"]["providers"]["ollama"]["baseUrl"]
    print(f"\n✅ OpenClaw config baseUrl: {ollama_baseurl}")
    
    # Test actual request
    try:
        resp = requests.get(f"{ollama_baseurl}/models", timeout=5)
        print(f"✅ OpenClaw can reach Ollama at {ollama_baseurl}")
    except Exception as e:
        print(f"❌ OpenClaw connection failed: {e}")

# Test 3: Try a quick completion
try:
    resp = requests.post(
        "http://127.0.0.1:11434/v1/chat/completions",
        json={
            "model": "qwen2.5:7b",
            "messages": [{"role": "user", "content": "test"}],
            "max_tokens": 10,
            "stream": False
        },
        timeout=30
    )
    if resp.status_code == 200:
        print(f"✅ Model completion works: {resp.json()['choices'][0]['message']['content'][:50]}")
    else:
        print(f"❌ Completion error: {resp.status_code}")
except Exception as e:
    print(f"❌ Completion failed: {e}")
