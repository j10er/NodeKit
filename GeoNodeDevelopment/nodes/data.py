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
from .attributes import get_attributes, set_attributes, defaults_for


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
            for output_data in node_data.outputs:
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
        attributes: dict[str, Any],
        inputs: list["SocketData"],
        outputs: list["SocketData"],
    ):
        self.attributes = attributes
        self.inputs = inputs
        self.outputs = outputs

    @classmethod
    def from_node(cls, node) -> "NodeData":
        node_attributes = get_attributes(node, defaults_for("Node"))
        return cls(
            inputs=[
                SocketData.from_socket(input)
                for input in node.inputs
                if not input.bl_idname == "NodeSocketVirtual"
            ],
            outputs=[
                SocketData.from_socket(output)
                for output in node.outputs
                if not output.bl_idname == "NodeSocketVirtual"
            ],
            attributes=node_attributes,
        )

    @classmethod
    def from_dict(cls, node_dict: dict[str, Any]) -> "NodeData":
        return cls(
            inputs=[SocketData.from_dict(s) for s in node_dict["inputs"]],
            outputs=[SocketData.from_dict(s) for s in node_dict["outputs"]],
            attributes=node_dict.get("attributes", {}),
        )

    def to_dict(self):
        return {
            "inputs": [socket_data.to_dict() for socket_data in self.inputs],
            "outputs": [socket_data.to_dict() for socket_data in self.outputs],
            **({} if not self.attributes else {"attributes": self.attributes}),
        }

    def to_node(self, tree):
        node = tree.nodes.new(
            type=self.bl_idname,
        )
        set_attributes(node, self.attributes, defaults_for("Node"))

        for socket_data in self.inputs:
            set_attributes(
                node.inputs[socket_data.index],
                socket_data.attributes,
                defaults_for("NodeSocket"),
            )
        for socket_data in self.outputs:
            set_attributes(
                node.outputs[socket_data.index],
                socket_data.attributes,
                defaults_for("NodeSocket"),
            )
        return node


class SocketData:
    def __init__(
        self,
        index: int,
        to_socket_index: list[int],
        to_node: list[str],
        attributes: dict[str, Any],
    ):
        self.to_socket_index = to_socket_index
        self.to_node = to_node
        self.index = index
        self.attributes = attributes

    @classmethod
    def from_socket(cls, socket: NodeSocket) -> "SocketData":
        to_socket_index = []
        to_node = []
        for link in socket.links:
            if link.from_socket == socket:
                to_socket_index.append(link.to_socket["index"])
                to_node.append(link.to_node.name)

        socket_attributes = get_attributes(socket, defaults_for(socket.bl_idname))

        return cls(
            to_socket_index=to_socket_index,
            to_node=to_node,
            index=socket["index"],
            attributes=socket_attributes,
        )

    @classmethod
    def from_dict(cls, socket_dict: dict[str, Any]) -> "SocketData":
        return cls(
            to_socket_index=socket_dict.get("to_socket_index", []),
            to_node=socket_dict.get("to_node", []),
            index=socket_dict["index"],
            attributes=socket_dict.get("attributes", {}),
        )

    def to_dict(self):
        return {
            **(
                {"to_socket_index": self.to_socket_index}
                if self.to_socket_index
                else {}
            ),
            **({"to_node": self.to_node} if self.to_node else {}),
            "index": self.index,
            **({} if not self.attributes else {"attributes": self.attributes}),
        }
