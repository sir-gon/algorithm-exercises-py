import os
import unittest
from .problem0005 import problem0005

BRUTEFORCE = os.getenv('BRUTEFORCE')
BRUTEFORCE = BRUTEFORCE.upper() == "TRUE" if BRUTEFORCE is not None else False


class TestProblem0005BruteForce(unittest.TestCase):

    @unittest.skipIf(not BRUTEFORCE, "skipping due a is a large BRUTEFORCE test")
    def test_problem0005_full(self):

        solution_found = 232792560
        start_from = 1

        tests = [{
            'input_bottom': 1,
            'input_top': 20,
            'start_from': start_from,
            'answer': solution_found
        }]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                problem0005(
                    _tt['input_bottom'],
                    _tt['input_top'],
                    _tt['start_from']),
                _tt['answer'],
                f"{_} | problem0005({_tt['input_bottom']}, {_tt['input_top']})"
                f" must be => {_tt['answer']}")
