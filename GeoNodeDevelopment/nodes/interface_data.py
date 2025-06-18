from bpy.types import NodeTreeInterfaceSocket, NodeTreeInterfacePanel
from typing import Any
from . import attributes
from .data_class import Data


class InterfaceItemData(Data):

    @classmethod
    def from_item(cls, item) -> "InterfaceItemData":
        match item.item_type:
            case "SOCKET":
                return InterfaceSocketData.from_socket(item)
            case "PANEL":
                return InterfacePanelData.from_panel(item)

    @classmethod
    def from_dict(cls, item_dict) -> "InterfaceItemData":
        match item_dict.get("item_type", "SOCKET"):
            case "SOCKET":
                return InterfaceSocketData.from_socket_dict(item_dict)
            case "PANEL":
                return InterfacePanelData.from_panel_dict(item_dict)


class InterfaceSocketData(InterfaceItemData):

    def __init__(
        self,
        attributes: dict[str, Any],
        parent_index: int,
    ):
        self.attributes = attributes
        self.parent_index = parent_index

    @classmethod
    def from_socket(cls, socket: NodeTreeInterfaceSocket) -> "InterfaceSocketData":
        return cls(
            attributes=attributes.from_element(
                socket,
                socket.socket_type,
            ),
            parent_index=socket.parent.index,
        )

    @classmethod
    def from_socket_dict(cls, socket_dict: dict[str, Any]) -> "InterfaceSocketData":
        return cls(
            attributes=attributes.from_dict(socket_dict, socket_dict["socket_type"]),
            parent_index=socket_dict.get("parent_index", -1),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, self.socket_type),
            **({"parent_index": self.parent_index} if self.parent_index != -1 else {}),
        }

    def to_item(self, interface) -> NodeTreeInterfaceSocket:
        socket = interface.new_socket(
            name=self.name,
            parent=(
                interface.items_tree[self.parent_index]
                if self.parent_index != -1
                else None
            ),
            socket_type=self.socket_type,
            in_out=self.in_out,
        )
        attributes.set_on_element(
            element=socket,
            attributes=self.attributes,
            class_name=self.socket_type,
        )
        return socket


class InterfacePanelData(InterfaceItemData):

    def __init__(self, attributes: dict[str, Any], items: list[InterfaceItemData]):
        self.attributes = attributes
        self.items = items

    @classmethod
    def from_panel(cls, panel: NodeTreeInterfacePanel) -> "InterfacePanelData":
        return cls(
            attributes=attributes.from_element(
                panel,
                "NodeTreeInterfacePanel",
            ),
            items=[InterfaceItemData.from_item(item) for item in panel.interface_items],
        )

    @classmethod
    def from_panel_dict(cls, panel_dict: dict[str, Any]) -> "InterfacePanelData":
        return cls(
            attributes=attributes.from_dict(panel_dict, "NodeTreeInterfacePanel"),
            items=[
                InterfaceItemData.from_dict(item)
                for item in panel_dict.get("items", [])
            ],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, "NodeTreeInterfacePanel"),
            **(
                {"items": [item.to_dict() for item in self.items]} if self.items else {}
            ),
        }

    def to_item(self, interface) -> NodeTreeInterfacePanel:
        panel = interface.new_panel(self.name)
        attributes.set_on_element(
            element=panel,
            attributes=self.attributes,
            class_name="NodeTreeInterfacePanel",
        )
        for item in self.items:
            item.to_item(interface)
        return panel
