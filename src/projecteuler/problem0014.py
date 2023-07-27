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
