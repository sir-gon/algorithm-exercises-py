import json


def load_test_cases(filename: str):
    with open(filename, encoding="utf-8"
              ) as file:
        return json.load(file)
