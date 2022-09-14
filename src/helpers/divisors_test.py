import unittest
from .divisors import divisors
from .divisors import divisors_unique
from .divisors import next_prime_factor
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

    def test_next_prime_factor(self):
        self.assertEqual(next_prime_factor(1), { 'factor': 1, 'carry': 1, 'cycles': 0})
        self.assertEqual(next_prime_factor(2), { 'factor': 2, 'carry': 1, 'cycles': 1})
        self.assertEqual(next_prime_factor(4), { 'factor': 2, 'carry': 2, 'cycles': 1})
        self.assertEqual(next_prime_factor(9), { 'factor': 3, 'carry': 3, 'cycles': 2})
        self.assertEqual(next_prime_factor(7), { 'factor': 7, 'carry': 1, 'cycles': 6})

    def test_prime_factors(self):

        self.assertEqual(prime_factors(1), {'factors': [1], 'cycles': 1})
        self.assertEqual(prime_factors(2), {'factors': [2], 'cycles': 2})
        self.assertEqual(prime_factors(6), {'factors': [2, 3], 'cycles': 5})
        self.assertEqual(prime_factors(12), {'factors': [2, 2, 3], 'cycles': 7})
        self.assertEqual(prime_factors(120), {'factors': [2, 2, 2, 3, 5], 'cycles': 14})
