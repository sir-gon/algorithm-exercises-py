# @link Problem definition [[docs/projecteuler/problem0022.md]]

import logging
from typing import List

from .helpers.word_score import word_score

LOGGER = logging.getLogger(__name__)


def problem0022(list_of_names: List[str]) -> int:

    names = list_of_names.copy()
    names.sort()

    counter = 0
    result = 0

    for name in names:
        counter += 1
        result += counter * word_score(name)

    LOGGER.info('Problem 0022 result: %i', result)
    return result
