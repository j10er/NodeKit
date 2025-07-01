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


def path_is_valid():
    return os.path.exists(get_folder_path()) and os.path.isdir(get_folder_path())


def setup():
    folder_path = get_folder_path()
    if not get_folder_path():
        raise ValueError("JSON folder path is not set.")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


def save_tree_dict(tree_dict: dict):
    directory = os.path.join(
        get_folder_path(), tree_dict["tree_type"], tree_dict["category"]
    )
    os.makedirs(directory, exist_ok=True)
    filename = f"{make_valid_filename(tree_dict['name'])}.json"
    filepath = os.path.join(directory, filename)
    json.dump(
        tree_dict,
        open(filepath, "w"),
        indent=4,
    )


def load_all() -> list[dict]:
    return load_from_folder(get_folder_path())


def load_from_folder(folder_path: str) -> list[dict]:
    data_dicts = []
    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            with open(f"{folder_path}/{file}", "r") as f:
                data_dict = json.load(f)
                data_dicts.append(data_dict)
        if os.path.isdir(f"{folder_path}/{file}"):
            subfolder_data = load_from_folder(f"{folder_path}/{file}")
            data_dicts.extend(subfolder_data)
    return data_dicts


def write_json(data: dict, file_path: str):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)


def read_json(file_path: str) -> dict:
    with open(file_path, "r") as f:
        return json.load(f)
