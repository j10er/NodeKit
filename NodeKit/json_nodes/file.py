import json
import logging
import re
from pathlib import Path
from typing import Any, get_type_hints

import bpy
from bpy.path import abspath

from .. import config

log = logging.getLogger(__name__)


def make_valid_filename(name: str, uuid_str: str, ext: str) -> str:

    safe_name = re.sub(
        config.INVALID_FILENAME_CHARS, config.FILENAME_REPLACEMENT_CHAR, name
    ).strip()
    return f"{safe_name}_{uuid_str}{ext}"


def _file_path_for(folder_path: Path, data_dict: dict[str, Any]) -> Path:
    return (
        folder_path
        / data_dict["tree_type"]
        / data_dict["category"]
        / make_valid_filename(data_dict["name"], data_dict["tree"]["uuid"], ".json")
    )


def write_trees_to(folder_path: Path, data_dicts: dict[str, config.ExportDict]) -> None:

    # Write all data_dicts that have changes
    for data_dict in data_dicts.values():

        file_path = _file_path_for(folder_path, data_dict)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with file_path.open("w") as f:
            json.dump(
                data_dict,
                f,
                indent=4,
            )

    # Clean up empty folders
    for root in folder_path.rglob("*/"):
        if root.is_dir() and not any(root.iterdir()):
            root.rmdir()


def remove_unreferenced_jsons(folder_path: Path, uuids: list[str]) -> None:
    for file in folder_path.rglob("*.json"):
        with file.open("r") as f:
            data_dict = json.load(f)
        if data_dict["tree"]["uuid"] not in uuids:
            log.info(f"Removing unreferenced JSON file: {file}")
            file.unlink()
        if (
            file.resolve()
            != (folder_path / _file_path_for(folder_path, data_dict)).resolve()
        ):
            log.info(f"Removing JSON file with wrong name: {file.name}")
            file.unlink()


def read_data_dicts_from(folder: Path) -> dict[str, config.ExportDict]:
    data_dicts = {}
    for file in folder.rglob("*.json"):
        with file.open("r") as f:
            data_dict = json.load(f)
        data_dicts[data_dict["tree"]["uuid"]] = data_dict

    return data_dicts


def validate_path(folder_path: str) -> str:
    folder_path_obj = Path(abspath(folder_path))
    try:
        if not folder_path:
            return "Select a directory to store the JSON files"
        elif not folder_path_obj.exists():
            return "Path does not exist"
        elif not folder_path_obj.is_dir():
            return "Path is not a directory"
        else:
            return _check_folder_structure(folder_path_obj)
    except Exception as e:
        log.error(f"Error validating path {folder_path}: {e}")
        return "An internal error occurred while validating the path"


def _check_folder_structure(folder_path: Path) -> str:
    for tree_type in folder_path.iterdir():
        if not tree_type.is_dir():
            continue
        tree_type_name = tree_type.name
        if tree_type_name == config.ASSETS_FOLDER:
            for asset_type in tree_type.iterdir():
                if not asset_type.is_dir():
                    continue
                asset_type_name = asset_type.name
                if asset_type_name not in config.ASSET_TYPES:
                    return f"Unexpected asset type folder '{asset_type_name}' found in '{tree_type_name}'"
                for asset_file in asset_type.iterdir():
                    if asset_file.is_file() and not asset_file.name.endswith(".blend"):
                        return f"Unexpected file '{asset_file.name}' found in '{tree_type_name}:{asset_type_name}'"
        elif tree_type_name not in config.SUPPORTED_TREE_TYPES:
            return f"Unexpected folder '{tree_type_name}' found"
        else:
            for category in tree_type.iterdir():
                if not category.is_dir():
                    continue
                category_name = category.name
                if category_name not in [config.CATEGORY_TESTS, config.CATEGORY_GROUPS]:
                    return f"Unexpected category '{category_name}' found in '{tree_type_name}'"

                for file in category.iterdir():
                    if file.is_file():
                        if not (
                            file.name.endswith(".json") or file.name.endswith(".blend")
                        ):
                            return f"Unexpected file '{file.name}' found in '{tree_type_name}:{category_name}'"
                        elif file.name.endswith(".json"):
                            error_msg = _check_json(file)
                            if error_msg:
                                return f"Invalid JSON structure in file '{file.name}' in '{tree_type_name}:{category_name}'"
    return ""


def number_of_files(folder_path: str, ext: str) -> int:
    counter = 0
    if not bpy.context.scene.node_kit.directory_error:
        folder_path_obj = Path(folder_path)
        for file in folder_path_obj.rglob(f"*{ext}"):
            counter += 1
    return counter


def folder_is_empty(folder_path: str) -> bool:
    folder_path_obj = Path(folder_path)
    return not any(folder_path_obj.iterdir())


def _check_json(file_path: Path) -> str:
    try:
        with file_path.open("r") as file:
            json_dict = json.load(file)
        if not _is_typed_dict(json_dict, config.ExportDict):
            return f"Invalid JSON structure in file {file_path}"
    except json.JSONDecodeError as e:
        return f"Invalid JSON in file {file_path}: {e}"
    return ""


def _is_typed_dict(data: dict, typed_dict_class) -> bool:
    """Validate if a dictionary matches a TypedDict structure"""
    keys = data.keys()
    types = get_type_hints(typed_dict_class)

    if keys != types.keys():
        log.debug(f"Keys mismatch: {keys} != {types.keys()}")
        return False
    for key in keys:
        if not isinstance(data[key], types[key]):
            log.debug(f"Key {key} has wrong type")
            return False
    return True
