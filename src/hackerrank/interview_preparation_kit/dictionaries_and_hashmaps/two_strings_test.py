import unittest

from .two_strings import two_strings

TEST_CASES = [
    {
        'title': 'Example 1',
        's1': "and",
        's2': "art",
        'answer': 'Yes'
    },
    {
        'title': 'Example 2',
        's1': "be",
        's2': "cat",
        'answer': 'No'
    },
    {
        'title': 'Sample Test Case 0',
        's1': "hello",
        's2': "world",
        'answer': 'Yes'
    }
]


class TestTwoStrings(unittest.TestCase):

    def test_two_strings(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                two_strings(_tt['s1'], _tt['s2']), _tt['answer'],
                f"{_} | two_strings({_tt['s1']}, {_tt['s2']}) must be "
                f"=> {_tt['answer']} in {_tt['title']}")
