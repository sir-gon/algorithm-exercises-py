###############################################################################
# <TITLE>
#
# https://projecteuler.net/problem=XX
#
# <DESCRIPTION>
#
################################################################################

import re
import logging
from .helpers.number_to_word import number_to_word

LOGGER = logging.getLogger(__name__)


def problem0017(_init: int, _last: int) -> int:

    acum = 0

    for i in range(_init, _last + 1):
        word = number_to_word(i)
        replaced = re.sub(r'[^a-zA-Z]', '', word)

        acum += len(replaced)

        LOGGER.debug('acum: %d => word: %s', acum, word)

    LOGGER.info('Problem 0017 result: %i', acum)
    return acum
