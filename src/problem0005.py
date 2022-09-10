###############################################################################
# Smallest multiple
#
# https://projecteuler.net/problem=5
#
# 2520 is the smallest number that can be divided by each of the
# numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by
# all of the numbers from 1 to 20?
###############################################################################

import logging

LOGGER = logging.getLogger(__name__)


def problem0005(_bottom, _top, _start_from = 0):

    found = None
    fail = None
    test = _start_from

    cycles = 0

    while not found:
        fail = False
        i = _bottom
        while i <= _top and not fail:
            cycles += 1
            LOGGER.debug('%d => cycle %d ', i, cycles)

            fail = test % i != 0

            if fail:
                LOGGER.debug('Fail %d not divisible by %d', test, i)
            else:
                LOGGER.debug('Testing: %d divisible by %d', test, i)

            i += 1

        if not fail:
            found = test

        fail = False
        test += 1

    LOGGER.info('Problem 0005 result: %i in %d cycles', found, cycles)
    return found
