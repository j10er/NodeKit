import bpy
import uuid
from bpy.types import (
    NodeTree,
    NodeSocket,
    NodeTreeInterfaceItem,
)
from typing import Any
import datetime
from .interface_data import InterfaceItemData


class NodeTreeData:

    def __init__(
        self,
        name: str,
        uuid: str,
        nodes: dict[str, Any],
        interface_items: list[NodeTreeInterfaceItem],
    ):
        self.name = name
        self.uuid = uuid
        self.nodes = nodes
        self.interface_items = interface_items

    @classmethod
    def from_tree(cls, tree: NodeTree):
        if not hasattr(tree, "uuid"):
            tree["uuid"] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input["index"] = i
            for i, output in enumerate(node.outputs):
                output["index"] = i

        return cls(
            name=tree.name,
            uuid=tree["uuid"],
            nodes={node.name: NodeData.from_node(node) for node in tree.nodes},
            interface_items=[
                InterfaceItemData.from_item(item)
                for item in tree.interface.items_tree
                if item.parent.index == -1
            ],
        )

    @classmethod
    def from_dict(cls, tree_dict: dict[str, Any]):
        return cls(
            name=tree_dict["name"],
            uuid=tree_dict["uuid"],
            nodes={
                name: NodeData.from_dict(node_dict)
                for name, node_dict in tree_dict["nodes"].items()
            },
            interface_items=[
                InterfaceItemData.from_dict(item)
                for item in tree_dict["interface_items"]
            ],
        )

    def to_dict(self):
        return {
            "name": self.name,
            "uuid": self.uuid,
            "nodes": {
                name: node_data.to_dict() for name, node_data in self.nodes.items()
            },
            "interface_items": [
                item_data.to_dict() for item_data in self.interface_items
            ],
        }

    def to_tree(self):
        print(f"Creating new node tree: {self.name} with UUID: {self.uuid}")
        tree = bpy.data.node_groups.new(
            name=self.name + str(datetime.datetime.now()), type="GeometryNodeTree"
        )
        tree["uuid"] = self.uuid

        for item_data in self.interface_items:
            item = item_data.to_item(tree.interface)

        for node_data in self.nodes.values():
            node = node_data.to_node(tree)

        for node_data in self.nodes.values():
            for output_data in node_data.outputs.values():
                if output_data.to_node and output_data.to_socket_index:
                    from_node = tree.nodes.get(node_data.name)
                    from_socket = from_node.outputs[output_data.index]

                    for i in range(len(output_data.to_node)):
                        to_node = tree.nodes.get(output_data.to_node[i])
                        to_socket = to_node.inputs[output_data.to_socket_index[i]]

                        tree.links.new(from_socket, to_socket)
        return tree


class NodeData:
    def __init__(
        self,
        name: str,
        label: str,
        bl_idname: str,
        location: list[float],
        width: float,
        inputs: dict[str, "SocketData"],
        outputs: dict[str, "SocketData"],
    ):
        self.name = name
        self.label = label
        self.bl_idname = bl_idname
        self.location = location
        self.width = width
        self.inputs = inputs
        self.outputs = outputs

    @classmethod
    def from_node(cls, node) -> "NodeData":
        return cls(
            name=node.name,
            label=node.label,
            bl_idname=node.bl_idname,
            location=list(node.location),
            width=node.width,
            inputs={
                input.identifier: SocketData.from_socket(input)
                for input in node.inputs
                if not input.bl_idname == "NodeSocketVirtual"
            },
            outputs={
                output.identifier: SocketData.from_socket(output)
                for output in node.outputs
                if not output.bl_idname == "NodeSocketVirtual"
            },
        )

    @classmethod
    def from_dict(cls, node_dict: dict[str, Any]) -> "NodeData":
        return cls(
            name=node_dict["name"],
            label=node_dict.get("label", ""),
            bl_idname=node_dict["bl_idname"],
            location=node_dict["location"],
            width=node_dict.get("width", 140),
            inputs={
                identifier: SocketData.from_dict(s)
                for identifier, s in node_dict["inputs"].items()
            },
            outputs={
                identifier: SocketData.from_dict(s)
                for identifier, s in node_dict["outputs"].items()
            },
        )

    def to_dict(self):
        return {
            "name": self.name,
            **({"label": self.label} if self.label != "" else {}),
            "bl_idname": self.bl_idname,
            "location": self.location,
            **({"width": self.width} if self.width != 140 else {}),
            "inputs": {
                identifier: socket_data.to_dict()
                for identifier, socket_data in self.inputs.items()
            },
            "outputs": {
                identifier: socket_data.to_dict()
                for identifier, socket_data in self.outputs.items()
            },
        }

    def to_node(self, tree):
        node = tree.nodes.new(
            type=self.bl_idname,
        )
        node.name = self.name
        node.label = self.label
        node.location = self.location
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
    def __init__(
        self,
        name: str,
        identifier: str,
        default_value: Any,
        index: int,
        to_socket_index: list[int],
        to_node: list[str],
    ):
        self.identifier = identifier
        self.default_value = default_value
        self.to_socket_index = to_socket_index
        self.to_node = to_node
        self.name = name
        self.index = index

    @classmethod
    def from_socket(cls, socket: NodeSocket) -> "SocketData":
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

        converter = SOCKET_TO_PYTHON.get(socket.type)
        default_value = (
            converter(socket.default_value)
            if hasattr(socket, "default_value") and converter
            else None
        )
        to_socket_index = []
        to_node = []
        for link in socket.links:
            if link.from_socket.identifier == socket.identifier:
                to_socket_index.append(link.to_socket["index"])
                to_node.append(link.to_node.name)

        return cls(
            identifier=socket.identifier,
            default_value=default_value,
            to_socket_index=to_socket_index,
            to_node=to_node,
            name=socket.name,
            index=socket["index"],
        )

    @classmethod
    def from_dict(cls, socket_dict: dict[str, Any]) -> "SocketData":
        return cls(
            identifier=socket_dict["identifier"],
            default_value=socket_dict.get("default_value", None),
            to_socket_index=socket_dict.get("to_socket_index", []),
            to_node=socket_dict.get("to_node", []),
            name=socket_dict["name"],
            index=socket_dict["index"],
        )

    def to_dict(self):
        return {
            "identifier": self.identifier,
            **({"default_value": self.default_value} if self.default_value else {}),
            **(
                {"to_socket_index": self.to_socket_index}
                if self.to_socket_index
                else {}
            ),
            **({"to_node": self.to_node} if self.to_node else {}),
            "name": self.name,
            "index": self.index,
        }
