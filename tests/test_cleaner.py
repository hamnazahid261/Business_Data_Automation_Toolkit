
from src.cleaner import clean_records


def test_valid_and_invalid_records():
    records = [
        {
            "property_id": "P001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": "25000000",
            "size_sqft": "1200",
            "status": "Available"
        },
        {
            "property_id": "P002",
            "location": "Bahria Town",
            "property_type": "Flat",
            "price": "-500000",
            "size_sqft": "900",
            "status": "Available"
        }
    ]

    valid_records, invalid_records = clean_records(records)

    assert len(valid_records) == 1
    assert len(invalid_records) == 1


def test_valid_price_conversion():
    records = [
        {
            "property_id": "P001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": "25000000",
            "size_sqft": "1200",
            "status": "Available"
        }
    ]

    valid_records, invalid_records = clean_records(records)

    assert valid_records[0]["price"] == 25000000.0
    assert valid_records[0]["size_sqft"] == 1200.0
    assert invalid_records == []


def test_duplicate_records_are_invalid():
    records = [
        {
            "property_id": "P001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": "25000000",
            "size_sqft": "1200",
            "status": "Available"
        },
        {
            "property_id": "P001",
            "location": "DHA Karachi",
            "property_type": "House",
            "price": "25000000",
            "size_sqft": "1200",
            "status": "Available"
        }
    ]

    valid_records, invalid_records = clean_records(records)

    assert valid_records == []
    assert len(invalid_records) == 2


def test_empty_records():
    valid_records, invalid_records = clean_records([])

    assert valid_records == []
    assert invalid_records == []
