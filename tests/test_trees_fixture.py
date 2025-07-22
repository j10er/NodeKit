import pytest
import bpy
import os
import shutil

test_tree_names = [
    "test_nested_menu",
    "test_foreach_element",
    "test_links",
    "test_reroute",
    "test_subgroups",
    "test_input_node_float",
]
other_tree_names = [
    "test_nested_menu-menu_switch_1",
    "test_nested_menu-menu_switch_2",
    "test_nested_menu-menu_switch_3",
    "test_subgroups_subgroup",
]


def _open_test_trees_file():
    """Open the test trees file."""
    filepath = os.path.join(
        os.path.dirname(__file__),
        "test_trees.blend",
    )
    bpy.ops.wm.open_mainfile(filepath=filepath)


@pytest.fixture(scope="module")
def fixture_test_trees():
    _open_test_trees_file()

    folder_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "test_trees_json"
    )
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path, exist_ok=True)
    # Export the JSON nodes to test_trees_json folder.
    bpy.context.scene.node_kit.folder_path = folder_path
    print(bpy.context.scene.node_kit.folder_path)
    bpy.ops.nodekit.export_json()

    # Import to new file
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.context.scene.node_kit.folder_path = folder_path
    bpy.ops.nodekit.import_json()

    # Test execution after import
    yield


def test_fixture():
    """Test if the fixture is imported correctly."""
    _open_test_trees_file()
    for tree_name in other_tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should be in the node groups"

    bpy.ops.wm.read_homefile(use_empty=True)
