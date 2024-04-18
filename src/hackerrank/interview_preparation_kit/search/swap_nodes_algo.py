# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/search/swap-nodes-algo.md]] # noqa
# pylint: enable=line-too-long

import logging
from typing import Dict, List, Callable
from ...lib.node import Node

LOGGER = logging.getLogger(__name__)

__INITIAL_LEVEL__: int = 1
__ROOT_VALUE__: int = 1


def callback_collect_nodes(
        root: Node | None,
        collect: Dict[int, list[Node]],
        level: int
) -> None:
    if root is not None:
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


def swap_branch(root: Node | None) -> Node | None:
    if root is not None:
        temp: Node | None = root.left
        root.left = root.right
        root.right = temp

    return root


def swap_nodes(indexes: List[List[int]], queries: List[int]) -> List[List[int]]:
    tree: Node = build_tree(indexes)

    plain: List[int]
    output: List[List[int]] = []

    node_collector: Dict[int, list[Node]] = {}

    traverse_in_order_collector(
        tree,
        node_collector,
        __INITIAL_LEVEL__,
        callback_collect_nodes)

    node_collector = dict(sorted(node_collector.items()))

    plain = plain_tree(tree)  # original

    LOGGER.debug('Triangle: %s', plain)

    for query in queries:
        for level, node_list in node_collector.items():
            if level % query == 0:
                for x in node_list:
                    swap_branch(x)

        plain = plain_tree(tree)
        output.append(plain)

    return output
