import logging

LOGGER = logging.getLogger(__name__)


def compare_triplets(_a: list[int], _b: list[int]) -> list[int]:
    if len(_a) == 0 or len(_b) == 0 or len(_a) != len(_b):
        raise ValueError('Empty input')

    awards: list[int] = [0, 0]

    for i, value in enumerate(_a):
        if value > _b[i]:
            awards[0] = awards[0] + 1
        if value < _b[i]:
            awards[1] = awards[1] + 1

    LOGGER.info('Problem 0000 result: %s', awards)
    return awards
