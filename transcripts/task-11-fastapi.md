# Task 11 - FastAPI endpoints

The endpoints were exercised with FastAPI's `TestClient`, using temporary
Chroma and log paths.

```text
POST /add-document {"doc_id":"transcript_demo","title":"Transcript API Demo", ...}
POST /add-document: 200
{"chunks_indexed": {"fixed": 2, "sentence": 1}, "doc_id": "transcript_demo"}

POST /ask {"query":"What documents are normally required for KYC? Aadhaar 2345 6789 0123",
           "conversation_id":"transcript-api-demo"}
POST /ask: 200 X-Trace-Id=transcript-trace-ask
{
  "conversation_id": "transcript-api-demo",
  "response": {
    "answer": "KYC Document Requirements: KYC documentation usually includes a valid identity proof, address proof, and a completed customer information form. For high-value or riskier profiles, the bank may ask for supplemental documents such as proof of income, business registration, or a recent bank statement. KYC verification is required before disbursement and before any major account or card changes are allowed.",
    "escalate": null,
    "escalation_score": null,
    "fallback": false,
    "intent": "rag",
    "record_id": null
  }
}
```
