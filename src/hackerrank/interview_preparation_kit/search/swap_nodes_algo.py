# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/search/swap-nodes-algo.md]] # noqa
# pylint: enable=line-too-long

from typing import Dict, List, Callable
from ...lib.node import Node

__INITIAL_LEVEL__: int = 1
__ROOT_VALUE__: int = 1


def callback_collect_nodes(
        root: Node | None,
        collect: Dict[int, list[Node]],
        level: int
) -> None:
    if root is not None and root.left is None and root.right is None:
        if level not in collect:
            collect[level] = [root]
        else:
            collect[level].append(root)


def callback_collect_plain(
        root: Node | None,
        collect: Dict[int, list[Node]],
        level: int
) -> None:

    _level = 0 * level  # set a unique key to use dict as a list
    if root is not None:
        if _level not in collect:
            collect[_level] = [root]
        else:
            collect[_level].append(root)


def callback_swap_nodes(
        root: Node | None,
        level: int,
        level_comparing: int

) -> None:
    if root is not None and level % level_comparing == 0:
        temp: Node | None = root.left
        root.left = root.right
        root.right = temp


def traverse_in_order_collector(
            root: Node | None,
            collect: Dict[int, list[Node]],
            level: int,
            callback: Callable[[Node | None, Dict[int, list[Node]], int], None] =
            lambda _, __, ___: None
        ) -> list[int] | None:
    if root is not None:

        traverse_in_order_collector(root.left, collect, level + 1, callback)

        callback(root, collect, level)

        traverse_in_order_collector(root.right, collect,  level + 1, callback)


def traverse_in_order_level_comparator(
            root: Node | None,
            level: int,
            level_comparing: int,
            callback: Callable[[Node | None, int, int], None]
        ) -> list[int] | None:
    if root is not None:

        traverse_in_order_level_comparator(
            root.left,
            level + 1,
            level_comparing,
            callback)

        callback(root, level, level_comparing)

        traverse_in_order_level_comparator(
            root.right,
            level + 1,
            level_comparing,
            callback)


def build_tree(indexes: List[List[int]]) -> Node:

    root: Node = Node(__ROOT_VALUE__)
    node_collector: Dict[int, list[Node]] = {}

    while len(indexes) > 0:
        traverse_in_order_collector(
            root,
            node_collector,
            __INITIAL_LEVEL__,
            callback_collect_nodes)

        last_level: int = list(node_collector)[-1]

        for leaf in node_collector[last_level]:
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


def plain_tree(root: Node) -> List[int]:
    node_collector: Dict[int, list[Node]] = {}

    traverse_in_order_collector(root,
                                node_collector,
                                __INITIAL_LEVEL__,
                                callback_collect_plain
                                )

    output: List[int] = []

    if len(node_collector) > 0:
        last_level: int = list(node_collector)[-1]
        # transform:
        for node in node_collector[last_level]:
            output.append(node.data)

    return output


def swap_nodes(indexes: List[List[int]], queries: List[int]) -> List[List[int]]:
    # Write your code here
    # print(indexes)
    # print('------')
    # print(queries)

    tree: Node = build_tree(indexes)

    plain: List[int]
    output: List[List[int]] = []

    for query in queries:
        traverse_in_order_level_comparator(
            tree,
            __INITIAL_LEVEL__,
            query,
            callback_swap_nodes
        )
        plain = plain_tree(tree)
        output.append(plain)

    return output
