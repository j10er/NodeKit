import logging
from deepdiff import DeepDiff
import bpy
from .data.file_data import FileData
from .data.blend_data import BlendData
from .. import config
from .representations.node_tree import NodeTreeData
from pathlib import Path
from pprint import pprint

log = logging.getLogger(__name__)


def compare_dicts(dict1: dict, dict2: dict) -> dict:
    return DeepDiff(dict1, dict2)


def test_import():
    file_data_dicts = FileData(
        Path(bpy.path.abspath(bpy.context.scene.node_kit.folder_path))
    ).get_data_dicts()
    bpy.ops.nodekit.import_json()
    blend_dicts = BlendData().get_data_dicts()
    for uuid, file_data_dict in file_data_dicts.items():
        if uuid not in blend_dicts:
            log.warning(f"UUID {uuid} not found in blend data")
            continue
        blend_data_dict = blend_dicts[uuid]
        if file_data_dict != blend_data_dict:
            log.warning(f"Difference in node group {file_data_dict['tree']['name']}:")
            pprint(compare_dicts(file_data_dict, blend_data_dict))
