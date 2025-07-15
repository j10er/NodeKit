import bpy
from typing import Any
from pprint import pprint
from . import file, assets
from .representations.node_tree import NodeTreeData
import uuid

import logging

log = logging.getLogger(__name__)


def export_trees() -> None:
    log.info(f"Exporting all node groups to {file.get_folder_path()}")
    setup()
    assets.export_all()
    tree_dicts = []
    for tree in bpy.data.node_groups:
        if tree.bl_idname != "GeometryNodeTree":
            continue
        tree_data = NodeTreeData.from_tree(tree)
        tree_dict = tree_data.to_dict()
        tree_dicts.append(
            {
                "file_type": "Tree",
                "name": tree_dict["name"],
                "tree": tree_dict,
                "blender_version": bpy.app.version_string,
                "tree_type": tree.bl_idname,
                "category": "Tests" if tree.name.startswith(".test: ") else "Groups",
            }
        )
    file.write_trees(tree_dicts)


def setup() -> None:
    file.setup()
    for tree in bpy.data.node_groups:
        if not hasattr(tree, "uuid"):
            tree["uuid"] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input["index"] = i
            for i, output in enumerate(node.outputs):
                output["index"] = i


def import_groups() -> None:
    log.info(f"Importing all node groups from {file.get_folder_path()}")
    log.info("Importing assets...")
    assets.import_all()
    log.info("Importing reading json files...")
    data_dicts = file.read_trees()
    log.info(f"Found {len(data_dicts)} node groups to import.")

    tree_datas = [NodeTreeData.from_dict(data_dict["tree"]) for data_dict in data_dicts]
    log.info("Creating node trees...")
    for tree_data in tree_datas:
        tree_data.create_tree_hull()
    log.info("Adding nodes to node trees...")
    for tree_data in tree_datas:
        tree_data.add_nodes()
    log.info("Setting socket values")
    for tree_data in tree_datas:
        tree_data.set_socket_attributes()
    log.info("Import completed successfully.")
