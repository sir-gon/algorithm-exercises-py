###############################################################################
# Names scores
#
# https://projecteuler.net/problem=22
#
# Using names.txt https:#projecteuler.net/project/resources/p022_names.txt
# (right click and 'Save Link/Target As...'),
# a 46K text file containing over five-thousand first names,
# begin by sorting it into alphabetical order.
# Then working out the alphabetical value for
# each name, multiply this value by its alphabetical position
# in the list to obtain a name score.
#
# For example, when the list is sorted into
# alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the
# 938th name in the list. So, COLIN would obtain
# a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?
###############################################################################
# See:
#    - src/data/p022_names.txt
#    - src/data/p022_names.json
###############################################################################

import logging
from typing import List

from .helpers.word_score import word_score

LOGGER = logging.getLogger(__name__)


def problem0022(list_of_names: List[str]):

    names = list_of_names.copy()
    names.sort()

    counter = 0
    result = 0

    for name in names:
        counter += 1
        result += counter * word_score(name)

    LOGGER.info('Problem 0022 result: %i', result)
    return result
