# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/linked_lists/ctci_linked_list_cycle.md]] # noqa: E501
# pylint: enable=line-too-long

from .lib.singly_linked_list import SinglyLinkedListNode


def has_cycle(head: SinglyLinkedListNode) -> bool:
    llindex: list[SinglyLinkedListNode] = []

    result = False
    node = head
    resume = True

    while node and resume:
        if node in llindex:
            resume = False
            result = True
            return result

        llindex.append(node)
        node = node.next

    return result
