import unittest

from .cruch_optimized import array_manipulation_optimized
from .cruch_testcases_test import CRUCH_SMALL_TEST_CASES


class TestCrush(unittest.TestCase):

    def test_array_manipulation_optimized(self):

        for _, _tt in enumerate(CRUCH_SMALL_TEST_CASES):

            self.assertEqual(
                array_manipulation_optimized(_tt['n'], _tt['queries']), _tt['answer'],
                f"{_} | array_manipulation_optimized({_tt['n']}, {_tt['queries']}) "
                f"must be => {_tt['answer']}")
