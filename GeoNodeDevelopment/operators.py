import bpy
import os

from .gnjson import exporter, importer


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        exporter.export_groups()
        return {"FINISHED"}


class OBJECT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "object.import_json"
    bl_label = "Import from JSON"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        importer.import_groups()
        return {"FINISHED"}
