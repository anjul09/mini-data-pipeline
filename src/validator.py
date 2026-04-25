def validate_record(record: dict) -> bool:
    """ Very basic validation for incoming records.
    For now we just check:
    - 'id' exists
    - 'value' exists and is numeric
    This can be expanded later if needed."""
    
    if not isinstance(record, dict):
        return False

    if "id" not in record or "value" not in record:
        return False

    value = record["value"]

    if not isinstance(value, (int, float)):
        return False

    return True