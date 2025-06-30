import bpy
from typing import Dict, Any, List, Union
import json
import os
from pathlib import Path


defaults = {
    "STR": "",
    "INT": 0,
    "FLOAT": 0.0,
    "BOOLEAN": False,
    "COLLECTION": [],
    "ENUM": "",
    "POINTER": None,
    "LIST": [],
    "NODE": None,
    "NONE": None,
    "NODE_ITEMS": [],
}

classes = {
    bpy.types.Node: {
        "subtypes": {
            bpy.types.NodeInternal: {
                "subtypes": {
                    bpy.types.GeometryNode: {"generate_subtypes": True},
                    bpy.types.FunctionNode: {"generate_subtypes": True},
                },
            }
        },
    },
    bpy.types.NodeTree: {
        "subtypes": {
            bpy.types.GeometryNodeTree: {
                "attributes": {
                    "name": ["STRING", ""],
                    "color_tag": ["STRING", "NONE"],
                    "default_group_node_width": ["INT", 140],
                    "description": ["STRING", ""],
                    "is_modifier": ["BOOLEAN", False],
                    "is_tool": ["BOOLEAN", False],
                },
                "subtypes": {},
            }
        },
    },
    bpy.types.NodeTreeInterfaceItem: {
        "subtypes": {
            bpy.types.NodeTreeInterfacePanel: {
                "subtypes": {},
            },
            bpy.types.NodeTreeInterfaceSocket: {"generate_subtypes": True},
        },
    },
    bpy.types.NodeSocket: {
        "subtypes": {bpy.types.NodeSocketStandard: {"generate_subtypes": True}}
    },
}


def attributes_for(cls, base_class):
    base_attributes = (
        [prop.identifier for prop in base_class.bl_rna.properties] if base_class else []
    )
    return {
        prop.identifier: prop.type
        for prop in cls.bl_rna.properties
        if prop.identifier not in base_attributes
    }


def subtypes_with_attributes(subtype_classes, base_class):
    return


def attributes_dict_for(
    curr_class: type, params: dict[str, Any], base_class=None
) -> Any:
    attributes = params.get(
        "attributes", attributes_for(cls=curr_class, base_class=base_class)
    )
    if params.get("generate_subtypes", False):
        subtypes = {
            cls.__name__: attributes_dict_for(
                cls, params={"subtypes": {}}, base_class=curr_class
            )
            for cls in curr_class.__subclasses__()
        }
    else:
        subtypes = (
            {
                cls.__name__: attributes_dict_for(cls, params=p, base_class=curr_class)
                for cls, p in params.get("subtypes", {}).items()
            },
        )

    return [attributes, subtypes] if subtypes else [attributes]


def generate_attributes_dict():
    return {
        "Element": [
            {},
            {
                cls.__name__: attributes_dict_for(curr_class=cls, params=params)
                for cls, params in classes.items()
            },
        ]
    }
