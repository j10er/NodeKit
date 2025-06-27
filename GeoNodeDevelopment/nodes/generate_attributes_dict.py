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
    bpy.types.bpy_struct: {
        bpy.types.Node: {
            bpy.types.NodeInternal: {
                bpy.types.GeometryNode: False,
                bpy.types.FunctionNode: True,
            }
        },
        bpy.types.NodeTree: {bpy.types.GeometryNodeTree: False},
        bpy.types.NodeTreeInterfaceItem: {
            bpy.types.NodeTreeInterfaceSocket: True,
            bpy.types.NodeTreeInterfacePanel: False,
        },
        bpy.types.NodeSocket: True,
    }
}


def generate_attributes_for(
    current_class: type, base_class: type, values: Any
) -> Dict[str, Union[str, List[Any]]]:
    attributes = {}
    if type(values) is not dict:
        if values == True:
            return {
                cls.__name__: generate_attributes_for(
                    current_class=cls, base_class=current_class, values=False
                )
                for cls in current_class.__subclasses__()
            }
        elif values == False:
            base_attributes = [prop.identifier for prop in base_class.bl_rna.properties]
            return {attr_name: [prop.type, defaults[prop.type]] for attr_name, prop in base_class.bl_rna.properties.items() if attr_name not in base_attributes}
    elif type(values) is dict:
        return {cls.}generate_attributes_for(

    return attributes


# Keep the original simple function for backward compatibility
def generate_simple_attributes_dict():
    base_classes = [bpy.types.GeometryNode]
    attributes = {}
    for base_class in base_classes:
        subtypes = {}
        base_attributes =
        for cls in base_class.__subclasses__():
            subtypes[cls.__name__] = {
                prop.identifier: prop.type
                for prop in cls.bl_rna.properties
                if prop.identifier not in base_attributes
            }
        attributes[base_class.__name__] = [{}, subtypes]
    return attributes
