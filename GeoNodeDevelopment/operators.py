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

        base = bpy.types.GeometryNode.bl_rna  # The RNA struct we want subclasses of

        print(f"Subclasses of {base.identifier}:")

        for cls in bpy.types.GeometryNode.__subclasses__():
            print(cls.__name__)

        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        pprint(generate_attributes_dict.generate_attributes_dict())
        return {"FINISHED"}


class OBJECT_OT_DebugGeometryNodes(bpy.types.Operator):
    bl_idname = "object.debug_geometry_nodes"
    bl_label = "Debug Geometry Nodes"

    def execute(self, context):
        generate_attributes_dict.debug_geometry_node_classes()

        print("\n=== Geometry Nodes Only Dictionary ===")
        geo_dict = generate_attributes_dict.filter_geometry_nodes_only()
        from pprint import pprint

        pprint(geo_dict)

        return {"FINISHED"}
