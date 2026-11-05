# Task 9 - Validated structured output

Command: `.\.venv\Scripts\python.exe agent\graph.py`

Responses are validated against the declared schema with fields `intent`,
`answer`, `fallback`, `record_id`, `escalation_score`, and `escalate`. The
schema-validated RAG response follows:

```json
{
  "intent": "rag",
  "answer": "KYC Document Requirements: KYC documentation usually includes a valid identity proof, address proof, and a completed customer information form. For high-value or riskier profiles, the bank may ask for supplemental documents such as proof of income, business registration, or a recent bank statement. KYC verification is required before disbursement and before any major account or card changes are allowed.",
  "fallback": false,
  "record_id": null,
  "escalation_score": null,
  "escalate": null
}
```
