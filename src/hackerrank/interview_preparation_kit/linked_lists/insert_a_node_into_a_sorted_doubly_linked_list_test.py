import unittest

from .lib.doubly_linked_list import DoublyLinkedList, double_linked_list_to_text
from .insert_a_node_into_a_sorted_doubly_linked_list import sorted_insert


TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'llist': DoublyLinkedList()
        .insert_node(1)
        .insert_node(2)
        .insert_node(4),
        'data': 3,
        'answer': '1 2 3 4'
    },
    {
        'title': 'Sample Test case 1',
        'llist': DoublyLinkedList()
        .insert_node(2)
        .insert_node(3)
        .insert_node(4),
        'data': 1,
        'answer': '1 2 3 4'
    },
    {
        'title': 'Sample Test case 2',
        'llist': DoublyLinkedList()
        .insert_node(1)
        .insert_node(2)
        .insert_node(3),
        'data': 4,
        'answer': '1 2 3 4'
    }
]


class TestSortedInsert(unittest.TestCase):

    def test_sorted_insert(self):

        for _, _tt in enumerate(TEST_CASES):

            llist = sorted_insert(
                _tt['llist'].head,
                _tt['data'])

            result = double_linked_list_to_text(llist, ' ')

            self.assertEqual(
                result,
                _tt['answer'],
                f"{_} | sorted_insert("
                f"{_tt['llist'].head},"
                f"{_tt['data']},"
                f") must be => {_tt['answer']}")

    def test_sorted_insert_edge_case(self):

        llist = DoublyLinkedList()
        data = 1

        head = sorted_insert(
            llist.head,
            data)

        result = double_linked_list_to_text(head, ' ')

        answer = '1'

        self.assertEqual(
            result,
            answer,
            f"sorted_insert("
            f"{llist},"
            f"{data}"
            f") must be => {answer}")
