import bpy
from pprint import pprint


def export_groups():

    groups = bpy.data.node_groups
    pprint(group_to_dict(groups[2]))


def group_to_dict(group):
    node_infos = []
    for node in group.nodes:
        node_infos.append(node_to_dict(node))

    return node_infos


def node_to_dict(node):
    return {
        "type": node.type,
        "location": (node.location.x, node.location.y),
        "width": node.width,
        "height": node.height,
        "dimensions": node.dimensions,
        "name": node.name,
        "label": node.label,
        "inputs": node.inputs,
        "outputs": node.outputs,
        "internal_links": node.internal_links,
        "parent": node.parent,
        "use_custom_color": node.use_custom_color,
        "color": node.color,
        "select": node.select,
        "show_options": node.show_options,
        "show_preview": node.show_preview,
        "hide": node.hide,
        "mute": node.mute,
    }


def convert_color_to_obj(color):
    color_obj = {}

    if hasattr(color, "r"):
        color_obj["r"] = color.r

    if hasattr(color, "g"):
        color_obj["g"] = color.g

    if hasattr(color, "b"):
        color_obj["b"] = color.b

    if hasattr(color, "a"):
        color_obj["a"] = color.a

    return color_obj


def convert_vector_to_obj(vector_value):
    vector_obj = {}

    if hasattr(vector_value, "x"):
        vector_obj["x"] = vector_value.x

    if hasattr(vector_value, "y"):
        vector_obj["y"] = vector_value.y

    if hasattr(vector_value, "z"):
        vector_obj["z"] = vector_value.z

    if hasattr(vector_value, "w"):
        vector_obj["w"] = vector_value.w

    return vector_obj

# Convert complex types into JSON compatible formats


def convert_complex_type_to_json_format(default_value):
    if isinstance(default_value, mathutils.Vector):
        return convert_vector_to_obj(default_value)

    if isinstance(default_value, float):
        return "{}".format(default_value)

    if isinstance(default_value, bpy_types.bpy_prop_array):
        socket_array = []
        for socket_value in default_value:
            socket_array.append("{}".format(socket_value))
        return socket_array
