###############################################################################
# Result found:
#      Factorial of 100! =
#            93326215443944152681699238856266700490715968264381621
#            46859296389521759999322991560894146397615651828625369
#            7920827223758251185210916864000000000000000000000000
###############################################################################

import math
import logging

LOGGER = logging.getLogger(__name__)


def problem0020(_input) -> int:

    big_number = [int(i) for i in str(math.factorial(_input))]
    result = sum(big_number)

    LOGGER.info('Problem 0020 result: %s', result)
    return result
