import logging
import uuid
from pathlib import Path
from typing import Any

import bpy
import shutil
from . import file
from .. import config

log = logging.getLogger(__name__)


def export_to(folder_path: Path) -> None:
    log.debug("Preparing assets for export...")
    assets = collect_assets()

    log.debug(
        f"Found {sum([len(asset_list) for asset_list in assets.values()])} assets to export."
    )

    _write_assets_to(folder_path, assets)
    return assets


def collect_assets() -> dict[str, set[Any]]:
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
    for asset_type in assets:
        for asset in assets[asset_type]:
            if not asset.get("uuid"):
                asset["uuid"] = str(uuid.uuid4())
    return assets


def _write_assets_to(folder_path: Path, assets: dict[str, set[Any]]) -> None:
    assets_folder = folder_path / config.ASSETS_FOLDER
    shutil.rmtree(assets_folder, ignore_errors=True)
    for asset_type in assets:
        asset_type_folder = assets_folder / asset_type
        for asset in assets[asset_type]:
            log.debug(f"Exporting asset {asset.name} of type {asset_type}")
            asset_type_folder.mkdir(parents=True, exist_ok=True)
            asset["name"] = asset.name
            filename = file.make_valid_filename(
                asset["name"], asset["uuid"], ext=".blend"
            )
            asset.name = asset["uuid"]

            log.debug(f"Asset name is {asset['name']} with uuid {asset['uuid']}")
            asset_path = asset_type_folder / filename
            bpy.data.libraries.write(
                str(asset_path),
                set([asset]),
                fake_user=True,
            )
            asset.name = asset["name"]


def import_from(
    folder_path: Path, append: bool = False
) -> tuple[str, dict[str, set[Any]]]:
    assets_path = folder_path / config.ASSETS_FOLDER
    if not assets_path.exists() or not assets_path.is_dir():
        log.info(f"No assets found in {assets_path}, skipping asset import.")
        return "", {}

    uuids = _all_uuids(assets_path)

    # Check for asset conflicts, cancel in append mode, delete all assets in import all mode
    for data_type in config.ASSET_TYPES:
        for data_block in getattr(bpy.data, config.ASSET_TYPES[data_type]):
            if append:
                if data_block.get("uuid", False) in uuids[data_type]:
                    return (
                        f"Asset {data_block.name} with uuid {data_block['uuid']} already exists, cannot append. Remove it in the current file or delete it from the assets folder.",
                        {},
                    )
            else:
                if data_block.get("uuid", False):
                    log.debug(
                        f"Removing asset {data_block.name} with uuid {data_block['uuid']}"
                    )
                    getattr(bpy.data, config.ASSET_TYPES[data_type]).remove(
                        data_block, do_unlink=True
                    )

    # Import the assets
    assets = {asset_type: [] for asset_type in config.ASSET_TYPES}

    for asset_type_dir in assets_path.iterdir():
        if not asset_type_dir.is_dir():
            continue
        asset_type = asset_type_dir.name
        for asset_file in asset_type_dir.iterdir():
            if asset_file.is_file() and asset_file.name.endswith(".blend"):
                log.debug(f"Appending asset from {asset_file}")

                uuid = asset_file.name.split("_")[-1][:-6]
                with bpy.data.libraries.load(str(asset_file), link=False) as (
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
    return "", assets


def _all_uuids(assets_path: Path) -> dict[str, list[str]]:
    uuids = {asset_type: [] for asset_type in config.ASSET_TYPES}
    for asset_type_dir in assets_path.iterdir():
        if not asset_type_dir.is_dir():
            continue
        asset_type = asset_type_dir.name
        for asset_file in asset_type_dir.iterdir():
            if asset_file.is_file() and asset_file.name.endswith(".blend"):
                uuid = asset_file.name.split("_")[-1][:-6]
                uuids[asset_type].append(uuid)
    return uuids
