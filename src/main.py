from src.processor import process_records

def run_demo():
    data = [
        {"id": 1, "value": 10},
        {"id": 2, "value": "oops"},
        {"id": 3, "value": 7.5},
        {"id": 4}  
    ]

    result = process_records(data)

    print("Processed output:")
    for r in result:
        print(r)


if __name__ == "__main__":
    run_demo()