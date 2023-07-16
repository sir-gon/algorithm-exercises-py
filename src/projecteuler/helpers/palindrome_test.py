import unittest
from .palindrome import is_palindrome


class TestPalindromes(unittest.TestCase):

    def test_is_palindrome(self):

        self.assertEqual(is_palindrome(0), True)
        self.assertEqual(is_palindrome(7), True)
        self.assertEqual(is_palindrome(101), True)
        self.assertEqual(is_palindrome(9889), True)

    def test_is_not_palindrome(self):

        self.assertEqual(is_palindrome(13), False)
        self.assertEqual(is_palindrome(29), False)
        self.assertEqual(is_palindrome(123), False)
        self.assertEqual(is_palindrome(534), False)
