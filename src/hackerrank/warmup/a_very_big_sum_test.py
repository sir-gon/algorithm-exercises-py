import unittest
from .a_very_big_sum import a_very_big_sum


class TestaVeryBigSum(unittest.TestCase):

    def test_a_very_big_sum(self):

        tests = [
            {
                'input': [1000000001, 1000000002, 1000000003, 1000000004, 1000000005],
                'answer': 5000000015
            }
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                a_very_big_sum(_tt['input']), _tt['answer'],
                f"{_} | a_very_big_sum({_tt['input']}) must be "
                f"=> {_tt['answer']}")
