# @link Problem definition [[docs/hackerrank/warmup/plus_minus.md]]

import logging

LOGGER = logging.getLogger(__name__)


def plusMinus(arr: list[int]) -> str:
    positives: int = 0
    negatives: int = 0
    zeros: int = 0

    for _, value in enumerate(arr):
        if value > 0:
            positives += 1
        if value < 0:
            negatives += 1
        if value == 0:
            zeros += 1

    result: list[str] = []

    result.append(f'{positives / len(arr):.6f}')
    result.append(f'{negatives / len(arr):.6f}')
    result.append(f'{zeros / len(arr):.6f}')

    output: str = '\n'.join(result)

    LOGGER.info('plusMinus result: %s', output)
    return output
