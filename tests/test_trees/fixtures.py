import os
import shutil

import bpy
import pytest
from bl_ext.user_default.nodekit.json_nodes.data.blend_data import BlendData
from ..test_nodekit import TestNodeKit


class TestTrees(TestNodeKit):
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

    nodes_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "test_trees_json"
    )
    blend_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "test_trees.blend"
    )
