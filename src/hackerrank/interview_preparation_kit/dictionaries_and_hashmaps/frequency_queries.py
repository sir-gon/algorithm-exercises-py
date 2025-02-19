# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/frequency-queries.md]]

from typing import Dict

__INITIAL__ = 0

__INSERT__ = 1
__DELETE__ = 2
__SELECT__ = 3

__NOT_FOUND__ = 0
__FOUND__ = 1


def freqQuery(queries):
    result = []
    data_map: Dict[int, int] = {}

    for query in queries:
        operation = query[0]
        data = query[1]
        current = data_map.get(data, __INITIAL__)

        if operation == __INSERT__:
            data_map[data] = current + 1
        elif operation == __DELETE__:
            data_map[data] = max(current - 1, 0)
        elif operation == __SELECT__:
            for value in data_map.values():
                if value == data:
                    result.append(__FOUND__)
                    break
            else:
                result.append(__NOT_FOUND__)
        else:
            raise ValueError('Invalid operation')

    return result
