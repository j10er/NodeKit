import logging
from pathlib import Path

import bpy

from . import assets
from .. import config
from .data.blend_data import BlendData
from .data.file_data import FileData

log = logging.getLogger(__name__)


def export_to(folder_path_str: str, include_assets: bool) -> str:
    """Export node trees from Blender to JSON files"""
    folder = Path(folder_path_str)
    log.info(f"Exporting all node groups to {folder.resolve()}")

    if include_assets:
        log.info("Exporting assets...")
        assets_dict = assets.export_to(folder)
    else:
        assets_dict = assets.collect_assets()

    status = FileData(folder).write(BlendData(), append=False)
    if status["success"]:
        num_assets = sum(len(assets_set) for assets_set in assets_dict.values())

        return f"Exported {status['total_trees']} ({status['total_trees'] - status['updated_trees']} unchanged) node groups and {num_assets} ({0 if include_assets else num_assets} unchanged) assets to {folder}"
    else:
        return "Export failed. Please check the console for errors."


def import_from(folder_path_str: str, append: bool, include_assets: bool) -> str:
    """Import node trees from JSON files to Blender"""
    folder = Path(folder_path_str)
    log.info(f"Importing all node groups from {folder}")

    # Handle assets
    if include_assets:
        log.info("Importing assets...")
        error, assets_dict = assets.import_from(folder, append=append)
        if error:
            return error

    status = BlendData().write(FileData(folder), append=append)
    num_assets = sum(len(assets_set) for assets_set in assets_dict.values())
    if status["success"]:
        return f"Imported {status['total_trees']} ({status['total_trees'] - status['updated_trees']} unchanged) node groups and {num_assets} ({0 if include_assets else num_assets} unchanged) assets from {folder.resolve()}"
    else:
        return "Import failed. Please check the console for errors."
