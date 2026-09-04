# APEX-Hiring-Framework

Evaluation harness for measuring geographic and credential bias in AI-mediated hiring decisions.

## Status

This repository contains the evaluation harness and a synthetic demo dataset. It supports an
ongoing matched-pair correspondence audit of frontier language models, currently under peer
review at ACM FAccT. The full study dataset and qualitative findings will be released after
publication. What's published here is the infrastructure, not the results.

## What this does

The harness builds qualification-identical candidate profile pairs that differ only in an
attribute that should not affect a hiring decision, such as where a credential was earned,
sends them to one or more frontier models for a hiring judgement, and scores the resulting
decisions for disparity between matched pairs.

Pilot results from the full study (four models, six occupational trades, 5,760 logged
judgements): every standard-run comparison was statistically significant at p < 0.0001, with
false-rejection rates on internationally credentialed candidates ranging from 3.3% to 63.3%
depending on the model.

## Structure

- `harness/task_generator.py` — builds matched-pair candidate profiles, with template
  variation so profiles are not reused verbatim across runs
- `harness/model_runner.py` — queries model APIs asynchronously and collects judgements
- `harness/scorer.py` — computes selection-rate disparities and runs significance tests
- `demo_data/synthetic_sample.csv` — illustrative candidate pairs and judgements, not from
  the real study
- `analysis/run_analysis.py` — runs the scoring pipeline against the demo data end to end

## Running the demo

```
pip install -r requirements.txt
python -m analysis.run_analysis
```

This runs entirely on the synthetic sample and does not require API keys.

## Methodology

See `methodology.md` for the audit design and the failure-taxonomy approach.

## License

MIT. See `LICENSE`.
