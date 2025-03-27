import bpy
import uuid


class Data:
    def __init__(self, element):
        self.uuid = element["uuid"] if "uuid" in element else str(uuid.uuid4())
        self.name = element.name

        self.type = element.type


class NodeTreeData(Data):

    def __init__(self, node_tree):
        super().__init__(node_tree)
        self.nodes = [NodeData(node) for node in node_tree.nodes]
        # self.links = [LinkData(link) for link in node_tree.links]

    def as_dict(self):
        attributes = vars(self)
        attributes["nodes"] = [node.as_dict() for node in self.nodes]
        return attributes


class NodeData(Data):

    def __init__(self, node):
        super().__init__(node)
        self.label = node.label
        self.location = (node.location.x, node.location.y)
        self.dimensions = (node.dimensions.x, node.dimensions.y)
        self.inputs = [SocketData(input, self.uuid) for input in node.inputs]
        self.outputs = [SocketData(output, self.uuid)
                        for output in node.outputs]

        # self.inputs = [input_to_dict(input) for input in node.inputs]
        # self.outputs = [output_to_dict(output) for output in node.outputs]
        # self.internal_links = [link_to_dict(link)
        # for link in node.internal_links]
        # self.parent = node.parent
        # self.use_custom_color = node.use_custom_color
        # self.color = (node.color.r, node.color.g, node.color.b)
        # self.select = node.select
        # self.show_options = node.show_options
        # self.show_preview = node.show_preview
        # self.hide = node.hide
        # self.mute = node.mute

    def as_dict(self):
        attributes = vars(self)
        attributes["inputs"] = [input.as_dict() for input in self.inputs]
        attributes["outputs"] = [output.as_dict() for output in self.outputs]
        return attributes


class SocketData(Data):
    def __init__(self, socket, uuid):
        super().__init__(socket)
        self.node_uuid = uuid
        self.label = socket.label
        if hasattr(socket, "default_value"):
            self.default_value = str(socket.default_value)

    def as_dict(self):
        return vars(self)
