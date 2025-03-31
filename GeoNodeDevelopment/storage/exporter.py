import os
import shutil
import bpy
import json
from pprint import pprint
from .data import NodeTreeData
from pathlib import Path
from . import file


def export_groups():
    file.setup()
    groups = bpy.data.node_groups
    for group in groups:
        group_data = NodeTreeData(group)
        print("Exporting", group_data.name)
        file.save(group_data)
