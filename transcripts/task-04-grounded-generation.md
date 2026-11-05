# Task 4 - Grounded answers and empirical threshold

Command:
`.\.venv\Scripts\python.exe -c "from rag.retriever import benchmark_queries; import json; print(json.dumps(benchmark_queries(), indent=2))"`

Five in-scope and two out-of-scope queries were measured with the local
embedding model. The selected midpoint threshold was `0.4530`.

| Scope | Query | Top-1 cosine |
|---|---|---:|
| In | What documents are normally required for KYC? | 0.7155 |
| In | What are the eligibility requirements for a personal loan? | 0.7971 |
| In | How are interest rate slabs determined? | 0.6947 |
| In | How is the account closure process completed? | 0.6706 |
| In | What are the main factors affecting a credit score? | 0.6815 |
| Out | How do I bake a chocolate cake? | 0.1089 |
| Out | How is the weather today? | 0.1442 |

All five in-scope questions returned a policy answer (`fallback: false`). Both
out-of-scope questions returned `fallback: true`:

```text
I don't know. The query is not supported by the available knowledge base.
```
