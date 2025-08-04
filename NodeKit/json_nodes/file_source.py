"""Data source for JSON files on disk"""

from pathlib import Path
from typing import Dict

import bpy

from .data_source import DataSource
from .representations.node_tree import NodeTreeData
from . import file
from .. import config


class FileDataSource(DataSource):
    """Data source for JSON files on disk"""

    def __init__(self, folder_path: Path):
        self.folder_path = folder_path

    def get_tree_data(self) -> Dict[str, NodeTreeData]:
        """Get NodeTreeData from JSON files"""
        data_dicts = self.get_data_dicts()
        return {
            uuid: NodeTreeData.from_dict(export_dict["tree"])
            for uuid, export_dict in data_dicts.items()
        }

    def get_data_dicts(self) -> Dict[str, config.ExportDict]:
        """Read data dictionaries from JSON files"""
        return file.read_data_dicts_from(self.folder_path)

    def write_data(self, tree_data: Dict[str, NodeTreeData]) -> None:
        """Write NodeTreeData to JSON files"""
        data_dicts = {
            uuid: {
                "name": tree_data_item.name,
                "tree": tree_data_item.to_dict(),
                "blender_version": bpy.app.version_string,
                "tree_type": tree_data_item.bl_idname,
                "category": (
                    config.CATEGORY_TESTS
                    if tree_data_item.name.startswith(config.TEST_PREFIX)
                    else config.CATEGORY_GROUPS
                ),
            }
            for uuid, tree_data_item in tree_data.items()
        }
        file.write_data_dicts_to(self.folder_path, data_dicts)
