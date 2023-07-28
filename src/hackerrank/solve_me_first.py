import logging

LOGGER = logging.getLogger(__name__)


def solve_me_first(_a, _b):
    result = _a + _b

    LOGGER.info('Solve Me First result: %i', result)
    return result
