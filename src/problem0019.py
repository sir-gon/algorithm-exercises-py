###############################################################################
# Counting Sundays

# https://projecteuler.net/problem=19

# You are given the following information, but you may prefer
# to do some research for yourself.

#  1 Jan 1900 was a Monday.
#  Thirty days has September,
#    April, June and November.
#    All the accumulatedRemainder have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
#  A leap year occurs on any year evenly divisible by 4,
#    but not on a century unless it is divisible by 400.

# How many Sundays fell on the first of the month during the
# twentieth century (1 Jan 1901 to 31 Dec 2000)?
################################################################################

import logging
from .constants.datetime import __DAYS_IN_MONTH__, __SUNDAY__

LOGGER = logging.getLogger(__name__)


def problem0019(
  _day_of_week: int = __SUNDAY__,
  _since_year: int = 1901,
  _until_year: int = 2000
):
    result_count = 0
    accumulated_remainder = 0
    excess = 0

    days_in_month = __DAYS_IN_MONTH__.copy()

    for year in range(1900, _until_year + 1):

        leap = 1 if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 0
        days_in_month['FEBRUARY'] = 28 + leap

        for month, days in days_in_month.items():

            LOGGER.debug('Month: %s | days: %d', month, days)

            accumulated_remainder += days % 7
            if accumulated_remainder % 7 == _day_of_week:
                if year <= _since_year:
                    excess += 1

                result_count += 1

    LOGGER.info('Problem 0019 result: %i', result_count)
    return result_count - excess
