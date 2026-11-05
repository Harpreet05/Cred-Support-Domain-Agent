# Task 13 - RAG-triad evaluation

Command:
`.\.venv\Scripts\python.exe -m rag.evaluate --rag-triad --output $env:TEMP\cred-rag-triad-transcript.json`

The deterministic `MOCK_LLM` judge scores each dimension from 1 to 5.

```text
01. Loan eligibility criteria | Context relevance: 2.00 | Groundedness: 5.00 | Answer relevance: 2.00
02. EMI calculation           | Context relevance: 5.00 | Groundedness: 4.78 | Answer relevance: 5.00
03. Credit-card fees           | Context relevance: 5.00 | Groundedness: 4.90 | Answer relevance: 5.00
04. KYC documents              | Context relevance: 3.00 | Groundedness: 4.80 | Answer relevance: 3.00
05. Fraud dispute              | Context relevance: 2.33 | Groundedness: 4.81 | Answer relevance: 3.00
06. Account closure            | Context relevance: 2.00 | Groundedness: 4.91 | Answer relevance: 2.00
07. Interest-rate slabs        | Context relevance: 3.40 | Groundedness: 5.00 | Answer relevance: 3.40
08. Prepayment penalties       | Context relevance: 3.86 | Groundedness: 5.00 | Answer relevance: 3.86
09. Minimum balance            | Context relevance: 2.33 | Groundedness: 4.91 | Answer relevance: 2.33
10. Credit-score impact        | Context relevance: 3.67 | Groundedness: 4.79 | Answer relevance: 4.33
11. Joint accounts             | Context relevance: 2.33 | Groundedness: 4.89 | Answer relevance: 3.00
12. NRI eligibility            | Context relevance: 2.60 | Groundedness: 4.90 | Answer relevance: 3.40
13. Loan closure / prepayment  | Context relevance: 2.78 | Groundedness: 5.00 | Answer relevance: 2.78
14. Chocolate cake (out of scope) | Context relevance: 1.00 | Groundedness: 5.00 | Answer relevance: 5.00
15. Mumbai weather (out of scope) | Context relevance: 1.00 | Groundedness: 5.00 | Answer relevance: 5.00

Averages across all 15 queries:
- context_relevance: 2.820
- groundedness: 4.913
- answer_relevance: 3.540
```
