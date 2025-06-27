import bpy
import os
import json

from . import file, data


def import_groups():

    tree_dicts = file.load_all()
    for tree_dict in tree_dicts:
        node_tree_data = data.NodeTreeData.from_dict(tree_dict)
        new_tree = node_tree_data.to_tree()
