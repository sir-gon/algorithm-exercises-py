import logging
from .lib.binary_node_builder import BinaryNodeBuilder

LOGGER = logging.getLogger(__name__)

ROOT_COORDINATE_I = 0
ROOT_COORDINATE_J = 0
ROOT_VALUE = 0


def problem0018(_triangle):

    leaves = []
    tree = BinaryNodeBuilder[int]().build_binary_node_tree_weigth(
        _triangle,
        ROOT_COORDINATE_I,
        ROOT_COORDINATE_J,
        ROOT_VALUE,
        leaves
    )

    LOGGER.debug('Triangle: %s', tree)
    LOGGER.debug('Leaves count: %d, %s', len(leaves), leaves)

    result = max(leaves)
    return result
