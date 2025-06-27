"""
Automatically Generated Blender Node Attributes Dictionary

This module contains the attributes dictionary for Blender node classes
including Node, NodeSocket, NodeTree, and related interface items.

The structure follows the format: [type, default_value] for each attribute.
"""

SOCKET_TYPES = {}

DEFAULTS = {
    "Element": [
        {},
        {
            "Node": [
                {
                    "bl_description": ["STR", ''],
                    "bl_height_default": ["FLOAT", 0.0],
                    "bl_height_max": ["FLOAT", 0.0],
                    "bl_height_min": ["FLOAT", 0.0],
                    "bl_icon": ["ENUM", 'NODE'],
                    "bl_idname": ["STR", ''],
                    "bl_label": ["STR", ''],
                    "bl_width_default": ["FLOAT", 0.0],
                    "bl_width_max": ["FLOAT", 0.0],
                    "bl_width_min": ["FLOAT", 0.0],
                    "color": ["FLOAT", 0.0],
                    "height": ["FLOAT", 0.0],
                    "hide": ["BOOLEAN", False],
                    "label": ["STR", ''],
                    "location": ["FLOAT", 0.0],
                    "location_absolute": ["FLOAT", 0.0],
                    "mute": ["BOOLEAN", False],
                    "name": ["STR", ''],
                    "parent": ["POINTER", None],
                    "select": ["BOOLEAN", False],
                    "show_options": ["BOOLEAN", False],
                    "show_preview": ["BOOLEAN", False],
                    "show_texture": ["BOOLEAN", False],
                    "use_custom_color": ["BOOLEAN", False],
                    "warning_propagation": ["ENUM", 'ALL'],
                    "width": ["FLOAT", 0.0],
                },
                {
                    "NodeInternal": [
                        {},
                        {
                            "CompositorNode": [
                                {},
                                {},
                            ],
                            "FunctionNode": [
                                {},
                                {},
                            ],
                            "GeometryNode": [
                                {},
                                {
                                    "GeometryNodeInputCollection": [
                                        {
                                            "collection": ["POINTER", None],
                                        },
                                    ],
                                    "GeometryNodeRepeatOutput": [
                                        {
                                            "active_index": ["INT", 0],
                                            "active_item": ["POINTER", None],
                                            "inspection_index": ["INT", 0],
                                        },
                                    ],
                                },
                            ],
                            "ShaderNode": [
                                {},
                                {},
                            ],
                            "TextureNode": [
                                {},
                                {},
                            ],
                        },
                    ],
                },
            ],
            "NodeSocket": [
                {
                    "bl_idname": ["STR", ''],
                    "bl_label": ["STR", ''],
                    "bl_subtype_label": ["STR", ''],
                    "description": ["STR", ''],
                    "display_shape": ["ENUM", 'CIRCLE'],
                    "enabled": ["BOOLEAN", False],
                    "hide": ["BOOLEAN", False],
                    "hide_value": ["BOOLEAN", False],
                    "link_limit": ["INT", 0],
                    "name": ["STR", ''],
                    "pin_gizmo": ["BOOLEAN", False],
                    "show_expanded": ["BOOLEAN", False],
                    "type": ["ENUM", 'VALUE'],
                },
                {},
            ],
            "NodeTree": [
                {
                    "asset_data": ["POINTER", None],
                    "bl_description": ["STR", ''],
                    "bl_icon": ["ENUM", 'NODETREE'],
                    "bl_idname": ["STR", ''],
                    "bl_label": ["STR", ''],
                    "bl_use_group_interface": ["BOOLEAN", True],
                    "color_tag": ["ENUM", 'NONE'],
                    "default_group_node_width": ["INT", 140],
                    "description": ["STR", ''],
                    "grease_pencil": ["POINTER", None],
                    "is_runtime_data": ["BOOLEAN", False],
                    "name": ["STR", ''],
                    "tag": ["BOOLEAN", False],
                    "use_extra_user": ["BOOLEAN", False],
                    "use_fake_user": ["BOOLEAN", False],
                },
                {},
            ],
            "NodeTreeInterfaceItem": [
                {},
                {
                    "NodeTreeInterfacePanel": [
                        {
                            "default_closed": ["BOOLEAN", False],
                            "description": ["STR", ''],
                            "name": ["STR", ''],
                        },
                        {},
                    ],
                    "NodeTreeInterfaceSocket": [
                        {
                            "attribute_domain": ["ENUM", 'POINT'],
                            "bl_socket_idname": ["STR", ''],
                            "default_attribute_name": ["STR", ''],
                            "default_input": ["ENUM", ''],
                            "description": ["STR", ''],
                            "force_non_field": ["BOOLEAN", False],
                            "hide_in_modifier": ["BOOLEAN", False],
                            "hide_value": ["BOOLEAN", False],
                            "is_inspect_output": ["BOOLEAN", False],
                            "layer_selection_field": ["BOOLEAN", False],
                            "name": ["STR", ''],
                            "socket_type": ["ENUM", 'DEFAULT'],
                        },
                        {},
                    ],
                },
            ],
        },
    ],
}
