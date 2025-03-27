import os
import shutil
import bpy
import json
from pprint import pprint
from .data import NodeTreeData
from pathlib import Path


def export_groups():
    blend_path = bpy.data.filepath
    if not blend_path:
        print("Save the blend file first")
        return

    stripped_filepath = Path(blend_path).with_suffix("")
    folder_path = f"{stripped_filepath}_nodes"

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(f"{stripped_filepath}_nodes")

    groups = bpy.data.node_groups
    for group in groups:
        group_data = NodeTreeData(group)
        print("Exporting", group_data.name)
        json.dump(group_data.as_dict(), open(
            f"{folder_path}/{group_data.name}.json", "w"))
