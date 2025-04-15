import bpy
import uuid

from typing import Any
from bpy.types import NodeTree, Node, NodeSocket


class Data:
    def __init__(self, element: NodeTree = None, json_dict: dict[str, Any] = None):

        if json_dict:
            self.name = json_dict["name"]
            self.uuid = json_dict["uuid"]
            return
        if element:
            self.uuid = element["uuid"] if "uuid" in element else str(
                uuid.uuid4())
            self.name = element.name

            self.type = element.type


class NodeTreeData(Data):

    def __init__(self, node_tree: NodeTree = None, json_dict: dict[str, Any] = None):

        if json_dict:
            super().__init__(json_dict)
            self.nodes = [NodeData(node) for node in json_dict["nodes"]]
            return
        if node_tree:
            super().__init__(node_tree)
            self.nodes = [NodeData(node) for node in node_tree.nodes]

    @classmethod
    def from_dict(cls, json_dict: dict[str, Any]):
        return cls(json_dict=json_dict)

    @classmethod
    def from_node_tree(cls, node_tree):
        return cls(node_tree=node_tree)

    def as_dict(self):
        attributes = vars(self)
        attributes["nodes"] = [node.as_dict() for node in self.nodes]
        return attributes

    def as_node_tree(self):
        return 1


class NodeData(Data):

    def __init__(self, node=None, node_dict=None):
        if node:
            super().__init__(node)
            self.label = node.label
            self.location = (node.location.x, node.location.y)
            self.dimensions = (node.dimensions.x, node.dimensions.y)
            self.inputs = [SocketData(input, self.uuid)
                           for input in node.inputs]
            self.outputs = [SocketData(output, self.uuid)
                            for output in node.outputs]
        elif node_dict:
            super().__init__(node_dict)
            self.label = node_dict["label"]
            self.location = (node_dict["location"][0],
                             node_dict["location"][1])
            self.dimensions = (node_dict["dimensions"][0],
                               node_dict["dimensions"][1])
            self.inputs = [SocketData(input) for input in node_dict["inputs"]]
            self.outputs = [SocketData(output)
                            for output in node_dict["outputs"]]

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
