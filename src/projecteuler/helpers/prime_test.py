import unittest
from .prime import isPrime


class TestPrimes(unittest.TestCase):

    def test_(self):

        self.assertFalse(isPrime(1))
        self.assertTrue(isPrime(2))
        self.assertTrue(isPrime(7))
        self.assertTrue(isPrime(13))

    def test_not_prime(self):

        self.assertFalse(isPrime(4))
        self.assertFalse(isPrime(10))
        self.assertFalse(isPrime(100))
        self.assertFalse(isPrime(3000))
