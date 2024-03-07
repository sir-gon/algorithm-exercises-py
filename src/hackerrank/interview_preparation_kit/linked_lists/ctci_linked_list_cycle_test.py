import unittest

from .lib.singly_linked_list import SinglyLinkedListNode
from .ctci_linked_list_cycle import has_cycle

# Linked list sample data:
ll1_1 = SinglyLinkedListNode(1)
ll1_2 = SinglyLinkedListNode(2)
ll1_3 = SinglyLinkedListNode(3)
ll1_4 = SinglyLinkedListNode(4)
ll1_5 = SinglyLinkedListNode(5)
ll1_1.next = ll1_2
ll1_2.next = ll1_3
ll1_3.next = ll1_4
ll1_4.next = ll1_5
ll1_4.next = ll1_3  # <- cycle

ll2_1 = SinglyLinkedListNode(1)
ll2_2 = SinglyLinkedListNode(2)
ll2_3 = SinglyLinkedListNode(3)

ll2_1.next = ll2_2
ll2_2.next = ll2_3


TEST_CASES = [
    {
        'title': 'Sample Test case X',
        'llist': ll1_1,
        'answer': True
    },
    {
        'title': 'Sample Test case Y',
        'llist': ll2_1,
        'answer': False
    },
]


class TestHasCycle(unittest.TestCase):

    def test_has_cycle(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                has_cycle(_tt['llist']),
                _tt['answer'],
                f"{_} | has_cycle("
                f"{_tt['llist']})"
                f") must be => {_tt['answer']}")
