from .attributes_dict import DEFAULTS
from typing import Any

GETTER = {
    "FLOAT": float,
    "INT": int,
    "BOOLEAN": bool,
    "LIST": list,
    "STRING": str,
    "NODE": lambda node: node.name,
    "NONE": lambda x: None,
    "COLLECTION": lambda items: [[item.name, item.socket_type] for item in items],
}
SETTER = {
    "STRING": setattr,
    "INT": setattr,
    "FLOAT": setattr,
    "BOOLEAN": setattr,
    "LIST": setattr,
    "NODE": lambda element, name, value: None,
    "NONE": lambda element, name, value: None,
    "COLLECTION": lambda element, name, value: [
        getattr(element, name).new(item[1], item[0])
        for item in value
        if item[0] not in getattr(element, name)
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
    attributes = {}
    for name, (attr_type, default_value) in defaults.items():
        attributes[name] = element_dict.get(name, default_value)
    return attributes


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
                f"Warning while setting: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue

        value = attributes[attr_name] if attr_name in attributes else default_value
        setter = SETTER[attr_type]
        try:
            setter(element, attr_name, value)
        except Exception as e:
            print(
                f"Error setting attribute '{attr_name}' on {element} of type {type(element)}: {e}"
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
        print(f"Warning: No class path found for {subtype_class} or {base_class}")
        return {}
    current_subtype = DEFAULTS["Element"]
    defaults = {}

    # Start with base Element attributes
    defaults.update(current_subtype[0])

    # Navigate through the class path and merge attributes
    try:
        for subtype_name in class_path:
            if len(current_subtype) < 2 or subtype_name not in current_subtype[1]:
                print(f"Warning: Subtype '{subtype_name}' not found in current path")
                break
            current_subtype = current_subtype[1][subtype_name]
            if len(current_subtype) > 0:
                defaults.update(current_subtype[0])
    except (IndexError, KeyError, TypeError) as e:
        print(f"Error navigating class path for {subtype_class}: {e}")
        return {}
    return defaults


def filter_out_keys(dictionary: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    """
    Remove specified keys from a dictionary and return a new dictionary.
    """
    return {k: v for k, v in dictionary.items() if k not in keys}
