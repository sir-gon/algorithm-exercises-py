# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/frequency-queries.md]]

from typing import Dict


def freq_query(queries):
    result = []
    data_map: Dict[int, int] = {}

    for q in queries:
        operation = q[0]
        data = q[1]

        if operation == 1:  # insert
            data_map[data] = data_map.get(data, 0) + 1
        elif operation == 2 and data_map.get(data, 0) > 0:  # delete
            data_map[data] -= 1
        elif operation == 3:  # "select"
            for v in data_map.values():
                if v == data:
                    result.append(1)
                    break
            else:
                result.append(0)
        else:
            raise ValueError('Invalid operation')

    return result
