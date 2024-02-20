import os
import unittest

from .cruch_bruteforce import array_manipulation
from .cruch_testcases_test import CRUCH_TEST_CASES

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestCrush(unittest.TestCase):

    @unittest.skipIf(not BRUTEFORCE, "skipping due a is a large BRUTEFORCE test")
    def test_array_manipulation(self):

        for _, _tt in enumerate(CRUCH_TEST_CASES):

            self.assertEqual(
                array_manipulation(_tt['n'], _tt['queries']), _tt['answer'],
                f"{_} | array_manipulation({_tt['n']}, {_tt['queries']}) must be "
                f"=> {_tt['answer']}")
