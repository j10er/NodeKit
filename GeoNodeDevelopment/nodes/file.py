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


def save_tree_dict(tree_dict: dict):
    json.dump(
        tree_dict,
        open(get_folder_path() + "/" + tree_dict["name"] + ".json", "w"),
        indent=4,
    )


def load_all() -> list[dict]:
    data_dicts = []
    for file in os.listdir(get_folder_path()):
        if file.endswith(".json"):
            with open(f"{get_folder_path()}/{file}", "r") as f:
                data_dict = json.load(f)
                data_dicts.append(data_dict)
    return data_dicts


def write_json(data: dict, file_path: str):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)
