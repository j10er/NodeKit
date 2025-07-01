import bpy
from bpy.types import Node, NodeTree, NodeSocket
from typing import Any
from pprint import pprint

from ..attributes import attributes
from .base_class import Data
from .tree_interface import InterfaceItemData
from .node import NodeData


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
        print(f"Creating NodeTreeData from tree: {tree.name} with UUID: {tree['uuid']}")
        if tree.bl_idname != "GeometryNodeTree":
            raise ValueError(
                f"Expected GeometryNodeTree, got {tree.bl_idname} for tree {tree.name}"
            )

        defaults = attributes.defaults_for(tree.bl_idname)
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
        defaults = attributes.defaults_for(tree_dict["bl_idname"])
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

    def create_tree_hull(self) -> NodeTree:
        tree = bpy.data.node_groups.new(name=self.name, type=self.bl_idname)
        self.tree = tree
        tree["uuid"] = self.uuid
        attributes.set_on_element(tree, self.attributes, self.defaults)
        print(f"Created node tree: {tree.name} with UUID: {self.uuid}")
        attributes.set_on_element(tree, self.attributes, self.defaults)
        for item_data in self.interface_items:
            item = item_data.to_item(tree.interface)
        print(
            f"Created {len(tree.interface.items_tree)} interface items for tree {tree.name}"
        )
        return tree

    def add_nodes(self) -> NodeTree:
        tree = self.tree
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
