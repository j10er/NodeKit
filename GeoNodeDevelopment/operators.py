import bpy
import os

from . import assets
from .storage import exporter


class OBJECT_OT_ImportAssets(bpy.types.Operator):
    "Example Operator to import assets"
    bl_idname = "object.import_assets"
    bl_label = "Import Assets"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        assets.import_assets()
        return {"FINISHED"}


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    "Example Operator to import assets"
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        exporter.export_groups()
        return {"FINISHED"}
