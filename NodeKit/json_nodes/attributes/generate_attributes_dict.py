import bpy
from typing import Any
from pprint import pprint
from .base_dict import CLASSES
import os
import logging
import inspect

log = logging.getLogger(__name__)

all_prop_types = set()
all_attribute_types = set()


def _prop_type(cls: type, prop: bpy.types.Property) -> str:
    all_prop_types.add(prop.type)

    match prop.type:
        case "FLOAT":
            if prop.is_array:
                all_attribute_types.add("LIST")
                return "LIST"
            else:
                all_attribute_types.add("FLOAT")
                return "FLOAT"
        case "COLLECTION":
            all_attribute_types.add("ITEMS")
            return "ITEMS"
        case "POINTER":
            type_identifier = prop.fixed_type.identifier.upper()
            if type_identifier not in (
                "NODE",
                "NODETREE",
                "OBJECT",
                "MATERIAL",
                "IMAGE",
                "COLLECTION",
            ):
                type_identifier = "NONE"
            all_attribute_types.add(type_identifier)
            return type_identifier
        case _:
            all_attribute_types.add(prop.type)
            return prop.type


def _attributes_for(
    cls: type, base_class: type | None, exclude_keywords
) -> dict[str, Any]:
    base_attributes = (
        [prop.identifier for prop in base_class.bl_rna.properties] if base_class else []
    )
    return {
        prop.identifier: _prop_type(cls, prop)
        for prop in cls.bl_rna.properties
        if prop.identifier not in base_attributes
        and not [True for keyword in exclude_keywords if keyword in prop.identifier]
    }


def _attributes_dict_for(
    curr_class: type,
    params: dict[str, Any] = {},
    base_class: type | None = None,
) -> list[dict[str, Any]] | list[tuple[dict[str, Any], dict[str, Any]]]:
    log.debug(
        f"Generating attributes for {curr_class.__name__} with base class {base_class.__name__ if base_class else 'None'}"
    )
    attributes = params.get(
        "attributes",
        _attributes_for(
            cls=curr_class,
            base_class=base_class,
            exclude_keywords=params.get("exclude_attribute_keywords", []),
        ),
    )
    if params.get("find_subtypes", False):
        subtypes = {
            cls_name: _attributes_dict_for(
                cls,
                base_class=curr_class,
                params=params.get("subtype_params", {}),
            )
            for cls_name, cls in inspect.getmembers(bpy.types, inspect.isclass)
            if issubclass(cls, curr_class) and cls != curr_class
        }
    else:
        subtypes = {
            cls.__name__: _attributes_dict_for(cls, params=p, base_class=curr_class)
            for cls, p in params.get("subtypes", {}).items()
        }

    return (
        {"attributes": attributes, "subtypes": subtypes}
        if subtypes
        else {"attributes": attributes}
    )


def generate_attributes_dict() -> dict[str, Any]:
    log.info("Generating attributes dictionary...")
    attributes = {
        cls.__name__: _attributes_dict_for(curr_class=cls, params=params)
        for cls, params in CLASSES.items()
    }

    file_path = os.path.join(os.path.dirname(__file__), "attributes_dict.py")
    log.info(f"Saving attributes dictionary in {file_path}")
    with open(file_path, "w") as file:
        file.write("ATTRIBUTES = ")
        pprint(attributes, stream=file)
        file.write("\nALL_ATTRIBUTE_TYPES = ")
        pprint(sorted(all_attribute_types), stream=file)
    log.info("Attributes dictionary generated successfully.")
    return attributes
