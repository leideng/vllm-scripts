import gc
import torch

# Set environment variables for KVComp before importing vllm
import os
os.environ["VLLM_ASCEND_ENABLE_KVCOMP_SPARSE"] = "1"
os.environ["VLLM_ASCEND_KVCOMP_CONFIG_PATH"] = "/docker/ldeng/kvcomp/vllm-ascend/vllm_ascend/worker/kvcomp_configs/vllm_ascend/worker/kvcomp_configs/vllm_ascend/worker/kvcomp_configs/KVComp_Qwen3_32B_config.json"
os.environ["VLLM_DISABLE_COMPILE_CACHE"] = "1"


from vllm import LLM, SamplingParams
from vllm.distributed.parallel_state import (destroy_distributed_environment,
                                             destroy_model_parallel)



def clean_up():
    destroy_model_parallel()
    destroy_distributed_environment()
    gc.collect()
    torch.npu.empty_cache()

print(f"VLLM_ASCEND_ENABLE_KVCOMP_SPARSE: {os.getenv('VLLM_ASCEND_ENABLE_KVCOMP_SPARSE', '0')}")
print(f"VLLM_ASCEND_KVCOMP_CONFIG_PATH: {os.getenv('VLLM_ASCEND_KVCOMP_CONFIG_PATH')}")
print(f"VLLM_DISABLE_COMPILE_CACHE: {os.getenv('VLLM_DISABLE_COMPILE_CACHE')}")

prompts = [
    "Hello, my name is",
    "The future of AI is",
]
sampling_params = SamplingParams(temperature=0.6, top_p=0.95, top_k=40)
llm = LLM(model="/docker/models/Qwen3-32B",
          tensor_parallel_size=8,
          trust_remote_code=True,
          distributed_executor_backend="mp",
          max_model_len=5500,
          max_num_batched_tokens=5500,
          enforce_eager=True,
          compilation_config={"cudagraph_mode": "FULL_DECODE_ONLY"})

outputs = llm.generate(prompts, sampling_params)
for output in outputs:
    prompt = output.prompt
    generated_text = output.outputs[0].text
    print(f"Prompt: {prompt!r}, Generated text: {generated_text!r}")

del llm
clean_up()
