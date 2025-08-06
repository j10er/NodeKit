import bpy
import pytest

from pathlib import Path
from deepdiff import DeepDiff

from bl_ext.user_default.nodekit.json_nodes.data.blend_data import BlendData

from .test_trees_fixture import capture_original_data, test_tree_names


@pytest.mark.parametrize("tree_name", test_tree_names)
def test_imported_tree_data(capture_original_data, tree_name):
    """Test that the imported node tree data matches the expected structure."""
    old_data_dicts = capture_original_data
    new_data_dicts = BlendData().get_data_dicts()
    uuid = next(
        (
            uuid
            for uuid, data_dict in old_data_dicts.items()
            if data_dict["name"] == tree_name
        ),
        None,
    )
    assert uuid, f"{tree_name} not found in old data dicts"
    assert uuid in new_data_dicts, f"{tree_name} not found in new data dicts"

    old_data_dict = old_data_dicts[uuid]
    new_data_dict = new_data_dicts[uuid]

    # Compare the two dictionaries
    diff = DeepDiff(old_data_dict, new_data_dict)
    assert diff == {}, f"Difference found in {tree_name}: {diff}"


@pytest.mark.parametrize("tree_name", test_tree_names)
def test_twice_imported_tree_data(capture_original_data, tree_name):
    """Test that the imported node tree data matches the expected structure."""
    old_data_dicts = capture_original_data
    bpy.ops.nodekit.import_json()
    new_data_dicts = BlendData().get_data_dicts()
    uuid = next(
        (
            uuid
            for uuid, data_dict in old_data_dicts.items()
            if data_dict["name"] == tree_name
        ),
        None,
    )
    assert uuid, f"{tree_name} not found in old data dicts"
    assert uuid in new_data_dicts, f"{tree_name} not found in new data dicts"

    old_data_dict = old_data_dicts[uuid]
    new_data_dict = new_data_dicts[uuid]

    # Compare the two dictionaries
    diff = DeepDiff(old_data_dict, new_data_dict)
    assert diff == {}, f"Difference found in {tree_name}: {diff}"
