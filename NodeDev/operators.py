import bpy
from .json_nodes.import_export import export_groups, import_groups
from .json_nodes.attributes import generate_attributes_dict
from .json_nodes import assets


class NODEDEV_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "nodedev.export_json"
    bl_label = "Export to JSON"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.gnd_props.directory_error

    def execute(self, context):
        export_groups()
        return {"FINISHED"}


class NODEDEV_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "nodedev.import_json"
    bl_label = "Import from JSON"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.gnd_props.directory_error

    def execute(self, context):
        import_groups()
        return {"FINISHED"}


class NODEDEV_OT_Surprise(bpy.types.Operator):
    bl_idname = "nodedev.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        # Get menu switch of tree Geometry Nodes
        # assets.import_assets()
        cls = bpy.types.NodeSocketCollection
        print(cls.bl_rna.properties["default_value"].fixed_type)
        return {"FINISHED"}


class NODEDEV_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "nodedev.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}


def save_handler(scene):
    bpy.ops.nodedev.export_json()
