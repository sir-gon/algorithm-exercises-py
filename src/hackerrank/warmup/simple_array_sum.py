import logging

LOGGER = logging.getLogger(__name__)


def simple_array_sum(arr: list[int]) -> int:
    acum = 0

    for _, value in enumerate(arr):
        acum += value

    LOGGER.info('Simple Array Sum result: %i', acum)
    return acum
