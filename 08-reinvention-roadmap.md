# Reinvention roadmap

Sequence the work so every wave pays for the next and nothing is automated before it is redesigned.

| Wave | Focus | Typical content | Gate to next wave |
|---|---|---|---|
| 0 | Baseline and design | Capability heat map, value chain leakage, step scoring, value case | Finance-agreed baseline and business case |
| 1 | Redesign | Remove non-value steps, fix handoffs and ownership, standardize policies | Process KPIs stable on the new design |
| 2 | Automate | Rules-based automation and RPA for high-volume, low-judgment steps | Straight-through rate and quality at target |
| 3 | Augment | Agents that assemble context and recommend; people decide | Recommendation acceptance and accuracy at target on the reference set |
| 4 | Agentic | Agents act within guardrails; people handle exceptions | Override rate, grounding failures and value realization on track |

## Across towers
Run towers in parallel but offset by one wave, so the platform, governance controls and evaluation sets built in the first tower are reused rather than rebuilt. A typical order: the tower with the clearest leakage and cleanest data first (often O2C cash application or S2P invoice matching), the most regulated or judgment-heavy last.

## What engineering, data and platform teams receive per wave
A build-ready pack: workflow states and exception paths, agent contracts, the grounding corpus and citation rule, guardrail thresholds, the evaluation set, the rollout cohorts, and the KPI each release must move.

## Operating model changes
Every wave changes roles. Plan the new roles (reviewers of agent recommendations, policy-corpus owners, AI product owners) and the training alongside the build, not after it.
