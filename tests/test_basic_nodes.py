import bpy
import pytest
from bl_ext.user_default.geo_node_development.nodes import importer, exporter
import os


@pytest.fixture()
def open_test_nodes_file():
    """Open the test nodes file."""
    filepath = os.path.join(
        os.path.dirname(__file__),
        "test_nodes.blend",
    )
    bpy.ops.wm.open_mainfile(filepath=filepath)


def test_fixture_import(open_test_nodes_file):
    """Test if the fixture is imported correctly."""
    assert "TestNodes" in bpy.data.node_groups, "TestNodes should be in the node groups"


def test_tree_element_count(open_test_nodes_file):
    tree = bpy.data.node_groups.get("TestNodes")
    num_of_nodes = len(tree.nodes)
    num_of_links = len(tree.links)
    num_of_sockets = get_num_of_interface_sockets(tree)
    exporter.export_group("TestNodes")

    clear_all()
    importer.import_groups()
    assert "TestNodes" in bpy.data.node_groups, "TestNodes should be imported"
    new_tree = bpy.data.node_groups.get("TestNodes")
    assert (
        len(new_tree.nodes) == num_of_nodes
    ), "Number of nodes should match the original"
    assert (
        len(new_tree.links) == num_of_links
    ), "Number of links should match the original"
    assert (
        get_num_of_interface_sockets(new_tree) == num_of_sockets
    ), "Number of inputs should match the original"


def clear_all():
    """Clear all node groups and objects."""
    for node_group in bpy.data.node_groups:
        bpy.data.node_groups.remove(node_group, do_unlink=True)

    for obj in bpy.data.objects:
        bpy.data.objects.remove(obj, do_unlink=True)


def get_num_of_interface_sockets(tree):
    """Get the number of inputs in the node tree."""
    return len(
        [item for item in tree.interface.items_tree if item.item_type == "SOCKET"]
    )
