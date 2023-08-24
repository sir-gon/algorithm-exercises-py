# @link Problem definition [[docs/projecteuler/problem0009.md]]

import logging

LOGGER = logging.getLogger(__name__)


class Triplet:

    n_a = 0
    n_b = 0
    n_c = 0

    def __init__(self, _a: int, _b: int, _c: int):
        self.n_a = _a
        self.n_b = _b
        self.n_c = _c

    def is_pythagorean(self) -> bool:
        return pow(self.n_a, 2) + pow(self.n_b, 2) == pow(self.n_c, 2)

    def product(self) -> int:
        return self.n_a * self.n_b * self.n_c


def problem0009(_limit: int) -> 'None | int':

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
                LOGGER.info(
                    "FOUND: a = %i, b = %i, c =%i",
                    found.n_a,
                    found.n_b,
                    found.n_c
                )

            t_b += 1
            t_c = _limit - t_b - t_a

        t_a += 1

    if found is not None:

        LOGGER.info("FOUND: a = %i, b = %i, c =%i", found.n_a, found.n_b, found.n_c)
        LOGGER.info("PRODUCT: a * b * c = %i ", found.product())

        return found.n_a * found.n_b * found.n_c

    return None
