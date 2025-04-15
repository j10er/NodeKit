import bpy

from .data import NodeTreeData, node_tree_to_dict
from . import file


def export_groups():
    file.setup()
    groups = bpy.data.node_groups
    for group in groups:
        group_data = node_tree_to_dict(group)  # NodeTreeData(group)
        print("Exporting", group_data["name"])
        file.save(group_data)
