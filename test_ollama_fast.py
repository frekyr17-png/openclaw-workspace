#!/usr/bin/env python3
import requests
import time

models_to_test = [
    "kimi-k2.5:cloud",
    "minimax-m2.5:cloud",
    "gpt-oss:120b-cloud",
    "qwen2.5:7b"
]

for model in models_to_test:
    try:
        start = time.time()
        resp = requests.post(
            "http://127.0.0.1:11434/v1/chat/completions",
            json={
                "model": model,
                "messages": [{"role": "user", "content": "hi"}],
                "max_tokens": 5,
                "stream": False
            },
            timeout=10
        )
        elapsed = time.time() - start
        if resp.status_code == 200:
            content = resp.json()['choices'][0]['message']['content']
            print(f"✅ {model:25} | {elapsed:.2f}s | {content}")
        else:
            print(f"❌ {model:25} | Status {resp.status_code}")
    except requests.exceptions.Timeout:
        print(f"⏱️  {model:25} | TIMEOUT (>10s)")
    except Exception as e:
        print(f"❌ {model:25} | {str(e)[:40]}")
