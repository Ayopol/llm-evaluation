# 🧪 LLM Evaluation Lab

## 📌 Overview

This project aims to systematically evaluate Large Language Model (LLM) performance on a sentiment classification task.

Rather than simply using LLMs, this project focuses on:

* prompt engineering (baseline vs few-shot)
* structured evaluation
* prompt comparison (A/B testing)
* LLM-as-a-judge methodology

---

## 🎯 Objectives

* Design and iterate on prompts
* Evaluate LLM outputs using quantitative metrics
* Compare prompting strategies
* Build a reproducible evaluation pipeline

---

## 📊 Dataset

We use a subset of the Kaggle Sentiment Analysis Dataset:

* 3 classes: negative, neutral, positive
* real-world user-generated text

---

## 🏗️ Project Structure

```
app/            # core logic (LLM calls, evaluation)
prompts/        # prompt templates
data/           # dataset (not versioned)
evaluation/     # results
notebooks/      # analysis
```

---

## ⚙️ Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key
```

---

## 🚀 Usage

```bash
python app/runner.py
```

---

## 📈 Evaluation Metrics

* Accuracy
* F1 Score
* LLM-as-a-judge

---

## 🔍 Experiments

| Prompt | Type      | Description       |
| ------ | --------- | ----------------- |
| V1     | Zero-shot | Basic instruction |
| V2     | Few-shot  | Includes examples |

---

## 🧠 Key Learnings

* Prompt design significantly impacts performance
* Few-shot prompting improves consistency
* Evaluation is critical for reliable LLM applications

---

## 🚧 Future Work

* Add more tasks (NER, summarization)
* Improve evaluation robustness
* Add UI dashboard

---

## 👤 Author

Aillot Paul
