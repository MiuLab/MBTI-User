export CUDA_VISIBLE_DEVICES=0

python3 -m vllm.entrypoints.openai.api_server \
        --host="localhost" \
        --port=5050 \
        --model="meta-llama/Llama-2-7b-chat-hf" \
        --dtype="float16" \
        --tensor-parallel-size=1 \
