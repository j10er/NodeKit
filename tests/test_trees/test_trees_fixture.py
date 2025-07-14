import pytest
import bpy
import os

tree_names = [
    "test_nested_menu",
    "test_nested_menu-menu_switch_1",
    "test_nested_menu-menu_switch_2",
    "test_nested_menu-menu_switch_3",
    "test_foreach_element",
]


def open_test_trees_file():
    """Open the test trees file."""
    filepath = os.path.join(
        os.path.dirname(__file__),
        "test_trees.blend",
    )
    bpy.ops.wm.open_mainfile(filepath=filepath)


@pytest.fixture(scope="module")
def fixture_test_trees():
    open_test_trees_file()

    json_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "test_trees_json")
    )
    os.makedirs(json_path, exist_ok=True)
    # Export the JSON nodes to test_trees_json folder.
    bpy.context.scene.gnd_props.folder_path = json_path
    print(bpy.context.scene.gnd_props.folder_path)
    bpy.ops.nodedev.export_json()

    # Import to new file
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.context.scene.gnd_props.folder_path = json_path
    bpy.ops.nodedev.import_json()

    # Test execution after import
    yield

    # Cleanup after test


def test_fixture():
    """Test if the fixture is imported correctly."""
    open_test_trees_file()
    for tree_name in tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should be in the node groups"

    bpy.ops.wm.read_homefile(use_empty=True)
