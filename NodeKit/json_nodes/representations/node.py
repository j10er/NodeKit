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
    base_class_name = "Node"

    def __init__(
        self,
        attributes: dict[str, Any],
        attribute_types: dict[str, Any],
        inputs: list["SocketData"],
        outputs: list["SocketData"],
    ) -> None:
        super().__init__(attributes, attribute_types)
        self.inputs = inputs
        self.outputs = outputs

    @classmethod
    def from_node(cls, node: Node) -> "NodeData":
        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=node.bl_idname
        )
        return cls(
            attributes=attributes.from_element(node, attribute_types),
            attribute_types=attribute_types,
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
        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=node_dict["bl_idname"]
        )
        return cls(
            attributes=attributes.from_dict(node_dict, attribute_types),
            attribute_types=attribute_types,
            inputs=[SocketData.from_dict(s) for s in node_dict.get("inputs", [])],
            outputs=[SocketData.from_dict(s) for s in node_dict.get("outputs", [])],
        )

    def to_dict(self) -> dict[str, Any]:
        inputs = [
            socket_data.to_dict()
            for socket_data in self.inputs
            if "default_value" in socket_data.to_dict()
            or "from_socket_index" in socket_data.to_dict()
        ]
        outputs = [
            socket_data.to_dict()
            for socket_data in self.outputs
            if "default_value" in socket_data.to_dict()
            or "from_socket_index" in socket_data.to_dict()
        ]
        return {
            **self.attributes,
            **({"inputs": inputs} if inputs else {}),
            **({"outputs": outputs} if outputs else {}),
        }

    def to_node(self, tree: NodeTree) -> Node:
        self.node = tree.nodes.new(type=self.bl_idname)
        self.node.name = self.name
        return self.node

    def set_attributes(self) -> None:
        attributes.set_on_element(self.node, self.attributes, self.attribute_types)

    def set_socket_attributes(self) -> None:
        for socket_data in self.inputs:
            if len(socket_data.attributes) > 0:
                log.debug(
                    f"Setting attributes on input socket {self.node.inputs[socket_data.index].name}"
                )
                attributes.set_on_element(
                    self.node.inputs[socket_data.index],
                    socket_data.attributes,
                    socket_data.attribute_types,
                )
        for socket_data in self.outputs:
            if len(socket_data.attributes) > 0:
                log.debug(
                    f"Setting attributes on output socket {self.node.outputs[socket_data.index].name}"
                )
                attributes.set_on_element(
                    self.node.outputs[socket_data.index],
                    socket_data.attributes,
                    socket_data.attribute_types,
                )

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, self.__class__):
            log.error(
                f"Cannot compare {self.__class__.__name__} with {value.__class__.__name__}"
            )
            return False
        if not super().__eq__(value):
            log.error(f"Node attributes are not equal: {self.name} != {value.name}")
        if not self.inputs == value.inputs:
            log.error(f"Node inputs of nodes {self.name}, {value.name} are not equal")
        if not self.outputs == value.outputs:
            log.error(f"Node outputs of nodes {self.name}, {value.name} are not equal")
        return (
            super().__eq__(value)
            and self.inputs == value.inputs
            and self.outputs == value.outputs
        )


class SocketData(Data):
    base_class_name = "NodeSocket"

    def __init__(
        self,
        attributes: dict[str, Any],
        attribute_types: dict[str, Any],
        index: int,
        from_socket_index: list[int],
        from_node: list[str],
    ) -> None:
        super().__init__(attributes, attribute_types)
        self.from_socket_index = from_socket_index
        self.from_node = from_node
        self.index = index

    @classmethod
    def from_socket(cls, socket: NodeSocket) -> "SocketData":
        from_socket_index = []
        from_node = []
        for link in socket.links:
            if (
                link.to_socket == socket
                and link.from_node.bl_idname not in EXCLUDED_NODE_TYPES
            ):
                from_socket_index.append(link.from_socket[config.JSON_KEY_INDEX])
                from_node.append(link.from_node.name)

        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=socket.bl_idname
        )
        return cls(
            from_socket_index=from_socket_index,
            from_node=from_node,
            index=socket[config.JSON_KEY_INDEX],
            attributes=attributes.from_element(socket, attribute_types),
            attribute_types=attribute_types,
        )

    @classmethod
    def from_dict(cls, socket_dict: dict[str, Any]) -> "SocketData":
        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=socket_dict["bl_idname"]
        )
        return cls(
            attributes=attributes.from_dict(socket_dict, attribute_types),
            attribute_types=attribute_types,
            from_socket_index=socket_dict.get("from_socket_index", []),
            from_node=socket_dict.get("from_node", []),
            index=socket_dict[config.JSON_KEY_INDEX],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **self.attributes,
            **(
                {"from_socket_index": self.from_socket_index}
                if self.from_socket_index
                else {}
            ),
            **({"from_node": self.from_node} if self.from_node else {}),
            config.JSON_KEY_INDEX: self.index,
        }

    def __eq__(self, value: object) -> bool:
        if not super().__eq__(value):
            log.debug(f"SocketData attributes are not equal for : {self.index}")
        if not self.index == value.index:
            log.debug(f"SocketData index is not equal: {self.index} != {value.index}")
        if not self.from_socket_index == value.from_socket_index:
            log.debug(
                f"SocketData from_socket_index is not equal: {self.from_socket_index} != {value.from_socket_index}"
            )
        if not self.from_node == value.from_node:
            log.debug(
                f"SocketData from_node is not equal: {self.from_node} != {value.from_node}"
            )

        return (
            super().__eq__(value)
            and self.index == value.index
            and self.from_socket_index == value.from_socket_index
            and self.from_node == value.from_node
        )
