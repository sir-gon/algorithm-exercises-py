import unittest
from .collatz import collatz


class TestCollatz(unittest.TestCase):

    def test_collatz_first(self):

        self.assertEqual(collatz(13), 40)
        self.assertEqual(collatz(40), 20)
        self.assertEqual(collatz(20), 10)
        self.assertEqual(collatz(10), 5)
        self.assertEqual(collatz(5), 16)

    def test_collatz_second(self):

        self.assertEqual(collatz(16), 8)
        self.assertEqual(collatz(8), 4)
        self.assertEqual(collatz(4), 2)
        self.assertEqual(collatz(2), 1)
