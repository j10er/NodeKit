import bpy

CLASSES = {
    bpy.types.Node: {
        "attributes": {
            "color": "LIST",
            "height": "FLOAT",
            "label": "STRING",
            "parent": "NODE",
            "location_absolute": "LIST",
            "mute": "BOOLEAN",
            "name": "STRING",
            "use_custom_color": "BOOLEAN",
            "warning_propagation": "STRING",
            "bl_idname": "STRING",
        },
        "subtypes": {
            bpy.types.NodeInternal: {
                "attributes": {},
                "subtypes": {
                    bpy.types.CompositorNode: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                        "find_subtypes": True,
                    },
                    bpy.types.FunctionNode: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                        "find_subtypes": True,
                    },
                    bpy.types.GeometryNode: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                        "find_subtypes": True,
                        "subtype_params": {"exclude_attribute_keywords": ["active"]},
                    },
                    bpy.types.NodeFrame: {
                        "attributes": {
                            "label_size": "INT",
                            "shrink": "BOOLEAN",
                            "width": "FLOAT",
                        }
                    },
                    bpy.types.NodeGroupInput: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                    },
                    bpy.types.NodeGroupOutput: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                    },
                    bpy.types.NodeReroute: {"attributes": {}},
                    bpy.types.ShaderNode: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                        "find_subtypes": True,
                    },
                    bpy.types.TextureNode: {
                        "attributes": {
                            "width": "FLOAT",
                        },
                        "find_subtypes": True,
                    },
                },
            },
        },
    },
    bpy.types.NodeTree: {
        "attributes": {
            "name": "STRING",
            "color_tag": "STRING",
            "default_group_node_width": "INT",
            "description": "STRING",
            "bl_idname": "STRING",
        },
        "subtypes": {
            bpy.types.GeometryNodeTree: {
                "attributes": {
                    "is_modifier": "BOOLEAN",
                    "is_tool": "BOOLEAN",
                },
            }
        },
    },
    bpy.types.NodeTreeInterfacePanel: {
        "attributes": {
            "default_closed": "BOOLEAN",
            "item_type": "STRING",
            "name": "STRING",
            "description": "STRING",
        }
    },
    bpy.types.NodeTreeInterfaceSocket: {
        "attributes": {
            "item_type": "STRING",
            "name": "STRING",
            "description": "STRING",
            "attribute_domain": "STRING",
            "default_attribute_name": "STRING",
            "description": "STRING",
            "force_non_field": "BOOLEAN",
            "hide_in_modifier": "BOOLEAN",
            "hide_value": "BOOLEAN",
            "socket_type": "STRING",
            "in_out": "STRING",
        },
        "find_subtypes": True,
    },
    bpy.types.NodeSocket: {
        "attributes": {
            "bl_idname": "STRING",
        },
        "subtypes": {
            bpy.types.NodeSocketStandard: {
                "find_subtypes": True,
            },
        },
    },
}
