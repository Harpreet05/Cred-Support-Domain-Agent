# Task 7 - Conditional agent routing

Command: `.\.venv\Scripts\python.exe agent\graph.py`

The graph has eight nodes. Conditional edges route blocked inputs away from
classification and route classified requests to either the loan-status tool
or the fixed-size RAG tool. The following status request took the tool route:

```text
User: Check status for LOAN APPLICATION-0005
Assistant: Status: Under Review; loan amount: INR 5849420; escalation score:
0.2000. No escalation recommended.
```

A policy question follows the RAG route, as also demonstrated in
`task-09-structured-output.md`.
