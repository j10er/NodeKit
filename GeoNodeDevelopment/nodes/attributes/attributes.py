import bpy
from typing import Any
from .attributes_dict import DEFAULTS
import logging

log = logging.getLogger(__name__.split(".")[2])


def get_item_info(item: Any) -> list[str]:
    if not hasattr(item, "name"):
        return []
    if not hasattr(item, "socket_type"):
        return [item.name]

    return [item.socket_type, item.name]


def add_item(item_info: list[str], collection: Any) -> Any:
    match len(item_info):
        case 0:
            collection.new()
        case 1:
            return collection.new(item_info[0])
        case 2:
            return collection.new(item_info[0], item_info[1])


none = lambda element, name, value: None

GETTER = {
    "FLOAT": float,
    "INT": int,
    "BOOLEAN": bool,
    "LIST": list,
    "STRING": str,
    "NODE": lambda node: node.name if node else None,
    "NODETREE": lambda node_tree: node_tree["uuid"] if node_tree else None,
    "NONE": lambda x: None,
    "COLLECTION": lambda items: [get_item_info(item) for item in items],
}


SETTER = {
    "STRING": setattr,
    "INT": setattr,
    "FLOAT": setattr,
    "BOOLEAN": setattr,
    "LIST": setattr,
    "NODE": none,
    "NODETREE": lambda element, name, value: setattr(
        element,
        name,
        next((tree for tree in bpy.data.node_groups if tree["uuid"] == value), None),
    ),
    "NONE": none,
    "COLLECTION": lambda element, name, value: [
        add_item(item, getattr(element, name))
        for item in value
        if item[1] not in getattr(element, name)
    ],
}


def from_element(element: Any, defaults: dict[str, Any]) -> dict[str, Any]:
    attribute_dict = {}
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            continue
        value = GETTER[attr_type](getattr(element, attr_name))

        attribute_dict[attr_name] = value
    return attribute_dict


def from_dict(element_dict: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
    return {
        name: element_dict.get(name, default_value)
        for name, (attr_type, default_value) in defaults.items()
    }


def to_dict(attributes: dict[str, Any], defaults: dict[str, Any]) -> dict[str, Any]:
    for name in list(attributes.keys()):
        if name not in defaults:
            print(f"Warning: Attribute '{name}' not found in defaults")
    return {
        name: value for name, value in attributes.items() if defaults[name][1] != value
    }


def set_on_element(
    element: Any,
    attributes: dict[str, Any],
    defaults: dict[str, Any],
):
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            print(
                f"Error: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue

        value = attributes[attr_name] if attr_name in attributes else default_value
        readonly = element.__class__.bl_rna.properties[attr_name].is_readonly
        if not readonly or attr_type == "COLLECTION":
            setter = SETTER[attr_type]
            try:
                setter(element, attr_name, value)
            except Exception as e:
                print(
                    f"Error: attribute '{attr_name}' on {element} of type {type(element)}: {e}"
                )
    return element


def find_class_path(
    target_name: str, subtype=DEFAULTS["Element"], path=None
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


def defaults_for(subtype_class: str, base_class: str = "Element") -> dict[str, Any]:
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
