import bpy
from .test_trees_fixture import fixture_test_trees, other_tree_names, test_tree_names


def test_trees_exist(fixture_test_trees):
    """Test if the trees exist after import."""
    for tree_name in test_tree_names + other_tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should exist after import"


def test_links(fixture_test_trees):
    tree = bpy.data.node_groups.get("test_links")
    # Test if Group Input is connected to Set Position
    group_input = tree.nodes.get("Group Input")
    group_output = tree.nodes.get("Group Output")
    set_position = tree.nodes.get("Set Position")
    assert group_input is not None, "Group Input node should exist"
    assert group_output is not None, "Group Output node should exist"
    assert set_position is not None, "Set Position node should exist"
    assert (
        group_input.outputs[0].links[0].to_node == set_position
    ), "Group Input should be linked to Set Position"
    assert (
        set_position.outputs[0].links[0].to_node == group_output
    ), "Set Position should be linked to Group Output"


def test_reroute(fixture_test_trees):
    """Test the reroute node."""
    tree = bpy.data.node_groups.get("test_reroute")
    reroute_node = tree.nodes.get("Reroute")
    assert reroute_node is not None, "Reroute node should exist"
    assert len(reroute_node.outputs) == 1, "Reroute node should have one output"
    assert (
        len(reroute_node.outputs[0].links) > 0
    ), "Reroute node should have outgoing links"


def test_subgroups(fixture_test_trees):
    """Test the subgroup structure."""
    tree = bpy.data.node_groups.get("test_subgroups")
    subtree = bpy.data.node_groups.get("test_subgroups_subgroup")
    assert "Group" in tree.nodes, "Subgroup node should exist"
    subgroup_node = tree.nodes.get("Group")
    assert (
        subgroup_node.node_tree == subtree
    ), "Subgroup node should reference the correct subtree"


def test_nested_menu(fixture_test_trees):
    """Test the nested menu structure."""

    tree = bpy.data.node_groups.get("test_nested_menu")

    socket = tree.interface.items_tree.get("Menu")
    assert socket is not None, "Menu interface socket should exist"
    assert socket.default_value == "Option 2", "Default value should be 'Option 2'"

    tree = bpy.data.node_groups.get("test_nested_menu-menu_switch_1")
    menu_switch = tree.nodes.get("Menu Switch")
    assert menu_switch is not None, "Menu Switch node should exist"
    item = menu_switch.enum_items[2]
    assert (
        item.name == "Option 3"
    ), "Menu Switch should have 'Option 3' as the third option"
    assert menu_switch.data_type == "FLOAT", "Menu Switch should have data type FLOAT"


def test_foreach_element(fixture_test_trees):
    """Test the foreach element node."""
    tree = bpy.data.node_groups.get("test_foreach_element")
    foreach_input = tree.nodes.get("For Each Geometry Element Input")
    assert (
        foreach_input is not None
    ), "For Each Geometry Element Input node should exist"
    foreach_output = tree.nodes.get("For Each Geometry Element Output")
    assert (
        foreach_output is not None
    ), "For Each Geometry Element Output node should exist"

    assert (
        foreach_input.paired_output == foreach_output
    ), "For Each Geometry Element Input should be paired with For Each Geometry Element Output"
    assert (
        foreach_output.main_items[0].name == "Value"
    ), "Output should have 'Value' item"
    assert (
        foreach_output.input_items[1].name == "Vector"
    ), "Input should have 'Vector' item"
    assert (
        foreach_output.generation_items[1].name == "Geometry.001"
    ), "Generation should have 'Geometry.001' item"


def test_node_frame(fixture_test_trees):
    """Test the node frame."""
    tree = bpy.data.node_groups.get("test_nodeframe")
    inner_frame = tree.nodes.get("Frame")
    outer_frame = tree.nodes.get("Frame.001")
    group_input = tree.nodes.get("Group Input")
    assert inner_frame is not None, "Node Frame should exist"
    assert outer_frame is not None, "Outer Frame should exist"
    assert group_input is not None, "Group Input should exist"
    assert (
        inner_frame.parent == outer_frame
    ), "Node Frame should be a child of Outer Frame"
    assert (
        inner_frame.label == "Inner Frame"
    ), "Node Frame should have the correct label"
    assert group_input.parent == inner_frame, "Group Input should be inside Node Frame"
    assert inner_frame.shrink == True, "Node Frame should have shrink enabled"


def test_interface_sockets(fixture_test_trees):
    """Test the interface sockets."""
    tree = bpy.data.node_groups.get("test_interface_sockets")
    input_socket = tree.interface.items_tree.get("Input Socket")
    assert input_socket.subtype == "DISTANCE", "Input Socket should be of type DISTANCE"
    assert (
        input_socket.default_value == 1.0
    ), "Input Socket should have a default value of 1.0"
    assert (
        input_socket.min_value == 0.0
    ), "Input Socket should have a minimum value of 0.0"


def test_index_switch(fixture_test_trees):
    """Test the index switch."""
    tree = bpy.data.node_groups.get("test_index_switch")
    index_switch = tree.nodes.get("Index Switch")
    assert index_switch is not None, "Index Switch node should exist"
    assert index_switch.data_type == "FLOAT", "Index Switch should have data type FLOAT"
    assert (
        len(index_switch.index_switch_items) == 3
    ), "Index Switch should have three options"
