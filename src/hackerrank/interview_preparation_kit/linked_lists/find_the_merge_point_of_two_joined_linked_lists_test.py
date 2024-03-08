import unittest

from .lib.singly_linked_list import SinglyLinkedListNode
from .find_the_merge_point_of_two_joined_linked_lists import find_merge_node

# Test Case 0
#
#  1
#   \
#    2--->3--->NULL
#   /
#  1
#
tc0_ll1_1 = SinglyLinkedListNode(1)
tc0_ll1_2 = SinglyLinkedListNode(2)
tc0_ll1_3 = SinglyLinkedListNode(3)
tc0_ll1_1.next = tc0_ll1_2
tc0_ll1_2.next = tc0_ll1_3

tc0_ll2_1 = SinglyLinkedListNode(1)
tc0_ll2_1.next = tc0_ll1_2

# Test Case 1
#
# 1--->2
#       \
#        3--->Null
#       /
#      1
#
tc1_ll1_1 = SinglyLinkedListNode(1)
tc1_ll1_2 = SinglyLinkedListNode(2)
tc1_ll1_3 = SinglyLinkedListNode(3)
tc1_ll1_1.next = tc1_ll1_2
tc1_ll1_2.next = tc1_ll1_3

tc1_ll2_1 = SinglyLinkedListNode(1)
tc1_ll2_1.next = tc1_ll1_3

TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'llist1': tc0_ll1_1,
        'llist2': tc0_ll2_1,
        'answer': 2
    },
    {
        'title': 'Sample Test case 1',
        'llist1': tc1_ll1_1,
        'llist2': tc1_ll2_1,
        'answer': 3
    },
]


class TestHasCycle(unittest.TestCase):

    def test_find_merge_node(self):

        for _, _tt in enumerate(TEST_CASES):

            self.assertEqual(
                find_merge_node(_tt['llist1'], _tt['llist2']),
                _tt['answer'],
                f"{_} | find_merge_node("
                f"{_tt['llist1']}, {_tt['llist2']})"
                f") must be => {_tt['answer']}")
