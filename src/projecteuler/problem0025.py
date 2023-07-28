import logging

LOGGER = logging.getLogger(__name__)


def problem0025(_top: int):

    top = 10 ** (_top - 1)
    last1 = 1
    last2 = 1
    counter = 2
    fibo = 0

    while fibo < top:
        fibo = last2 + last1

        LOGGER.debug("Fibonacci(%d) = %d", counter, fibo)

        # next keys:
        last2 = last1
        last1 = fibo
        counter += 1

    LOGGER.info('Problem 0025 result: %i', counter)

    return counter
