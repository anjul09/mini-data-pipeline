from src.processor import process_records

def test_valid_records():
    data = [{"id": 1, "value": 10}]
    result = process_records(data)

    assert result == [{"id": 1, "processed_value": 20}]

def test_invalid_records_are_skipped():
    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "bad"},
    ]

    result = process_records(data)

    assert result == [{"id": 1, "processed_value": 20}]

def test_empty_input():
    result = process_records([])
    assert result == []