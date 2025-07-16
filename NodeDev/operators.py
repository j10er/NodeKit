import bpy
from .json_nodes.import_export import export_trees, import_groups
from .json_nodes.attributes import generate_attributes_dict
from .json_nodes import file


class NODEDEV_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "nodedev.import_json"
    bl_label = "Import from JSON"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.gnd_props.directory_error

    def invoke(self, context, event):
        num_of_json = file.number_of_files(".json")
        num_of_blend = file.number_of_files(".blend")
        return context.window_manager.invoke_confirm(
            self,
            event=event,
            title=f"Found {num_of_json} node group{'s' if num_of_json > 1 else ''} and {num_of_blend} asset{'s' if num_of_blend>1 else ''}. This will overwrite all node groups and assets in this file that are managed by the add-on. Are you sure?",
        )

    def execute(self, context):
        import_groups()
        bpy.context.scene.gnd_props.is_imported = True
        return {"FINISHED"}


class NODEDEV_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "nodedev.export_json"
    bl_label = "Export to JSON"

    @classmethod
    def poll(cls, context):
        return (
            not bpy.context.scene.gnd_props.directory_error
            and bpy.context.scene.gnd_props.is_imported
        )

    def execute(self, context):
        export_trees()
        return {"FINISHED"}


class NODEDEV_OT_Surprise(bpy.types.Operator):
    bl_idname = "nodedev.surprise"
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


class NODEDEV_OT_SETUP_FOLDER(bpy.types.Operator):
    bl_idname = "nodedev.setup_folder"
    bl_label = "Confirm Action"

    filepath: bpy.props.StringProperty(subtype="DIR_PATH")

    def execute(self, context):
        self.report({"INFO"}, f"Confirmed for folder: {self.filepath}")
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}

    def draw(self, context):
        layout = self.layout
        layout.label(text=f"Use folder: {self.filepath}?")

    def execute_post_confirm(self, context):
        self.report({"INFO"}, "Action executed!")
        return {"FINISHED"}

    def invoke_confirm(self, context):
        wm = context.window_manager
        return wm.invoke_confirm(self, event=None)

    def execute(self, context):
        # Called after file browser selection — now show confirmation dialog
        return context.window_manager.invoke_confirm(self, event=None)
