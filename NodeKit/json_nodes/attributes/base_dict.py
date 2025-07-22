import bpy

classes = {
    bpy.types.Node: {
        "attributes": {
            "color": [
                "LIST",
                [0.6079999804496765, 0.6079999804496765, 0.6079999804496765],
            ],
            "height": ["FLOAT", 100],
            "label": ["STRING", ""],
            "location": ["LIST", [0, 0]],
            "mute": ["BOOLEAN", False],
            "name": ["STRING", ""],
            "use_custom_color": ["BOOLEAN", False],
            "warning_propagation": ["STRING", "ALL"],
            "width": ["FLOAT", 140],
            "bl_idname": ["STRING", ""],
        },
        "subtypes": {
            bpy.types.NodeInternal: {
                "attributes": {},
                "subtypes": {
                    bpy.types.GeometryNode: {
                        "attributes": {},
                        "find_subtypes": True,
                        "subtype_params": {
                            "exclude_attribute_keywords": ["active", "index"]
                        },
                    },
                    bpy.types.FunctionNode: {
                        "attributes": {},
                        "find_subtypes": True,
                    },
                },
            }
        },
    },
    bpy.types.NodeTree: {
        "attributes": {
            "name": ["STRING", ""],
            "color_tag": ["STRING", "NONE"],
            "default_group_node_width": ["INT", 140],
            "description": ["STRING", ""],
            "bl_idname": ["STRING", ""],
        },
        "subtypes": {
            bpy.types.GeometryNodeTree: {
                "attributes": {
                    "is_modifier": ["BOOLEAN", False],
                    "is_tool": ["BOOLEAN", False],
                },
            }
        },
    },
    bpy.types.NodeTreeInterfaceItem: {
        "attributes": {
            "item_type": ["STRING", "SOCKET"],
            "name": ["STRING", ""],
            "description": ["STRING", ""],
        },
        "subtypes": {
            bpy.types.NodeTreeInterfacePanel: {
                "attributes": {
                    "default_closed": ["BOOLEAN", False],
                }
            },
            bpy.types.NodeTreeInterfaceSocket: {
                "attributes": {
                    "attribute_domain": ["STRING", "POINT"],
                    "default_attribute_name": ["STRING", ""],
                    "description": ["STRING", ""],
                    "force_non_field": ["BOOLEAN", False],
                    "hide_in_modifier": ["BOOLEAN", False],
                    "hide_value": ["BOOLEAN", False],
                    "socket_type": ["STRING", "DEFAULT"],
                    "in_out": ["STRING", "INPUT"],
                },
                "find_subtypes": True,
            },
        },
    },
    bpy.types.NodeSocket: {
        "attributes": {
            "bl_idname": ["STRING", ""],
        },
        "subtypes": {
            bpy.types.NodeSocketStandard: {
                "find_subtypes": True,
            }
        },
    },
}
