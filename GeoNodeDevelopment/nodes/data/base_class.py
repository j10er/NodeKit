from typing import Any


class Data:
    attributes = {}
    defaults = {}

    def __init__(self, attributes: dict[str, Any], defaults: dict[str, Any]):
        self.attributes = attributes
        self.defaults = defaults

    def __getattr__(self, name):
        if name in self.attributes:
            return self.attributes[name]
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )
