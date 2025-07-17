import os
from bpy.path import abspath
import bpy
from .json_nodes import file
from . import config
import logging

log = logging.getLogger(__name__)


def save_handler(scene):
    bpy.ops.nodekit.export_json()


class NodeKitPreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    export_on_save: bpy.props.BoolProperty(
        name="Export on Save",
        description="Automatically export node groups to JSON files when saving the Blender file",
        default=False,
        update=lambda self, context: self.set_save_handler(),
    )  # type: ignore

    def set_save_handler(self):
        if self.export_on_save:
            if save_handler not in bpy.app.handlers.save_post:
                bpy.app.handlers.save_post.append(save_handler)
        else:
            if save_handler in bpy.app.handlers.save_post:
                bpy.app.handlers.save_post.remove(save_handler)

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "export_on_save", text="Export on Save")


class NodeKitProperties(bpy.types.PropertyGroup):
    folder_path: bpy.props.StringProperty(
        name="Folder Path",
        description="Path to a selected folder",
        subtype="DIR_PATH",
        update=lambda self, context: self.on_path_update(),
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

    def on_path_update(self):
        self.directory_error = file.validate_path(self.folder_path)
        self.is_imported = False
        if not self.directory_error:
            log.info(f"JSON Folder path set to: {self.folder_path}")
        else:
            log.error(f"Invalid JSON Folder path: {self.directory_error}")
