import logging
from typing import Any

log = logging.getLogger(__name__)


class Data:
    attributes: dict[str, Any] = {}
    attribute_types: dict[str, str] = {}

    def __init__(
        self, attributes: dict[str, Any], attribute_types: dict[str, str]
    ) -> None:
        self.attributes = attributes
        self.attribute_types = attribute_types

    def __getattr__(self, name: str) -> Any:
        if name in self.attributes:
            return self.attributes[name]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    def __eq__(self, value: object) -> bool:
        for attribute_name in self.attributes:
            if attribute_name not in value.attributes:
                log.error(
                    f"Attribute '{attribute_name}' not found in {value.__class__.__name__}"
                )
            elif self.attributes[attribute_name] != value.attributes[attribute_name]:
                log.error(
                    f"Attribute '{attribute_name}' does not match: {self.attributes[attribute_name]} != {value.attributes[attribute_name]}"
                )
        return (
            self.attributes == value.attributes
            and self.attribute_types == value.attribute_types
        )
