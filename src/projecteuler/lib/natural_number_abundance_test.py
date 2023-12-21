import unittest

from .natural_number_abundance import (
    NaturalNumberAbundance,
    ___DIVISORS_ABUNDANT___,
    ___DIVISORS_DEFICIENT___,
    ___DIVISORS_PERFECT___
)


class TestDivisors(unittest.TestCase):

    def test_abundance(self):

        self.assertEqual(
            NaturalNumberAbundance(10).abundance().value,
            ___DIVISORS_DEFICIENT___,
            f"NaturalNumberAbundance({10}).abundance() must be "
            f"=> {___DIVISORS_DEFICIENT___}"
        )

        self.assertEqual(
            NaturalNumberAbundance(12).abundance().value,
            ___DIVISORS_ABUNDANT___,
            f"NaturalNumberAbundance({12}).abundance() must be "
            f"=> {___DIVISORS_ABUNDANT___}"
        )

        self.assertEqual(
            NaturalNumberAbundance(28).abundance().value,
            ___DIVISORS_PERFECT___,
            f"NaturalNumberAbundance({28}).abundance() must be "
            f"=> {___DIVISORS_PERFECT___}"
        )

    def test_abundance_of_first_12(self):
        for i in range(1, 12):
            self.assertNotEqual(
                NaturalNumberAbundance(i).abundance().value,
                ___DIVISORS_ABUNDANT___,
                f"NaturalNumberAbundance({i}).abundance() must be "
                f"=> {___DIVISORS_ABUNDANT___}"
            )

    def test_abundance_conflict(self):

        self.assertNotEqual(
            NaturalNumberAbundance(110).abundance().value,
            ___DIVISORS_ABUNDANT___,
            f"NaturalNumberAbundance({110}).abundance() must be "
            f"=> {___DIVISORS_ABUNDANT___}"
        )

        self.assertNotEqual(
            NaturalNumberAbundance(18632).abundance().value,
            ___DIVISORS_ABUNDANT___,
            f"NaturalNumberAbundance({18632}).abundance() must be "
            f"=> {___DIVISORS_ABUNDANT___}"
        )
