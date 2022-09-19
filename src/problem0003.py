###############################################################################
# Largest prime factor
#
# https://projecteuler.net/problem=3
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
###############################################################################

import logging
from .helpers.natural_number import NaturalNumber

LOGGER = logging.getLogger(__name__)


def problem0003(_top):

    number = NaturalNumber(_top)
    divs = number.divisors()
    LOGGER.debug('Divisors of %d: %s', _top, divs)

    # not-unique divisors are always even, then the middle term is:
    middle = int(len(divs) / 2 - 1)

    LOGGER.debug('Middle position of %d: %d | Middle divisor %d',
                 _top, middle, divs[middle])

    # check half divisors, each is Prime? wich is largest?
    max_prime_factor = None

    i = middle

    check = True

    while check:
        test_factor = NaturalNumber(divs[i])
        prime = test_factor.is_prime()

        LOGGER.debug('%d is Prime? %s', divs[i], prime)

        if prime:
            max_prime_factor = divs[i]

        # end of cycle
        i -= 1
        check = i >= 0 and max_prime_factor is None

    LOGGER.info('Problem 0003 result: %d', max_prime_factor)
    return max_prime_factor
