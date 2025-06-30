import bpy
from pprint import pprint

from .nodes.exporter import export_groups
from .nodes.importer import import_groups
from .nodes.attributes import generate_attributes_dict


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
        tree = bpy.data.node_groups.get("TestNodes")
        socket = tree.interface.items_tree[0]
        print(socket.__class__.__name__)
        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}
