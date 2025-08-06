import os
import shutil

import bpy
import pytest
from bl_ext.user_default.nodekit.json_nodes.data.blend_data import BlendData

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


def _open_test_trees_file():
    """Open the test trees file."""
    _clear_test_trees_folder()
    filepath = os.path.join(
        os.path.dirname(__file__),
        "test_trees.blend",
    )
    bpy.ops.wm.open_mainfile(filepath=filepath)
    bpy.context.scene.node_kit.folder_path = folder_path


def _clear_test_trees_folder():
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)


def _open_new_file():
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.context.scene.node_kit.folder_path = folder_path


@pytest.fixture(scope="module")
def fixture_test_trees():
    _open_test_trees_file()

    bpy.ops.nodekit.export_json()

    # Import to new file
    _open_new_file()
    bpy.ops.nodekit.import_json()

    yield

    _open_new_file()


def test_fixture():
    """Test if the fixture is imported correctly."""
    _open_test_trees_file()
    for tree_name in other_tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should be in the node groups"


@pytest.fixture(scope="module")
def get_data_dicts():
    _open_test_trees_file()
    old_data_dicts = BlendData().get_data_dicts()
    bpy.ops.nodekit.export_json()
    _open_new_file()
    bpy.ops.nodekit.import_json()
    new_data_dicts = BlendData().get_data_dicts()

    yield old_data_dicts, new_data_dicts

    _open_new_file()
