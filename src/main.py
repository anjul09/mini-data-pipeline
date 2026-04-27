from src.processor import process_records

if __name__ == "__main__":
    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "invalid"},
        {"id": 3, "value": 7.5},
    ]

    result = process_records(data)

    print("Processed output:")
    for r in result:
        print(r)