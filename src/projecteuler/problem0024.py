###############################################################################
# Lexicographic Permutations
#
# https://projecteuler.net/problem=24
#
# A permutation is an ordered arrangement of objects.
# For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
# If all of the permutations are listed numerically or alphabetically,
# we call it lexicographic order.
# The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the
# digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
################################################################################

import logging
import math

LOGGER = logging.getLogger(__name__)


def permute(symbols: str, target: int):
    choices = list(symbols)
    answer = ""
    minimum = 0

    while len(choices) > 0:
        index = 0
        combos = math.factorial(len(choices)-1)
        minimum += combos
        while target > minimum:
            index += 1
            minimum += combos
        answer += choices.pop(index)
        minimum -= combos

    return answer


def problem0024(
    input_elements: str,
    input_permutation_to_find: int
) -> str:

    permutation_found = permute(input_elements, input_permutation_to_find)

    LOGGER.info("Problem 0024 result: %s", permutation_found)
    return permutation_found
