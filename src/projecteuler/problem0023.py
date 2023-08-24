# @link Problem definition [[docs/projecteuler/problem0023.md]]

import logging
from .helpers.natural_number import NaturalNumber, DivisorsAbundance

LOGGER = logging.getLogger(__name__)


def problem0023(_under_limit: int, _super_limit: int) -> int:
    abundant_number_list = []

    # Produce a list of abundant numbers below limit
    for i in range(_under_limit, _super_limit):
        abundancy_of = NaturalNumber(i).abundance()

        if abundancy_of.value == DivisorsAbundance.DIVISORS_ABUNDANT.value:
            abundant_number_list.append(i)

    LOGGER.info("abundant nums list size => %i", len(abundant_number_list))
    LOGGER.debug("abundant nums list result: => %s", abundant_number_list)

    sums_abundant_nums = []

    for abundant in abundant_number_list:
        j = 0
        while (
            abundant + abundant_number_list[j] <= _super_limit
            and j < len(abundant_number_list)
        ):
            sums_abundant_nums.append(abundant + abundant_number_list[j])
            j += 1

    result = 0

    LOGGER.info("sumsAbundantNums size => %s", len(sums_abundant_nums))
    LOGGER.debug("sumsAbundantNums => %s", sums_abundant_nums)

    # filter duplicates
    sums_abundant_nums = [*set(sums_abundant_nums)]

    LOGGER.info("filtered sumsAbundantNums size => %s", len(sums_abundant_nums))
    LOGGER.debug("filtered sumsAbundantNums => %s", sums_abundant_nums)

    # All numbers below limit that not present in list of sums of pair of abundant numbers
    found = []
    for i in range(1, _super_limit):
        if i not in sums_abundant_nums:
            found.append(i)

    LOGGER.info("found size => %i", len(found))
    LOGGER.debug("found result => %s", found)

    result = sum(found)

    LOGGER.info("Problem 0023 result: %i", result)
    return result
