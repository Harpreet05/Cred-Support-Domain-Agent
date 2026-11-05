# Task 16 - Retries and timeouts

Command: `.\.venv\Scripts\python.exe -m agent.resilience_demo`

```text
Production policies: loan_status_tool timeout=5.0s; global graph timeout=30.0s
Transient node attempt 1/3
Transient node attempt 2/3
Transient node attempt 3/3
Retry recovered: attempts=3, initial_interval=0.2s, max_interval=2.0s,
 backoff_factor=2.0, jitter=True
Per-node timeout fired cleanly: Node 'slow_node' exceeded its run timeout
 of 0.050s; node_cancelled=True
Global graph timeout fired cleanly: Agent graph exceeded its 0.050s global
 timeout; slow_node_cancelled=True; downstream_node_ran=False
```
