import bpy
import uuid
from bpy.types import (
    Node,
    NodeTree,
    NodeSocket,
    NodeTreeInterfaceItem,
)
from typing import Any, Union
import datetime
from .interface_data import InterfaceItemData
from . import attributes
from .data_base_class import Data


class NodeTreeData(Data):

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        uuid: str,
        nodes: dict[str, "NodeData"],
        interface_items: list[InterfaceItemData],
    ) -> None:
        super().__init__(attributes, defaults)
        self.uuid = uuid
        self.nodes = nodes
        self.interface_items = interface_items

    @classmethod
    def from_tree(cls, tree: NodeTree) -> "NodeTreeData":
        if not hasattr(tree, "uuid"):
            tree["uuid"] = str(uuid.uuid4())
        for node in tree.nodes:
            for i, input in enumerate(node.inputs):
                input["index"] = i
            for i, output in enumerate(node.outputs):
                output["index"] = i

        defaults = attributes.defaults_for("NodeTree")
        return cls(
            attributes=attributes.from_element(tree, defaults),
            defaults=defaults,
            uuid=tree["uuid"],
            nodes={node.name: NodeData.from_node(node) for node in tree.nodes},
            interface_items=[
                InterfaceItemData.from_item(item)
                for item in tree.interface.items_tree
                if item.parent.index == -1
            ],
        )

    @classmethod
    def from_dict(cls, tree_dict: dict[str, Any]) -> "NodeTreeData":
        defaults = attributes.defaults_for("NodeTree")
        return cls(
            attributes=attributes.from_dict(tree_dict, defaults),
            defaults=defaults,
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

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, self.defaults),
            "uuid": self.uuid,
            "nodes": {
                name: node_data.to_dict() for name, node_data in self.nodes.items()
            },
            "interface_items": [
                item_data.to_dict() for item_data in self.interface_items
            ],
        }

    def to_tree(self) -> NodeTree:
        print(f"Creating new node tree: {self.name}...")
        tree = bpy.data.node_groups.new(
            name=self.attributes["name"] + str(datetime.datetime.now()),
            type="GeometryNodeTree",
        )
        tree["uuid"] = self.uuid
        print(f"Created node tree {tree.name} with UUID: {tree['uuid']}")
        attributes.set_on_element(tree, self.attributes, self.defaults)
        for item_data in self.interface_items:
            item = item_data.to_item(tree.interface)
        print(
            f"Created {len(tree.interface.items_tree)} interface items for tree {tree.name}"
        )
        for node_data in self.nodes.values():
            node = node_data.to_node(tree)
        print(f"Created {len(tree.nodes)} nodes for tree {tree.name}")
        for node_data in self.nodes.values():
            if hasattr(node_data, "paired_output"):
                tree.nodes[node_data.name].pair_with_output(
                    tree.nodes[node_data.paired_output]
                )
        for node_data in self.nodes.values():
            node = tree.nodes[node_data.name]
            node_data.set_socket_attributes(node)

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


class NodeData(Data):

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        inputs: list["SocketData"],
        outputs: list["SocketData"],
    ) -> None:
        super().__init__(attributes, defaults)
        self.inputs = inputs
        self.outputs = outputs

    @classmethod
    def from_node(cls, node: Node) -> "NodeData":
        defaults = attributes.defaults_for(
            base_class="Node", subtype_class=node.bl_idname
        )
        return cls(
            attributes=attributes.from_element(node, defaults),
            defaults=defaults,
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
        )

    @classmethod
    def from_dict(cls, node_dict: dict[str, Any]) -> "NodeData":
        defaults = attributes.defaults_for(
            base_class="Node", subtype_class=node_dict["bl_idname"]
        )
        return cls(
            attributes=attributes.from_dict(node_dict, defaults),
            defaults=defaults,
            inputs=[SocketData.from_dict(s) for s in node_dict.get("inputs", [])],
            outputs=[SocketData.from_dict(s) for s in node_dict.get("outputs", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        inputs = [
            socket_data.to_dict()
            for socket_data in self.inputs
            if "default_value" in socket_data.to_dict()
            or "to_socket_index" in socket_data.to_dict()
        ]
        outputs = [
            socket_data.to_dict()
            for socket_data in self.outputs
            if "default_value" in socket_data.to_dict()
            or "to_socket_index" in socket_data.to_dict()
        ]
        return {
            **attributes.to_dict(self.attributes, self.defaults),
            **({"inputs": inputs} if inputs else {}),
            **({"outputs": outputs} if outputs else {}),
        }

    def to_node(self, tree: NodeTree) -> Node:
        node = tree.nodes.new(
            type=self.bl_idname,
        )
        attributes.set_on_element(node, self.attributes, self.defaults)

        return node

    def set_socket_attributes(self, node: Node) -> None:
        for socket_data in self.inputs:
            attributes.set_on_element(
                node.inputs[socket_data.index],
                socket_data.attributes,
                socket_data.defaults,
            )

        for socket_data in self.outputs:
            attributes.set_on_element(
                node.outputs[socket_data.index],
                socket_data.attributes,
                socket_data.defaults,
            )


class SocketData(Data):

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        index: int,
        to_socket_index: list[int],
        to_node: list[str],
    ) -> None:
        super().__init__(attributes, defaults)
        self.to_socket_index = to_socket_index
        self.to_node = to_node
        self.index = index

    @classmethod
    def from_socket(cls, socket: NodeSocket) -> "SocketData":
        to_socket_index = []
        to_node = []
        for link in socket.links:
            if link.from_socket == socket:
                to_socket_index.append(link.to_socket["index"])
                to_node.append(link.to_node.name)

        defaults = attributes.defaults_for(socket.type)
        return cls(
            to_socket_index=to_socket_index,
            to_node=to_node,
            index=socket["index"],
            attributes=attributes.from_element(socket, defaults),
            defaults=defaults,
        )

    @classmethod
    def from_dict(cls, socket_dict: dict[str, Any]) -> "SocketData":
        defaults = attributes.defaults_for(socket_dict["type"])
        return cls(
            attributes=attributes.from_dict(socket_dict, defaults),
            defaults=defaults,
            to_socket_index=socket_dict.get("to_socket_index", []),
            to_node=socket_dict.get("to_node", []),
            index=socket_dict["index"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, self.defaults),
            **(
                {"to_socket_index": self.to_socket_index}
                if self.to_socket_index
                else {}
            ),
            **({"to_node": self.to_node} if self.to_node else {}),
            "index": self.index,
        }
