import unittest
from .number_to_word import number_to_word


class TestNumberToWord(unittest.TestCase):

    def test_number_to_word_up_to_two_digits(self):

        self.assertEqual(number_to_word(1), 'one')
        self.assertEqual(number_to_word(16), 'sixteen')
        self.assertEqual(number_to_word(20), 'twenty')
        self.assertEqual(number_to_word(30), 'thirty')
        self.assertEqual(number_to_word(64), 'sixty-four')

    def test_number_to_word_up_to_three_digit(self):

        self.assertEqual(number_to_word(301), 'three hundred and one')
        self.assertEqual(number_to_word(348), 'three hundred and forty-eight')
        self.assertEqual(number_to_word(500), 'five hundred')

    def test_number_to_word_border_cases(self):

        self.assertEqual(number_to_word(1000), 'one thousand')

        self.assertRaisesRegex(AttributeError,
                               'Invalid value',
                               number_to_word, 9999)
