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
