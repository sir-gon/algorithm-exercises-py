import unittest

from .lib.singly_linked_list import SinglyLinkedList, singlyLinkedListToText
from .insert_a_node_at_a_specific_position_in_a_linked_list import insertNodeAtPosition


TEST_CASES = [
    {
        'title': 'Sample Test case 0',
        'llist': SinglyLinkedList()
        .insert_node(16)
        .insert_node(13)
        .insert_node(7),
        'data': 1,
        'position': 2,
        'answer': '16 13 1 7'
    }
]


class TestInsertNodeAtPosition(unittest.TestCase):

    def test_insert_node_at_position(self):

        for _, _tt in enumerate(TEST_CASES):

            insertNodeAtPosition(
                _tt['llist'].head,
                _tt['data'],
                _tt['position'])

            result = singlyLinkedListToText(_tt['llist'].head, ' ')

            self.assertEqual(
                result,
                _tt['answer'],
                f"{_} | insertNodeAtPosition("
                f"{_tt['llist'].head},"
                f"{_tt['data']},"
                f"{_tt['position']},"
                f") must be => {_tt['answer']}")

    def test_insert_node_at_position_edge_case(self):

        llist = SinglyLinkedList().insert_node(1)
        data = 2
        position = 0

        head = insertNodeAtPosition(
            llist.head,
            data,
            position)

        result = singlyLinkedListToText(head, ' ')

        answer = '2 1'

        self.assertEqual(
            result,
            answer,
            f"insertNodeAtPosition("
            f"{llist},"
            f"{data},"
            f"{position},"
            f") must be => {answer}")
