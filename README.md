# 🔬 Can You Regulate This AI?

**An interactive challenge for policymakers to discover how AI systems can be accurate and discriminatory at the same time.**

Built as a prototype for the [Stanford SAFE](https://saige.stanford.edu) project:
*"Designing Interactive Modules to Introduce High-Ranking Decision Makers to Technical AI Fundamentals"*

## The scenario

A government agency wants to deploy AI to screen job applications for civil service positions. The vendor says it's 92% accurate. You're the regulator — should it be deployed?

## Three rounds

1. **You vs. the AI** — Review candidates and decide: interview or pass? Compare your judgment to the AI's, then examine its mistakes.
2. **Spot the flaw** — Two nearly identical candidates got opposite decisions. Find what tiny detail caused the flip. Discover that age alone can reverse the AI's decision.
3. **Find the bias** — Adjust a candidate's CV with sliders and uncover what the AI really cares about — including factors the job description says should not matter.

## Key concepts demonstrated

- **Accuracy ≠ fairness**: A system can be 92% accurate and still discriminate
- **Inherited bias**: AI trained on historical data reproduces historical discrimination at scale
- **Robustness failures**: Tiny, meaningless changes (1 year of age, 1 language) flip life-altering decisions
- **Why testing must go beyond accuracy**: Bias auditing, robustness testing, and explainability requirements

## The hidden model

The AI has a logistic regression with intentional biases:
- **Over-penalizes age** (learned from historical data where older candidates were hired less)
- **Over-weights languages** (treats a 3rd language as essential when the job only requires 2)
- **Under-values experience** relative to formal education

The ground truth uses fair rules matching the job description: bachelor's + 3 years, or master's + 2 years, with age having zero weight.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Cloud

1. Push this repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Point it at `app.py`
4. Deploy (takes ~2 minutes)

## Tech stack

- **Streamlit** — Interactive web framework
- **NumPy** — Model computations

## License

MIT
