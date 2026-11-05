# Task 14 - MCP client-server round trip

Start the server with `.\.venv\Scripts\python.exe mcp\mcp_server.py`; in a
second terminal run `.\.venv\Scripts\python.exe mcp\mcp_client.py`. The
server runs at `http://127.0.0.1:8001/mcp`.

```text
MCP response for LOAN APPLICATION-0001:
structuredContent = {"record_id":"LOAN APPLICATION-0001","status":"Under Review",
 "loan_amount_inr":749255,"escalation_score":0.3067,"escalate":false}
isError = false

MCP response for LOAN APPLICATION-0002:
structuredContent = {"record_id":"LOAN APPLICATION-0002","status":"Approved",
 "loan_amount_inr":2082502,"escalation_score":0.3867,"escalate":false}
isError = false
```
