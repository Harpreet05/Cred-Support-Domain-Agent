# Task 1 - Deterministic dataset

Captured 2026-11-05. Command: `.\.venv\Scripts\python.exe dataset.py`

```text
Category counts:
  Personal Loan: 15
  Home Loan: 8
  Auto Loan: 10
  Education Loan: 10
  Business Loan: 7

Status counts:
  Submitted: 18
  Under Review: 14
  Approved: 8
  Rejected: 4
  Disbursed: 6

Flagged for fraud review: 20.00%
```

The generator uses seed `75` and increments it if a whole generated batch
does not pass the requirements. Category weights are
`0.30/0.22/0.18/0.15/0.15` for Personal/Home/Auto/Education/Business Loan;
status weights are `0.30/0.25/0.20/0.15/0.10` for Submitted/Under Review/
Approved/Rejected/Disbursed. Category-specific amount bands span INR 50,000
to INR 80,00,000 overall and reflect differing lending needs across products.
The output contains 50 records, at least three per category, all required
statuses, and a 20% fraud-review share.
