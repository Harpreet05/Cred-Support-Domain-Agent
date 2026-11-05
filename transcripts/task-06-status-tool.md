# Task 6 - Status lookup and escalation score

Command:
`.\.venv\Scripts\python.exe -c "from agent.tool import check_loan_application_status; print(check_loan_application_status('LOAN APPLICATION-0001')); print(check_loan_application_status('LOAN APPLICATION-0002'))"`

The designed score is
`0.6 * fraud_signal + 0.4 * min(days_since_created, 30) / 30`.
Escalation is recommended only when the score is strictly above `0.90`. In
this 50-record dataset, the nearest-rank 80th percentile of age is 23 days.
A fraud-flagged record at that age scores
`0.6 + 0.4 * (23/30) = 0.9067`, above the threshold; an unflagged record
cannot exceed `0.40`.

```text
check_loan_application_status("LOAN APPLICATION-0001")
{'record_id': 'LOAN APPLICATION-0001', 'status': 'Under Review',
 'loan_amount_inr': 749255, 'escalation_score': 0.3067, 'escalate': False}

check_loan_application_status("LOAN APPLICATION-0002")
{'record_id': 'LOAN APPLICATION-0002', 'status': 'Approved',
 'loan_amount_inr': 2082502, 'escalation_score': 0.3867, 'escalate': False}
```
