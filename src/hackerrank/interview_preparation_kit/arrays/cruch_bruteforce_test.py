import unittest

from .cruch_bruteforce import array_manipulation
from .cruch_testcases_test import CRUCH_SMALL_TEST_CASES


class TestCrushBruteForce(unittest.TestCase):

    def test_array_manipulation(self):

        for _, _tt in enumerate(CRUCH_SMALL_TEST_CASES):

            self.assertEqual(
                array_manipulation(_tt['n'], _tt['queries']), _tt['answer'],
                f"{_} | array_manipulation({_tt['n']}, {_tt['queries']}) must be "
                f"=> {_tt['answer']}")
