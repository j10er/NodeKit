import bpy
import os
import shutil
from typing import Any
import json
import logging
import re
import copy

log = logging.getLogger(__name__)


def make_valid_filename(name: str, uuid_str: str, ext: str) -> str:

    safe = re.sub(r'[<>:"/\\|?*\n\r\t ]', "_", name).strip()
    return f"{safe}_{uuid_str}{ext}"


def get_assets_folder() -> str:
    return os.path.join(
        bpy.path.abspath(bpy.context.scene.gnd_props.folder_path), "Assets"
    )


def get_folder_path() -> str:
    return bpy.path.abspath(bpy.context.scene.gnd_props.folder_path)


def setup() -> None:
    folder_path = get_folder_path()
    if not get_folder_path():
        raise ValueError("JSON folder path is not set.")
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


def write_trees(tree_dicts: list[dict]) -> None:
    for tree_dict in tree_dicts:

        directory = os.path.join(
            get_folder_path(), tree_dict["tree_type"], tree_dict["category"]
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


def read_trees() -> list[dict[str, Any]]:
    return read_trees_from_folder(get_folder_path())


def read_trees_from_folder(folder_path: str) -> list[dict[str, Any]]:
    data_dicts = []
    for file in os.listdir(folder_path):
        if file.endswith(".json"):
            with open(f"{folder_path}/{file}", "r") as f:
                data_dict = json.load(f)
                data_dicts.append(data_dict)
        if os.path.isdir(f"{folder_path}/{file}"):
            subfolder_data = read_trees_from_folder(f"{folder_path}/{file}")
            data_dicts.extend(subfolder_data)
    return data_dicts


def write_assets(assets: dict[str, Any]) -> None:
    assets_folder = get_assets_folder()
    for asset_type in assets:
        folder_path = os.path.join(assets_folder, asset_type)
        for asset in assets[asset_type]:
            os.makedirs(folder_path, exist_ok=True)
            asset["name"] = asset.name
            filename = make_valid_filename(asset["name"], asset["uuid"], ext=".blend")
            asset.name = asset["uuid"]

            log.debug(f"Asset name is {asset['name']} with uuid {asset['uuid']}")
            asset_path = os.path.join(folder_path, filename)
            bpy.data.libraries.write(
                asset_path,
                set([asset]),
                fake_user=True,
            )
            asset.name = asset["name"]


mapping = {
    "Object": "objects",
    "Material": "materials",
    "Image": "images",
    "Collection": "collections",
}


def read_assets() -> list[Any]:

    uuids = {asset_type: [] for asset_type in mapping}
    assets = {asset_type: [] for asset_type in mapping}
    assets_folder = get_assets_folder()
    for asset_type in os.listdir(assets_folder):
        for filename in os.listdir(os.path.join(assets_folder, asset_type)):
            if filename.endswith(".blend"):
                asset_path = os.path.join(assets_folder, asset_type, filename)
                log.debug(f"Appending asset from {asset_path}")

                uuid = filename.split("_")[-1][:-6]
                with bpy.data.libraries.load(asset_path, link=False) as (
                    data_from,
                    data_to,
                ):
                    setattr(data_to, mapping[asset_type], [uuid])

                uuids[asset_type].append(uuid)

    for asset_type in mapping:
        for uuid, element in getattr(bpy.data, mapping[asset_type]).items():
            if element.get("uuid", False) and element["uuid"] in uuids[asset_type]:
                element.name = element["name"]
                print(f"Adding {element.name} to assets")
                assets[asset_type].append(element)
    return assets
