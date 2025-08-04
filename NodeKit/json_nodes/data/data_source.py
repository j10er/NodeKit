"""Abstract data source interface for node tree data"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict
from ..representations.node_tree import NodeTreeData
from ... import config


class DataSource(ABC):
    """Abstract base class for node tree data sources"""

    tree_datas: Dict[str, NodeTreeData]
    data_dicts: Dict[str, config.ExportDict]

    def get_uuids(self) -> set[str]:
        """Get all UUIDs of node trees in this data source"""
        return self.tree_datas.keys()

    def get_tree_datas(self) -> Dict[str, NodeTreeData]:
        return self.tree_datas

    def get_data_dicts(self) -> Dict[str, config.ExportDict]:
        return self.data_dicts

    def _uuids_to_write(
        self,
        write_data_dicts: Dict[str, config.ExportDict],
    ) -> set[str]:
        current_data_dicts = self.get_data_dicts()
        return {
            uuid
            for uuid in write_data_dicts
            if current_data_dicts.get(uuid, {}) != write_data_dicts[uuid]
        }

    @abstractmethod
    def _calculate_tree_datas(self) -> Dict[str, NodeTreeData]:
        """Get NodeTreeData objects indexed by UUID"""
        pass

    @abstractmethod
    def _calculate_data_dicts(self) -> Dict[str, config.ExportDict]:
        """Get export-ready data dictionaries indexed by UUID"""
        pass

    @abstractmethod
    def write(self, source: "DataSource", append: bool) -> None:
        """Write NodeTreeData to this data source"""
        pass
