#!/bin/bash
# Speed test for Ollama models

test_model() {
    local model=$1
    local start=$(date +%s%N)
    
    response=$(curl -s http://127.0.0.1:11434/v1/chat/completions \
        -H "Content-Type: application/json" \
        -d "{\"model\": \"$model\", \"messages\": [{\"role\": \"user\", \"content\": \"Say hi\", \"temperature\": 0.1}], \"max_tokens\": 5}" 2>/dev/null)
    
    local end=$(date +%s%N)
    local elapsed=$(( (end - start) / 1000000 ))  # Convert to ms
    
    if echo "$response" | grep -q '"error"'; then
        echo "$model|ERROR|$elapsed ms|$response"
    else
        echo "$model|OK|$elapsed ms|-"
    fi
}

echo "Testing Ollama models..."
for model in "kimi-k2.5:cloud" "gpt-oss:120b-cloud" "glm-5:cloud" "minimax-m2.5:cloud" "qwen2.5:7b" "mistral:7b" "deepseek-coder:6.7b"; do
    test_model "$model"
done
