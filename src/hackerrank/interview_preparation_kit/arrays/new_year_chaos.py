# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/new_year_chaos.md]]

import logging

LOGGER = logging.getLogger(__name__)

TOO_CHAOTIC_ERROR = 'Too chaotic'


def minimum_bribes(q: list[int]) -> 'int | None':
    bribes = 0

    for i, o in enumerate(q):
        cur = i + 1

        if o - cur > 2:
            return None

        for k in q[max(o - 2, 0):i]:
            if k > o:
                bribes += 1

    return bribes


def minimum_bribes_transform(q: list[int]) -> 'int | str':

    result = minimum_bribes(q)
    if result is None:
        return TOO_CHAOTIC_ERROR

    return result
