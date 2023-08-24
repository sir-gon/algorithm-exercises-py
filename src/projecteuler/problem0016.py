# @link Problem definition [[docs/projecteuler/problem0016.md]]

##############################################################################
# Result found:
#  Digits:
#      1071508607186267320948425049060001810561404811705
#      5336074437503883703510511249361224931983788156958
#      5812759467291755314682518714528569231404359845775
#      7469857480393456777482423098542107460506237114187
#      7954182153046474983581941267398767559165543946077
#      0629145711964776865421676604298316526243868372056
#      68069376
#  Sum: 1366
##############################################################################

import logging

LOGGER = logging.getLogger(__name__)


def problem0016(base: int, exponent: int) -> int:
    number = base ** exponent

    digits = [int(x) for x in str(number)]
    result = sum(digits)

    LOGGER.debug('Problem 0016 digits: %a', digits)
    LOGGER.info('Problem 0016 result sum of digits: %a', result)
    return result
