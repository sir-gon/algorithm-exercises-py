import logging

LOGGER = logging.getLogger(__name__)

def divisors(target):
    top = abs(target)
    divs = []

    if target == 1:
        divs.append(1)
        return divs

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

    divs.sort()
    LOGGER.debug("sorted divisors %s", divs)

    return divs

def divisors_unique(target):
    divs = divisors(target)
    divs = [*set(divs)]
    divs.sort()

    LOGGER.debug("unique divisors %s", divs)

    return divs

def factor_find(_target):
    top = abs(_target)
    cycles = 1

    if top == 1:
        return {
          'factor': 1,
          'carry': 1,
          'cycles': cycles
        }

    i = 2
    while i <= top:
        cycles += 1
        if 0 == top % i:
            return {
              'factor': i,
              'carry': int(top / i),
              'cycles': cycles
            }
        i += 1

def prime_factors(target):
    factors = []
    cycles = 0

    if target == 1:
        return {'factors': [1], 'cycles': 1}

    factor = target
    while factor != 1:
        partial = factor_find(factor)
        cycles += partial['cycles']

        factors.append(partial['factor'])
        factor = partial['carry']

    return {'factors': factors, 'cycles': cycles}
