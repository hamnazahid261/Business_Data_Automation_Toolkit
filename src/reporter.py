
import csv
import json
from pathlib import Path


def save_clean_data(records, output_path):
    """Save valid records into a CSV file."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "property_id",
        "location",
        "property_type",
        "price",
        "size_sqft",
        "status"
    ]

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)


def save_exception_report(invalid_records, output_path):
    """Save invalid records and their errors into a CSV report."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "property_id",
        "location",
        "property_type",
        "price",
        "size_sqft",
        "status",
        "errors"
    ]

    with output_path.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()

        for item in invalid_records:
            record = item["record"]

            row = {
                field: record.get(field, "")
                for field in fieldnames
                if field != "errors"
            }

            row["errors"] = "; ".join(item["errors"])
            writer.writerow(row)


def save_summary(total, valid, invalid, output_path):
    """Save processing summary into a JSON file."""

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    summary = {
        "total_records": total,
        "valid_records": valid,
        "invalid_records": invalid
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(summary, file, indent=4)
