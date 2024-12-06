export CUDA_VISIBLE_DEVICES=2,3

python3 -m vllm.entrypoints.openai.api_server \
        --host="140.112.29.236" \
        --port=5050 \
        --model="meta-llama/Llama-2-7b-chat-hf" \
        --dtype="float16" \
        --tensor-parallel-size=2 \
