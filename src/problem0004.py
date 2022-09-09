###############################################################################
# Largest palindrome product
#
# https://projecteuler.net/problem=4
#
# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit
# numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
###############################################################################

import logging
from .helpers.palindrome import is_palindrome

LOGGER = logging.getLogger(__name__)


def problem0004(_bottom, _top):

    foundi = None
    foundj = None
    found_palindrome = None
    large_found_palindrome = None

    # Find all cases
    count = 0
    i = _top
    while i >= _bottom:

        j = i
        while j >= _bottom:

            count += 1

            if is_palindrome(i * j):

                found_palindrome = i * j
                LOGGER.debug("FOUND %d x %d = %d is Palindrome", i, j, found_palindrome)

                if large_found_palindrome is None or found_palindrome > large_found_palindrome:
                    foundi = i
                    foundj = j
                    large_found_palindrome = found_palindrome

            j -= 1

        i -= 1

    LOGGER.info("Problem 0004 Largest Palindrome => %s 𝗑 %s = %s in %s cycles",
        str(foundi), str(foundj), str(large_found_palindrome), str(count)
    )

    return large_found_palindrome
