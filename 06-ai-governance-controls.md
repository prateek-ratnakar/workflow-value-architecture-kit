# AI governance controls

These are the release controls I applied to production AI systems. They apply to any agent that touches customers, money or regulated decisions.

## Before build
- Exit criteria agreed and written down: the accuracy, grounding and adoption thresholds that define done.
- Human-in-the-loop boundaries set from the AI-readiness scoring: which decisions the agent may take, which it may only recommend.
- Data and privacy review of the retrieval corpus; no personal data sent that the use case does not need.

## Before users
- UAT on a defined sample of real historical cases, with accuracy measured against human decisions and written sign-off.
- Grounding check: every automatic output must cite retrieved sources; ungrounded outputs route to a person.
- Rollback path built and tested, not just documented.

## At launch
- Phased rollout by cohort behind feature flags.
- Monitoring of accuracy, override rate and grounding failures by cohort.

## After launch
- Silent-regression watch: model or prompt changes re-run the reference set before release.
- Incident rule: if ungrounded answers reach users, roll back the same day, find the root cause, and add the missing check to the definition of done.
- Quarterly review of human-in-the-loop boundaries as accuracy evidence accumulates; boundaries move only on evidence.

## Responsible-AI questions every design must answer
Who could be harmed by a wrong decision? Is any group systematically routed differently? Can every decision be explained from its audit trail? Who is accountable when the agent is wrong?
