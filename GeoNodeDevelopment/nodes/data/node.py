import bpy
from typing import Any
from bpy.types import Node, NodeTree, NodeSocket
from ..attributes import attributes
from .base_class import Data


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

        defaults = attributes.defaults_for(socket.bl_idname)
        return cls(
            to_socket_index=to_socket_index,
            to_node=to_node,
            index=socket["index"],
            attributes=attributes.from_element(socket, defaults),
            defaults=defaults,
        )

    @classmethod
    def from_dict(cls, socket_dict: dict[str, Any]) -> "SocketData":
        defaults = attributes.defaults_for(socket_dict["bl_idname"])
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
