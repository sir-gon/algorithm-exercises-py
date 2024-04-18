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
        root: Node,
        collect: Dict[int, list[Node]],
        level: int
) -> None:
    if level not in collect:
        collect[level] = [root]
    else:
        collect[level].append(root)


def callback_collect_plain(
        root: Node,
        collect: Dict[int, list[Node]],
        level: int
) -> None:

    _level = 0 * level  # set a unique key to use dict as a list

    if _level not in collect:
        collect[_level] = [root]
    else:
        collect[_level].append(root)


def traverse_in_order_collector(
            root: Node,
            collect: Dict[int, list[Node]],
            level: int,
            callback: Callable[[Node, Dict[int, list[Node]], int], None]
        ) -> Dict[int, list[Node]]:

    if root.left is not None:
        traverse_in_order_collector(root.left, collect, level + 1, callback)

    callback(root, collect, level)

    if root.right is not None:
        traverse_in_order_collector(root.right, collect, level + 1, callback)

    return collect


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

        for i in range(0, min(len(indexes), len(node_collector[last_level]))):
            current_node: Node = node_collector[last_level][i]
            new_element: List[int] = indexes.pop(0)

            if new_element[0] != -1:
                current_node.left = Node(new_element[0])
            if new_element[1] != -1:
                current_node.right = Node(new_element[1])

    return root


def plain_tree(root: Node) -> List[int]:
    node_collector: Dict[int, list[Node]] = {}

    node_collector = traverse_in_order_collector(
        root,
        node_collector,
        __INITIAL_LEVEL__,
        callback_collect_plain
    )

    output: List[int] = []

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

    LOGGER.debug('Plain tree: %s', plain)

    for query in queries:
        for level, node_list in node_collector.items():
            if level % query == 0:
                for x in node_list:
                    swap_branch(x)

        plain = plain_tree(tree)
        output.append(plain)

    return output
