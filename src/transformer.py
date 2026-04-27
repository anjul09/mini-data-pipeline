from src.config import DEFAULT_MULTIPLIER

def transform_record(record):
    """Applies a simple transformation.
    Note: assumes record is already valid."""
    
    return {
        "id": record["id"],
        "processed_value": record["value"] * DEFAULT_MULTIPLIER,
    }