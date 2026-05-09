import pandas as pd

from llm_evaluation.llm.llm import call_llm


df = pd.read_csv("data/dataset.csv")
df = df.head(5)

with open("prompts/prompt_v1.txt", "r") as f:
    prompt_template = f.read()


for index, row in df.iterrows():

    text = row["text"]

    prompt = prompt_template.replace("{text}", text)

    response = call_llm(prompt)

    print("\nTEXT:")
    print(text)

    print("\nLLM RESPONSE:")
    print(response)

    print("-" * 50)
