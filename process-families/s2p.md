# Source to Pay

| Step | Key handoff | Common exceptions | AI role (first pass) |
|---|---|---|---|
| Sourcing and contracting | Business to procurement and legal | Non-standard clauses | Augment clause comparison; human-led negotiation |
| Supplier onboarding | Procurement to vendor master | Due diligence, sanctions hits | Augment |
| Requisition and purchase order | Requester to buyer | Off-catalogue buys, missing budget | Automate catalogue buys; augment exceptions |
| Receiving | Warehouse or requester to accounts payable | Partial delivery, no goods receipt | Automate matching |
| Invoice processing | Supplier to accounts payable | Price, quantity, tax, duplicate, no-PO exceptions | Automate within tolerance; augment the rest |
| Payment | Accounts payable to treasury | Holds, early-payment terms | Automate scheduling |

**KPIs:** spend under management, PO compliance, first-pass match rate, invoice cycle time, duplicate payments prevented, early-payment discount capture.

The invoice-exception step is the third workflow in the prototype repo; no-PO invoices and new suppliers are always routed to a person there.
