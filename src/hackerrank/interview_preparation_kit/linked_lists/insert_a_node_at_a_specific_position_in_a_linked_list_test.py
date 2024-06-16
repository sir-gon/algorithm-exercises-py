import unittest

from .lib.singly_linked_list import SinglyLinkedList, singly_linked_list_to_text
from .insert_a_node_at_a_specific_position_in_a_linked_list import insert_node_at_position


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

            insert_node_at_position(
                _tt['llist'].head,
                _tt['data'],
                _tt['position'])

            result = singly_linked_list_to_text(_tt['llist'].head, ' ')

            self.assertEqual(
                result,
                _tt['answer'],
                f"{_} | insert_node_at_position("
                f"{_tt['llist'].head},"
                f"{_tt['data']},"
                f"{_tt['position']},"
                f") must be => {_tt['answer']}")

    def test_insert_node_at_position_edge_case(self):

        llist = SinglyLinkedList().insert_node(1)
        data = 2
        position = 0

        head = insert_node_at_position(
            llist.head,
            data,
            position)

        result = singly_linked_list_to_text(head, ' ')

        answer = '2 1'

        self.assertEqual(
            result,
            answer,
            f"insert_node_at_position("
            f"{llist},"
            f"{data},"
            f"{position},"
            f") must be => {answer}")
