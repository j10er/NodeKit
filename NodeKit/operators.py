import bpy
from .json_nodes.import_export import export_groups, import_groups
from .json_nodes.attributes import generate_attributes_dict
from .json_nodes import file


class NODEKIT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "nodekit.import_json"
    bl_label = "Import from JSON"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.node_kit.directory_error

    def invoke(self, context, event):
        num_of_json = file.number_of_files(".json")
        num_of_blend = file.number_of_files(".blend")
        return context.window_manager.invoke_confirm(
            self,
            event=event,
            title=f"Found {num_of_json} node group{'s' if num_of_json != 1 else ''} and {num_of_blend} asset{'s' if num_of_blend != 1 else ''}. This will overwrite all node groups and assets in this file that are managed by the add-on. Are you sure?",
        )

    def execute(self, context):
        import_groups()
        bpy.context.scene.node_kit.is_imported = True
        return {"FINISHED"}


class NODEKIT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "nodekit.export_json"
    bl_label = "Export to JSON"

    @classmethod
    def poll(cls, context):
        return (
            not bpy.context.scene.node_kit.directory_error
            and (bpy.context.scene.node_kit.is_imported or file.folder_is_empty())
        )

    def execute(self, context):
        export_groups()
        bpy.context.scene.node_kit.is_imported = True
        return {"FINISHED"}


class NODEKIT_OT_Surprise(bpy.types.Operator):
    bl_idname = "nodekit.surprise"
    bl_label = "Surprise"

    def invoke(self, context, event=None):
        wm = context.window_manager
        return wm.invoke_confirm(self, event=event)

    def execute_post_confirm(self, context):
        self.report({"INFO"}, "Action executed!")
        return {"FINISHED"}

    def cancel(self, context):
        self.report({"WARNING"}, "Operation cancelled.")

    def execute(self, context):

        return {"FINISHED"}


class NODEKIT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "nodekit.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}


def save_handler(scene):
    bpy.ops.nodekit.export_json()