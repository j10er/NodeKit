import bpy
from pprint import pprint
from .nodes import attributes_dict, exporter, importer
from .nodes import data, file
from .nodes.exporter import export_groups
from .nodes.importer import import_groups
from bpy.types import GeometryNodeRepeatOutput, GeometryNodeInputCollection
from .nodes import generate_attributes_dict


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"

    def execute(self, context):
        export_groups()
        return {"FINISHED"}


class OBJECT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "object.import_json"
    bl_label = "Import from JSON"

    def execute(self, context):
        import_groups()
        return {"FINISHED"}


class OBJECT_OT_Surprise(bpy.types.Operator):
    bl_idname = "object.surprise"
    bl_label = "Surprise"

    def execute(self, context):

        print("awd")
        for cls in sorted(operator_classes, key=lambda c: c.__name__):
            print(cls.__name__)
        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        pprint(generate_attributes_dict.generate_attributes_dict())
        return {"FINISHED"}
