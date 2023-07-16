###############################################################################
# 1000-digit Fibonacci Number
#
# https://projecteuler.net/problem=25
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1
#
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
#
# The 12th term, F12 is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci
# sequence to contain 1000 digits?
################################################################################

import logging

LOGGER = logging.getLogger(__name__)


def problem0025(_top: int):

    top = 10 ** (_top - 1)
    last1 = 1
    last2 = 1
    counter = 2
    fibo = 0

    while fibo < top:
        fibo = last2 + last1

        LOGGER.debug("Fibonacci(%d) = %d", counter, fibo)

        # next keys:
        last2 = last1
        last1 = fibo
        counter += 1

    LOGGER.info('Problem 0025 result: %i', counter)

    return counter
