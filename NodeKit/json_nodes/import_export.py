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
        if not tree.get("uuid"):
            tree["uuid"] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input["index"] = i
            for i, output in enumerate(node.outputs):
                output["index"] = i


def export_to(folder_path: str, include_assets: bool):
    log.info(
        f"Exporting {len(bpy.data.node_groups)} node group{'s' if len(bpy.data.node_groups) != 1 else ''} to {folder_path}"
    )
    _setup(folder_path)

    if include_assets:
        log.info("Exporting assets...")
        assets.export_to(folder_path)

    data_dicts: list[config.ExportDict] = []

    # Process each tree
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
    return f"Exported {len(data_dicts)} node group{'s' if len(data_dicts) != 1 else ''} to {folder_path}"


def import_from(folder_path: str, append: bool, include_assets: bool):
    log.info(f"Importing all node groups from {folder_path}")

    if include_assets:
        log.info("Importing assets...")
        error = assets.import_from(folder_path, append=append)
        if error:
            log.info(error)
            return error

    log.info("Reading json files...")
    data_dicts = file.read_trees_from(folder_path)
    log.info(f"Found {len(data_dicts)} node groups to import.")

    tree_datas = {
        data_dict["tree"]["uuid"]: NodeTreeData.from_dict(data_dict["tree"])
        for data_dict in data_dicts
    }

    _setup_existing_trees(tree_datas, append)

    if not tree_datas:
        return "No groups imported, all groups already exist."

    _create_trees(tree_datas)

    return f"Imported {len(tree_datas)} node group{'s' if len(tree_datas) != 1 else ''} from {folder_path}."


def _setup_existing_trees(tree_datas: dict[str, NodeTreeData], append: bool):
    for tree in bpy.data.node_groups:
        if append:
            if tree.get("uuid") in tree_datas:
                log.info(f"Tree {tree.name} already exists, skipping.")
                tree_datas.pop(tree.get("uuid"))
        else:
            if (
                tree.bl_idname == config.SUPPORTED_TREE_TYPES
                and tree.get("uuid") not in tree_datas
            ):
                bpy.data.node_groups.remove(tree, do_unlink=True)


def _create_trees(tree_datas: dict[str, NodeTreeData]):
    log.info("Creating node trees...")
    for tree_data in tree_datas.values():
        tree_data.create_tree_hull()

    log.info("Adding nodes to node trees...")
    for tree_data in tree_datas.values():
        tree_data.add_nodes()

    log.info("Setting socket values")
    for tree_data in tree_datas.values():
        tree_data.set_socket_attributes()
