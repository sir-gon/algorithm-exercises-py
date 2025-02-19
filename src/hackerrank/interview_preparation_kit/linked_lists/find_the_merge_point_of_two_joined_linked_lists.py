# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/linked_lists/find-the-merge-point-of-two-joined-linked-lists.md]] # noqa: E501
# pylint: enable=line-too-long

from .lib.singly_linked_list import SinglyLinkedListNode


def findMergeNode(
        head1: SinglyLinkedListNode,
        head2: SinglyLinkedListNode) -> int | None:
    llindex: list[SinglyLinkedListNode] = []

    result: int | None = None
    node = head1

    while node:
        llindex.append(node)
        node = node.next

    node = head2
    resume = True
    while node and resume:
        if node in llindex:
            result = node.data
            resume = False

        llindex.append(node)
        node = node.next

    return result
