from .singly_linked_list import SinglyLinkedListNode


def insert_node_at_position(llist: SinglyLinkedListNode | None, data: int, position: int):

    new_node = SinglyLinkedListNode(data)

    if position == 0:
        new_node.next = llist
        return new_node

    counter = -1
    node = llist
    while node and counter < position:
        counter += 1

        if counter == position - 1:
            new_node.next = node.next
            node.next = new_node

        node = node.next

    return llist
