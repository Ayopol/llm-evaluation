# LLM Evaluation Lab

## Overview

A systematic framework to evaluate how prompt engineering strategies affect Large Language Model (LLM) performance on a sentiment analysis task.

This project focuses on **prompt design, evaluation, and behavioral analysis**, not model training.


---

## Objectives

* Design and iterate on prompts
* Evaluate LLM outputs using quantitative metrics
* Compare prompting strategies
* Build a reproducible evaluation pipeline

---

## Dataset

We use a subset of the Kaggle Sentiment Analysis Dataset:

* 3 classes: negative, neutral, positive
* real-world user-generated text

---

## Project Structure

```
src/            # core logic (LLM calls, evaluation)
prompts/        # prompt templates
data/           # dataset (not versioned)
evaluation/     # results
notebooks/      # analysis
```

---

## Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key
```

---

## Usage

```bash
python app/runner.py
```

---

## Evaluation Metrics

* Accuracy
* F1 Score
* LLM-as-a-judge

---

## Key Learnings

* Prompt design significantly impacts performance
* Few-shot prompting did not systematically improve performance on sentiment classification. While it improved recall for neutral cases, it degraded precision on positive and overall F1-score.
* Adding explicit behavioral constraints in prompts led to systematic bias towards the neutral class, reducing overall classification performance.
* Evaluation is critical for reliable LLM applications

---

## Tech Stack
Python
OpenAI API
Pandas
Scikit-learn
Matplotlib / Seaborn
---

## 👤 Author

Aillot Paul
