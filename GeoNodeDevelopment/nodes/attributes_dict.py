"""
Blender Node Attributes Dictionary

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
                    "bl_idname": ["str", ""],
                    "color": [
                        "list",
                        [0.6079999804496765, 0.6079999804496765, 0.6079999804496765],
                    ],
                    "height": ["float", 100],
                    "label": ["str", ""],
                    "location": ["list", [0, 0]],
                    "mute": ["bool", False],
                    "name": ["str", ""],
                    "use_custom_color": ["bool", False],
                    "warning_propagation": ["str", "ALL"],
                    "width": ["float", 140],
                }
            ],
            "NodeSocket": [
                {"type": ["str", ""]},
                {
                    "VALUE": [{"default_value": ["float", 0]}],
                    "INT": [{"default_value": ["int", 0]}],
                    "BOOLEAN": [{"default_value": ["bool", False]}],
                    "VECTOR": [{"default_value": ["list", [0, 0, 0]]}],
                    "ROTATION": [{"default_value": ["list", [0, 0, 0]]}],
                    "MATRIX": [{}],
                    "STRING": [{"default_value": ["str", ""]}],
                    "RGBA": [{"default_value": ["list", [0, 0, 0, 1.0]]}],
                    "SHADER": [{"default_value": ["None", None]}],
                    "OBJECT": [{"default_value": ["None", None]}],
                    "IMAGE": [{"default_value": ["None", None]}],
                    "GEOMETRY": [{}],
                    "COLLECTION": [{"default_value": ["None", None]}],
                    "TEXTURE": [{"default_value": ["None", None]}],
                    "MATERIAL": [{"default_value": ["None", None]}],
                    "MENU": [{"default_value": ["None", None]}],
                },
            ],
            "NodeTree": [
                {
                    "name": ["str", ""],
                    "color_tag": ["str", "NONE"],
                    "default_group_node_width": ["int", 140],
                    "description": ["str", ""],
                    "is_modifier": ["bool", False],
                    "is_tool": ["bool", False],
                }
            ],
            "NodeTreeInterfaceItem": [
                {
                    "item_type": ["str", "SOCKET"],
                    "name": ["str", ""],
                    "description": ["str", ""],
                },
                {
                    "NodeTreeInterfacePanel": [
                        {
                            "default_closed": ["bool", False],
                        }
                    ],
                    "NodeTreeInterfaceSocket": [
                        {
                            "attribute_domain": ["str", "POINT"],
                            "default_attribute_name": ["str", ""],
                            "description": ["str", ""],
                            "force_non_field": ["bool", False],
                            "hide_in_modifier": ["bool", False],
                            "hide_value": ["bool", False],
                            "socket_type": ["str", "DEFAULT"],
                            "in_out": ["str", "INPUT"],
                        },
                        {
                            "NodeSocketString": [
                                {
                                    "subtype": ["str", "NONE"],
                                    "default_value": ["str", ""],
                                }
                            ],
                            "NodeSocketBool": [{"default_value": ["bool", False]}],
                            "NodeSocketMaterial": [{"default_value": ["None", None]}],
                            "NodeSocketVector": [
                                {
                                    "subtype": ["str", "NONE"],
                                    "max_value": ["float", 3.4028234663852886e38],
                                    "min_value": ["float", -3.4028234663852886e38],
                                    "default_value": ["list", [0, 0, 0]],
                                }
                            ],
                            "NodeSocketInt": [
                                {
                                    "subtype": ["str", "NONE"],
                                    "max_value": ["int", 2147483647],
                                    "min_value": ["int", -2147483648],
                                    "default_value": ["int", 0],
                                }
                            ],
                            "NodeSocketMenu": [{"default_value": ["None", None]}],
                            "NodeSocketCollection": [{"default_value": ["None", None]}],
                            "NodeSocketGeometry": [{}],
                            "NodeSocketTexture": [{"default_value": ["None", None]}],
                            "NodeSocketFloat": [
                                {
                                    "subtype": ["str", "NONE"],
                                    "max_value": ["float", 3.4028234663852886e38],
                                    "min_value": ["float", -3.4028234663852886e38],
                                    "default_value": ["float", 0],
                                }
                            ],
                            "NodeSocketColor": [
                                {"default_value": ["list", [0, 0, 0, 1.0]]}
                            ],
                            "NodeSocketObject": [{"default_value": ["None", None]}],
                            "NodeSocketRotation": [
                                {"default_value": ["list", [0, 0, 0]]}
                            ],
                            "NodeSocketMatrix": [{}],
                            "NodeSocketImage": [{"default_value": ["None", None]}],
                        },
                    ],
                },
            ],
        },
    ]
}
