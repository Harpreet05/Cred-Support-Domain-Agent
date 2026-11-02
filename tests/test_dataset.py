from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import call, patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from dataset import (
    _generate_loan_application_batch,
    _meets_dataset_requirements,
    generate_loan_applications,
)


class LoanApplicationDatasetTests(unittest.TestCase):
    def test_default_seed_generates_a_qualifying_dataset_reproducibly(self):
        first = generate_loan_applications()
        second = generate_loan_applications()

        self.assertEqual(first, second)
        self.assertEqual(len(first), 50)
        self.assertTrue(_meets_dataset_requirements(first))

    def test_generator_retries_with_next_seed_after_invalid_batch(self):
        valid_records = _generate_loan_application_batch(count=50, seed=75)
        invalid_records = [record.copy() for record in valid_records]
        for record in invalid_records:
            record["status"] = "Submitted"

        with patch(
            "dataset._generate_loan_application_batch",
            side_effect=[invalid_records, valid_records],
        ) as generate_batch:
            result = generate_loan_applications(count=50, seed=75)

        self.assertEqual(result, valid_records)
        self.assertEqual(generate_batch.call_args_list, [call(50, 75), call(50, 76)])

    def test_generator_rejects_count_below_required_minimum(self):
        with self.assertRaisesRegex(ValueError, "at least 40"):
            generate_loan_applications(count=39)


if __name__ == "__main__":
    unittest.main()
