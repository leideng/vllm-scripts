#!/usr/bin/env bash
# vLLM online serving for Qwen3-32B with full attention (no KVComp).

set -e

# Full attention: do not enable KVComp sparse attention
export VLLM_ASCEND_ENABLE_KVCOMP_SPARSE=0
export VLLM_DISABLE_COMPILE_CACHE=1

MODEL_PATH="/docker/models/Qwen3-32B"
HOST=0.0.0.0
PORT=8000


# Compile config https://docs.vllm.ai/en/latest/api/vllm/config/compilation/
# "cudagraph_mode": "PIECEWISE", "FULL_DECODE_ONLY", "FULL_AND_PIECEWISE", "FULL", "NONE"


exec vllm serve "${MODEL_PATH}" \
  --tensor-parallel-size 8 \
  --trust-remote-code \
  --distributed-executor-backend mp \
  --max-model-len 5500 \
  --max-num-batched-tokens 5500 \
  --enforce-eager \
  --host 0.0.0.0 \
  --port 8000 \
  --compilation-config '{"cudagraph_mode": "PIECEWISE"}' \
  --gpu-memory-utilization 0.8 
