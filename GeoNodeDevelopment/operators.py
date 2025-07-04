import bpy
from .nodes.nodes import export_groups, import_groups
from .nodes.attributes import generate_attributes_dict
from .nodes import file
import logging

log = logging.getLogger(__name__)


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"

    @classmethod
    def poll(cls, context):
        return (
            bpy.context.scene.gnd_props.json_folder_path != "" and file.path_is_valid()
        )

    def execute(self, context):
        export_groups()
        return {"FINISHED"}


class OBJECT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "object.import_json"
    bl_label = "Import from JSON"

    @classmethod
    def poll(cls, context):
        return (
            bpy.context.scene.gnd_props.json_folder_path != "" and file.path_is_valid()
        )

    def execute(self, context):
        import_groups()
        return {"FINISHED"}


class OBJECT_OT_Surprise(bpy.types.Operator):
    bl_idname = "object.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        socket = bpy.types.NodeSocketFloat
        print(issubclass(socket, socket))
        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}


def save_handler(scene):
    bpy.ops.object.export_json()
