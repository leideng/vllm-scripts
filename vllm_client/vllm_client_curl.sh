curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "/docker/models/Qwen3-Next-80B-A3B-Thinking",
        "prompt": "San Francisco is a",
        "max_tokens": 700,
        "temperature": 0
    }'
