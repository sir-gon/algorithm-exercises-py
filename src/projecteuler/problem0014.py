###############################################################################
# Longest Collatz sequence
#
# https://projecteuler.net/problem=14
#
#
# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
# Although it has not been proved yet (Collatz Problem), it is thought that all
# starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.
################################################################################

import logging
from .helpers.collatz import collatz

LOGGER = logging.getLogger(__name__)


def problem0014(_bottom=1, _top=10) -> int:
    if _bottom < 1:
        raise ValueError('bottom must be a positive integer')
    if _bottom >= _top:
        raise ValueError('top must be and integer, higher than bottom')

    max_sequence = []

    for starting_number in range(_bottom, _top):
        sequence = []
        sequence.append(starting_number)

        check = True
        current_collatz_sequence_number = starting_number
        while check:
            current_collatz_sequence_number = collatz(current_collatz_sequence_number)
            sequence.append(current_collatz_sequence_number)

            check = current_collatz_sequence_number != 1

        LOGGER.debug('sequence of %d: %s', starting_number, sequence)

        if len(sequence) > len(max_sequence):
            max_sequence = sequence

    LOGGER.debug(
        'Large sequence found: %s has %d elements',
        max_sequence,
        len(max_sequence)
    )

    result = max_sequence.pop(0)
    LOGGER.info('Problem 0014 result: %s', result)
    return result
