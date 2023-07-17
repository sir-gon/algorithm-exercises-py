import unittest
from .prime import is_prime


class TestPrimes(unittest.TestCase):

    def test_(self):

        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(7), True)
        self.assertEqual(is_prime(13), True)

    def test_not_prime(self):

        self.assertEqual(is_prime(4), False)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(100), False)
        self.assertEqual(is_prime(3000), False)
