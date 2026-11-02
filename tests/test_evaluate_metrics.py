from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from rag.evaluate import _precision_at_k, evaluate_collection
from rag.retriever import RetrievedChunk


class PrecisionAtKTests(unittest.TestCase):
    def test_precision_uses_fixed_k_when_fewer_unique_documents_are_returned(self):
        self.assertAlmostEqual(_precision_at_k(["relevant"], {"relevant"}, k=3), 1 / 3)

    def test_precision_deduplicates_parent_documents_and_uses_fixed_k(self):
        self.assertAlmostEqual(
            _precision_at_k(["relevant", "relevant", "other"], {"relevant"}, k=3),
            1 / 3,
        )

    def test_evaluation_arithmetic_reports_fixed_k_denominator(self):
        retrieved = [
            RetrievedChunk(
                strategy="fixed",
                chunk_id="chunk-1",
                doc_id="relevant",
                title="Relevant",
                text="Relevant content",
                similarity=0.9,
            ),
        ]
        with patch("rag.evaluate.retrieve_top_k", return_value=retrieved):
            result = evaluate_collection(
                strategy="fixed",
                queries={"sample query": {"relevant"}},
            )[0]

        self.assertAlmostEqual(result["precision_at_3"], 1 / 3)
        self.assertEqual(result["arithmetic"]["precision"], "1/3")
        self.assertAlmostEqual(result["recall_at_3"], 1.0)


if __name__ == "__main__":
    unittest.main()
