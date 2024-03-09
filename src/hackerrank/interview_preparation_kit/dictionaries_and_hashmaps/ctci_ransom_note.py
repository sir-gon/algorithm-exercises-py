# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/ctci-ransom-note.md]]

from typing import Dict

__YES__ = 'Yes'
__NO__ = 'No'


def check_magazine_compute(magazine: str, note: str) -> bool:
    dictionary: Dict[str, int] = {}

    for x in magazine:

        if x in dictionary:
            dictionary[x] += 1
        else:
            dictionary[x] = 1

    for x in note:

        if x in dictionary and dictionary[x] > 0:
            dictionary[x] -= 1
        else:
            return False

    return True


def check_magazine(magazine: str, note: str) -> str:
    return __YES__ if check_magazine_compute(magazine, note) else __NO__
