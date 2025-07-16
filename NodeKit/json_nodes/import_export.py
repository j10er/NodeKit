import bpy
from typing import Any
from pprint import pprint
from . import file, assets
from .representations.node_tree import NodeTreeData
import uuid

import logging

log = logging.getLogger(__name__)

def setup(folder_path) -> None:
    file.setup(folder_path)
    for tree in bpy.data.node_groups:
        if not tree.get("uuid"):
            tree["uuid"] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input["index"] = i
            for i, output in enumerate(node.outputs):
                output["index"] = i

def export_to(folder_path: str) -> None:
    log.info(f"Exporting {len(bpy.data.node_groups)} node group{'s' if len(bpy.data.node_groups) != 1 else ''} to {folder_path}")
    setup(folder_path)
    assets.export_to(folder_path)
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
    log.info(f"Writing {len(tree_dicts)} node groups to JSON files.")
    file.write_trees_to(folder_path, tree_dicts)





def import_from(folder_path: str, append:bool=False) -> str:
    log.info(f"Importing all node groups from {folder_path}")

    log.info("Importing assets...")
    assets.import_from(folder_path, append=append)

    log.info("Reading json files...")
    data_dicts = file.read_trees_from(folder_path)
    log.info(f"Found {len(data_dicts)} node groups to import.")
    tree_datas = {data_dict["tree"]["uuid"]: NodeTreeData.from_dict(data_dict["tree"]) for data_dict in data_dicts}
    if append:
        log.info("Appending node groups...")
        for tree in bpy.data.node_groups:
            if tree.get("uuid") in tree_datas:
                log.info(f"Tree {tree.name} already exists, skipping.")
                tree_datas.pop(tree.get("uuid"))
    else:
        log.info("Clearing existing node groups, keeping untracked groups...")
        for tree in bpy.data.node_groups:
            if tree.bl_idname == "GeometryNodeTree" and tree.get("uuid") not in tree_datas:
                bpy.data.node_groups.remove(tree, do_unlink=True)

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
    return f"Imported {len(tree_datas)} node group{'s' if len(tree_datas) != 1 else ''} from {folder_path}."
