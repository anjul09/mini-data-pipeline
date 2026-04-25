from src.validator import validate_record

def process_records(records: list[dict]) -> list[dict]:
    """Takes a list of records, filters out invalid ones,
    and applies a simple transformation.Right now the transformation 
    is just doubling the value."""
    processed = []

    for record in records:
        if not validate_record(record):
            continue

        transformed = {
            "id": record["id"],
            "processed_value": record["value"] * 2
        }

        processed.append(transformed)

    return processed