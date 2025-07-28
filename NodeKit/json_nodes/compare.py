import bpy
from .representations.node_tree import NodeTreeData
from .. import config
import logging

log = logging.getLogger(__name__)


def test_conversion():

    bpy.ops.nodekit.export_json()
    original_trees = {
        tree["uuid"]: NodeTreeData.from_tree(tree)
        for tree in bpy.data.node_groups
        if tree.bl_idname in config.SUPPORTED_TREE_TYPES
    }
    bpy.ops.nodekit.import_json()
    bpy.ops.nodekit.export_json()
    new_trees = {
        tree["uuid"]: NodeTreeData.from_tree(tree)
        for tree in bpy.data.node_groups
        if tree.bl_idname in config.SUPPORTED_TREE_TYPES
    }
    for uuid in original_trees:
        if uuid not in new_trees:
            log.error(f"Tree with UUID {uuid} not found in imported trees")
            log.error(
                f"Tree {original_trees[uuid].name} with UUID {uuid} not found in imported trees"
            )
            continue
        if not original_trees[uuid] == new_trees[uuid]:
            log.error(
                f"Tree {original_trees[uuid].name} with UUID {uuid} does not match after import"
            )
