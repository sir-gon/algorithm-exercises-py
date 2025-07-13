# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/search/swap-nodes-algo.md]] # noqa
# pylint: enable=line-too-long


import logging
import sys
from typing import Dict, List, Callable
from ...lib.node import Node

LOGGER = logging.getLogger(__name__)

# CONSTANTS
__INITIAL_LEVEL__: int = 1
__ROOT_VALUE__: int = 1
__HIGH_RECURSION_LIMIT__: int = 3000

LOGGER = logging.getLogger(__name__)

# Next line avoid hit python error:
# RecursionError: maximum recursion depth exceeded
sys.setrecursionlimit(__HIGH_RECURSION_LIMIT__)


def callbackCollectNodes(
        root: Node,
        collect: Dict[int, list[Node]],
        level: int
) -> None:
    if level not in collect:
        collect[level] = [root]
    else:
        collect[level].append(root)


def callbackCollectPlain(
        root: Node,
        collect: Dict[int, list[Node]],
        level: int
) -> None:

    _level = 0 * level  # set a unique key to use dict as a list

    if _level not in collect:
        collect[_level] = [root]
    else:
        collect[_level].append(root)


def traverseInOrderCollector(
    root: Node,
    collect: Dict[int, list[Node]],
    level: int,
    callback: Callable[[Node, Dict[int, list[Node]], int], None]
) -> Dict[int, list[Node]]:

    if root.left is not None:
        traverseInOrderCollector(root.left, collect, level + 1, callback)

    callback(root, collect, level)

    if root.right is not None:
        traverseInOrderCollector(root.right, collect, level + 1, callback)

    return collect


def buildTree(indexes: List[List[int]]) -> Node:

    indexes_copy = indexes[:]
    root: Node = Node(__ROOT_VALUE__)
    node_collector: Dict[int, list[Node]]

    while len(indexes_copy) > 0:
        node_collector = {}
        traverseInOrderCollector(
            root,
            node_collector,
            __INITIAL_LEVEL__,
            callbackCollectNodes)

        last_level: int = sorted(node_collector)[-1]

        for i in range(0, min(len(indexes_copy), len(node_collector[last_level]))):
            current_node: Node = node_collector[last_level][i]
            new_element: List[int] = indexes_copy.pop(0)

            if new_element[0] != -1:
                current_node.left = Node(new_element[0])
            if new_element[1] != -1:
                current_node.right = Node(new_element[1])

    return root


def flattenTree(root: Node) -> List[int]:
    node_collector: Dict[int, list[Node]] = {}

    node_collector = traverseInOrderCollector(
        root,
        node_collector,
        __INITIAL_LEVEL__,
        callbackCollectPlain
    )

    output: List[int] = []

    last_level: int = list(node_collector)[-1]
    # transform:
    for node in node_collector[last_level]:
        output.append(node.data)

    return output


def swapBranch(root: Node | None) -> Node | None:
    if root is not None:
        temp: Node | None = root.left
        root.left = root.right
        root.right = temp

    return root


def swapNodes(indexes: List[List[int]], queries: List[int]) -> List[List[int]]:
    tree: Node = buildTree(indexes)

    plain: List[int]
    output: List[List[int]] = []

    node_collector: Dict[int, list[Node]] = {}

    traverseInOrderCollector(
        tree,
        node_collector,
        __INITIAL_LEVEL__,
        callbackCollectNodes)

    node_collector = dict(sorted(node_collector.items()))

    plain = flattenTree(tree)  # original

    LOGGER.debug('Plain tree: %s', plain)

    for query in queries:
        for level, node_list in node_collector.items():
            if level % query == 0:
                for node in node_list:
                    swapBranch(node)

        plain = flattenTree(tree)
        output.append(plain)

    return output
