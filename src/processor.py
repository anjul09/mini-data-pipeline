from src.validator import is_valid_record
from src.transformer import transform_record
from src.config import ENABLE_STRICT_VALIDATION

def process_records(records):
    """Processes a list of records.
    Current behavior:
    - invalid records are silently skipped (unless strict mode is enabled)"""
    processed = []

    for record in records:
        if not is_valid_record(record):
            if ENABLE_STRICT_VALIDATION:
                raise ValueError(f"Invalid record: {record}")
            continue

        transformed = transform_record(record)
        processed.append(transformed)

    return processed