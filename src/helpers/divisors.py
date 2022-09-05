import logging

LOGGER = logging.getLogger(__name__)

def divisors(target):
    top = abs(target)
    divs = []

    divs.append(1)
    if target != 1:
        divs.append(target)

    LOGGER.debug("Find divisors of %s", target)

    # fast divisors finding loop
    i = 1
    while i <= top:
        if 0 == target % i:
            divs.append(i)
            divs.append(int(target / i))

        i += 1
        top = int(target / i)

    LOGGER.debug("collected divisors %s", divs)

    divs = list(set(divs))
    LOGGER.debug("unique divisors %s", list(set(divs)))

    divs.sort()
    LOGGER.debug("sorted unique divisors %s", divs)

    return divs
