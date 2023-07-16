import unittest
from .minmax import minimum, maximum


class TestMinMax(unittest.TestCase):

    def test_minimum(self):

        self.assertEqual(minimum(1, 99), 1)
        self.assertEqual(minimum(99, 1), 1)

    def test_maximum(self):

        self.assertEqual(maximum(1, 99), 99)
        self.assertEqual(maximum(99, 1), 99)
