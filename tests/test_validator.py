from src.validator import validate_record, find_duplicate_records


def test_valid_property():
    record = {
        "property_id": "P001",
        "location": "DHA Karachi",
        "property_type": "House",
        "price": "25000000",
        "size_sqft": "1200",
        "status": "Available"
    }

    assert validate_record(record) == []


def test_missing_price():
    record = {
        "property_id": "P002",
        "location": "Bahria Town",
        "property_type": "Flat",
        "price": "",
        "size_sqft": "900",
        "status": "Available"
    }

    errors = validate_record(record)

    assert "Price is missing" in errors


def test_negative_price():
    record = {
        "property_id": "P003",
        "location": "DHA Karachi",
        "property_type": "House",
        "price": "-500000",
        "size_sqft": "1200",
        "status": "Available"
    }

    errors = validate_record(record)

    assert "Price cannot be negative" in errors


def test_invalid_price():
    record = {
        "property_id": "P004",
        "location": "Clifton Karachi",
        "property_type": "Flat",
        "price": "not_available",
        "size_sqft": "800",
        "status": "Available"
    }

    errors = validate_record(record)

    assert "Price must be a number" in errors


def test_invalid_size():
    record = {
        "property_id": "P005",
        "location": "Gulshan Karachi",
        "property_type": "House",
        "price": "18000000",
        "size_sqft": "-300",
        "status": "Available"
    }

    errors = validate_record(record)

    assert "Property size must be greater than zero" in errors


def test_duplicate_records():
    records = [
        {"property_id": "P001"},
        {"property_id": "P002"},
        {"property_id": "P001"}
    ]

    duplicates = find_duplicate_records(records)

    assert duplicates == {"P001"}