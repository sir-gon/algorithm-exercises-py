# Given by problem:
# https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/

# pylint: disable=too-few-public-methods,duplicate-code
# pyright: reportOptionalMemberAccess=none

from __future__ import annotations


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data: int = node_data
        self.next: SinglyLinkedListNode | None = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data) -> SinglyLinkedList:
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

        return self  # added to allow chained call


# modified from original, this return a string instead of print
def singlyLinkedListToText(node, sep) -> str:
    output: str = ''

    while node:
        output = output + str(node.data)

        node = node.next

        if node:
            output = output + sep

    return output
