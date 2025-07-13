from typing import Any


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
