from typing import Any
import logging

log = logging.getLogger(__name__)


class Data:
    attributes: dict[str, Any] = {}
    defaults: dict[str, tuple[str, Any]] = {}

    def __init__(
        self, attributes: dict[str, Any], defaults: dict[str, tuple[str, Any]]
    ) -> None:
        self.attributes = attributes
        self.defaults = defaults

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
        return self.attributes == value.attributes and self.defaults == value.defaults
