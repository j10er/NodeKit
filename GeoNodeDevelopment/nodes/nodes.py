import bpy

from pprint import pprint
from . import file, data
import uuid


def export_groups():
    setup()
    for tree in bpy.data.node_groups:
        if tree.bl_idname != "GeometryNodeTree":
            continue
        export_tree(tree)


def export_tree(tree):
    tree_data = data.NodeTreeData.from_tree(tree)
    tree_dict = tree_data.to_dict()
    data_dict = {
        "name": tree_dict["name"],
        "tree": tree_dict,
        "blender_version": bpy.app.version_string,
    }
    file.save_tree_dict(data_dict)


def setup():
    file.setup()
    for tree in bpy.data.node_groups:
        if not hasattr(tree, "uuid"):
            tree["uuid"] = str(uuid.uuid4())


def import_groups():

    data_dicts = file.load_all()
    tree_datas = [
        data.NodeTreeData.from_dict(data_dict["tree"]) for data_dict in data_dicts
    ]
    for tree_data in tree_datas:
        tree_data.create_tree_hull()
    for tree_data in tree_datas:
        tree_data.add_nodes()
