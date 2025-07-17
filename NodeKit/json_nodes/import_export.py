import bpy
from typing import Any
from pprint import pprint
from . import file, assets
from .representations.node_tree import NodeTreeData
from .. import config
import uuid

import logging

log = logging.getLogger(__name__)


def _setup(folder_path) -> None:
    file.setup(folder_path)
    for tree in bpy.data.node_groups:
        if not tree.get(config.JSON_KEY_UUID):
            tree[config.JSON_KEY_UUID] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input[config.JSON_KEY_INDEX] = i
            for i, output in enumerate(node.outputs):
                output[config.JSON_KEY_INDEX] = i


def export_to(folder_path: str) -> None:
    log.info(
        f"Exporting {len(bpy.data.node_groups)} node group{'s' if len(bpy.data.node_groups) != 1 else ''} to {folder_path}"
    )
    _setup(folder_path)
    assets.export_to(folder_path)
    data_dicts: list[config.ExportDict] = []
    for tree in bpy.data.node_groups:
        if tree.bl_idname not in config.SUPPORTED_TREE_TYPES:
            continue
        tree_data = NodeTreeData.from_tree(tree)
        tree_dict = tree_data.to_dict()
        data_dicts.append(
            {
                "name": tree_dict["name"],
                "tree": tree_dict,
                "blender_version": bpy.app.version_string,
                "tree_type": tree.bl_idname,
                "category": (
                    config.CATEGORY_TESTS
                    if tree.name.startswith(config.TEST_PREFIX)
                    else config.CATEGORY_GROUPS
                ),
            }
        )
    log.info(f"Writing {len(data_dicts)} node groups to JSON files.")
    file.write_trees_to(folder_path, data_dicts)


def import_from(folder_path: str, append: bool) -> str:
    log.info(f"Importing all node groups from {folder_path}")

    log.info("Importing assets...")
    error = assets.import_from(folder_path, append=append)
    if error:
        log.info(error)
        return error

    log.info("Reading json files...")
    data_dicts = file.read_trees_from(folder_path)
    log.info(f"Found {len(data_dicts)} node groups to import.")
    tree_datas = {
        data_dict[config.JSON_KEY_TREE][config.JSON_KEY_UUID]: NodeTreeData.from_dict(
            data_dict[config.JSON_KEY_TREE]
        )
        for data_dict in data_dicts
    }

    _handle_existing_trees(tree_datas, append)

    _create_trees(tree_datas)
    return f"Imported {len(tree_datas)} node group{'s' if len(tree_datas) != 1 else ''} from {folder_path}."


def _handle_existing_trees(tree_datas: dict[str, NodeTreeData], append: bool) -> str:
    for tree in bpy.data.node_groups:
        if append:
            if tree.get(config.JSON_KEY_UUID) in tree_datas:
                log.info(f"Tree {tree.name} already exists, skipping.")
                tree_datas.pop(tree.get(config.JSON_KEY_UUID))
        else:
            if (
                tree.bl_idname == config.SUPPORTED_TREE_TYPES
                and tree.get(config.JSON_KEY_UUID) not in tree_datas
            ):
                bpy.data.node_groups.remove(tree, do_unlink=True)


def _create_trees(tree_datas: dict[str, NodeTreeData]) -> None:
    if not tree_datas:
        return "No groups imported, all groups already exist."
    log.info("Creating node trees...")
    for tree_data in tree_datas.values():
        tree_data.create_tree_hull()
    log.info("Adding nodes to node trees...")
    for tree_data in tree_datas.values():
        tree_data.add_nodes()
    log.info("Setting socket values")
    for tree_data in tree_datas.values():
        tree_data.set_socket_attributes()
