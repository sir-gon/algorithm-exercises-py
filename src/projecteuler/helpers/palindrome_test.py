import unittest
from .palindrome import isPalindrome


class TestPalindromes(unittest.TestCase):

    def test_is_palindrome(self):

        self.assertTrue(isPalindrome(0))
        self.assertTrue(isPalindrome(7))
        self.assertTrue(isPalindrome(101))
        self.assertTrue(isPalindrome(9889))

    def test_is_not_palindrome(self):

        self.assertFalse(isPalindrome(13), False)
        self.assertFalse(isPalindrome(29), False)
        self.assertFalse(isPalindrome(123), False)
        self.assertFalse(isPalindrome(534), False)
