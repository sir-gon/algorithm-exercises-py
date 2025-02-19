# Given by problem:
# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list

# pylint: disable=too-few-public-methods,duplicate-code
# pyright: reportOptionalMemberAccess=none

from __future__ import annotations


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data: int = node_data
        self.next: DoublyLinkedListNode | None = None
        self.prev: DoublyLinkedListNode | None = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
        return self


def doubleLinkedListToText(node, sep):
    output: str = ''

    while node:
        output = output + str(node.data)

        node = node.next

        if node:
            output = output + sep

    return output
