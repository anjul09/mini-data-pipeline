from src.processor import process_records


def test_process_records_filters_invalid():
    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "bad"},  # invalid
        {"id": 3, "value": 5}
    ]

    result = process_records(data)

    assert len(result) == 2


def test_process_records_transforms_values():
    data = [
        {"id": 1, "value": 3}
    ]

    result = process_records(data)

    assert result[0]["processed_value"] == 6