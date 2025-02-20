import unittest
from .plus_minus import plusMinus


class TestPlusMinus(unittest.TestCase):

    def test_plus_minus(self):

        tests = [
            {
                'input': [-4, 3, -9, 0, 4, 1],
                'answer': '\n'.join(['0.500000', '0.333333', '0.166667'])
            }
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                plusMinus(_tt['input']), _tt['answer'],
                f"{_} | plusMinus({_tt['input']}) must be "
                f"=> {_tt['answer']}")
