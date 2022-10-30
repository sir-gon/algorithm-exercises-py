###############################################################################
# Special Pythagorean triplet
#
# https://projecteuler.net/problem=9
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a² + b² = c²
# For example, 3² + 4² = 9 + 16 = 25 = 5².
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
###############################################################################


import logging

from tomlkit import integer

LOGGER = logging.getLogger(__name__)

class Triplet:

    n_a = None
    n_b = None
    n_c = None

    def __init__(self, _a: integer, _b: integer, _c: integer):
        self.n_a = _a
        self.n_b = _b
        self.n_c = _c

    def is_pythagorean(self):
        return pow(self.n_a, 2) + pow(self.n_b, 2) == pow(self.n_c, 2)

    def product(self):
        return self.n_a * self.n_b * self.n_c

def problem0009(_limit: int):

    result = 0

    t_a = 1
    t_b = 2
    t_c = _limit - t_b - t_a

    found = None

    LOGGER.info('Problem 0009: %s', result)

    while (t_a < t_b and not found):
        t_b = t_a + 1

        while (t_a < t_b < t_c and not found):

            LOGGER.debug("TESTING: a = {%i} b = {%i} c = {%i}", t_a, t_b, t_c)

            test_triplet = Triplet(t_a, t_b, t_c)

            if test_triplet.is_pythagorean():
                found = test_triplet
                LOGGER.info("FOUND: a = %i, b = %i, c =%i", found.n_a, found.n_b, found.n_c)

            t_b += 1
            t_c = _limit - t_b - t_a

        t_a += 1


    LOGGER.info("FOUND: a = %i, b = %i, c =%i", found.n_a, found.n_b, found.n_c)
    LOGGER.info("PRODUCT: a * b * c = %i ", found.product())

    return found.n_a * found.n_b * found.n_c
