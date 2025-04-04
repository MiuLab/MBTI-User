"""
Use FastChat with Hugging Face generation APIs.

Usage:
python3 -m fastchat.serve.huggingface_api --model lmsys/vicuna-7b-v1.5
python3 -m fastchat.serve.huggingface_api --model lmsys/fastchat-t5-3b-v1.0
"""

import argparse

import torch

from fastchat.model import load_model, get_conversation_template, add_model_args


PREFIX = "Dialogue History:"
SUFFIX = "Here is a list of potential intents that might be referred by the user: ['FindAttraction', 'FindRestaurants', 'FindMovie', 'LookUpMusic', 'SearchHotel', 'FindEvents']. Think carefully to determine the potential intent and provide suitable response given the above dialog history. Output Format: \nThought: <thought>\nResponse: <response>"
SYSREM_PROMPT = "<|begin_of_text|> A chat  between a  curious  user  and  an  artificial  intelligence  assistant. USER: <value> ASSISTANT:"


@torch.inference_mode()
def main(args):
    # Load model

    model, tokenizer = load_model(
        args.model_path,
        device=args.device,
        num_gpus=args.num_gpus,
        max_gpu_memory=args.max_gpu_memory,
        load_8bit=args.load_8bit,
        cpu_offloading=args.cpu_offloading,
        revision=args.revision,
        debug=args.debug,
    )

    # Build the prompt with a conversation template
    history = ""
    while True:
        msg = input("User: ")
        if msg == "exit":
            print("End Conversation")
            break
        msg_prompt = PREFIX + history + "User: " + msg + " " + SUFFIX
        msg_prompt = SYSREM_PROMPT.replace("<value>", msg_prompt)
        conv = get_conversation_template(args.model_path)
        # print(conv.name)
        conv.append_message(conv.roles[0], msg_prompt)
        conv.append_message(conv.roles[1], None)
        prompt = conv.get_prompt()
        # print(f"Context: {prompt}")

        # Run inference
        prompt = prompt.split("<|begin_of_text|>")[-1]
        prompt = "<|begin_of_text|> " + prompt
        prompt = prompt.replace("### Assistant:", "")
        inputs = tokenizer([prompt], return_tensors="pt").to(args.device)
        print("Token len", len(inputs["input_ids"][0]))
        output_ids = model.generate(
            **inputs,
            do_sample=True if args.temperature > 1e-5 else False,
            temperature=args.temperature,
            repetition_penalty=args.repetition_penalty,
            max_new_tokens=args.max_new_tokens,
        )

        if model.config.is_encoder_decoder:
            output_ids = output_ids[0]
        else:
            output_ids = output_ids[0][len(inputs["input_ids"][0]) :]
        outputs = tokenizer.decode(
            output_ids, skip_special_tokens=True, spaces_between_special_tokens=False
        )
        thought = outputs.split("Response: ")[0].strip()
        outputs = outputs.split("Response: ")[-1].strip("</s>")
        print(f"{thought}")
        print(f"{conv.roles[1]}: {outputs}")
        history += "User: " + msg + "\n" + "Agent: " + outputs + "\n"


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    add_model_args(parser)
    parser.add_argument("--temperature", type=float, default=0)
    parser.add_argument("--repetition_penalty", type=float, default=1.0)
    parser.add_argument("--max-new-tokens", type=int, default=512)
    parser.add_argument("--debug", action="store_true")
    parser.add_argument(
        "--test_data_path",
        type=str,
        default="./data/final_data_narrative_in_the_end/test.json",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="./data/final_data_narrative_in_the_end/test_output.json",
    )
    # parser.add_argument("--message", type=str, default="Hello! Who are you?")
    args = parser.parse_args()

    # Reset default repetition penalty for T5 models.
    if "t5" in args.model_path and args.repetition_penalty == 1.0:
        args.repetition_penalty = 1.2

    main(args)
