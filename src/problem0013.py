###############################################################################
#
# Large sum
#
# https://projecteuler.net/problem=13
#
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
#
# See: src/data/problem0013.json
#
################################################################################

import logging

LOGGER = logging.getLogger(__name__)


def problem0013(_arrayOfNumbers, _firtsDigits):

    sumOfBigNumbers = sum(_arrayOfNumbers)
    sumOfBigNumbers = str(sumOfBigNumbers)[0:_firtsDigits]
    sumOfBigNumbers = int(sumOfBigNumbers)

    LOGGER.info('Problem 0013 result: %i', sumOfBigNumbers)
    return sumOfBigNumbers
