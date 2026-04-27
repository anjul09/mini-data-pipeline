def is_valid_record(record):
    """Basic validation:
    - must have 'id' and 'value'
    - value must be int or float"""
    
    if not isinstance(record, dict):
        return False

    if "id" not in record or "value" not in record:
        return False

    if not isinstance(record["value"], (int, float)):
        return False

    return True