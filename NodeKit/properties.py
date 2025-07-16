import os
from bpy.path import abspath
import bpy
from .json_nodes import file
import logging
log = logging.getLogger(__name__)
class NodeKitProperties(bpy.types.PropertyGroup):
    folder_path: bpy.props.StringProperty(
        name="Folder Path",
        description="Path to a selected folder",
        subtype="DIR_PATH",
        update=lambda self, context: self.on_update(),
    )  # type: ignore
    directory_error: bpy.props.StringProperty(
        name="Path Error",
        description="Error message if the path is not valid",
        default="Select a directory to store the JSON files",
    )  # type: ignore
    is_imported: bpy.props.BoolProperty(
        name="Is Imported",
        description="Indicates if the JSON files have been imported",
        default=False,
    )  # type: ignore

    def on_update(self):
        self.directory_error = file.validate_path(self.folder_path)
        self.is_imported = False
        if not self.directory_error:
            log.info(f"JSON Folder path set to: {self.folder_path}")
        else:
            log.error(f"Invalid JSON Folder path: {self.directory_error}")
