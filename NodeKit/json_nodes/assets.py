import bpy
import os
import uuid
import logging
from typing import Any
from . import file
from .. import config

log = logging.getLogger(__name__)


def export_to(folder_path: str) -> None:
    log.debug("Preparing assets for export...")
    assets = _collect_assets()
    for asset_type in assets:
        for asset in assets[asset_type]:
            if not hasattr(asset, config.JSON_KEY_UUID):
                asset[config.JSON_KEY_UUID] = str(uuid.uuid4())
    log.debug(
        f"Found {sum([len(asset_list) for asset_list in assets.values()])} assets to export."
    )

    _write_assets_to(folder_path, assets)


def _collect_assets():
    assets = {asset_type: set() for asset_type in config.ASSET_TYPES}

    for node_tree in bpy.data.node_groups:
        for node in node_tree.nodes:
            # Check node inputs for references
            for input in node.inputs:
                if hasattr(input, "default_value"):
                    val = input.default_value
                    for asset_type in assets:
                        if isinstance(val, getattr(bpy.types, asset_type)):
                            assets[asset_type].add(val)
            # Input nodes may have assets as properties
            for asset_type in assets:
                attribute_name = asset_type.lower()
                if hasattr(node, attribute_name):
                    asset = getattr(node, attribute_name)
                    if isinstance(asset, getattr(bpy.types, asset_type)):
                        assets[asset_type].add(asset)
    return assets


def _write_assets_to(folder_path: str, assets: dict[str, Any]) -> None:
    assets_folder = os.path.join(folder_path, config.ASSETS_FOLDER)
    for asset_type in assets:
        folder_path = os.path.join(assets_folder, asset_type)
        for asset in assets[asset_type]:
            os.makedirs(folder_path, exist_ok=True)
            asset["name"] = asset.name
            filename = file.make_valid_filename(
                asset["name"], asset[config.JSON_KEY_UUID], ext=".blend"
            )
            asset.name = asset[config.JSON_KEY_UUID]

            log.debug(
                f"Asset name is {asset['name']} with uuid {asset[config.JSON_KEY_UUID]}"
            )
            asset_path = os.path.join(folder_path, filename)
            bpy.data.libraries.write(
                asset_path,
                set([asset]),
                fake_user=True,
            )
            asset.name = asset["name"]


def import_from(folder_path: str, append: bool = False) -> str:
    assets_path = os.path.join(folder_path, config.ASSETS_FOLDER)
    if not os.path.exists(assets_path) or not os.path.isdir(assets_path):
        log.info(f"No assets found in {assets_path}, skipping asset import.")
        return ""

    uuids = _all_uuids(assets_path)

    # Check for asset conflicts, cancel in append mode, delete all assets in import all mode
    for data_type in config.ASSET_TYPES:
        for data_block in getattr(bpy.data, config.ASSET_TYPES[data_type]):
            if append:
                if data_block.get(config.JSON_KEY_UUID, False) in uuids[data_type]:
                    return f"Asset {data_block.name} with uuid {data_block[config.JSON_KEY_UUID]} already exists, cannot append. Remove it in the current file or delete it from the assets folder."
            else:
                if data_block.get(config.JSON_KEY_UUID, False):
                    log.debug(
                        f"Removing asset {data_block.name} with uuid {data_block[config.JSON_KEY_UUID]}"
                    )
                    getattr(bpy.data, config.ASSET_TYPES[data_type]).remove(
                        data_block, do_unlink=True
                    )

    # Import the assets
    assets = {asset_type: [] for asset_type in config.ASSET_TYPES}

    for asset_type in os.listdir(assets_path):
        for filename in os.listdir(os.path.join(assets_path, asset_type)):
            if filename.endswith(".blend"):
                asset_path = os.path.join(assets_path, asset_type, filename)
                log.debug(f"Appending asset from {asset_path}")

                uuid = filename.split("_")[-1][:-6]
                with bpy.data.libraries.load(asset_path, link=False) as (
                    data_from,
                    data_to,
                ):
                    setattr(data_to, config.ASSET_TYPES[asset_type], [uuid])
                asset = getattr(bpy.data, config.ASSET_TYPES[asset_type])[uuid]
                asset.name = asset["name"]
                assets[asset_type].append(asset)

    # Link collections and objects to the scene

    if assets["Object"] or assets["Collection"]:
        col_name = config.ASSETS_COLLECTION_NAME
        log.info(f"Linking assets to collection {col_name}")
        if col_name not in bpy.data.collections:
            assets_collection = bpy.data.collections.new(col_name)
            bpy.context.scene.collection.children.link(assets_collection)
        else:
            assets_collection = bpy.data.collections[col_name]

        for obj in assets["Object"]:
            if obj.name not in assets_collection.objects:
                assets_collection.objects.link(obj)

        for col in assets["Collection"]:
            if col.name not in assets_collection.children:
                assets_collection.children.link(col)


def _all_uuids(assets_path: str) -> dict[str, list[str]]:
    uuids = {asset_type: [] for asset_type in config.ASSET_TYPES}
    for asset_type in os.listdir(assets_path):
        for filename in os.listdir(os.path.join(assets_path, asset_type)):
            if filename.endswith(".blend"):
                uuid = filename.split("_")[-1][:-6]
                uuids[asset_type].append(uuid)
    return uuids
