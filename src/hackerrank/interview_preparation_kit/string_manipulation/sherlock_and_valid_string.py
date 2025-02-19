# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/string_manipulation/sherlock-and-valid-string.md]] # noqa
# pylint: enable=line-too-long

from collections import Counter


def isValid(word: str) -> bool:

    if len(word) <= 1:
        return True

    string_map = {}
    for letter in word:
        string_map[letter] = 1 + string_map.get(letter, 0)

    frequencies = Counter(string_map.values())
    frequencies_size = len(frequencies)

    if frequencies_size == 1:
        return True

    if frequencies_size == 2:
        frequencies = dict(sorted(frequencies.items(), key=lambda x: x[1]))
        frequencies_list = list(frequencies.keys())

        minor_freq = frequencies_list[0]
        major_freq = frequencies_list[1]
        tolerance = 1

        if frequencies[minor_freq] == tolerance \
           and tolerance in {minor_freq, (minor_freq - major_freq)}:
            return True

    return False
