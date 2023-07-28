import logging
import math

LOGGER = logging.getLogger(__name__)


def permute(symbols: str, target: int) -> str:
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
