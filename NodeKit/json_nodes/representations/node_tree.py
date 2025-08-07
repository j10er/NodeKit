import logging
from typing import Any

import bpy
from bpy.types import NodeTree

from ..attributes import attributes
from .base_class import Data
from .interface_item import InterfaceItemData
from .node import NodeData, EXCLUDED_NODE_TYPES

log = logging.getLogger(__name__)


class NodeTreeData(Data):
    base_class_name = "NodeTree"

    def __init__(
        self,
        attributes: dict[str, Any],
        attribute_types: dict[str, str],
        uuid: str,
        nodes: dict[str, NodeData],
        interface_items: list[InterfaceItemData],
    ) -> None:
        super().__init__(attributes, attribute_types)
        self.uuid = uuid
        self.nodes = nodes
        self.interface_items = interface_items

    @classmethod
    def from_tree(cls, tree: NodeTree) -> "NodeTreeData":
        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=tree.bl_idname
        )
        return cls(
            attributes=attributes.from_element(tree, attribute_types),
            attribute_types=attribute_types,
            uuid=tree["uuid"],
            nodes={
                node.name: NodeData.from_node(node)
                for node in sorted(tree.nodes, key=lambda node: node.location[0])
                if node.bl_idname not in EXCLUDED_NODE_TYPES
            },
            interface_items=[
                InterfaceItemData.from_item(item)
                for item in tree.interface.items_tree
                if item.parent.index == -1
            ],
        )

    @classmethod
    def from_dict(cls, tree_dict: dict[str, Any]) -> "NodeTreeData":
        log.debug(f"{tree_dict['name']}: Creating NodeTreeData from dict...")
        attribute_types = attributes.types_for(
            base_class_name=cls.base_class_name, class_name=tree_dict["bl_idname"]
        )
        return cls(
            attributes=attributes.from_dict(tree_dict, attribute_types),
            attribute_types=attribute_types,
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
            **self.attributes,
            "uuid": self.uuid,
            "nodes": {
                name: node_data.to_dict() for name, node_data in self.nodes.items()
            },
            "interface_items": [
                item_data.to_dict() for item_data in self.interface_items
            ],
        }

    def _reset_tree(self):
        for node in self.tree.nodes:
            self.tree.nodes.remove(node)
        self.tree.interface.clear()

    def create_tree_hull(self):

        existing_tree = next(
            (
                tree
                for tree in bpy.data.node_groups.values()
                if tree.get("uuid", "") == self.uuid
            ),
            None,
        )
        if existing_tree:
            log.info(
                f"{self.name}: Overwriting existing node tree {existing_tree.name}"
            )
            self.tree = existing_tree
            self._reset_tree()
        else:
            log.debug(f"{self.name}: Creating new node tree")
            self.tree = bpy.data.node_groups.new(name=self.name, type=self.bl_idname)
        self.tree = self.tree
        self.tree["uuid"] = self.uuid
        attributes.set_on_element(self.tree, self.attributes, self.attribute_types)
        for item_data in self.interface_items:
            log.debug(f"{self.name}: Creating interface item {item_data.name}")
            item = item_data.to_item(self.tree.interface)
        log.debug(
            f"{self.name}: Created {len(self.tree.interface.items_tree)} interface items"
        )

    def add_nodes(self):
        log.debug("=" * 40)
        log.debug(f"{self.name}: Adding {len(self.nodes)} nodes")
        tree = self.tree

        for node_data in self.nodes.values():
            # log.debug(f"{self.name}:{node_data.name}: Creating node")
            node = node_data.to_node(tree)
        log.debug(f"{self.name}: Created {len(tree.nodes)} nodes")
        for node_data in self.nodes.values():
            node_data.set_attributes()

        log.debug(f"{self.name}: Connecting nodes with links")
        for node_data in self.nodes.values():
            for input_data in node_data.inputs:
                if input_data.from_node and input_data.from_socket_index:

                    to_node = tree.nodes.get(node_data.name)
                    # links.new adds links to the top, so we reverse the order
                    for i in reversed(range(len(input_data.from_node))):
                        to_socket = to_node.inputs[input_data.index]

                        from_node = tree.nodes.get(input_data.from_node[i])
                        from_socket = from_node.outputs[input_data.from_socket_index[i]]

                        # log.debug(
                        #     f"{self.name}:{from_node.name}: Linking socket {from_socket.name} to {node_data.name}:{to_socket.name}"
                        # )
                        tree.links.new(from_socket, to_socket)

    def set_socket_attributes(self):
        log.debug(f"{self.name}: Setting interface item attributes")
        for item_data in self.interface_items:
            # log.debug(
            #     f"{self.name}: - Setting interface item attributes for {item_data.name}"
            # )
            item_data.set_attributes()
        log.debug(f"{self.name}: - Setting NodeSocket attributes")
        for node_data in self.nodes.values():
            # log.debug(
            #     f"{self.name}: -- Setting socket attributes for node {node_data.name}"
            # )
            node_data.set_socket_attributes()
        log.debug(f"{self.name}: Done.")
        log.debug("=" * 40)
