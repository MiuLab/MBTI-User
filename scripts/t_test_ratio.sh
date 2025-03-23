#!/bin/bash

# Ensure the script exits on error
set -e


# Run the Python script with the provided arguments
python ../eval/t_test_ratio.py --model_eval1 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_E_u_t75.json --model_eval2 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_I_u_t75.json --label E
python ../eval/t_test_ratio.py --model_eval1 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_S_u_t75.json --model_eval2 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_N_u_t75.json --label S
python ../eval/t_test_ratio.py --model_eval1 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_T_u_t75.json --model_eval2 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_F_u_t75.json --label T
python ../eval/t_test_ratio.py --model_eval1 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_P_u_t75.json --model_eval2 ../eval/eval_output/salesagent_neg_wo_dup_chitchat_e10/eval_J_u_t75.json --label P

# Print success message
echo "T-test analysis completed successfully."
