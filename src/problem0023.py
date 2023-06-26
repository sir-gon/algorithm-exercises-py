###############################################################################
# Non-abundant sums
#
# https://projecteuler.net/problem=23
#
# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is
# less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
# smallest number that can be written as the sum of two abundant numbers is 24.
# By mathematical analysis, it can be shown that all integers greater
# than 28123 can be written as the sum of two abundant numbers.
# However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed
#  as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.
################################################################################

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

    LOGGER.debug(
        "abundant nums list: %i => %s", len(abundant_number_list), abundant_number_list
    )

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

    # filter duplicates
    sums_abundant_nums = [*set(sums_abundant_nums)]

    LOGGER.info("sumsAbundantNums size: %i. result => %s",
                len(sums_abundant_nums),
                sums_abundant_nums)

    # All numbers below limit that not present in list of sums of pair of abundant numbers
    found = []
    for i in range(1, _super_limit):
        if i not in sums_abundant_nums:
            found.append(i)

    LOGGER.info("found size: %i, found => %s", len(found), found)

    result = sum(found)

    LOGGER.info("Problem 0023 result: %i", result)
    return result
