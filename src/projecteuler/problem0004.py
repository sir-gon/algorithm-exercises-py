import logging
from .helpers.palindrome import is_palindrome

LOGGER = logging.getLogger(__name__)


def problem0004(_bottom, _top):

    foundi = None
    foundj = None
    found_palindrome = None
    large_found_palindrome = None

    # Find all cases
    cycles = 0
    i = _top
    while i >= _bottom:

        j = i
        while j >= _bottom and (foundj is None or j >= foundj):

            cycles += 1

            if is_palindrome(i * j):

                found_palindrome = i * j
                LOGGER.debug("FOUND %d x %d = %d is Palindrome",
                             i, j, found_palindrome)

                if (large_found_palindrome is None or
                        found_palindrome > large_found_palindrome):
                    foundi = i
                    foundj = j
                    large_found_palindrome = found_palindrome

            j -= 1

        i -= 1

    LOGGER.info("Problem 0004 Largest Palindrome => %s 𝗑 %s = %s in %s cycles",
                str(foundi), str(foundj), str(
                    large_found_palindrome), str(cycles)
                )

    return large_found_palindrome
