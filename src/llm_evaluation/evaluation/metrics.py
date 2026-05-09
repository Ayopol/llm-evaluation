from sklearn.metrics import accuracy_score, f1_score, classification_report



def evaluate_predictions(results_df):

    y_true = results_df["true_label"]
    y_pred = results_df["predicted_label"]

    accuracy = accuracy_score(y_true, y_pred)

    f1 = f1_score(
        y_true,
        y_pred,
        average="macro"
    )

    report = classification_report(y_true, y_pred, zero_division=0)

    return {
        "accuracy": accuracy,
        "f1_macro": f1,
        "classification_report": report
    }
