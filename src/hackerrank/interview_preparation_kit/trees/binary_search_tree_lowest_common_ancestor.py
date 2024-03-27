# pylint: disable=line-too-long
# @link Problem definition [[docs/hackerrank/interview_preparation_kit/trees/binary-search-tree-lowest-common-ancestor.md]] # noqa
# pylint: enable=line-too-long

from ...lib.tree import Node


def find(node: Node | None, value: int, results: list[Node]) -> list[Node] | None:
    if node is None:
        return []

    if value == node.info:
        results.append(node)
        return results

    if value < node.info and node.left is not None:
        results.append(node)
        return find(node.left, value, results)

    if value > node.info and node.right is not None:
        results.append(node)
        return find(node.right, value, results)

    return None


def lca(root: Node | None, v1: int, v2: int) -> Node | None:

    paths1 = find(root, v1, []) or []
    paths2 = find(root, v2, []) or []

    the_lca: Node | None = None

    for i in range(0, min(len(paths1), len(paths2))):
        if paths1[i].info == paths2[i].info:
            the_lca = paths1[i]

    return the_lca
