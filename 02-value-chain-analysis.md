# Value chain analysis

Start from where money and time are created or lost, not from where AI is fashionable.

## Primary and support activities (illustrative, consumer goods)

| Activity | Value created | Typical leakage | KPI that shows it | AI lever |
|---|---|---|---|---|
| Inbound and sourcing | Cost of goods | Off-contract spend, price variance | Spend under management, PO compliance | Spend classification, contract-clause retrieval |
| Operations and fulfilment | Service level | Shortages, damage, late delivery | Fill rate, on-time in-full | Exception triage, carrier claim drafting |
| Sales and trade | Revenue | Trade spend without proof of performance | Trade spend ROI | Promotion-deduction matching |
| Order to cash | Cash conversion | Invalid deductions written off, slow disputes | DSO, deduction write-off rate, dispute cycle time | Agentic dispute resolution (see the prototype repo) |
| Service and returns | Retention | Repeat contacts, unresolved complaints | First-contact resolution, repeat-contact rate | Context assembly for agents, root-cause clustering |
| Support: finance, HR, procurement | Control and capacity | Manual reconciliations, slow close | Days to close, cost per transaction | Reconciliation matching, variance explanation |

## Method

1. Quantify leakage per activity from the client's own data before proposing anything.
2. Rank by leakage times addressability, not by technical interest.
3. For the top three, trace the leakage to process steps in `process-families/` and score those steps.

The recurring finding: the largest leakage usually sits in handoffs between functions - where no single team owns the outcome - not inside any one function.
