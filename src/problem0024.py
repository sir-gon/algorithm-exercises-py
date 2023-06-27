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
from typing import List

LOGGER = logging.getLogger(__name__)


class Permutations:
    # pylint: disable=too-few-public-methods

    # "inner global variables" to catch the results shared across recursive branch calls.
    current_cycle = 0
    last_branch_collector: List[str] = []

    def lexicographic_permutation_find(
        self, elements: List[str], number_of_permutation_to_find: int
    ) -> List[str]:

        # Initial values
        self.current_cycle = 0
        self.last_branch_collector: List[str] = []
        init_branch_collector: List[str] = []

        def compute_permutations(
            stop_at_cycle: int, input_elements: List[str], branch_collector: List[str]
        ) -> None:
            if self.current_cycle >= stop_at_cycle:
                return

            for i in input_elements:
                root_element = i
                rest_of_elements = []

                for j in input_elements:
                    if i != j:
                        rest_of_elements.append(j)

                new_branch_collector = branch_collector.copy()
                new_branch_collector.append(root_element)

                # finally
                if len(rest_of_elements) > 0:
                    LOGGER.debug('REST: %s', rest_of_elements)

                    compute_permutations(
                        stop_at_cycle,
                        rest_of_elements,
                        new_branch_collector
                    )
                else:
                    self.last_branch_collector = new_branch_collector
                    self.current_cycle += 1

                    LOGGER.debug('FINISH BRANCH: %i -> %s',
                                 self.current_cycle,
                                 rest_of_elements)

            return

        compute_permutations(
            number_of_permutation_to_find,
            elements,
            init_branch_collector)

        return self.last_branch_collector


def problem0024(
    input_elements: List[str],
    input_permutation_to_find: int
) -> List[str]:
    permutation_found = Permutations().lexicographic_permutation_find(
        input_elements,
        input_permutation_to_find
    )

    LOGGER.info("Problem 0024 result: %s", permutation_found)
    return permutation_found
