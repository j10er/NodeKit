"""Data source for current Blender scene"""

import uuid
from typing import Dict

import bpy
import logging
from .data_source import DataSource
from ..representations.node_tree import NodeTreeData
from ... import config

log = logging.getLogger(__name__)


class BlendData(DataSource):
    """Data source for current Blender scene"""

    def __init__(self):
        self._setup_node_trees()
        self.tree_datas = self._calculate_tree_datas()
        self.data_dicts = self._calculate_data_dicts()

    def write(self, source: DataSource, append: bool) -> dict:

        source_data_dicts = source.get_data_dicts()
        uuids_to_write = self._uuids_to_write(source_data_dicts)

        tree_datas_to_write = {
            uuid: tree_data
            for uuid, tree_data in source.get_tree_datas().items()
            if uuid in uuids_to_write
        }
        for tree in bpy.data.node_groups:
            uuid = tree.get("uuid")
            if append:
                if uuid in tree_datas_to_write:
                    log.info(f"Tree {tree.name} already exists, skipping.")
                    tree_datas_to_write.pop(uuid)
            else:
                if (
                    tree.bl_idname in config.SUPPORTED_TREE_TYPES
                    and uuid not in uuids_to_write
                ):
                    log.info(f"Removing existing tree: {tree.name}")
                    bpy.data.node_groups.remove(tree, do_unlink=True)

        self._create_trees(tree_datas_to_write)

        return {
            "success": True,
            "total_trees": len(source_data_dicts),
            "updated_trees": len(tree_datas_to_write),
        }

    def _create_trees(self, tree_datas: dict[str, NodeTreeData]):
        log.info("Creating node trees...")
        for tree_data in tree_datas.values():
            tree_data.create_tree_hull()

        log.info("Adding nodes to node trees...")
        for tree_data in tree_datas.values():
            tree_data.add_nodes()

        log.info("Setting socket values")
        for tree_data in tree_datas.values():
            tree_data.set_socket_attributes()

    def _setup_node_trees(self):
        """Prepare all node groups with needed attributes"""
        for tree in bpy.data.node_groups:
            if tree.bl_idname not in config.SUPPORTED_TREE_TYPES:
                continue
            if not tree.get("uuid"):
                tree["uuid"] = str(uuid.uuid4())
            for node in tree.nodes:
                for i, input in enumerate(node.inputs):
                    input["index"] = i
                for i, output in enumerate(node.outputs):
                    output["index"] = i

    def _calculate_tree_datas(self) -> Dict[str, NodeTreeData]:
        """Get NodeTreeData from current Blender scene"""
        return {
            tree.get("uuid"): NodeTreeData.from_tree(tree)
            for tree in bpy.data.node_groups
            if tree.bl_idname in config.SUPPORTED_TREE_TYPES
        }

    def _calculate_data_dicts(self) -> Dict[str, config.ExportDict]:
        """Get export-ready data dictionaries from current Blender scene"""
        return {
            uuid: {
                "name": tree_data_item.name,
                "tree": tree_data_item.to_dict(),
                "blender_version": bpy.app.version_string,
                "tree_type": tree_data_item.bl_idname,
                "category": (
                    config.CATEGORY_TESTS
                    if tree_data_item.name.startswith(config.TEST_PREFIX)
                    else config.CATEGORY_GROUPS
                ),
            }
            for uuid, tree_data_item in self.get_tree_datas().items()
        }

    def _remove_unmanaged_trees(self, json_data_dicts: dict) -> None:
        for tree in bpy.data.node_groups:
            uuid = tree.get("uuid")
            if (
                tree.bl_idname in config.SUPPORTED_TREE_TYPES
                and uuid not in json_data_dicts
            ):
                log.info(f"Removing existing tree: {tree.name}")
                bpy.data.node_groups.remove(tree, do_unlink=True)
