from typing import Dict, List
from ...lib.node import Node


def traverse_leaves(
        root: Node | None,
        collect: Dict[int, list[Node]],
        level: int = 1) -> list[int] | None:
    if root is not None:

        traverse_leaves(root.left, collect, level + 1)

        if root.left is None and root.right is None:
            if level not in collect:
                collect[level] = [root]
            else:
                collect[level].append(root)

        traverse_leaves(root.right, collect,  level + 1)


def build_tree(indexes: List[List[int]]) -> Node:
    root: Node = Node(1)
    leaves = {}

    while len(indexes) > 0:
        traverse_leaves(root, leaves)

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
