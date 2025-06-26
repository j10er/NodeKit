import bpy
from pprint import pprint
from .nodes import attributes_dict, exporter, importer
from .nodes import data, file
from .nodes.exporter import export_groups
from .nodes.importer import import_groups


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
        # Create a new for each element zone
        # input = tree.nodes.new("GeometryNodeRepeatInput")
        # output = tree.nodes.new("GeometryNodeRepeatOutput")
        # input.pair_with_output(output)
        input = tree.nodes.get("Repeat Input")
        output = tree.nodes.get("Repeat Output")
        output.repeat_items.new("GEOMETRY", "Geometry")
        print(output.repeat_items)
        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes_dict.save_attribute_dict()
        print("Default values generated for all socket types.")
        return {"FINISHED"}
