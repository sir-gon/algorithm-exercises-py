# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/linked_lists/ctci_linked_list_cycle.md]] # noqa: E501
# pylint: enable=line-too-long

from .lib.singly_linked_list import SinglyLinkedListNode


def has_cycle(head: SinglyLinkedListNode) -> bool:
    llindex: list[SinglyLinkedListNode] = []

    node: SinglyLinkedListNode | None = head

    while node is not None:
        if node in llindex:
            return True

        llindex.append(node)
        node = node.next

    return False
