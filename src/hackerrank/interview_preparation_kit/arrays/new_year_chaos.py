# @link Problem definition
# [[docs/hackerrank/interview_preparation_kit/arrays/new_year_chaos.md]]

import logging

LOGGER = logging.getLogger(__name__)
TOO_CHAOTIC_ERROR = 'Too chaotic'


def minimumBribesCompute(queue: list[int]) -> 'int | None':
    bribes = 0

    for i, value in enumerate(queue):
        position = i + 1

        if value - position > 2:
            return None

        for k in queue[max(value - 2, 0):i]:
            if k > value:
                bribes += 1

    return bribes


def minimumBribesText(queue: list[int]) -> 'int | str':

    result = minimumBribesCompute(queue)
    if result is None:
        return TOO_CHAOTIC_ERROR

    return result


def minimumBribes(queue: list[int]):
    print(minimumBribesText(queue))
