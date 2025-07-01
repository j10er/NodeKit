import bpy
from typing import Dict, Any
from pathlib import Path
from pprint import pprint
from .base_attributes_dict import classes

all_prop_types = set()
all_attribute_types = set()


def convert_type(cls, prop) -> str:
    all_prop_types.add(prop.type)

    match prop.type:
        case "FLOAT":
            if prop.is_array:
                all_attribute_types.add("LIST")
                return "LIST"
            else:
                all_attribute_types.add("FLOAT")
                return "FLOAT"
        case "POINTER":
            identifier = prop.identifier.upper()
            if identifier not in ("NODE", "NODE_TREE"):
                identifier = "NONE"
            all_attribute_types.add(identifier)
            return identifier
        case "ENUM":
            all_attribute_types.add("STRING")
            return "STRING"
        case _:
            all_attribute_types.add(prop.type)
            return prop.type


def attributes_for(cls, base_class):
    base_attributes = (
        [prop.identifier for prop in base_class.bl_rna.properties] if base_class else []
    )
    return {
        prop.identifier: [
            (convert_type(cls, prop)),
            getattr(prop, "default", None),
        ]
        for prop in cls.bl_rna.properties
        if prop.identifier not in base_attributes
    }


SEARCH_EXCLUDE = ["GeometryNodeTree"]


def attributes_dict_for(
    curr_class: type, params: dict[str, Any], base_class=None
) -> Any:
    attributes = params.get(
        "attributes", attributes_for(cls=curr_class, base_class=base_class)
    )
    if params.get("find_subtypes", False):
        subtypes = {
            cls.__name__: attributes_dict_for(
                cls, params={"subtypes": {}}, base_class=curr_class
            )
            for cls in [
                getattr(bpy.types, subtype)
                for subtype in dir(bpy.types)
                if subtype.startswith(params["find_subtypes"])
                and subtype != params["find_subtypes"]
                and not subtype in SEARCH_EXCLUDE
            ]
        }
    else:
        subtypes = {
            cls.__name__: attributes_dict_for(cls, params=p, base_class=curr_class)
            for cls, p in params.get("subtypes", {}).items()
        }

    return [attributes, subtypes] if subtypes else [attributes]


def generate_attributes_dict():
    attributes = {
        "Element": [
            {},
            {
                cls.__name__: attributes_dict_for(curr_class=cls, params=params)
                for cls, params in classes.items()
            },
        ]
    }

    file_path = Path(__file__).parent / "attributes_dict.py"
    with open(file_path, "w") as file:
        file.write("DEFAULTS = ")
        pprint(attributes, stream=file)
        file.write("\nALL_ATTRIBUTE_TYPES = ")
        pprint(sorted(all_attribute_types), stream=file)
    return attributes
