import unittest
from .number_to_word import numberToWord


class TestNumberToWord(unittest.TestCase):

    def test_number_to_word_up_to_two_digits(self):

        self.assertEqual(numberToWord(1), 'one')
        self.assertEqual(numberToWord(16), 'sixteen')
        self.assertEqual(numberToWord(20), 'twenty')
        self.assertEqual(numberToWord(30), 'thirty')
        self.assertEqual(numberToWord(64), 'sixty-four')

    def test_number_to_word_up_to_three_digit(self):

        self.assertEqual(numberToWord(301), 'three hundred and one')
        self.assertEqual(numberToWord(348), 'three hundred and forty-eight')
        self.assertEqual(numberToWord(500), 'five hundred')

    def test_number_to_word_border_cases(self):

        self.assertEqual(numberToWord(1000), 'one thousand')

        self.assertRaisesRegex(AttributeError,
                               'Invalid value',
                               numberToWord, 9999)
