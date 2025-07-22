import bpy
from typing import Any
import logging
from bpy.types import Node, NodeTree, NodeSocket
from ..attributes import attributes
from .base_class import Data
from ... import config


log = logging.getLogger(__name__)

EXCLUDED_NODE_TYPES = ["GeometryNodeViewer"]


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
        self.node = tree.nodes.new(type=self.bl_idname)
        self.node.name = self.name
        return self.node

    def set_attributes(self) -> None:
        attributes.set_on_element(self.node, self.attributes, self.defaults)

    def set_socket_attributes(self) -> None:
        for socket_data in self.inputs:
            log.debug(
                f"Setting attributes on input socket {self.node.inputs[socket_data.index].name}"
            )
            attributes.set_on_element(
                self.node.inputs[socket_data.index],
                socket_data.attributes,
                socket_data.defaults,
            )
        for socket_data in self.outputs:
            log.debug(
                f"Setting attributes on output socket {self.node.outputs[socket_data.index].name}"
            )

            attributes.set_on_element(
                self.node.outputs[socket_data.index],
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
            if (
                link.from_socket == socket
                and link.to_node.bl_idname not in EXCLUDED_NODE_TYPES
            ):
                to_socket_index.append(link.to_socket[config.JSON_KEY_INDEX])
                to_node.append(link.to_node.name)

        defaults = attributes.defaults_for(socket.bl_idname)
        return cls(
            to_socket_index=to_socket_index,
            to_node=to_node,
            index=socket[config.JSON_KEY_INDEX],
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
            index=socket_dict[config.JSON_KEY_INDEX],
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
            config.JSON_KEY_INDEX: self.index,
        }
