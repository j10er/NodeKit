import os
from bpy.types import PropertyGroup
from bpy.props import StringProperty
from bpy.path import abspath


class GNDProperties(PropertyGroup):
    folder_path: StringProperty(
        name="Folder Path",
        description="Path to a selected folder",
        subtype="DIR_PATH",
        update=lambda self, context: self.validate_path(),
    )  # type: ignore
    directory_error: StringProperty(
        name="Path Error",
        description="Error message if the path is not valid",
        default="Select a directory to store the JSON files",
    )  # type: ignore

    def validate_path(self):
        if not self.folder_path:
            self.directory_error = "Select a directory to store the JSON files"
        elif not os.path.exists(abspath(self.folder_path)):
            self.directory_error = "Path does not exist"
        elif not os.path.isdir(abspath(self.folder_path)):
            self.directory_error = "Path is not a directory"
        elif not self.directory_is_valid(abspath(self.folder_path)):
            self.directory_error = "The directory contains other content, must only contain JSON files and directories"
        else:
            self.directory_error = ""

    def directory_is_valid(self, path) -> bool:
        """Check recursively if the directory only contains jsons and directories."""
        for file in os.listdir(path):
            if not file.endswith(".json") and not os.path.isdir(
                os.path.join(path, file)
            ):
                return False
            if os.path.isdir(os.path.join(self.folder_path, file)):
                return self.directory_is_valid(os.path.join(path, file))

        return True
