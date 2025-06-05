import bpy

from .data import NodeTreeData
from . import file


def export_groups():
    file.setup()
    groups = bpy.data.node_groups
    for group in groups:
        group_data = NodeTreeData(tree=group)
        print("Exporting", group_data["name"])
        file.save(group_data)
