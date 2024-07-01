# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/stacks_and_queues/balanced-brackets.md]]

from __future__ import annotations
import logging

LOGGER = logging.getLogger(__name__)


def is_balanced(text: str) -> bool:

    pairs = {'{': '}', '(': ')', '[': ']'}
    brackets = []

    for letter in text:
        if letter in pairs:
            brackets.append(letter)
        else:
            if brackets and pairs[brackets[-1]] == letter:
                brackets.pop(-1)
            else:
                return False

        print(letter)

    return not brackets
