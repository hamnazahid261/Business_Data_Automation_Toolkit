
REQUIRED_FIELDS = [
    "property_id",
    "location",
    "property_type",
    "price",
    "size_sqft",
    "status"
]


def validate_record(record):
    """Validate one property record."""

    errors = []

    # Check required fields
    for field in REQUIRED_FIELDS:
        value = record.get(field)

        if value is None or not str(value).strip():
            errors.append(f"{field.capitalize()} is missing")

    # Validate price
    price_value = str(record.get("price") or "").strip()

    if price_value:
        try:
            price = float(price_value)

            if price < 0:
                errors.append("Price cannot be negative")

        except ValueError:
            errors.append("Price must be a number")

    # Validate property size
    size_value = str(record.get("size_sqft") or "").strip()

    if size_value:
        try:
            size = float(size_value)

            if size <= 0:
                errors.append("Property size must be greater than zero")

        except ValueError:
            errors.append("Property size must be a number")

    # Validate property status
    status = str(record.get("status") or "").strip().lower()

    if status and status not in ["available", "sold"]:
        errors.append("Invalid property status")

    return errors


def find_duplicate_records(records):
    """Find duplicate property IDs."""

    seen_ids = set()
    duplicate_ids = set()

    for record in records:
        property_id = str(record.get("property_id") or "").strip()

        if property_id:
            if property_id in seen_ids:
                duplicate_ids.add(property_id)
            else:
                seen_ids.add(property_id)

    return duplicate_ids
