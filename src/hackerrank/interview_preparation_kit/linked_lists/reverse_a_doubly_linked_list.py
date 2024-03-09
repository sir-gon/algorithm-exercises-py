# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/linked_lists/reverse-a-doubly-linked-list.md]] # noqa: E501
# pylint: enable=line-too-long

import logging
from .lib.doubly_linked_list import DoublyLinkedListNode

LOGGER = logging.getLogger(__name__)


def reverse(llist: DoublyLinkedListNode) -> DoublyLinkedListNode:

    current = llist
    last = None
    while current:
        tnext = current.next

        current.next = None
        current.prev = None

        if last:
            current.next = last
            last.prev = current

        last = current
        llist = current
        current = tnext

    return llist
