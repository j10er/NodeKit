from .attributes_dict import DEFAULTS
from typing import Any
from pprint import pprint

CONVERTERS = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
    "list": list,
    "None": lambda x: None,
}


def get_attributes(element: Any, defaults: dict[str, list[str, Any]]) -> dict[str, Any]:

    attribute_dict = {}
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            print(
                f"Warning while getting: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue
        value = CONVERTERS[attr_type](getattr(element, attr_name))
        if value != default_value:
            attribute_dict[attr_name] = value
    return attribute_dict


def set_attributes(element: Any, attributes: dict[str, Any], defaults: dict[str, Any]):
    """
    Set the values of specified attributes on an element based on a predefined attributes dictionary.

    Args:
        attributes_dict: A dictionary containing attribute names and their default values.
        element: The object or data structure to set attributes on.
        attribute_values: A dictionary with attribute names as keys and their corresponding values.
    """
    for attr_name, (attr_type, default_value) in defaults.items():
        if not hasattr(element, attr_name):
            print(
                f"Warning while setting: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue
        value = attributes[attr_name] if attr_name in attributes else default_value
        setattr(element, attr_name, value)
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


def defaults_for(class_name: str):
    class_path = find_class_path(class_name)
    if not class_path:
        print(f"Warning: No class path found for {class_name}")
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
        print(f"Error navigating class path for {class_name}: {e}")
        return {}
    return defaults
