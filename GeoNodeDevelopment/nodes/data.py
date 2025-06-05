import bpy
import uuid
from bpy.types import GeometryNodeTree, NodeTree, NodeSocket
from typing import Any
import datetime


class NodeTreeData:

    def __init__(self, tree: NodeTree = None, tree_dict: dict[str, Any] = None):
        if tree:
            if not hasattr(tree, "uuid"):
                tree["uuid"] = str(uuid.uuid4())
            for node in tree.nodes:
                if not hasattr(node, "uuid"):
                    node["uuid"] = str(uuid.uuid4())
            self.init_from_tree(tree)
        elif tree_dict:
            self.init_from_dict(tree_dict)
        else:
            Exception("Either group or group_dict must be provided")

    def init_from_tree(self, tree: NodeTree):
        self.name = tree.name
        self.uuid = tree["uuid"]
        self.nodes = {}
        for node in tree.nodes:
            self.nodes[node.name] = NodeData(node=node, links=tree.links)

    def init_from_dict(self, tree_dict: dict[str, Any]):
        self.name = tree_dict["name"]
        self.uuid = tree_dict["uuid"]
        self.nodes = {
            name: NodeData(node_dict=node_dict)
            for name, node_dict in tree_dict["nodes"].items()
        }

    def as_dict(self):
        return {
            "name": self.name,
            "uuid": self.uuid,
            "nodes": {
                name: node_data.as_dict() for name, node_data in self.nodes.items()
            },
        }

    def as_tree(self):
        tree = bpy.data.node_groups.new(
            name=self.name + str(datetime.datetime.now()), type="GeometryNodeTree"
        )
        tree["uuid"] = self.uuid

        for node_data in self.nodes.values():
            node = node_data.to_node(tree)

        for node_data in self.nodes.values():
            for output_data in node_data.outputs.values():
                if output_data.to_node and output_data.to_socket:
                    from_node = tree.nodes.get(node_data.name)
                    from_socket = from_node.outputs.get(output_data.identifier)
                    to_node = tree.nodes.get(output_data.to_node)
                    to_socket = to_node.inputs.get(output_data.to_socket)
                    print(
                        f"Linking {node_data.name}.{output_data.identifier} to {output_data.to_node}.{output_data.to_socket}"
                    )
                    tree.links.new(from_socket, to_socket)

        return tree


class NodeData:

    def __init__(self, node=None, links=None, node_dict=None):
        if node:
            self.init_from_node(node, links)
        elif node_dict:
            self.init_from_dict(node_dict)
        else:
            Exception("Either node or node_dict must be provided")

    def init_from_node(self, node, links):
        self.name = node.name
        self.label = node.label
        self.bl_idname = node.bl_idname
        self.location = list(node.location)
        self.width = node.width
        self.inputs = {}
        for input in node.inputs:
            self.inputs[input.identifier] = SocketData(socket=input)
        self.outputs = {}
        for output in node.outputs:
            self.outputs[output.identifier] = SocketData(socket=output)

        print(len(links))
        connected_links = [link for link in links if link.from_node.name == self.name]
        print(f"Node {self.name} has {len(connected_links)} connected links")
        for link in connected_links:
            self.outputs[link.from_socket.identifier].to_socket = (
                link.to_socket.identifier
            )
            self.outputs[link.from_socket.identifier].to_node = link.to_node.name

    def init_from_dict(self, node_dict):
        self.name = node_dict["name"]
        self.label = node_dict["label"]
        self.bl_idname = node_dict["bl_idname"]
        self.location = node_dict["location"]
        self.width = node_dict["width"]
        self.inputs = {
            identifier: SocketData(socket_dict=s)
            for identifier, s in node_dict["inputs"].items()
        }
        self.outputs = {
            identifier: SocketData(socket_dict=s)
            for identifier, s in node_dict["outputs"].items()
        }

    def as_dict(self):
        return {
            "name": self.name,
            "label": self.label,
            "bl_idname": self.bl_idname,
            "location": self.location,
            "width": self.width,
            "inputs": {
                identifier: socket_data.as_dict()
                for identifier, socket_data in self.inputs.items()
            },
            "outputs": {
                identifier: socket_data.as_dict()
                for identifier, socket_data in self.outputs.items()
            },
        }

    def to_node(self, tree):
        node = tree.nodes.new(type=self.bl_idname)
        node.name = self.name
        node.label = self.label
        node.location = tuple(self.location)
        node.width = self.width
        for socket_data in self.inputs.values():
            if socket_data.default_value:
                node.inputs[socket_data.identifier].default_value = (
                    socket_data.default_value
                )
        for socket_data in self.outputs.values():
            if socket_data.default_value:
                node.outputs[socket_data.identifier].default_value = (
                    socket_data.default_value
                )
        return node


class SocketData:
    def __init__(self, socket=None, socket_dict=None):
        if socket:
            self.init_from_socket(socket)
        elif socket_dict:
            self.init_from_dict(socket_dict)
        else:
            Exception("Either node or node_dict must be provided")

    def init_from_socket(self, socket):
        self.identifier = socket.identifier
        SOCKET_TO_PYTHON = {
            "VALUE": float,
            "INT": int,
            "BOOLEAN": bool,
            "VECTOR": list,
            "ROTATION": list,
            "MATRIX": list,
            "STRING": str,
            "RGBA": list,
        }
        if hasattr(socket, "default_value"):
            converter = SOCKET_TO_PYTHON.get(socket.type, lambda val: None)
            self.default_value = converter(socket.default_value)
        else:
            self.default_value = None
        self.to_socket = None
        self.to_node = None

    def init_from_dict(self, socket_dict):
        self.identifier = socket_dict["identifier"]
        self.default_value = socket_dict.get("default_value", None)
        self.to_socket = socket_dict.get("to_socket", None)
        self.to_node = socket_dict.get("to_node", None)

    def as_dict(self):
        return {
            "identifier": self.identifier,
            **({"default_value": self.default_value} if self.default_value else {}),
            **({"to_socket": self.to_socket} if self.to_socket else {}),
            **({"to_node": self.to_node} if self.to_node else {}),
        }
