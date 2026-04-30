import json

def load_test_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return [
        (d["username"], d["password"], d["result"])
        for d in data
    ]
