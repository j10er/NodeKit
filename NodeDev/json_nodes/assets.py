import bpy
import uuid
import os
from . import file
from .file import mapping
import logging

log = logging.getLogger(__name__)


def export_all():
    log.debug("Preparing assets for export...")
    assets = collect_assets()
    for asset_type in assets:
        for asset in assets[asset_type]:
            if not hasattr(asset, "uuid"):
                asset["uuid"] = str(uuid.uuid4())
    log.debug(f"Found {len(assets)} assets to export.")

    file.write_assets(assets)


def collect_assets():
    assets = {asset_type: set() for asset_type in mapping}

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


def import_all():
    clear_assets()
    assets = file.read_assets()
    col_name = "Node-Assets"
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


def clear_assets():

    for data_col_name in mapping.values():
        for data_block in getattr(bpy.data, data_col_name):
            if data_block.get("uuid", False):
                log.debug(
                    f"Removing data block {data_block.name} with uuid {data_block['uuid']}"
                )
                getattr(bpy.data, data_col_name).remove(data_block, do_unlink=True)
