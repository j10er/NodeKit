import os
from pathlib import Path
import shutil
import bpy
import json
from pprint import pprint


def get_folder_path():
    blend_path = bpy.data.filepath
    stripped_filepath = Path(blend_path).with_suffix("")
    folder_path = f"{stripped_filepath}_nodes"
    return folder_path


def setup():
    blend_path = bpy.data.filepath
    stripped_filepath = Path(blend_path).with_suffix("")
    folder_path = f"{stripped_filepath}_nodes"
    if not blend_path:
        print("Save the blend file first")
        return

    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(f"{stripped_filepath}_nodes")


def save(group_data):
    json.dump(group_data, open(
        get_folder_path() + "/" + group_data["name"] + ".json", "w"))


def load():
    group_dicts = []
    for file in os.listdir(get_folder_path()):
        if file.endswith(".json"):
            with open(f"{get_folder_path()}/{file}", "r") as f:
                group_dict = json.load(f)
                group_dicts.append(group_dict)
    return group_dicts
