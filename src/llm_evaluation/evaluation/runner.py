import pandas as pd

from llm_evaluation.llm.llm import call_llm
from llm_evaluation.utils.parser import parse_json_response
from llm_evaluation.evaluation.metrics import evaluate_predictions


df = pd.read_csv("data/dataset.csv")
df = df.sample(50, random_state=42)

def run_experiment(prompt_path, output_path):

    with open(prompt_path, "r") as f:
        prompt_template = f.read()

    results = []

    for index, row in df.iterrows():

        text = row["text"]
        true_label = row["label"]

        prompt = prompt_template.replace("{text}", text)

        response = call_llm(prompt)

        parsed_response = parse_json_response(response)
        if parsed_response is None:
            continue

        predicted_label = parsed_response.get("sentiment")
        confidence = parsed_response.get("confidence")

        results.append({
        "text": text,
        "true_label": true_label,
        "predicted_label": predicted_label,
        "confidence": confidence
            })


    results_df = pd.DataFrame(results)
    metrics = evaluate_predictions(results_df)

    results_df.to_csv(output_path, index=False)

    return results_df, metrics

results_v1, metrics_v1 = run_experiment(
    "prompts/prompt_v1.txt",
    "results_v1.csv"
)

results_v2, metrics_v2 = run_experiment(
    "prompts/prompt_v2.txt",
    "results_v2.csv"
)

print("\nV1 METRICS")
print(metrics_v1)

print("\nV2 METRICS")
print(metrics_v2)
