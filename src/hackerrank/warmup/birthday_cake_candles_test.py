import unittest
import pytest
from .birthday_cake_candles import birthday_cake_candles


class TestBirthdayCakeCandles(unittest.TestCase):

    def test_birthday_cake_candles(self):

        tests = [
            {'input': [3, 2, 1, 3], 'answer': 2},
            {'input': [1, 2, 3, 3], 'answer': 2},
        ]

        for _, _tt in enumerate(tests):

            self.assertEqual(
                birthday_cake_candles(_tt['input']), _tt['answer'],
                f"{_} | birthday_cake_candles({_tt['input']}) must be "
                f"=> {_tt['answer']}")

    def test_birthday_cake_candles_wrong_input(self):

        with pytest.raises(Exception):
            birthday_cake_candles([])
