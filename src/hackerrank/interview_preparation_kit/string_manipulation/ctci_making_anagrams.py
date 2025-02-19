# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/string_manipulation/ctci-making-anagrams.md]]

from __future__ import annotations
import logging

LOGGER = logging.getLogger(__name__)


def charToDict(word: str) -> dict:
    word_map = {char: (word.count(char)) for char in ''.join(sorted(word[:]))}

    return word_map


def makeAnagram(word_a: str, word_b: str) -> int:

    a_map = charToDict(word_a)
    b_map = charToDict(word_b)

    diff = 0
    for key in a_map:
        if b_map.get(key):
            a_map[key] = abs(a_map[key] - b_map[key])
            b_map[key] = 0

    diff = sum(a_map.values()) + sum(b_map.values())
    return diff
