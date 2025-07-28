from bpy.types import NodeTreeInterfaceSocket, NodeTreeInterfacePanel
from typing import Any
import logging
from ..attributes import attributes
from .base_class import Data

log = logging.getLogger(__name__)


class InterfaceItemData(Data):

    def __init__(self, attributes: dict[str, Any], defaults: dict[str, Any]) -> None:
        super().__init__(attributes, defaults)

    @classmethod
    def from_item(
        cls, item: NodeTreeInterfaceSocket | NodeTreeInterfacePanel
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

    def __eq__(self, value):
        return super().__eq__(value)


class InterfaceSocketData(InterfaceItemData):

    base_class_name = "NodeTreeInterfaceSocket"

    def __init__(
        self,
        attributes: dict[str, Any],
        defaults: dict[str, Any],
        parent_index: int,
        bl_idname: str,
    ) -> None:
        super().__init__(attributes, defaults)
        self.parent_index = parent_index
        self.bl_idname = bl_idname

    @classmethod
    def from_socket(cls, socket: NodeTreeInterfaceSocket) -> "InterfaceSocketData":
        bl_idname = socket.__class__.__name__
        defaults = attributes.defaults_for(
            base_class_name=cls.base_class_name, class_name=bl_idname
        )
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
        defaults = attributes.defaults_for(
            base_class_name=cls.base_class_name, class_name=socket_dict["bl_idname"]
        )
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
            "bl_idname": self.bl_idname,
        }

    def to_item(self, interface: Any) -> NodeTreeInterfaceSocket:
        self.socket = interface.new_socket(
            name=self.name,
            parent=(
                interface.items_tree[self.parent_index]
                if self.parent_index != -1
                else None
            ),
            socket_type=self.socket_type,
            in_out=self.in_out,
        )

    def set_attributes(self) -> NodeTreeInterfaceSocket:

        return attributes.set_on_element(
            element=self.socket,
            attributes=self.attributes,
            defaults=self.defaults,
        )

    def __eq__(self, value: object) -> bool:
        equal = (
            super().__eq__(value)
            and self.parent_index == value.parent_index
            and self.bl_idname == value.bl_idname
        )
        if not equal:
            log.debug(f"InterfaceSocketData __eq__ failed: {self.name} != {value.name}")
        return equal


class InterfacePanelData(InterfaceItemData):
    base_class_name = "NodeTreeInterfacePanel"

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
        defaults = attributes.defaults_for(base_class_name=cls.base_class_name)
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
        defaults = attributes.defaults_for(base_class_name=cls.base_class_name)
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

    def set_attributes(self) -> NodeTreeInterfacePanel:
        for item in self.items:
            item.set_attributes()
