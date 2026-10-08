# Agentic solution design canvas

Fill one canvas per workflow before any build. If a box cannot be filled, the design is not ready.

| Box | Question | Example (O2C deductions) |
|---|---|---|
| Outcome and KPI | What number moves, from what baseline? | Dispute cycle time, deduction write-off rate |
| Agent roles | Which agents, one job each? | Intake, evidence, policy, decision |
| Prompt logic | What does each agent receive and return, in what format? | Intake returns one of five categories plus confidence, JSON only |
| RAG grounding | Which corpus, what chunking, what must be cited? | Customer contracts and trade agreements; every decision cites a retrieved clause |
| Orchestration | Sequence, parallelism, retries, state? | Linear state graph; evidence and policy retrieval can run in parallel |
| Guardrails | What stops an agent from acting? | Confidence floor, grounding threshold, value limit, account flags |
| Human-in-the-loop | Where does a person decide, and with what context? | Above-limit and key-account cases, with the agent's proposal pre-assembled |
| Exception paths | What happens when data is missing or rules conflict? | Missing evidence becomes a named request, never a guess |
| Evaluation | How is it tested before users see it? | Reference set of real historical cases, scored against human decisions |
| Token cost | What goes into each call? | Top-k grounded clauses only, not the full corpus |
| Rollback | How is it switched off safely? | Feature flag per cohort, tested before go-live |
| Ownership | Who owns the model, the policy corpus and the KPI after launch? | Named owners in operations, policy and finance |
