import bpy
import uuid
import os
from . import file
import logging

log = logging.getLogger(__name__)


def export():
    log.debug("Preparing assets for export...")
    assets = get_assets_for_export()
    log.debug(f"Found {len(assets)} assets to export.")

    assets_folder = file.get_assets_folder()
    os.makedirs(assets_folder, exist_ok=True)

    for asset_type in assets:
        for asset in assets[asset_type]:
            log.debug(f"Exporting asset: {asset.name}")
            if not hasattr(asset, "uuid"):
                asset["uuid"] = str(uuid.uuid4())
            folder_path = os.path.join(file.get_assets_folder(), asset_type.__name__)
            os.makedirs(folder_path, exist_ok=True)
            asset_path = os.path.join(folder_path, f"{asset.name}.blend")
            bpy.data.libraries.write(
                os.path.join(asset_path),
                set([asset]),
                fake_user=True,
            )


def get_assets_for_export():
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

            for asset_type in assets:
                attribute_name = asset_type.__name__.lower()
                if hasattr(node, attribute_name):
                    asset = getattr(node, attribute_name)
                    if isinstance(asset, asset_type):
                        assets[asset_type].add(asset)
    return assets


asset_type_mapping = {
    "Object": "objects",
    "Material": "materials",
    "Image": "images",
    "Collection": "collections",
}


def import_assets():
    log.debug("Importing assets...")
    assets_folder = file.get_assets_folder()
    for asset_type in os.listdir(assets_folder):
        for asset_file in os.listdir(os.path.join(assets_folder, asset_type)):
            if asset_file.endswith(".blend"):
                asset_path = os.path.join(assets_folder, asset_type, asset_file)
                log.debug(f"Appending asset from {asset_path}")
                with bpy.data.libraries.load(asset_path, link=False) as (
                    data_from,
                    data_to,
                ):
                    asset_name = asset_file[:-6]
                    type_name = asset_type_mapping.get(asset_type, None)
                    setattr(data_to, type_name, [asset_name])
                match asset_type:
                    case "Object":
                        bpy.context.collection.objects.link(
                            bpy.data.objects[asset_name]
                        )
                    case "Collection":
                        bpy.data.collections.new(asset_name)
                        bpy.context.scene.collection.children.link(
                            bpy.data.collections[asset_name]
                        )
