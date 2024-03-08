import unittest
from .prime import is_prime


class TestPrimes(unittest.TestCase):

    def test_(self):

        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(13))

    def test_not_prime(self):

        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(100))
        self.assertFalse(is_prime(3000))
