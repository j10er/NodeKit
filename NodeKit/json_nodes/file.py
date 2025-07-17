import bpy
import os
import shutil
from typing import Any
import json
import logging
import re
import copy
from bpy.path import abspath
log = logging.getLogger(__name__)


def make_valid_filename(name: str, uuid_str: str, ext: str) -> str:

    safe = re.sub(r'[<>:"/\\|?*\n\r\t ]', "_", name).strip()
    return f"{safe}_{uuid_str}{ext}"


def setup(folder_path: str) -> None:
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)

def write_trees_to(folder_path: str, tree_dicts: list[dict]) -> None:
    for tree_dict in tree_dicts:

        directory = os.path.join(
            folder_path, tree_dict["tree_type"], tree_dict["category"]
        )
        os.makedirs(directory, exist_ok=True)
        filename = make_valid_filename(
            tree_dict["name"], tree_dict["tree"]["uuid"], ".json"
        )
        filepath = os.path.join(directory, filename)
        json.dump(
            tree_dict,
            open(filepath, "w"),
            indent=4,
        )


def read_trees_from(folder_path: str) -> list[dict[str, Any]]:
    data_dicts = []
    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            with open(f"{folder_path}/{file}", "r") as f:
                data_dict = json.load(f)
                data_dicts.append(data_dict)
        if os.path.isdir(f"{folder_path}/{file}"):
            subfolder_data = read_trees_from(f"{folder_path}/{file}")
            data_dicts.extend(subfolder_data)
    return data_dicts





def validate_path(folder_path: str) -> str:
        if not folder_path:
            return "Select a directory to store the JSON files"
        elif not os.path.exists(abspath(folder_path)):
            return "Path does not exist"
        elif not os.path.isdir(abspath(folder_path)):
            return "Path is not a directory"
        elif not directory_is_valid(abspath(folder_path)):
            return "The directory contains other content, must only contain JSON files and directories"
        else:
            return ""

def directory_is_valid(folder_path: str) -> bool:
    """Check recursively if the directory only contains jsons and directories."""
    for file in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, file)):
            if not directory_is_valid(os.path.join(folder_path, file)):
                return False
        elif not (
            file.endswith(".json")
            or file.endswith(".blend")
        ):
            return False

    return True


def number_of_files(folder_path: str, ext: str) -> int:
    counter = 0
    if not bpy.context.scene.node_kit.directory_error:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(ext):
                    counter += 1
    return counter


def folder_is_empty(folder_path: str) -> bool:
    return len(os.listdir(folder_path)) == 0