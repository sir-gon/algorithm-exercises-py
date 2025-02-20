# @link Problem definition [[docs/hackerrank/warmup/mini_max_sum.md]]

import logging

LOGGER = logging.getLogger(__name__)


def miniMaxSum(arr: list[int]) -> str:
    if len(arr) == 0:
        raise ValueError('Empty input')

    tsum: int = 0
    tmin: int = arr[0]
    tmax: int = arr[1]

    for _, value in enumerate(arr):
        tsum += value

        tmin = min(tmin, value)
        tmax = max(tmax, value)

    result = f"{tsum - tmax} {tsum - tmin}"

    LOGGER.info('Mini-Max Sum result: %s', result)
    return result
