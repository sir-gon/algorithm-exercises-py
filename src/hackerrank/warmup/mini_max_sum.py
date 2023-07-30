import logging

LOGGER = logging.getLogger(__name__)


def mini_max_sum(arr: list[int]) -> str:
    if len(arr) == 0:
        raise ValueError('Empty input')

    tsum: int = 0
    tmin: int = arr[0]
    tmax: int = arr[1]

    for _, value in enumerate(arr):
        tsum += value

        if value < tmin:
            tmin = value

        if value > tmax:
            tmax = value

    result = f"{tsum - tmax} {tsum - tmin}"

    LOGGER.info('Mini-Max Sum result: %s', result)
    return result
