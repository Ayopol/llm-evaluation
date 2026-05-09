import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns

def plot_global_metrics(metrics_dict):

    models = list(metrics_dict.keys())
    accuracy = [metrics_dict[m]["accuracy"] for m in models]
    f1 = [metrics_dict[m]["f1_macro"] for m in models]

    plt.figure()

    plt.plot(models, accuracy, marker="o", label="Accuracy")
    plt.plot(models, f1, marker="o", label="F1 Macro")

    plt.title("LLM Prompt Performance Comparison")
    plt.xlabel("Model / Prompt version")
    plt.ylabel("Score")
    plt.legend()

    plt.show()


def plot_label_distribution(results_dict):

    for model_name, df in results_dict.items():

        plt.figure()

        df["predicted_label"].value_counts().plot(kind="bar")

        plt.title(f"Predicted labels distribution - {model_name}")
        plt.show()


def plot_confusion_matrix(df, title):

    cm = confusion_matrix(df["true_label"], df["predicted_label"])

    plt.figure()

    sns.heatmap(cm, annot=True, fmt="d")

    plt.title(title)
    plt.xlabel("Predicted")
    plt.ylabel("True")

    plt.show()
