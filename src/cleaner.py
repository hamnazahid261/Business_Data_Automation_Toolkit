from src.validator import validate_record, find_duplicate_records


def clean_records(records):
    """
    Separate valid and invalid property records.
    """

    valid_records = []
    invalid_records = []

    # Find duplicate property IDs
    duplicate_ids = find_duplicate_records(records)

    for record in records:

        # Remove extra spaces
        cleaned_record = {
            key: value.strip() if isinstance(value, str) else value
            for key, value in record.items()
        }

        # Validate the current record
        errors = validate_record(cleaned_record)

        # Check duplicate property ID
        property_id = str(
            cleaned_record.get("property_id", "")
        ).strip()

        if property_id in duplicate_ids:
            errors.append("Duplicate property ID")

        # Separate valid and invalid records
        if errors:
            invalid_records.append({
                "record": cleaned_record,
                "errors": errors
            })

        else:
            cleaned_record["price"] = float(cleaned_record["price"])
            cleaned_record["size_sqft"] = float(
                cleaned_record["size_sqft"]
            )

            valid_records.append(cleaned_record)

    return valid_records, invalid_records