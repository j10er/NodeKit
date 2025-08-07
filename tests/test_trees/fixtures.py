import os
import shutil

import bpy
import pytest
from bl_ext.user_default.nodekit.json_nodes.data.blend_data import BlendData
from .. import file

test_tree_names = [
    "test_compare_node",
    "test_foreach_element",
    "test_index_switch",
    "test_input_node_float",
    "test_interface_sockets",
    "test_links",
    "test_nested_menu",
    "test_nested_panels",
    "test_nodeframe",
    "test_reroute",
    "test_subgroups",
    "test_multi_input_order",
]
other_tree_names = [
    "test_nested_menu-menu_switch_1",
    "test_nested_menu-menu_switch_2",
    "test_nested_menu-menu_switch_3",
    "test_subgroups_subgroup",
]

folder_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "test_trees_json"
)
blend_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "test_trees.blend"
)


@pytest.fixture(scope="module")
def fixture_test_trees():
    file.open_blend(blend_path, folder_path)

    bpy.ops.nodekit.export_json()

    file.new(nodes_path=folder_path)
    bpy.ops.nodekit.import_json()

    yield

    file.new(nodes_path=folder_path)


def test_fixture():
    """Test if the fixture is imported correctly."""
    file.open_blend(blend_path, folder_path)
    for tree_name in other_tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should be in the node groups"


@pytest.fixture(scope="module")
def capture_original_data():
    file.open_blend(blend_path, folder_path)
    data_dicts = BlendData().get_data_dicts()
    bpy.ops.nodekit.export_json()
    file.new(nodes_path=folder_path)
    bpy.ops.nodekit.import_json()

    yield data_dicts

    file.new(nodes_path=folder_path)
