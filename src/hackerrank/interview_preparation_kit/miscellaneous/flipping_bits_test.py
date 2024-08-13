import unittest
from pathlib import Path

from ....hackerrank.lib.loader import load_test_cases
from .flipping_bits import flipping_bits

FILE_PATH = str(Path(__file__).resolve().parent)

TEST_CASES = load_test_cases(
    FILE_PATH + '/flipping_bits.testcases.json')


class TestFlippingBits(unittest.TestCase):

    def test_flipping_bits(self):

        for _, testset in enumerate(TEST_CASES):

            for _, _tt in enumerate(testset['tests']):

                self.assertEqual(
                    flipping_bits(_tt['input']), _tt['answer'],
                    f"{_} | flipping_bits({_tt['input']}) must be "
                    f"=> {_tt['answer']}")
