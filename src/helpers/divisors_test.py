import unittest
from .divisors import divisors
from .divisors import divisors_unique
from .divisors import factor_find
from .divisors import prime_factors


class TestDivisors(unittest.TestCase):

    def test_divisors(self):
        self.assertEqual(divisors(1), [1])
        self.assertEqual(divisors(2), [1, 2])
        self.assertEqual(divisors(9), [1, 3, 3, 9])
        self.assertEqual(divisors(16), [1, 2, 4, 4, 8, 16])

    def test_divisors_unique(self):

        self.assertEqual(divisors_unique(1), [1])
        self.assertEqual(divisors_unique(2), [1, 2])
        self.assertEqual(divisors_unique(10), [1, 2, 5, 10])
        self.assertEqual(divisors_unique(16), [1, 2, 4, 8, 16])

    def test_divisors_unique_large(self):
        self.assertEqual(divisors_unique(6008514751),
        [1, 1747, 3439333, 6008514751])

    def test_factor_find(self):
        self.assertEqual(factor_find(1), { 'factor': 1, 'carry': 1, 'cycles': 1})
        self.assertEqual(factor_find(2), { 'factor': 2, 'carry': 1, 'cycles': 2})
        self.assertEqual(factor_find(4), { 'factor': 2, 'carry': 2, 'cycles': 2})

    def test_prime_factors(self):

        self.assertEqual(prime_factors(1), [1])
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(6), [2, 3])
        self.assertEqual(prime_factors(12), [2, 2, 3])
        self.assertEqual(prime_factors(120), [2, 2, 2, 3, 5])
