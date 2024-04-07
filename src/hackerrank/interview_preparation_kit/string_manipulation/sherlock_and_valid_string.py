# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/string_manipulation/sherlock-and-valid-string.md]] # noqa
# pylint: enable=line-too-long

from collections import Counter


def is_valid(s: str) -> bool:

    if len(s) <= 1:
        return True

    string_map = {}
    for c in s:
        string_map[c] = 1 + string_map.get(c, 0)

    frequencies = Counter(string_map.values())
    frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1]))
    frequencies_size = len(frequencies)

    if frequencies_size == 1:
        return True

    if frequencies_size == 2:
        frequencies_list = list(frequencies.keys())

        if frequencies[frequencies_list[0]] == 1 and \
            (frequencies_list[0] - 1 == 0 or
             frequencies_list[0] - 1 == frequencies_list[1]):
            return True

    return False
