import unittest

from .lib.doubly_linked_list import DoublyLinkedList, double_linked_list_to_text
from .reverse_a_doubly_linked_list import reverse


TEST_CASES = [
    {
        'title': 'Test case 0',
        'llist': DoublyLinkedList()
        .insert_node(1)
        .insert_node(2)
        .insert_node(3)
        .insert_node(4),
        'answer': '4 3 2 1'
    },
    {
        'title': 'Test case 1',
        'llist': DoublyLinkedList()
        .insert_node(2)
        .insert_node(3)
        .insert_node(4),
        'answer': '4 3 2'
    },
    {
        'title': 'Test case 7',
        'llist': DoublyLinkedList()
        .insert_node(17)
        .insert_node(20)
        .insert_node(23)
        .insert_node(35)
        .insert_node(47),
        'answer': '47 35 23 20 17'
    }
]


class TestDoubleLinkedListReverse(unittest.TestCase):

    def test_reverse(self):

        for _, _tt in enumerate(TEST_CASES):

            llist = reverse(_tt['llist'].head)

            result = double_linked_list_to_text(llist, ' ')

            self.assertEqual(
                result,
                _tt['answer'],
                f"{_} | reverse({_tt['llist'].head},"
                f") must be => {_tt['answer']}")
