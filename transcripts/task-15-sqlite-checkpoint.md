# Task 15 - SQLite checkpoint interruption and resume

Command: `.\.venv\Scripts\python.exe -m agent.checkpoint_demo`

```text
Paused thread_id: checkpoint-demo-b34badc5c4834a36aba63dde9416dd20
Nodes executed before pause: ['input_guardrails', 'classify_intent']
Checkpointed state: query='Check status for LOAN APPLICATION-0001',
 intent='status', record_id='LOAN APPLICATION-0001'
Next scheduled node(s): ('loan_status_tool',)
Restored from SQLite: thread_id=checkpoint-demo-b34badc5c4834a36aba63dde9416dd20,
 intent='status', record_id='LOAN APPLICATION-0001'
Nodes executed after resume:
 ['loan_status_tool', 'format_response', 'validate_response']
Previously completed nodes re-executed: none
Completed response: {'intent': 'status', 'answer': 'Status: Under Review;
 loan amount: INR 749255; escalation score: 0.3067. No escalation recommended.',
 'fallback': False, 'record_id': 'LOAN APPLICATION-0001',
 'escalation_score': 0.3067, 'escalate': False}
```
