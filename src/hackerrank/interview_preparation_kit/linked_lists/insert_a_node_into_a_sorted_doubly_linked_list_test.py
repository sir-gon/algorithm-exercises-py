import unittest

from .lib.doubly_linked_list import DoublyLinkedList, doubleLinkedListToText
from .insert_a_node_into_a_sorted_doubly_linked_list import sortedInsert


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

            llist = sortedInsert(
                _tt['llist'].head,
                _tt['data'])

            result = doubleLinkedListToText(llist, ' ')

            self.assertEqual(
                result,
                _tt['answer'],
                f"{_} | sortedInsert("
                f"{_tt['llist'].head},"
                f"{_tt['data']},"
                f") must be => {_tt['answer']}")

    def test_sorted_insert_edge_case(self):

        llist = DoublyLinkedList()
        data = 1

        head = sortedInsert(
            llist.head,
            data)

        result = doubleLinkedListToText(head, ' ')

        answer = '1'

        self.assertEqual(
            result,
            answer,
            f"sortedInsert("
            f"{llist},"
            f"{data}"
            f") must be => {answer}")
