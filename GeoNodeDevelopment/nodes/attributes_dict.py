"""
Blender Node Attributes Dictionary

This module contains the attributes dictionary for Blender node classes
including Node, NodeSocket, NodeTree, and related interface items.

The structure follows the format: [type, default_value] for each attribute.
"""

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
                {},
                {
                    "NodeSocketBool": [{"default_value": ["bool", False]}],
                    "NodeSocketCollection": [{"default_value": ["None", None]}],
                    "NodeSocketColor": [{"default_value": ["list", [0, 0, 0, 1.0]]}],
                    "NodeSocketFloat": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatAngle": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatColorTemperature": [
                        {"default_value": ["float", 0]}
                    ],
                    "NodeSocketFloatDistance": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatFactor": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatFrequency": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatPercentage": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatTime": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatTimeAbsolute": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatUnsigned": [{"default_value": ["float", 0]}],
                    "NodeSocketFloatWavelength": [{"default_value": ["float", 0]}],
                    "NodeSocketGeometry": [{}],
                    "NodeSocketImage": [{"default_value": ["None", None]}],
                    "NodeSocketInt": [{"default_value": ["int", 0]}],
                    "NodeSocketIntFactor": [{"default_value": ["int", 0]}],
                    "NodeSocketIntPercentage": [{"default_value": ["int", 0]}],
                    "NodeSocketIntUnsigned": [{"default_value": ["int", 0]}],
                    "NodeSocketMaterial": [{"default_value": ["None", None]}],
                    "NodeSocketMatrix": [{}],
                    "NodeSocketMenu": [{"default_value": ["None", None]}],
                    "NodeSocketObject": [{"default_value": ["None", None]}],
                    "NodeSocketRotation": [{"default_value": ["list", [0, 0, 0]]}],
                    "NodeSocketShader": [{"default_value": ["None", None]}],
                    "NodeSocketString": [{"default_value": ["str", ""]}],
                    "NodeSocketStringFilePath": [{"default_value": ["str", ""]}],
                    "NodeSocketTexture": [{"default_value": ["None", None]}],
                    "NodeSocketVector": [{"default_value": ["list", [0, 0, 0]]}],
                    "NodeSocketVectorAcceleration": [
                        {"default_value": ["list", [0, 0, 0]]}
                    ],
                    "NodeSocketVectorDirection": [
                        {"default_value": ["list", [0, 0, 0]]}
                    ],
                    "NodeSocketVectorEuler": [{"default_value": ["list", [0, 0, 0]]}],
                    "NodeSocketVectorTranslation": [
                        {"default_value": ["list", [0, 0, 0]]}
                    ],
                    "NodeSocketVectorVelocity": [
                        {"default_value": ["list", [0, 0, 0]]}
                    ],
                    "NodeSocketVectorXYZ": [{"default_value": ["list", [0, 0, 0]]}],
                },
            ],
            "NodeTree": [
                {
                    "color_tag": ["str", "NONE"],
                    "default_group_node_width": ["int", 140],
                    "description": ["str", ""],
                    "type": ["str", "SHADER"],
                    "view_center": ["list", [0, 0]],
                    "is_modifier": ["bool", False],
                    "is_tool": ["bool", False],
                }
            ],
            "NodeTreeInterfaceItem": [
                {
                    "index": ["int", -1],
                    "item_type": ["str", "PANEL"],
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
