"""Data source for JSON files on disk"""

from pathlib import Path
from typing import Dict

import bpy
import json
from .data_source import DataSource
from ..representations.node_tree import NodeTreeData
from .. import file
from ... import config


class FileData(DataSource):
    """Data source for JSON files on disk"""

    def __init__(self, folder: Path):
        self.folder = folder
        self.data_dicts = self._calculate_data_dicts()
        self.tree_datas = self._calculate_tree_datas()

    def _calculate_tree_datas(self) -> Dict[str, NodeTreeData]:
        return {
            uuid: NodeTreeData.from_dict(export_dict["tree"])
            for uuid, export_dict in self.get_data_dicts().items()
        }

    def _calculate_data_dicts(self) -> Dict[str, config.ExportDict]:
        return file.read_data_dicts_from(self.folder)

    def write(self, source: DataSource, append: bool) -> dict:

        source_data_dicts = source.get_data_dicts()
        uuids_to_write = self._uuids_to_write(source_data_dicts)

        data_dicts_to_write = {
            uuid: data_dict
            for uuid, data_dict in source_data_dicts.items()
            if uuid in uuids_to_write
        }
        if not append:
            file.remove_unreferenced_jsons(
                folder=self.folder, uuids=source_data_dicts.keys()
            )
        file.write_data_dicts_to(self.folder, data_dicts_to_write)
        file.remove_empty_folders(self.folder)
        return {
            "success": True,
            "total_trees": len(source_data_dicts),
            "updated_trees": len(uuids_to_write),
        }
