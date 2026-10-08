# Order to Cash

| Step | Key handoff | Common exceptions | AI role (first pass) |
|---|---|---|---|
| Order capture | Sales to order management | Pricing or terms mismatch, incomplete orders | Automate validation; augment non-standard terms |
| Credit management | Order management to credit | New customer, limit breach | Human-led for new limits; augment reviews |
| Fulfilment coordination | Credit to warehouse and logistics | Stock-outs, split shipments | Augment |
| Billing | Logistics to billing | Wrong price, missing proof of delivery | Automate checks |
| Collections | Billing to collections | Promises broken, disputes raised | Automate reminders; augment disputes |
| Cash application | Bank to accounts receivable | Unmatched remittances, short-pays | Automate matching |
| Deductions and disputes | Accounts receivable to sales, logistics, trade | Promotion, pricing, shortage, damage, compliance claims | Augment, with automatic resolution for clear low-value cases |

**KPIs:** days sales outstanding, collection effectiveness index, dispute cycle time, deduction write-off rate, unapplied cash, first-pass cash application rate.

**Where value leaks:** invalid deductions written off because the evidence is spread across sales, logistics and trade teams and no one assembles it in time. This is the workflow run in the prototype repo.
