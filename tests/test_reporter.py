
import csv
import json

from src.reporter import (
    save_clean_data,
    save_exception_report,
    save_summary
)


def test_save_clean_data(tmp_path):
    records = [
        {
            "property_id": "P001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": 25000000.0,
            "size_sqft": 1200.0,
            "status": "Available"
        }
    ]

    output_path = tmp_path / "cleaned_data.csv"

    save_clean_data(records, output_path)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        saved_records = list(csv.DictReader(file))

    assert len(saved_records) == 1
    assert saved_records[0]["property_id"] == "P001"


def test_save_empty_clean_data(tmp_path):
    output_path = tmp_path / "empty_data.csv"

    save_clean_data([], output_path)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        reader = csv.reader(file)
        headers = next(reader)

    assert headers == [
        "property_id",
        "location",
        "property_type",
        "price",
        "size_sqft",
        "status"
    ]


def test_save_exception_report(tmp_path):
    invalid_records = [
        {
            "record": {
                "property_id": "P002",
                "location": "DHA Karachi",
                "property_type": "House",
                "price": "-500000",
                "size_sqft": "1200",
                "status": "Available"
            },
            "errors": ["Price cannot be negative"]
        }
    ]

    output_path = tmp_path / "exception_report.csv"

    save_exception_report(invalid_records, output_path)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        saved_records = list(csv.DictReader(file))

    assert len(saved_records) == 1
    assert "Price cannot be negative" in saved_records[0]["errors"]


def test_save_summary(tmp_path):
    output_path = tmp_path / "summary.json"

    save_summary(10, 4, 6, output_path)

    assert output_path.exists()

    with output_path.open("r", encoding="utf-8") as file:
        summary = json.load(file)

    assert summary["total_records"] == 10
    assert summary["valid_records"] == 4
    assert summary["invalid_records"] == 6
