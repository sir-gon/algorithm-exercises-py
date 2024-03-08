import unittest
from .palindrome import is_palindrome


class TestPalindromes(unittest.TestCase):

    def test_is_palindrome(self):

        self.assertTrue(is_palindrome(0))
        self.assertTrue(is_palindrome(7))
        self.assertTrue(is_palindrome(101))
        self.assertTrue(is_palindrome(9889))

    def test_is_not_palindrome(self):

        self.assertFalse(is_palindrome(13), False)
        self.assertFalse(is_palindrome(29), False)
        self.assertFalse(is_palindrome(123), False)
        self.assertFalse(is_palindrome(534), False)
