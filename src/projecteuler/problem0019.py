import logging
from .constants.datetime import __DAYS_IN_MONTH__, __SUNDAY__

LOGGER = logging.getLogger(__name__)


def problem0019(
  _day_of_week: int = __SUNDAY__,
  _since_year: int = 1901,
  _until_year: int = 2000
) -> int:
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
