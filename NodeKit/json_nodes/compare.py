import logging

import bpy

from .. import config
from .representations.node_tree import NodeTreeData

log = logging.getLogger(__name__)


def compare_dicts(dict1: dict, dict2: dict) -> bool:
    values1 = set(dict1.items())
    values2 = set(dict2.items())
    difference = values1.symmetric_difference(values2)
    for key, value in difference:
        log.warning(f"Difference found in key '{key}': {value}")
    return not difference
