from __future__ import annotations

import unittest

from agent.graph import classify_intent


class AgentIntentClassificationTests(unittest.TestCase):
    def test_generic_status_question_does_not_use_previous_application(self):
        result = classify_intent({
            "query": "How can I check the status of my loan application?",
            "last_record_id": "LOAN APPLICATION-0039",
        })

        self.assertEqual(result, {"intent": "status", "record_id": ""})

    def test_generic_status_question_without_memory_requests_application(self):
        result = classify_intent({"query": "Check application status"})

        self.assertEqual(result, {"intent": "status", "record_id": ""})

    def test_referential_status_follow_up_uses_previous_application(self):
        result = classify_intent({
            "query": "What is its status?",
            "last_record_id": "LOAN APPLICATION-0039",
        })

        self.assertEqual(
            result,
            {"intent": "status", "record_id": "LOAN APPLICATION-0039"},
        )

    def test_explicit_application_id_takes_precedence(self):
        result = classify_intent({
            "query": "Check status for LOAN APPLICATION-0002",
            "last_record_id": "LOAN APPLICATION-0039",
        })

        self.assertEqual(
            result,
            {"intent": "status", "record_id": "LOAN APPLICATION-0002"},
        )


if __name__ == "__main__":
    unittest.main()
