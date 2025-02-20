# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/linked_lists/insert-a-node-into-a-sorted-doubly-linked-list.md]] # noqa: E501
# pylint: enable=line-too-long

import logging
from .lib.doubly_linked_list import DoublyLinkedListNode

LOGGER = logging.getLogger(__name__)


def sortedInsert(
        llist: DoublyLinkedListNode | None,
        data: int) -> DoublyLinkedListNode | None:

    new_node = DoublyLinkedListNode(data)
    current = llist

    if llist is None:
        return new_node

    resume = True
    while current and resume:
        LOGGER.debug('Node: %d', current.data)

        if current.data >= new_node.data:
            LOGGER.debug('Stop at: %d', current.data)
            tprev = None

            if current.prev:
                LOGGER.debug('Prev: %d', current.data)

                tprev = current.prev

                current.prev.next = new_node
                new_node.prev = tprev
            else:
                llist = new_node

            new_node.next = current
            current.prev = new_node

            resume = False

        if resume and current.next is None:
            current.next = new_node
            new_node.prev = current
            resume = False

        current = current.next

    return llist
