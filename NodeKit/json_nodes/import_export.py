import logging
import uuid
from pathlib import Path
from typing import Any

import bpy

from . import assets, file
from .. import config
from .representations.node_tree import NodeTreeData

log = logging.getLogger(__name__)


def export_to(folder_path_str: str, include_assets: bool):
    folder = Path(folder_path_str)
    log.info(f"Exporting all node groups to {folder.resolve()}")
    if include_assets:
        log.info("Exporting assets...")
        assets_dict = assets.export_to(folder)
    else:
        assets_dict = assets.collect_assets()

    blend_data_dicts = _get_blend_data_dicts()

    log.info(f"Found {len(blend_data_dicts)} node groups to export.")
    json_data_dicts = file.read_data_dicts_from(folder)
    export_data_dicts = {
        uuid: data_dict
        for uuid, data_dict in blend_data_dicts.items()
        if json_data_dicts.get(uuid, {}) != data_dict
    }
    file.write_trees_to(folder, export_data_dicts)
    num_of_assets = sum(len(assets_set) for assets_set in assets_dict.values())
    return f"Exported {len(blend_data_dicts)} ({len(blend_data_dicts) - len(export_data_dicts)} unchanged) node groups and {num_of_assets} ({0 if include_assets else num_of_assets} unchanged) assets to {folder}"


def _get_blend_data_dicts() -> dict[str, config.ExportDict]:

    # Prepare all node groups and nodes with needed attributes
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
    data_dicts = {}

    for tree in bpy.data.node_groups:
        if tree.bl_idname not in config.SUPPORTED_TREE_TYPES:
            continue

        tree_data = NodeTreeData.from_tree(tree)
        tree_dict = tree_data.to_dict()

        data_dicts[tree_dict["uuid"]] = {
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
    return data_dicts


def import_from(folder_path_str: str, append: bool, include_assets: bool):
    folder = Path(folder_path_str)
    log.info(f"Importing all node groups from {folder}")

    if include_assets:
        log.info("Importing assets...")
        error = assets.import_from(folder, append=append)
        if error:
            log.info(error)
            return error

    log.info("Reading json files...")
    json_data_dicts = file.read_data_dicts_from(folder)
    log.info(f"Found {len(json_data_dicts)} node groups.")

    blend_data_dicts = _get_blend_data_dicts()

    new_tree_datas = {
        uuid: NodeTreeData.from_dict(export_dict["tree"])
        for uuid, export_dict in json_data_dicts.items()
        if uuid not in blend_data_dicts or export_dict != blend_data_dicts[uuid]
    }
    log.info(f"Of these, {len(new_tree_datas)} have changes.")
    for tree in bpy.data.node_groups:
        uuid = tree.get("uuid")
        if append:
            if uuid in new_tree_datas:
                log.info(f"Tree {tree.name} already exists, skipping.")
                new_tree_datas.pop(uuid)
        else:
            if (
                tree.bl_idname in config.SUPPORTED_TREE_TYPES
                and uuid not in json_data_dicts
            ):
                log.info(f"Removing existing tree: {tree.name}")
                bpy.data.node_groups.remove(tree, do_unlink=True)

    if not new_tree_datas:
        return "No groups imported, all groups are already up to date."

    _create_trees(new_tree_datas)

    return f"Imported {len(json_data_dicts)} node groups, of which {len(json_data_dicts) - len(new_tree_datas)} were unchanged, from {folder}."


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
