# Task 12 - Structured JSONL logging

Two API requests produced two JSONL records with method, route, trace ID,
duration, and status. The `/ask` request included a fabricated Aadhaar value;
the logged text contains its masked value, not the original.

```json
{"timestamp":"<UTC timestamp>","trace_id":"59d60b76-221c-429c-9b82-c74b9834c158","method":"POST","route":"/add-document","request_text":"{\"doc_id\": \"transcript_demo\", \"title\": \"Transcript API Demo\", \"text\": \"A transcript demo document with banking-policy context for checking document indexing.\"}","duration_ms":2114.563,"status_code":200}
{"timestamp":"<UTC timestamp>","trace_id":"transcript-trace-ask","method":"POST","route":"/ask","request_text":"{\"query\": \"What documents are normally required for KYC? Aadhaar [AADHAAR_REDACTED]\", \"conversation_id\": \"transcript-api-demo\"}","duration_ms":1827.181,"status_code":200}
```
