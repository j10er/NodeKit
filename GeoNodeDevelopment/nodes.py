import bpy


def add_to_object(object, group_name):
    modifier = object.modifiers.new(group_name, "NODES")
    modifier.node_group = bpy.data.node_groups[group_name]
    return


def set_inputs(modifier, inputs):
    interface_items = modifier.node_group.interface.items_tree
    for input_name in inputs.keys():
        if input_name in interface_items.keys():
            identifier = interface_items[input_name].identifier
            modifier[identifier] = inputs[input_name]
        else:
            print(
                f"Input '{input_name}' not found in node group interface of group {modifier.node_group.name}"
            )
