import bpy
import os
import shutil

import json
from pprint import pprint


def make_valid_filename(name: str) -> str:
    invalid_chars = r'<>:"/\|?*.'
    for char in invalid_chars:
        name = name.replace(char, "_")
    return name.strip()


def get_folder_path():
    return bpy.context.scene.gnd_props.json_folder_path


def setup():
    folder_path = get_folder_path()
    if not get_folder_path():
        raise ValueError("JSON folder path is not set.")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


def save_tree_dict(tree_dict: dict):
    filepath = f"{get_folder_path()}/{make_valid_filename(tree_dict['name'])}.json"
    json.dump(
        tree_dict,
        open(filepath, "w"),
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
