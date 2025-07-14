import bpy
from .test_trees_fixture import fixture_test_trees, tree_names


def test_trees_exist(fixture_test_trees):
    """Test if the trees exist after import."""
    for tree_name in tree_names:
        assert (
            tree_name in bpy.data.node_groups
        ), f"{tree_name} should exist after import"


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
