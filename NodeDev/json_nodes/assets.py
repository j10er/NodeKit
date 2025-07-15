import bpy
import uuid
import os
from . import file
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
    assets = {
        bpy.types.Object: set(),
        bpy.types.Material: set(),
        bpy.types.Image: set(),
        bpy.types.Collection: set(),
    }

    for node_tree in bpy.data.node_groups:
        for node in node_tree.nodes:
            # Check node inputs for references
            for input in node.inputs:
                if hasattr(input, "default_value"):
                    val = input.default_value
                    for asset_type in assets:
                        if isinstance(val, asset_type):
                            assets[asset_type].add(val)
            # Input nodes may have assets as properties
            for asset_type in assets:
                attribute_name = asset_type.__name__.lower()
                if hasattr(node, attribute_name):
                    asset = getattr(node, attribute_name)
                    if isinstance(asset, asset_type):
                        assets[asset_type].add(asset)
    return assets


def import_all():
    log.debug("Importing assets...")

    assets = file.read_assets()
    col_name = "Node-Assets"
    if col_name not in bpy.data.collections:
        assets_collection = bpy.data.collections.new(col_name)
        bpy.context.scene.collection.children.link(assets_collection)
    else:
        assets_collection = bpy.data.collections[col_name]
    for asset in assets:
        match type(asset).__name__:
            case "Object":
                if asset.name not in assets_collection.objects:
                    assets_collection.objects.link(asset)
            case "Collection":
                if asset.name not in assets_collection.children:
                    assets_collection.children.link(asset)
