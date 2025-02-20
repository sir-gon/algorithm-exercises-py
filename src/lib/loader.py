import json


def loadTestCases(filename: str):
    with open(filename, encoding="utf-8"
              ) as file:
        return json.load(file)
