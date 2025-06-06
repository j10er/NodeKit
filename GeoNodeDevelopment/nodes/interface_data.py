from bpy.types import NodeTreeInterfaceSocket, NodeTreeInterfacePanel
from typing import Any


class InterfaceItemData:
    item_type: str
    name: str
    index: int

    @classmethod
    def set_attributes(
        cls,
        item_data: "InterfaceItemData",
        index: int,
        item_type: str,
        name: str,
    ):
        item_data.index = index
        item_data.item_type = item_type
        item_data.name = name

    @classmethod
    def from_item(cls, item) -> "InterfaceItemData":
        match item.item_type:
            case "SOCKET":
                item_data = InterfaceSocketData.from_socket(item)
            case "PANEL":
                item_data = InterfacePanelData.from_panel(item)

        cls.set_attributes(
            item_data=item_data,
            item_type=item.item_type,
            name=item.name,
            index=item.index,
        )
        return item_data

    @classmethod
    def from_dict(cls, item_dict) -> "InterfaceItemData":
        match item_dict["item_type"]:
            case "SOCKET":
                item_data = InterfaceSocketData.from_socket_dict(item_dict)
            case "PANEL":
                item_data = InterfacePanelData.from_panel_dict(item_dict)
        cls.set_attributes(
            item_data=item_data,
            item_type=item_dict["item_type"],
            name=item_dict["name"],
            index=item_dict["index"],
        )
        return item_data

    def to_dict(self) -> dict[str, Any]:
        return {
            "item_type": self.item_type,
            "name": self.name,
            "index": self.index,
        }


class InterfaceSocketData(InterfaceItemData):
    def __init__(
        self,
        socket_type: str,
        in_out: str,
        parent_index: int,
        description: str,
        force_non_field: bool,
        hide_in_modifier: bool,
        hide_value: bool,
    ):
        self.socket_type = socket_type
        self.in_out = in_out
        self.parent_index = parent_index
        self.description = description
        self.force_non_field = force_non_field
        self.hide_in_modifier = hide_in_modifier
        self.hide_value = hide_value

    @classmethod
    def from_socket(cls, socket: NodeTreeInterfaceSocket) -> "InterfaceSocketData":

        return cls(
            socket_type=socket.socket_type,
            in_out=socket.in_out,
            parent_index=socket.parent.index,
            description=socket.description,
            force_non_field=socket.force_non_field,
            hide_in_modifier=socket.hide_in_modifier,
            hide_value=socket.hide_value,
        )

    @classmethod
    def from_socket_dict(cls, socket_dict: dict[str, Any]) -> "InterfaceSocketData":
        return cls(
            socket_type=socket_dict["socket_type"],
            in_out=socket_dict["in_out"],
            parent_index=socket_dict.get("parent_index", -1),
            description=socket_dict.get("description", ""),
            force_non_field=socket_dict.get("force_non_field", False),
            hide_in_modifier=socket_dict.get("hide_in_modifier", False),
            hide_value=socket_dict.get("hide_value", False),
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            "socket_type": self.socket_type,
            "in_out": self.in_out,
            **({"parent_index": self.parent_index} if self.parent_index != -1 else {}),
            **({"description": self.description} if self.description else {}),
            **(
                {"force_non_field": self.force_non_field}
                if self.force_non_field
                else {}
            ),
            **(
                {"hide_in_modifier": self.hide_in_modifier}
                if self.hide_in_modifier
                else {}
            ),
            **({"hide_value": self.hide_value} if self.hide_value else {}),
        }

    def to_item(self, interface) -> NodeTreeInterfaceSocket:
        socket = interface.new_socket(
            name=self.name,
            socket_type=self.socket_type,
            in_out=self.in_out,
            parent=(
                interface.items_tree[self.parent_index]
                if self.parent_index != -1
                else None
            ),
        )
        socket.description = self.description
        socket.force_non_field = self.force_non_field
        socket.hide_in_modifier = self.hide_in_modifier
        socket.hide_value = self.hide_value
        return socket


class InterfacePanelData(InterfaceItemData):

    def __init__(self, items: list[InterfaceItemData]):
        self.items = items

    @classmethod
    def from_panel(cls, panel: NodeTreeInterfacePanel) -> "InterfacePanelData":
        return cls(
            items=[InterfaceItemData.from_item(item) for item in panel.interface_items],
        )

    @classmethod
    def from_panel_dict(cls, panel_dict: dict[str, Any]) -> "InterfacePanelData":
        return cls(
            items=[
                InterfaceItemData.from_dict(item)
                for item in panel_dict.get("items", [])
            ],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **super().to_dict(),
            **(
                {"items": [item.to_dict() for item in self.items]} if self.items else {}
            ),
        }

    def to_item(self, interface) -> NodeTreeInterfacePanel:
        panel = interface.new_panel(
            name=self.name,
        )
        for item in self.items:
            item.to_item(interface)
        return panel
