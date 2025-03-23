import numpy as np
from scipy.stats import ttest_ind
import pprint
import json 
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_eval1', type=str, default='model_eval.json', help='model eval file')
    parser.add_argument('--model_eval2', type=str, default='model_eval.json', help='model eval file')
    return parser.parse_args()  

def main(args):
    pprint.pprint(args.model_eval1)
    pprint.pprint(args.model_eval2)
    print('##############################################')
    # READ FILE
    with open(args.model_eval1, 'r') as f:
        model_eval1 = json.load(f)
    with open(args.model_eval2, 'r') as f:
        model_eval2 = json.load(f)
    
    model_success1 = []
    model_success2 = []
    for i in range(len(model_eval1)):
        terminate_reason = model_eval1[i]['terminate_reason']
        for i ,reason in enumerate(terminate_reason):
            # if reason is "Success"
            if reason == "Success":
                model_success1.append(1)
            else:
                model_success1.append(0)

    for i in range(len(model_eval2)):
        terminate_reason = model_eval2[i]['terminate_reason']
        for i ,reason in enumerate(terminate_reason):
            # if reason is "Success"
            if reason == "Success":
                model_success2.append(1)
            else:
                model_success2.append(0)

    # persona1 和 persona2 每个对话的结果 (0/1)
    # persona1_results = np.random.choice([0, 1], size=50, p=[0.4, 0.6])  # 60% success
    # persona2_results = np.random.choice([0, 1], size=50, p=[0.5, 0.5])  # 50% success

    print(model_success1)
    print(model_success2)
    print('##############################################')
    pprint.pprint(sum(model_success1))
    pprint.pprint(sum(model_success2)) 
    # 计算 t 检定
    t_stat, p_value = ttest_ind(model_success1, model_success2)
    print(f"T检定结果: t值={t_stat:.3f}, p值={p_value:.3f}")

    # 解读
    if p_value < 0.05:
        print("两组成功率存在显著差异")
    else:
        print("两组成功率无显著差异")

if __name__ == '__main__':
    args = parse_args()
    main(args)