from typing import Dict, List, Callable
from ...lib.node import Node

__INITIAL_LEVEL__: int = 1
__ROOT_VALUE__: int = 1


def callback_collect_nodes(
        root: Node | None,
        collect: Dict[int, list[Node]],
        level: int
):
    if root is not None and root.left is None and root.right is None:
        if level not in collect:
            collect[level] = [root]
        else:
            collect[level].append(root)


def traverse_in_order(
            root: Node | None,
            collect: Dict[int, list[Node]],
            level: int,
            callback: Callable[[Node | None, Dict[int, list[Node]], int], None]
        ) -> list[int] | None:
    if root is not None:

        traverse_in_order(root.left, collect, level + 1, callback)

        callback(root, collect, level)

        traverse_in_order(root.right, collect,  level + 1, callback)


def build_tree(indexes: List[List[int]]) -> Node:

    root: Node = Node(__ROOT_VALUE__)
    leaves = {}

    while len(indexes) > 0:
        traverse_in_order(root, leaves, __INITIAL_LEVEL__, callback_collect_nodes)

        last_level: List[Node] = list(leaves)[-1]

        for leaf in leaves[last_level]:
            if len(indexes) > 0:
                element: List[int] = indexes.pop(0)
                print(element)
                if element[0] != -1:
                    leaf.left = Node(element[0])
                if element[1] != -1:
                    leaf.right = Node(element[1])
            else:
                return root

    return root


def swap_nodes(indexes: List[List[int]], queries: List[int]) -> List[List[int]]:
    # Write your code here
    print(indexes)
    print('------')
    print(queries)

    tree: Node = build_tree(indexes)

    return []
