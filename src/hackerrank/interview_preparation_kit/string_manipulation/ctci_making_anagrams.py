# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/string_manipulation/ctci-making-anagrams.md]]

from __future__ import annotations
import logging

LOGGER = logging.getLogger(__name__)


def char_to_dict(a: str) -> dict:
    a_map = {char: (a.count(char)) for char in ''.join(sorted(a[:]))}

    return a_map


def make_anagram(a: str, b: str) -> int:

    a_map = char_to_dict(a)
    b_map = char_to_dict(b)

    diff = 0
    for key in a_map:
        if b_map.get(key):
            a_map[key] = abs(a_map[key] - b_map[key])
            b_map[key] = 0

    diff = sum(a_map.values()) + sum(b_map.values())
    return diff
