export CUDA_VISIBLE_DEVICES=0,1
python run_conv_localhost.py --output_file  eval/eval_output/1205/E_with_conv_test.json --input_file ./data/8types_10personas_0720/E.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading --user_temperature 0.75
# python run_conv_localhost.py --output_file  I_with_conv_test.json --input_file ./data/8types_10personas_0720/I.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading --user_temperature 0.75
# python run_conv_localhost.py --output_file  E_with_conv_test_agent_user_t75.json --input_file ./data/8types_10personas_0720/E.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading --agent_temperature 0.75 --user_temperature 0.75
# python run_conv_localhost.py --output_file  I_with_conv_test_agent_user_t75.json --input_file ./data/8types_10personas_0720/I.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading --agent_temperature 0.75 --user_temperature 0.75
# python run_conv_localhost.py --output_file  S_with_conv_test.json --input_file ./data/8types_0720/S.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
# python run_conv_localhost.py --output_file  N_with_conv_test.json --input_file ./data/8types_0720/N.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
# python run_conv_localhost.py --output_file  T_with_conv_test.json --input_file ./data/8types_0720/T.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
# python run_conv_localhost.py --output_file  F_with_conv_test.json --input_file ./data/8types_0720/F.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
# python run_conv_localhost.py --output_file  P_with_conv_test.json --input_file ./data/8types_0720/T.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
# python run_conv_localhost.py --output_file  J_with_conv_test.json --input_file ./data/8types_0720/T.json --num-gpus 2 --max-gpu-memory 10GiB --load-8bit --cpu-offloading
