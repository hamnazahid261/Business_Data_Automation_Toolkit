
import csv
import json

from src.main import main


def test_complete_csv_workflow(tmp_path, monkeypatch):
    # Create a temporary input folder
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    input_file = input_dir / "properties.csv"

    # Create sample property data
    input_file.write_text(
        "property_id,location,property_type,price,size_sqft,status\n"
        "P001,DHA Karachi,House,25000000,1200,Available\n"
        "P002,Bahria Town,Flat,-500000,900,Available\n",
        encoding="utf-8"
    )

    # Configure application paths
    monkeypatch.setenv("INPUT_FILE", str(input_file))
    monkeypatch.setenv("OUTPUT_DIR", str(tmp_path / "output"))
    monkeypatch.setenv("REPORT_DIR", str(tmp_path / "reports"))
    monkeypatch.setenv("LOG_FILE", str(tmp_path / "logs" / "test.log"))

    # Run the complete application
    main()

    # Check cleaned data
    cleaned_file = tmp_path / "output" / "cleaned_data.csv"

    assert cleaned_file.exists()

    with cleaned_file.open("r", encoding="utf-8") as file:
        cleaned_records = list(csv.DictReader(file))

    assert len(cleaned_records) == 1
    assert cleaned_records[0]["property_id"] == "P001"

    # Check exception report
    exception_file = tmp_path / "reports" / "exception_report.csv"

    assert exception_file.exists()

    with exception_file.open("r", encoding="utf-8") as file:
        exception_records = list(csv.DictReader(file))

    assert len(exception_records) == 1
    assert exception_records[0]["property_id"] == "P002"

    # Check summary
    summary_file = tmp_path / "reports" / "summary.json"

    with summary_file.open("r", encoding="utf-8") as file:
        summary = json.load(file)

    assert summary["total_records"] == 2
    assert summary["valid_records"] == 1
    assert summary["invalid_records"] == 1
def test_complete_json_workflow(tmp_path, monkeypatch):
    # Create a temporary input folder
    input_dir = tmp_path / "input"
    input_dir.mkdir()

    input_file = input_dir / "properties.json"

    # Create sample JSON property data
    sample_data = [
        {
            "property_id": "J001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": "25000000",
            "size_sqft": "1200",
            "status": "Available"
        },
        {
            "property_id": "J002",
            "location": "Bahria Town",
            "property_type": "Flat",
            "price": "-500000",
            "size_sqft": "900",
            "status": "Available"
        }
    ]

    input_file.write_text(
        json.dumps(sample_data),
        encoding="utf-8"
    )

    # Configure application paths
    monkeypatch.setenv("INPUT_FILE", str(input_file))
    monkeypatch.setenv("OUTPUT_DIR", str(tmp_path / "output"))
    monkeypatch.setenv("REPORT_DIR", str(tmp_path / "reports"))
    monkeypatch.setenv("LOG_FILE", str(tmp_path / "logs" / "test.log"))

    # Run the complete application
    main()

    # Check cleaned data
    cleaned_file = tmp_path / "output" / "cleaned_data.csv"

    assert cleaned_file.exists()

    with cleaned_file.open("r", encoding="utf-8") as file:
        cleaned_records = list(csv.DictReader(file))

    assert len(cleaned_records) == 1
    assert cleaned_records[0]["property_id"] == "J001"

    # Check exception report
    exception_file = tmp_path / "reports" / "exception_report.csv"

    assert exception_file.exists()

    with exception_file.open("r", encoding="utf-8") as file:
        exception_records = list(csv.DictReader(file))

    assert len(exception_records) == 1
    assert exception_records[0]["property_id"] == "J002"

    # Check summary
    summary_file = tmp_path / "reports" / "summary.json"

    with summary_file.open("r", encoding="utf-8") as file:
        summary = json.load(file)

    assert summary["total_records"] == 2
    assert summary["valid_records"] == 1
    assert summary["invalid_records"] == 1
