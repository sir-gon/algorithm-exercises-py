from __future__ import annotations
from enum import Enum

import logging
from .natural_number import (
    NaturalNumber
)

LOGGER = logging.getLogger(__name__)

___DIVISORS_ABUNDANT___ = 'abundant'
___DIVISORS_PERFECT___ = 'perfect'
___DIVISORS_DEFICIENT___ = 'deficient'


class DivisorsAbundance(Enum):
    DIVISORS_ABUNDANT = ___DIVISORS_ABUNDANT___
    DIVISORS_PERFECT = ___DIVISORS_PERFECT___
    DIVISORS_DEFICIENT = ___DIVISORS_DEFICIENT___


class NaturalNumberAbundance(NaturalNumber):

    def abundance(self) -> DivisorsAbundance:
        target = abs(self.num)

        divisors = self.proper_divisors()
        div_sum = sum(divisors)

        if div_sum > target:
            return DivisorsAbundance.DIVISORS_ABUNDANT

        if div_sum < target:
            return DivisorsAbundance.DIVISORS_DEFICIENT

        return DivisorsAbundance.DIVISORS_PERFECT
