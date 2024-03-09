import unittest

from .ctci_ransom_note import check_magazine

TEST_CASES = [
    {
        'title': 'Sample Test Case 0',
        'magazine': ['give', 'me', 'one', 'grand', 'today', 'night'],
        'note': ['give', 'one', 'grand', 'today'],
        'answer': 'Yes'
    },
    {
        'title': 'Sample Test Case 1',
        'magazine': ['two', 'times', 'three', 'is', 'not', 'four'],
        'note': ['two', 'times', 'two', 'is', 'four'],
        'answer': 'No'
    },
    {
        'title': 'Sample Test',
        'magazine': ['two', 'two', 'times', 'three', 'is', 'not', 'four'],
        'note': ['two', 'times', 'two', 'is', 'four'],
        'answer': 'Yes'
    }
]


class TestSherlockAndAnagrams(unittest.TestCase):

    def test_sherlock_and_anagrams(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                check_magazine(_tt['magazine'], _tt['note']), _tt['answer'],
                f"{_} | sherlock_and_anagrams({_tt['magazine']}, {_tt['note']}) must be "
                f"=> {_tt['answer']}")
