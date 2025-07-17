import bpy
from .json_nodes.import_export import export_to, import_from
from .json_nodes.attributes import generate_attributes_dict
from .json_nodes import file
from . import config
import os


class NODEKIT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "nodekit.import_json"
    bl_label = "Import from JSON"
    bl_description = "Import node groups and assets from JSON files"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.node_kit.directory_error

    def invoke(self, context, event):
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        num_of_json = file.number_of_files(folder_path, ".json")
        num_of_blend = file.number_of_files(folder_path, ".blend")
        return context.window_manager.invoke_confirm(
            self,
            event=event,
            title=f"Found {num_of_json} node group{'s' if num_of_json != 1 else ''} and {num_of_blend} asset{'s' if num_of_blend != 1 else ''}. This will overwrite all node groups and assets in this file that are managed by the add-on. Are you sure?",
        )

    def execute(self, context):
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        message = import_from(folder_path, append=False)
        self.report({"INFO"}, message)
        bpy.context.scene.node_kit.is_imported = True
        return {"FINISHED"}


class NODEKIT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "nodekit.export_json"
    bl_label = "Export to JSON"
    bl_description = "Export node groups and assets to JSON files"

    @classmethod
    def poll(cls, context):

        return not bpy.context.scene.node_kit.directory_error and (
            bpy.context.scene.node_kit.is_imported
            or file.folder_is_empty(
                bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
            )
        )

    def execute(self, context):
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        export_to(folder_path)
        bpy.context.scene.node_kit.is_imported = True
        return {"FINISHED"}


class NODEKIT_OT_AppendJSON(bpy.types.Operator):
    bl_idname = "nodekit.append_json"
    bl_label = "Append JSON from"
    bl_description = "Pick a folder to append its node groups"

    directory: bpy.props.StringProperty(
        name="Folder", description="Select a folder", subtype="DIR_PATH"
    )  # type: ignore

    def execute(self, context):
        folder_path = bpy.path.abspath(self.directory)

        directory_error = file.validate_path(folder_path)
        if directory_error:
            self.report({"ERROR"}, directory_error)
            return {"CANCELLED"}

        message = import_from(folder_path, append=True)
        self.report({"INFO"}, message)
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class NODEKIT_OT_Surprise(bpy.types.Operator):
    bl_idname = "nodekit.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        print(__package__.split(".")[-1])
        return {"FINISHED"}


class NODEKIT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "nodekit.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}
