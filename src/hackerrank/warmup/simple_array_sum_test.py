import unittest
from .simple_array_sum import simpleArraySum


class TestSimpleArraySum(unittest.TestCase):

    def test_simple_array_sum(self):

        tests = [
            {'input': [1, 2, 3, 4, 10, 11], 'answer': 31}
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                simpleArraySum(_tt['input']), _tt['answer'],
                f"{_} | simpleArraySum({_tt['input']}) must be "
                f"=> {_tt['answer']}")
