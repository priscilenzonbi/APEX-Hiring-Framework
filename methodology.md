# Methodology

## Matched-pair correspondence audit

This project adapts the matched-pair correspondence design long used in labor economics to
detect discrimination in human hiring (e.g. Bertrand & Mullainathan, 2004), applying it to
model-mediated hiring decisions instead of human recruiters.

For each occupational trade, two candidate profiles are constructed that are identical on
every qualification-relevant dimension (years of experience, skills, certifications) and
differ only in a single attribute that should not affect the hiring decision: the country or
institution where a credential was obtained. Both profiles are sent to the same model under
the same prompt conditions, and the resulting decisions are compared.

A disparity between matched pairs that cannot be explained by qualifications is attributed to
the varied attribute. Running this across many pairs and trades produces a selection-rate
gap rather than a single flagged instance, which is what makes the design resistant to
one-off explanations.

## Failure taxonomy

The full study codes model reasoning text into a taxonomy of recurring failure patterns. The specific category names and descriptions are withheld until publication. This repository does not include the qualitative corpus or the taxonomy labels, since that material is part of the manuscript currently under review.

## Contamination resistance

Because this harness is public, candidate profiles are not fixed strings. `task_generator.py`
produces template-based variants (names, phrasing, and non-substantive details) on each run,
so a model cannot simply memorize a fixed benchmark text.
