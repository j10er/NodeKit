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
