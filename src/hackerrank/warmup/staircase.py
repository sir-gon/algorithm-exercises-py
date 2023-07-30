import logging

LOGGER = logging.getLogger(__name__)


def staircase(_n: int) -> str:

    result: list[str] = []

    for i in range(1, _n + 1):
        line: str = ''

        for j in range(1, _n + 1):
            if j <= _n - i:
                line += ' '
            else:
                line += '#'

        result.append(line)

    output = '\n'.join(result)
    LOGGER.info('Staircase result: %s', output)

    return output
