from __future__ import annotations
import logging

LOGGER = logging.getLogger(__name__)


class NaturalNumber:

    # pylint: disable=too-many-instance-attributes
    # Eight is reasonable in this case.

    num = 0
    prime = None

    __initialized = None
    __prime_factor = 1
    __divisor = 1
    __prime_factors = None

    __cycles_of_divisors = 0
    __cycles_of_prime_factor = 0
    __cycles_of_prime_factors = 0

    def __init__(self, num: int):
        self.num = num

    def get_value(self):
        return self.num

    def get_divisors_cycles(self):
        return self.__cycles_of_divisors

    def get_prime_cycles(self):
        return self.__cycles_of_prime_factor

    def get_prime_factors_cycles(self):
        return self.__cycles_of_prime_factors

    def divisors(self) -> list:
        target = abs(self.num)
        top = target
        divs = []

        if top == 1:
            divs.append(1)
            return divs

        LOGGER.debug("Find divisors of %s", top)

        # fast divisors finding loop
        i = 1
        while i <= top:
            if 0 == target % i:
                divs.append(i)
                divs.append(int(target / i))

            i += 1
            top = int(target / i)

        self.__cycles_of_divisors = i
        LOGGER.debug("collected divisors %s in %d cycles", divs, i)

        divs.sort()
        LOGGER.debug("sorted divisors %s", divs)

        if len(divs) == 2:
            self.prime = True
        else:
            self.prime = False

        return divs

    def divisors_unique(self) -> list:
        divs = self.divisors()
        divs = [*set(divs)]
        divs.sort()

        LOGGER.debug("unique divisors %s", divs)

        return divs

    def get_divisor(self) -> int:
        if self.__initialized is None:
            self.__calculate_next_prime_factor()
        return self.__divisor

    def get_prime_factor(self) -> int:
        if self.__initialized is None:
            self.__calculate_next_prime_factor()
        return self.__prime_factor

    def get_prime_factor_cycles(self) -> int:
        if self.__cycles_of_prime_factor == 0:
            self.__calculate_next_prime_factor()

        return self.__cycles_of_prime_factor

    def is_prime(self) -> bool:

        if self.prime is not None:
            return self.prime

        prime_factor = self.__calculate_next_prime_factor().get_prime_factor()

        self.prime = self.num != 1 and prime_factor == self.num

        return self.prime

    def __calculate_next_prime_factor(self) -> NaturalNumber:
        self.__initialized = True
        top = abs(self.num)

        if top == 1:
            self.__prime_factor = 1
            self.__divisor = 1
            self.__cycles_of_prime_factor = 0
            return self

        i = 2
        while i < top:
            if 0 == top % i:
                self.__prime_factor = i
                self.__divisor = int(top / i)
                self.__cycles_of_prime_factor = i - 1
                return self
            i += 1

        self.__prime_factor = i
        self.__divisor = int(top / i)
        self.__cycles_of_prime_factor = i - 1
        return self

    def prime_factors(self) -> list:
        self.__initialized = True

        if self.__prime_factors is not None:
            return self.__prime_factors

        target = abs(self.num)

        factors = []
        self.__cycles_of_prime_factors = 0

        if target == 1:
            self.__prime_factors = [1]
            return self.__prime_factors

        divisor = target
        while divisor != 1:
            rest = NaturalNumber(divisor)
            partial = rest.get_prime_factor()
            divisor = rest.get_divisor()

            factors.append(partial)
            self.__cycles_of_prime_factors += rest.get_prime_factor_cycles()

        self.__prime_factors = factors

        return factors
