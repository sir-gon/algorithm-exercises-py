import unittest
from .divisors import divisors


class TestDivisors(unittest.TestCase):

    def test_divisors(self):

        self.assertEqual(divisors(1), [1])
        self.assertEqual(divisors(2), [1, 2])
        self.assertEqual(divisors(10), [1, 2, 5, 10])
        self.assertEqual(divisors(16), [1, 2, 4, 8, 16])

    def test_divisors_large(self):
        self.assertEqual(divisors(6008514751),
        [1, 1747, 3439333, 6008514751])
