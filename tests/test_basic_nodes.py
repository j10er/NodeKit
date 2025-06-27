import bpy
import mathutils
import pytest
from bl_ext.user_default.geo_node_development.nodes import importer, exporter, data
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


@pytest.fixture()
def create_test_nodes():
    """Base fixture for creating test nodes."""
    clear_all()
    yield
    clear_all()


@pytest.fixture()
def create_basic_test_nodes(create_test_nodes):
    tree = bpy.data.node_groups.new(type="GeometryNodeTree", name="BasicTestNodes")

    # Socket Geometry
    geometry_socket = tree.interface.new_socket(
        name="Geometry", in_out="OUTPUT", socket_type="NodeSocketGeometry"
    )

    # Socket Geometry
    geometry_socket_1 = tree.interface.new_socket(
        name="Geometry", in_out="INPUT", socket_type="NodeSocketGeometry"
    )

    # initialize basictestnodes_001 nodes
    # node Group Input
    group_input = tree.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"

    # node Set Position
    set_position = tree.nodes.new("GeometryNodeSetPosition")
    set_position.name = "Set Position"
    # Selection
    set_position.inputs[1].default_value = True
    # Offset
    set_position.inputs[3].default_value = (0.0, 1.0, 0.0)

    # node Group Output
    group_output = tree.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True

    # node Vector
    vector = tree.nodes.new("FunctionNodeInputVector")
    vector.name = "Vector"
    vector.vector = (1.0, 2.0, 3.0)

    # node Set Position.001
    set_position_001 = tree.nodes.new("GeometryNodeSetPosition")
    set_position_001.name = "Set Position.001"
    # Selection
    set_position_001.inputs[1].default_value = True
    # Offset
    set_position_001.inputs[3].default_value = (0.0, 1.0, 0.0)

    # node Join Geometry
    join_geometry = tree.nodes.new("GeometryNodeJoinGeometry")
    join_geometry.name = "Join Geometry"

    # Set locations
    group_input.location = (-500.0, 0.0)
    set_position.location = (140.0, 140.0)
    group_output.location = (600.0, -40.0)
    vector.location = (-220.0, -180.0)
    set_position_001.location = (140.0, -120.0)
    join_geometry.location = (360.0, 20.0)

    # initialize basictestnodes_001 links
    # group_input.Geometry -> set_position.Geometry
    tree.links.new(group_input.outputs[0], set_position.inputs[0])
    # join_geometry.Geometry -> group_output.Geometry
    tree.links.new(join_geometry.outputs[0], group_output.inputs[0])
    # vector.Vector -> set_position.Position
    tree.links.new(vector.outputs[0], set_position.inputs[2])
    # group_input.Geometry -> set_position_001.Geometry
    tree.links.new(group_input.outputs[0], set_position_001.inputs[0])
    # vector.Vector -> set_position_001.Position
    tree.links.new(vector.outputs[0], set_position_001.inputs[2])
    # set_position_001.Geometry -> join_geometry.Geometry
    tree.links.new(set_position_001.outputs[0], join_geometry.inputs[0])
    # set_position.Geometry -> join_geometry.Geometry
    tree.links.new(set_position.outputs[0], join_geometry.inputs[0])
    return tree


def test_basic_nodes(create_basic_test_nodes):
    tree = create_basic_test_nodes
    node_dict = data.NodeTreeData.from_tree(tree).to_dict()
    clear_all()
    data.NodeTreeData.from_dict(node_dict).to_tree()

    assert "BasicTestNodes" in bpy.data.node_groups, "BasicTestNodes should be created"
    tree = bpy.data.node_groups["BasicTestNodes"]
    for node_name in [
        "Group Input",
        "Set Position",
        "Group Output",
        "Vector",
        "Set Position.001",
        "Join Geometry",
    ]:
        assert node_name in tree.nodes, f"{node_name} should be in the node tree"
    assert tree.nodes["Vector"].vector == mathutils.Vector((1.0, 2.0, 3.0))


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
