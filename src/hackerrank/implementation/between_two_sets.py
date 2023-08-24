# @link Problem definition [[docs/hackerrank/implementation/between_two_sets.md]]

import logging

LOGGER = logging.getLogger(__name__)


def is_factor(_n: int, group: list[int]) -> bool:
    result: bool = True
    i: int = 0

    if len(group) == 0:
        return False

    while (i < len(group) and result):
        if _n % group[i] != 0:
            result = False

        i += 1

    return result


def factor_of(_n: int, group: list[int]):
    result: bool = True
    i: int = 0

    if len(group) == 0:
        return False

    while (i < len(group) and result):
        if group[i] % _n != 0:
            result = False

        i += 1

    return result


def get_total_x(_a: list[int], _b: list[int]) -> int:
    _max_ = 0
    for _, j in enumerate(_b):
        if j > _max_:
            _max_ = j

    result: list[int] = []

    for i in range(2, _max_):
        if is_factor(i, _a) and factor_of(i, _b):
            result.append(i)

    output = len(result)
    LOGGER.info('Between Two Sets result: %i', output)

    return output
