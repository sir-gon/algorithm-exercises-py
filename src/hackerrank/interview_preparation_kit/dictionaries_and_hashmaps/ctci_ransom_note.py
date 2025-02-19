# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/dictionaries_and_hashmaps/ctci-ransom-note.md]]

from typing import Dict, List

__YES__ = 'Yes'
__NO__ = 'No'


def checkMagazineCompute(magazine: List[str], note: List[str]) -> bool:
    dictionary: Dict[str, int] = {}

    word: str

    for word in magazine:

        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    for word in note:

        if word in dictionary and dictionary[word] > 0:
            dictionary[word] -= 1
        else:
            return False

    return True


def checkMagazineText(magazine: List[str], note: List[str]) -> str:
    return __YES__ if checkMagazineCompute(magazine, note) else __NO__


def checkMagazine(magazine: List[str], note: List[str]):
    print(checkMagazineText(magazine, note))
