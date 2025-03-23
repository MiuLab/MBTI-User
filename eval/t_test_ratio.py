import json
import os
import argparse
import pprint
from scipy.stats import ttest_ind
import pandas as pd

def main(args):
    pprint.pprint(args.model_eval1)
    pprint.pprint(args.model_eval2)
    print('##############################################')
    with open(args.model_eval1, 'r') as f:
        model_eval1 = json.load(f)
    with open(args.model_eval2, 'r') as f:
        model_eval2 = json.load(f)

    # Functionality 1: Calculate Total Turns for Successful Conversations
    total_turns_for_success = 0
    successful_conversations = 0
    turn_list1 = []

    for persona in model_eval1:
        terminate_reason = persona['terminate_reason']
        num_of_turns = persona['num_turns']

        for i, reason in enumerate(terminate_reason):
            if reason == "Success":
                total_turns_for_success += num_of_turns[i]
                successful_conversations += 1
                turn_list1.append(num_of_turns[i])
            else:
                turn_list1.append(20)
    if successful_conversations > 0:
        print(f"Total Turns for Successful Conversations 1: {total_turns_for_success}")
        print(f"Average Turns for Successful Conversations 1: {total_turns_for_success / successful_conversations}")
    else:
        print("No successful conversations to calculate turns.")
    
     # Functionality 1.1: Calculate Total Turns for Successful Conversations
    total_turns_for_success = 0
    successful_conversations = 0
    turn_list2 = []

    for persona in model_eval2:
        terminate_reason = persona['terminate_reason']
        num_of_turns = persona['num_turns']

        for i, reason in enumerate(terminate_reason):
            if reason == "Success":
                total_turns_for_success += num_of_turns[i]
                successful_conversations += 1
                turn_list2.append(num_of_turns[i])
            else:
                turn_list2.append(20)
    if successful_conversations > 0:
        print(f"Total Turns for Successful Conversations 2: {total_turns_for_success}")
        print(f"Average Turns for Successful Conversations 2: {total_turns_for_success / successful_conversations}")
    else:
        print("No successful conversations to calculate turns.")

    # Functionality 2: Calculate Agent Thought Ratio ("I should continue the topic.")
    thought_keyword = "I should continue the topic."
    total_agent_turns_with_keyword = 0
    total_agent_turns = 0
    conversation_count = 0
    total_conversation_ratios = 0
    ratio_list1 = []

    for persona in model_eval1:
        conversations = persona['conversations']

        for turn_set in conversations.values():
            agent_turns = 0
            agent_turns_with_keyword = 0
            for turn in turn_set:
                if turn['role'] == 'user':
                    agent_turns += 1
                    # the first turn does not have user's thought, so we need to check the second turn
                    if agent_turns > 1:
                        if thought_keyword in turn['thought']:
                            
                            agent_turns_with_keyword += 1
            
            thought_ratio = agent_turns_with_keyword / agent_turns if agent_turns > 0 else 0
            total_conversation_ratios += thought_ratio
            conversation_count += 1
            ratio_list1.append(thought_ratio)

    if conversation_count > 0:
        avg_thought_ratio = total_conversation_ratios / conversation_count
        print(f"Agent Thought Ratio (\"I should continue the topic.\"): {avg_thought_ratio:.2%}")
    else:
        print("No agent turns found to calculate thought ratio.")

    # Functionality 2: Calculate Agent Thought Ratio ("I should continue the topic.")
    thought_keyword = "I should continue the topic."
    total_agent_turns_with_keyword = 0
    total_agent_turns = 0
    conversation_count = 0
    total_conversation_ratios = 0
    ratio_list2 = []

    for persona in model_eval2:
        conversations = persona['conversations']

        for turn_set in conversations.values():
            agent_turns = 0
            agent_turns_with_keyword = 0
            for turn in turn_set:
                if turn['role'] == 'user':
                    agent_turns += 1
                    # the first turn does not have user's thought, so we need to check the second turn
                    if agent_turns > 1:
                        if thought_keyword in turn['thought']:
                            
                            agent_turns_with_keyword += 1
            
            thought_ratio = agent_turns_with_keyword / agent_turns if agent_turns > 0 else 0
            total_conversation_ratios += thought_ratio
            conversation_count += 1
            ratio_list2.append(thought_ratio)

    if conversation_count > 0:
        avg_thought_ratio = total_conversation_ratios / conversation_count
        print(f"Agent Thought Ratio (\"I should continue the topic.\"): {avg_thought_ratio:.2%}")
    else:
        print("No agent turns found to calculate thought ratio.")
    
    

    print('##############################################')

    significance_level = 0.05
    t_test_results = []
    # # Functionality 3: Calculate T-Test for Total Turns for Successful Conversations
    # t_stat, p_value = ttest_ind(turn_list1, turn_list2, equal_var=False)
    # significance = "Significant" if p_value < significance_level else "Not Significant"
    # t_test_results.append({
    #         "test": "Turns for Conversations",
    #         "T-Statistic": t_stat,
    #         "P-Value": p_value,
    #         "Significance": significance
    # })

    # t_stat2, p_value2 = ttest_ind(ratio_list1, ratio_list2, equal_var=False)
    # significance2 = "Significant" if p_value2 < significance_level else "Not Significant"
    # t_test_results.append({
    #         "test": "Agent Thought Ratio",
    #         "T-Statistic": t_stat2,
    #         "P-Value": p_value2,
    #         "Significance": significance2
    # })

    # # Convert results to DataFrame and display
    # df_results = pd.DataFrame(t_test_results)

    # # Show the results
    # print(df_results)

    # Functionality 3: One-Sided T-Test for Total Turns for Successful Conversations
    t_stat_greater, p_value_greater = ttest_ind(turn_list1, turn_list2, alternative='greater', equal_var=False)
    significance_greater = "Significant" if p_value_greater < significance_level else "Not Significant"

    t_stat_less, p_value_less = ttest_ind(turn_list1, turn_list2, alternative='less', equal_var=False)
    significance_less = "Significant" if p_value_less < significance_level else "Not Significant"

    t_test_results = [
        {
            "Test": "Turns for Conversations",
            "T-Statistic": t_stat_greater,
            "P-Value": p_value_greater,
            "Significance": significance_greater,
            "Direction": "Model 1 > Model 2"
        },
        {
            "Test": "Turns for Conversations",
            "T-Statistic": t_stat_less,
            "P-Value": p_value_less,
            "Significance": significance_less,
            "Direction": "Model 1 < Model 2"
        }
    ]

    # Print results
    print(f"Test: Turns for Conversations")
    print(f"T-Statistic: {t_stat_greater:.4f}, P-Value (Model 1 > Model 2): {p_value_greater:.4f}")
    print(f"Conclusion: Model 1 > Model 2 is {significance_greater} at the {significance_level*100}% significance level.\n")

    print(f"T-Statistic: {t_stat_less:.4f}, P-Value (Model 1 < Model 2): {p_value_less:.4f}")
    print(f"Conclusion: Model 1 < Model 2 is {significance_less} at the {significance_level*100}% significance level.\n")

    # Functionality 3: One-Sided T-Test for Agent Thought Ratio
    t_stat_greater2, p_value_greater2 = ttest_ind(ratio_list1, ratio_list2, alternative='greater', equal_var=False)
    significance_greater2 = "Significant" if p_value_greater2 < significance_level else "Not Significant"

    t_stat_less2, p_value_less2 = ttest_ind(ratio_list1, ratio_list2, alternative='less', equal_var=False)
    significance_less2 = "Significant" if p_value_less2 < significance_level else "Not Significant"

    t_test_results.extend([
        {
            "Test": "Agent Thought Ratio",
            "T-Statistic": t_stat_greater2,
            "P-Value": p_value_greater2,
            "Significance": significance_greater2,
            "Direction": "Model 1 > Model 2"
        },
        {
            "Test": "Agent Thought Ratio",
            "T-Statistic": t_stat_less2,
            "P-Value": p_value_less2,
            "Significance": significance_less2,
            "Direction": "Model 1 < Model 2"
        }
    ])

    # Print results
    print(f"Test: Agent Thought Ratio")
    print(f"T-Statistic: {t_stat_greater2:.4f}, P-Value (Model 1 > Model 2): {p_value_greater2:.4f}")
    print(f"Conclusion: Model 1 > Model 2 is {significance_greater2} at the {significance_level*100}% significance level.\n")

    print(f"T-Statistic: {t_stat_less2:.4f}, P-Value (Model 1 < Model 2): {p_value_less2:.4f}")
    print(f"Conclusion: Model 1 < Model 2 is {significance_less2} at the {significance_level*100}% significance level.\n")

    # Convert results to DataFrame
    df_results = pd.DataFrame(t_test_results)

    # Save results to an Excel file
    output_file = args.label+".xlsx"
    df_results.to_excel(output_file, index=False)



def args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_eval1', type=str, default='../eval/persona_with_conv_with_eval.json')
    parser.add_argument('--model_eval2', type=str, default='../eval/persona_with_conv_with_eval.json')

    parser.add_argument('--baseline_eval', type=str, default='../eval/persona_with_conv_salesbot1_baseline_with_eval.json')
    parser.add_argument('--label', type=str, default='E')

    parser.add_argument('--llama_baseline_eval', type=str, default='../eval/persona_with_conv_llama_baseline_proceed_with_eval.json')
    args = parser.parse_args()
    return args
if __name__ == '__main__':
    args = args_parser()
    main(args)
