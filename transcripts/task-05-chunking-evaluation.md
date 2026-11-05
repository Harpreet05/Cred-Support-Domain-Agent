# Task 5 - Document-level Precision@3 and Recall@3

Command: `.\.venv\Scripts\python.exe -m rag.evaluate`

Retrieved chunks are mapped to parent document IDs and deduplicated. There is
one relevant parent document per query; Precision@3 is relevant documents
retrieved divided by 3, and Recall@3 is relevant documents retrieved divided
by 1.

```text
Fixed strategy
- KYC requirements:            Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Personal-loan eligibility:    Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Interest-rate slabs:          Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Account closure:              Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Credit-score factors:         Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
Average Precision@3: 0.33
Average Recall@3: 1.00

Sentence strategy
- KYC requirements:            Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Personal-loan eligibility:    Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Interest-rate slabs:          Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Account closure:              Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
- Credit-score factors:         Precision@3 = 0.33 (1/3) | Recall@3 = 1.00 (1/1)
Average Precision@3: 0.33
Average Recall@3: 1.00
```

Both strategies tie on this five-query sample. The README recommends the
fixed strategy because the sample shows no measured reason to switch; it does
not establish a general winner.
