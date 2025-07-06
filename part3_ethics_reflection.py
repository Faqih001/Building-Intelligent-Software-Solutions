# Part 3: Ethical Reflection

# Prompt: Your predictive model from Task 3 is deployed in a company. Discuss:
# - Potential biases in the dataset (e.g., underrepresented teams).
# - How fairness tools like IBM AI Fairness 360 could address these biases.

reflection = '''
Deploying the predictive model in a company may introduce biases if the dataset underrepresents certain teams or issue types, leading to unfair prioritization. For example, if historical data contains more examples from one team, the model may favor their issues. Tools like IBM AI Fairness 360 can help detect and mitigate such biases by evaluating model outcomes across different groups and applying fairness metrics or reweighting techniques. This ensures that predictions are equitable and do not disadvantage any particular group, promoting fairness and trust in AI-driven decision-making.
'''

if __name__ == "__main__":
    print(reflection)
