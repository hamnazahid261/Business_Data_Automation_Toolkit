
import json
import pytest

from src.reader import read_csv, read_json


def test_read_csv(tmp_path):
    file_path = tmp_path / "properties.csv"

    file_path.write_text(
        "property_id,price\nP001,25000000\n",
        encoding="utf-8"
    )

    records = read_csv(file_path)

    assert len(records) == 1
    assert records[0]["property_id"] == "P001"


def test_read_json(tmp_path):
    file_path = tmp_path / "properties.json"

    data = [
        {"property_id": "J001", "price": "25000000"}
    ]

    file_path.write_text(
        json.dumps(data),
        encoding="utf-8"
    )

    records = read_json(file_path)

    assert len(records) == 1
    assert records[0]["property_id"] == "J001"


def test_read_missing_file(tmp_path):
    file_path = tmp_path / "missing.csv"

    with pytest.raises(FileNotFoundError):
        read_csv(file_path)


def test_invalid_json_format(tmp_path):
    file_path = tmp_path / "invalid.json"

    file_path.write_text(
        "{ invalid json data }",
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="Invalid JSON file format"):
        read_json(file_path)


def test_read_empty_json(tmp_path):
    file_path = tmp_path / "empty.json"

    file_path.write_text(
        "[]",
        encoding="utf-8"
    )

    records = read_json(file_path)

    assert records == []
    assert len(records) == 0
