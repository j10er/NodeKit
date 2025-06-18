import bpy

from pprint import pprint
from . import file, data


def export_groups():
    export_group("TestNodes")


def export_group(group_name):
    if group_name not in bpy.data.node_groups:
        print(f"Node group '{group_name}' not found.")
        return
    tree = bpy.data.node_groups.get(group_name)
    tree_data = data.NodeTreeData.from_tree(tree)
    tree_dict = tree_data.to_dict()
    print("=" * 20)
    pprint(tree_dict)
    file.save_tree_dict(tree_dict)
