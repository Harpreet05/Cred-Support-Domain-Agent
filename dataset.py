from __future__ import annotations

import random
import re
from collections import Counter
from typing import Dict, List

category_weights = {
    "Personal Loan" : 0.30,
    "Home Loan" : 0.22,
    "Auto Loan" : 0.18,
    "Education Loan" : 0.15,
    "Business Loan" : 0.15,
}

status_weights = {
    "Submitted" : 0.30,
    "Under Review" : 0.25,
    "Approved" : 0.20,
    "Rejected" : 0.15,
    "Disbursed" : 0.10,
}

category_amount_ranges = {
    "Personal Loan": (50_000, 20_00_000),
    "Home Loan": (4_00_000, 80_00_000),
    "Auto Loan": (1_00_000, 30_00_000),
    "Education Loan": (1_00_000, 25_00_000),
    "Business Loan": (3_00_000, 60_00_000),
}

categories = list(category_weights.keys())
statuses = list(status_weights.keys())
MIN_APPLICATION_COUNT = 40
MIN_CATEGORY_COUNT = 3
FRAUD_REVIEW_PERCENTAGE_BAND = (10, 30)
MAX_GENERATION_ATTEMPTS = 1000


def normalize_record_id(record_id: str) -> str:
    if record_id is None:
        return ""

    match = re.fullmatch(r"LOAN\s+APPLICATION\s*-\s*(\d+)", str(record_id).strip(), re.IGNORECASE)
    if not match:
        return str(record_id).strip().upper()

    application_number = int(match.group(1))
    return f"LOAN APPLICATION-{application_number:04d}"


def weighted_choice(weights: Dict[str, float], rng: random.Random) -> str:
    values = list(weights.keys())
    probs = list(weights.values())
    return rng.choices(values, weights=probs, k=1)[0]

def _generate_loan_application_batch(count: int, seed: int) -> List[Dict[str, object]]:
    rng = random.Random(seed)
    records = []

    for i in range(count):
        category = weighted_choice(category_weights, rng)
        status = weighted_choice(status_weights, rng)
        min_amt, max_amt = category_amount_ranges[category]
        loan_amount = rng.randint(min_amt, max_amt)
        days_since_created = rng.randint(0, 30)

        if category in {"Auto Loan", "Business Loan"}:
            flagged_prob = 0.20
        elif category == "Home Loan":
            flagged_prob = 0.18
        else:
            flagged_prob = 0.16

        flagged_for_fraud_review = rng.random() < flagged_prob

        record_id = normalize_record_id(f"LOAN APPLICATION-{i+1:04d}")

        records.append(
            {
                "record_id": record_id,
                "category": category,
                "status": status,
                "loan_amount_inr": loan_amount,
                "days_since_created": days_since_created,
                "flagged_for_fraud_review": flagged_for_fraud_review,
            }
        )

    return records


def _meets_dataset_requirements(records: List[Dict[str, object]]) -> bool:
    if len(records) < MIN_APPLICATION_COUNT:
        return False

    category_counts = Counter(record["category"] for record in records)
    status_counts = Counter(record["status"] for record in records)
    flagged_percentage = (
        sum(bool(record["flagged_for_fraud_review"]) for record in records)
        / len(records)
        * 100
    )
    return (
        all(category_counts[category] >= MIN_CATEGORY_COUNT for category in categories)
        and all(status_counts[status] >= 1 for status in statuses)
        and FRAUD_REVIEW_PERCENTAGE_BAND[0]
        <= flagged_percentage
        <= FRAUD_REVIEW_PERCENTAGE_BAND[1]
    )


def generate_loan_applications(count: int = 50, seed: int = 75) -> List[Dict[str, object]]:
    if count < MIN_APPLICATION_COUNT:
        raise ValueError(
            f"count must be at least {MIN_APPLICATION_COUNT} to meet dataset requirements."
        )

    for attempt in range(MAX_GENERATION_ATTEMPTS):
        records = _generate_loan_application_batch(count, seed + attempt)
        if _meets_dataset_requirements(records):
            return records

    raise ValueError(
        f"Could not generate a valid dataset after {MAX_GENERATION_ATTEMPTS} deterministic seed attempts."
    )


loan_applications = generate_loan_applications()


def summarize_records(records: List[Dict[str, object]]) -> Dict[str, object]:
    category_counts = Counter(r["category"] for r in records)
    status_counts = Counter(r["status"] for r in records)
    flagged_pct = (sum(1 for r in records if r["flagged_for_fraud_review"]) / len(records)) * 100

    print("Category counts:")
    for name in categories:
        print(f"  {name}: {category_counts.get(name, 0)}")
    print("\nStatus counts:")
    for name in statuses:
        print(f"  {name}: {status_counts.get(name, 0)}")
    print(f"\nFlagged for fraud review: {flagged_pct:.2f}%")

    return {
        "category_counts": dict(category_counts),
        "status_counts": dict(status_counts),
        "flagged_pct": flagged_pct,
    }


if __name__ == "__main__":
    summarize_records(loan_applications)