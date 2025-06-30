from bpy.types import NodeTreeInterfaceSocket, NodeTreeInterfacePanel
from typing import Any, Union
from .attributes import attributes
from .data_base_class import Data


class InterfaceItemData(Data):

    def __init__(self, attributes: dict[str, Any], defaults: dict[str, Any]) -> None:
        super().__init__(attributes, defaults)

    @classmethod
    def from_item(
        cls, item: Union[NodeTreeInterfaceSocket, NodeTreeInterfacePanel]
    ) -> "InterfaceItemData":
        match item.item_type:
            case "SOCKET":
                return InterfaceSocketData.from_socket(item)
            case "PANEL":
                return InterfacePanelData.from_panel(item)

    @classmethod
    def from_dict(cls, item_dict: dict[str, Any]) -> "InterfaceItemData":
        match item_dict.get("item_type", "SOCKET"):
            case "SOCKET":
                return InterfaceSocketData.from_socket_dict(item_dict)
            case "PANEL":
                return InterfacePanelData.from_panel_dict(item_dict)


class InterfaceSocketData(InterfaceItemData):

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        parent_index: int,
        bl_idname: str,
    ) -> None:
        super().__init__(attributes, defaults)
        self.parent_index = parent_index
        self.attributes["bl_idname"] = bl_idname

    @classmethod
    def from_socket(cls, socket: NodeTreeInterfaceSocket) -> "InterfaceSocketData":
        bl_idname = socket.__class__.__name__
        defaults = attributes.defaults_for(bl_idname)
        return cls(
            attributes=attributes.from_element(
                socket,
                defaults,
            ),
            defaults=defaults,
            parent_index=socket.parent.index,
            bl_idname=bl_idname,
        )

    @classmethod
    def from_socket_dict(cls, socket_dict: dict[str, Any]) -> "InterfaceSocketData":
        defaults = attributes.defaults_for(socket_dict["bl_idname"])
        return cls(
            attributes=attributes.from_dict(socket_dict, defaults),
            defaults=defaults,
            parent_index=socket_dict.get("parent_index", -1),
            bl_idname=socket_dict["bl_idname"],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, self.defaults),
            **({"parent_index": self.parent_index} if self.parent_index != -1 else {}),
        }

    def to_item(self, interface: Any) -> NodeTreeInterfaceSocket:
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
            defaults=self.defaults,
        )
        return socket


class InterfacePanelData(InterfaceItemData):

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        items: list[InterfaceItemData],
    ) -> None:
        super().__init__(attributes, defaults)
        self.items = items

    @classmethod
    def from_panel(cls, panel: NodeTreeInterfacePanel) -> "InterfacePanelData":
        defaults = attributes.defaults_for("NodeTreeInterfacePanel")
        return cls(
            attributes=attributes.from_element(
                panel,
                defaults,
            ),
            defaults=defaults,
            items=[InterfaceItemData.from_item(item) for item in panel.interface_items],
        )

    @classmethod
    def from_panel_dict(cls, panel_dict: dict[str, Any]) -> "InterfacePanelData":
        defaults = attributes.defaults_for("NodeTreeInterfacePanel")
        return cls(
            attributes=attributes.from_dict(panel_dict, defaults),
            defaults=defaults,
            items=[
                InterfaceItemData.from_dict(item)
                for item in panel_dict.get("items", [])
            ],
        )

    def to_dict(self) -> dict[str, Any]:
        return {
            **attributes.to_dict(self.attributes, self.defaults),
            **(
                {"items": [item.to_dict() for item in self.items]} if self.items else {}
            ),
        }

    def to_item(self, interface: Any) -> NodeTreeInterfacePanel:
        panel = interface.new_panel(self.name)
        attributes.set_on_element(
            element=panel,
            attributes=self.attributes,
            defaults=self.defaults,
        )
        for item in self.items:
            item.to_item(interface)
        return panel
