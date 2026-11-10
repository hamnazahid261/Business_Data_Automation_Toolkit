
import csv
import json
from pathlib import Path


def read_csv(file_path):
    """Read records from a CSV file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        with file_path.open("r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            if not reader.fieldnames:
                raise ValueError("CSV file is empty or has no headers.")

            records = list(reader)

        return records

    except UnicodeDecodeError as error:
        raise ValueError("CSV file encoding is not supported.") from error


def read_json(file_path):
    """Read records from a JSON file."""

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if file_path.suffix.lower() != ".json":
        raise ValueError("Only JSON files are supported.")

    try:
        with file_path.open("r", encoding="utf-8") as file:
            records = json.load(file)

        if not isinstance(records, list):
            raise ValueError("JSON must contain a list of records.")

        if not all(isinstance(record, dict) for record in records):
            raise ValueError("Each JSON record must be an object.")

        return records

    except json.JSONDecodeError as error:
        raise ValueError("Invalid JSON file format.") from error
