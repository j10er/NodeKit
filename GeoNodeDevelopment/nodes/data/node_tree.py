import bpy
from bpy.types import NodeTree
from typing import Any
import logging
from ..attributes import attributes
from .base_class import Data
from .interface_item import InterfaceItemData
from .node import NodeData, EXCLUDED_NODE_TYPES


log = logging.getLogger(__name__)


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
        log.info(
            f"Creating NodeTreeData from tree: {tree.name} with UUID: {tree['uuid']}..."
        )

        if tree.bl_idname != "GeometryNodeTree":
            log.error(
                f"Expected GeometryNodeTree, got {tree.bl_idname} for tree {tree.name}"
            )
            return None

        defaults = attributes.defaults_for(tree.bl_idname)
        return cls(
            attributes=attributes.from_element(tree, defaults),
            defaults=defaults,
            uuid=tree["uuid"],
            nodes={
                node.name: NodeData.from_node(node)
                for node in tree.nodes
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
        log.debug(f"{self.name}: Converting to dict")
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
        try:
            if [
                tree
                for tree in bpy.data.node_groups.values()
                if tree.get("uuid", "") == self.uuid
            ]:
                log.info(
                    f"Warning: Overwriting existing node tree {self.name} with UUID {self.uuid}"
                )
                tree = bpy.data.node_groups[self.name]
                for node in tree.nodes:
                    tree.nodes.remove(node)
                tree.interface.clear()

            else:
                log.debug(f"{self.name}: Creating new node tree")
                tree = bpy.data.node_groups.new(name=self.name, type=self.bl_idname)
            self.tree = tree
            tree["uuid"] = self.uuid
            attributes.set_on_element(tree, self.attributes, self.defaults)
            for item_data in self.interface_items:
                log.debug(f"{self.name}: Creating interface item {item_data.name}")
                item = item_data.to_item(tree.interface)
            log.debug(
                f"{self.name}: Created {len(tree.interface.items_tree)} interface items"
            )
        except Exception as e:
            if tree:
                return tree
                bpy.data.node_groups.remove(tree, do_unlink=True)
            log.error(f"{self.name}: Error creating tree hull: {e}")
            raise e
        return tree

    def add_nodes(self) -> NodeTree:
        log.debug("=" * 40)
        log.debug(f"{self.name}: Adding {len(self.nodes)} nodes")
        tree = self.tree

        for node_data in self.nodes.values():
            log.debug(f"{self.name}: Creating node {node_data.name}")
            node = node_data.to_node(tree)
        log.debug(f"{self.name}: Created {len(tree.nodes)} nodes")
        for node_data in self.nodes.values():
            if hasattr(node_data, "paired_output"):
                log.debug(
                    f"{self.name}: Pairing zone node '{node_data.name}' to output '{node_data.paired_output}'"
                )
                tree.nodes[node_data.name].pair_with_output(
                    tree.nodes[node_data.paired_output]
                )

        log.debug(f"{self.name}: Setting socket attributes")
        for node_data in self.nodes.values():
            node = tree.nodes[node_data.name]

        log.debug(f"{self.name}: Connecting nodes with links")
        for node_data in self.nodes.values():
            log.debug(f"{self.name}: Adding links for node {node_data.name}")
            for output_data in node_data.outputs:
                if output_data.to_node and output_data.to_socket_index:
                    from_node = tree.nodes.get(node_data.name)
                    from_socket = from_node.outputs[output_data.index]

                    for i in range(len(output_data.to_node)):

                        to_node = tree.nodes.get(output_data.to_node[i])
                        to_socket = to_node.inputs[output_data.to_socket_index[i]]
                        log.debug(
                            f"{self.name}: Linking {from_node.name}.{from_socket.name} to {to_node.name}.{to_socket.name}"
                        )
                        tree.links.new(from_socket, to_socket)

        log.debug(f"{self.name}: Setting interface items attributes")
        for item_data in self.interface_items:
            log.debug(
                f"{self.name}: Setting interface item attributes for {item_data.name}"
            )
            item_data.set_attributes()

        log.debug(f"{self.name}: Setting NodeSocket attributes")
        for node_data in self.nodes.values():
            log.debug(f"{self.name}: Setting socket attributes for node {node.name}")
            node_data.set_socket_attributes()
        log.debug(f"{self.name}: Done.")
        log.debug("=" * 40)
        return tree
