import bpy
from typing import Any, Callable
from .attributes_dict import DEFAULTS

import logging
from inspect import signature

log = logging.getLogger(__name__)


def get_item_info(item: Any) -> list[str]:
    if not hasattr(item, "name"):
        return []
    if hasattr(item, "socket_type"):
        return [item.socket_type, item.name]
    if hasattr(item, "data_type"):
        return [ATTRIBUTE_TYPE_MAPPING[item.data_type], item.name]

    return [item.name]


ATTRIBUTE_TYPE_MAPPING = {
    "FLOAT": "FLOAT",
    "INT": "INT",
    "FLOAT_VECTOR": "VECTOR",
    "FLOAT_COLOR": "COLOR",
    "BYTE_COLOR": "COLOR",
    "STRING": "STRING",
    "BOOLEAN": "BOOLEAN",
    "FLOAT2": "VECTOR",
    "INT8": "INT",
    "INT16_2D": "VECTOR",
    "INT32_2D": "VECTOR",
    "QUATERNION": "ROTATION",
    "FLOAT4X4": "MATRIX",
}


def set_items(element, name, value):
    log.debug(f"Setting collection {name} on {element.name} with value: {value}")
    collection = getattr(element, name)
    collection.clear()
    for item_info in value:
        match len(item_info):
            case 0:
                collection.new()
            case 1:
                log.debug(
                    f"Adding item {item_info[0]} to collection {name} on {element.name}"
                )
                collection.new(item_info[0])
            case 2:
                collection.new(item_info[0], item_info[1])


none = lambda element, name, value: None


def get_pointer(element: Any) -> str:
    return element["uuid"] if element else None


def set_pointer(collection_name: str) -> Callable[[Any, str, str], None]:
    return lambda element, name, uuid: setattr(
        element,
        name,
        next(
            o for o in getattr(bpy.data, collection_name) if o.get("uuid", "") == uuid
        ),
    )


GETTER = {
    "FLOAT": float,
    "INT": int,
    "BOOLEAN": bool,
    "LIST": list,
    "STRING": str,
    "ENUM": str,
    "NODE": lambda node: node.name if node else None,
    "NODETREE": get_pointer,
    "OBJECT": get_pointer,
    "MATERIAL": get_pointer,
    "IMAGE": get_pointer,
    "COLLECTION": get_pointer,
    "NONE": lambda x: None,
    "ITEMS": lambda items: [get_item_info(item) for item in items],
}


SETTER = {
    "STRING": setattr,
    "INT": setattr,
    "FLOAT": setattr,
    "BOOLEAN": setattr,
    "ENUM": setattr,
    "LIST": setattr,
    "NODE": none,
    "NODETREE": set_pointer("node_groups"),
    "OBJECT": set_pointer("objects"),
    "MATERIAL": set_pointer("materials"),
    "IMAGE": set_pointer("images"),
    "COLLECTION": set_pointer("collections"),
    "NONE": none,
    "ITEMS": set_items,
}


def from_element(element: Any, defaults: dict[str, tuple[str, Any]]) -> dict[str, Any]:
    attribute_dict = {}
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            continue
        value = GETTER[attr_type](getattr(element, attr_name))

        attribute_dict[attr_name] = value
    return attribute_dict


def from_dict(
    element_dict: dict[str, Any], defaults: dict[str, tuple[str, Any]]
) -> dict[str, Any]:
    return {
        name: element_dict.get(name, default_value)
        for name, (attr_type, default_value) in defaults.items()
    }


def to_dict(
    attributes: dict[str, Any], defaults: dict[str, tuple[str, Any]]
) -> dict[str, Any]:
    for name in list(attributes.keys()):
        if name not in defaults:
            log.warning(f"Attribute '{name}' not found in defaults")
    return {
        name: value for name, value in attributes.items() if defaults[name][1] != value
    }


def set_on_element(
    element: Any,
    attributes: dict[str, Any],
    defaults: dict[str, tuple[str, Any]],
) -> Any:
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            log.warning(
                f"{element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue

        value = attributes[attr_name] if attr_name in attributes else default_value
        readonly = element.__class__.bl_rna.properties[attr_name].is_readonly
        if value != default_value and (not readonly or attr_type == "ITEMS"):

            setter = SETTER[attr_type]
            try:
                setter(element, attr_name, value)
            except Exception as e:
                log.warning(
                    f"Error when setting attribute '{attr_name}' on element '{element.name}' of type {type(element).__name__}: {e}"
                )
    return element


def find_class_path(
    target_name: str,
    subtype: Any = DEFAULTS["Element"],
    path: list[str] | None = None,
) -> list[str]:
    if path is None:
        path = []

    for name, subtype_data in subtype[1].items() if len(subtype) > 1 else []:
        if name == target_name:
            return path + [name]
        result = find_class_path(target_name, subtype_data, path + [name])
        if result:
            return result
    return []


def defaults_for(
    subtype_class: str, base_class: str = "Element"
) -> dict[str, tuple[str, Any]]:
    class_path = find_class_path(subtype_class)
    if not class_path:
        class_path = find_class_path(base_class)
    if not class_path:
        print(f"Error: No class path found for {subtype_class} or {base_class}")
        return {}
    current_subtype = DEFAULTS["Element"]
    defaults = {}

    defaults.update(current_subtype[0])

    for subtype_name in class_path:
        if len(current_subtype) < 2 or subtype_name not in current_subtype[1]:
            print(f"Error: Subtype '{subtype_name}' not found in current path")
            break
        current_subtype = current_subtype[1][subtype_name]
        if len(current_subtype) > 0:
            defaults.update(current_subtype[0])
    return defaults
