import logging
from inspect import signature
from typing import Any, Callable

import bpy

from ... import config
from .attributes_dict import ATTRIBUTES

log = logging.getLogger(__name__)


def _get_item_info(item: Any) -> list[str]:
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


def _get_pointer(element: Any) -> str:
    return element["uuid"] if element else None


def _set_items(element, name, value):
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


_set_skip = lambda element, name, value: None


def _set_pointer(collection_name: str) -> Callable[[Any, str, str], None]:
    return lambda element, name, uuid: setattr(
        element,
        name,
        next(
            (
                o
                for o in getattr(bpy.data, collection_name)
                if o.get("uuid", "") == uuid
            ),
            None,
        ),
    )


def _set_node(element, attr_name, value):

    tree = element.id_data
    if value not in tree.nodes:
        log.warning(
            f"Node {value} not found in tree {tree.name} when setting attribute {attr_name} on {element.name}"
        )
        return
    node = tree.nodes.get(value)
    if attr_name == "paired_output":
        # This should be a zone node (like ForEachGeometryElementInput), so we need to set the paired output
        log.debug(f"Pairing zone node {element.name} with output {node.name}")
        element.pair_with_output(node)
    else:
        setattr(element, attr_name, node)


GETTER = {
    "FLOAT": float,
    "INT": int,
    "BOOLEAN": bool,
    "LIST": list,
    "STRING": str,
    "ENUM": str,
    "NODE": lambda node: node.name if node else None,
    "NODETREE": _get_pointer,
    "OBJECT": _get_pointer,
    "MATERIAL": _get_pointer,
    "IMAGE": _get_pointer,
    "COLLECTION": _get_pointer,
    "NONE": lambda x: None,
    "ITEMS": lambda items: [_get_item_info(item) for item in items],
}


SETTER = {
    "STRING": setattr,
    "INT": setattr,
    "FLOAT": setattr,
    "BOOLEAN": setattr,
    "ENUM": setattr,
    "LIST": setattr,
    "NODE": _set_node,
    "NODETREE": _set_pointer("node_groups"),
    "OBJECT": _set_pointer("objects"),
    "MATERIAL": _set_pointer("materials"),
    "IMAGE": _set_pointer("images"),
    "COLLECTION": _set_pointer("collections"),
    "NONE": _set_skip,
    "ITEMS": _set_items,
}


def from_element(element: Any, attribute_types: dict[str, str]) -> dict[str, Any]:
    attributes = {}
    for attr_name, attr_type in attribute_types.items():
        if not hasattr(element, attr_name):
            log.warning(
                f"Error when trying to get attribute value: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue
        value = GETTER[attr_type](getattr(element, attr_name))

        attributes[attr_name] = value
    return attributes


IGNORE_ATTRIBUTES_NAMES = ["bl_idname"]
IGNORE_READONLY_ATTRIBUTE_NAMES = ["paired_output"]
IGNORE_READONLY_ATTRIBUTE_TYPES = ["ITEMS"]


def from_dict(
    element_dict: dict[str, Any], attribute_types: dict[str, str]
) -> dict[str, Any]:
    return {
        attr_name: value
        for attr_name, value in element_dict.items()
        if attr_name in attribute_types
    }


def set_on_element(
    element: Any,
    attributes: dict[str, str],
    attribute_types: dict[str, str],
) -> Any:
    for attr_name, attr_type in attribute_types.items():

        if not hasattr(element, attr_name):
            log.warning(
                f"Error when trying to set attribute value: {element} of type {type(element)} has no attribute '{attr_name}'"
            )
            continue

        value = attributes[attr_name]
        readonly = element.__class__.bl_rna.properties[attr_name].is_readonly

        if (
            not readonly
            or attr_type in IGNORE_READONLY_ATTRIBUTE_TYPES
            or attr_name in IGNORE_READONLY_ATTRIBUTE_NAMES
        ) and attr_name not in IGNORE_ATTRIBUTES_NAMES:
            # Only set the attribute if it is different from the current value
            current_value = GETTER[attr_type](getattr(element, attr_name))
            if value != current_value:
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
    subtype: Any,
    path: list[str] = [],
) -> list[str]:

    subtype_dict = subtype.get("subtypes", {})
    if target_name in subtype_dict:
        return path + [target_name]

    # Prioritize classes that contain the target name
    for name in subtype_dict:
        if target_name.startswith(name):
            return find_class_path(target_name, subtype_dict[name], path + [name])

    # Otherwise, search recursively
    for name in subtype_dict:
        result = find_class_path(target_name, subtype_dict[name], path + [name])
        if result:
            return result

    return []


def types_for(base_class_name: str, class_name: str = "") -> dict[str, str]:

    if class_name == "":
        class_path = []
    else:
        class_path = find_class_path(
            target_name=class_name, subtype=ATTRIBUTES[base_class_name]
        )

        if not class_path:
            log.error(f"Error: No class path found for {class_name}")
            return {}

    attribute_types = {}
    subtype_dict = ATTRIBUTES[base_class_name]
    attribute_types.update(subtype_dict.get("attributes", {}))
    for subtype_name in class_path:
        subtype_dict = subtype_dict["subtypes"].get(subtype_name, {})
        attribute_types.update(subtype_dict.get("attributes", {}))
    return attribute_types
