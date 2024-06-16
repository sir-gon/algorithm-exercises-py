# pylint: disable=duplicate-code

import os
import unittest
from .problem0010 import problem0010

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestProblem0010BruteForce(unittest.TestCase):

    @unittest.skipIf(not BRUTEFORCE, "skipping due a is a large BRUTEFORCE test")
    def test_problem0010_bruteforce(self):

        tests = [
            {'inputLimit': 2000000, 'answer': 142913828922}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0010(_tt['inputLimit']), _tt['answer'],
                f"{_} | problem0010({_tt['inputLimit']}) must be "
                f"=> {_tt['answer']}")
