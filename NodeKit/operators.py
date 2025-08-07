import bpy
from pprint import pprint
from pathlib import Path
from . import config
from .json_nodes import file
from .json_nodes.attributes import generate_attributes_dict
from .json_nodes.import_export import export_to, import_from


class NODEKIT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "nodekit.import_json"
    bl_label = "Import Nodes from JSON"
    bl_description = "Import node groups and assets from JSON files"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.node_kit.directory_error

    def invoke(self, context, event):
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        num_of_json = file.number_of_files(folder_path, ".json")
        num_of_blend = file.number_of_files(folder_path, ".blend")
        return context.window_manager.invoke_confirm(
            self,
            event=event,
            title=f"Found {num_of_json} node group{'s' if num_of_json != 1 else ''} and {num_of_blend} asset{'s' if num_of_blend != 1 else ''}. This will overwrite all node groups and assets in this file that are managed by the add-on. Are you sure?",
        )

    def execute(self, context):
        print("Executing import operator")
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        result = import_from(
            folder_path,
            append=False,
            include_assets=True,
        )

        if result.startswith("Error"):
            self.report({"ERROR"}, result)
            return {"CANCELLED"}
        else:
            self.report({"INFO"}, result)
            bpy.context.scene.node_kit.is_imported = True
            return {"FINISHED"}


class NODEKIT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "nodekit.export_json"
    bl_label = "Export Nodes to JSON"
    bl_description = "Export node groups to JSON files"

    @classmethod
    def poll(cls, context):

        return not bpy.context.scene.node_kit.directory_error and (
            bpy.context.scene.node_kit.is_imported
            or file.folder_is_empty(
                bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
            )
            or True
        )

    def execute(self, context):
        print("Executing export operator")
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        result = export_to(
            folder_path_str=folder_path,
            include_assets=False,
        )

        self.report({"INFO"}, result)
        bpy.context.scene.node_kit.is_imported = True
        return {"FINISHED"}


class NODEKIT_OT_ExportUpdateAssets(bpy.types.Operator):
    bl_idname = "nodekit.export_update_assets"
    bl_label = "Export Nodes to JSON (Update assets)"
    bl_description = "Export assets to JSON files"

    @classmethod
    def poll(cls, context):
        return not bpy.context.scene.node_kit.directory_error and (
            bpy.context.scene.node_kit.is_imported
            or file.folder_is_empty(
                bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
            )
            or True
        )

    def execute(self, context):
        folder_path = bpy.path.abspath(bpy.context.scene.node_kit.folder_path)
        result = export_to(
            folder_path_str=folder_path,
            include_assets=True,
        )

        self.report({"INFO"}, result)
        return {"FINISHED"}


class NODEKIT_OT_AppendJSON(bpy.types.Operator):
    bl_idname = "nodekit.append_json"
    bl_label = "Append Nodes from JSON"
    bl_description = "Pick a folder to append its node groups"

    directory: bpy.props.StringProperty(
        name="Folder", description="Select a folder", subtype="DIR_PATH"
    )  # type: ignore

    def execute(self, context):
        folder_path = bpy.path.abspath(self.directory)

        directory_error = file.validate_path(folder_path)
        if directory_error:
            self.report({"ERROR"}, directory_error)
            return {"CANCELLED"}

        message = import_from(folder_path_str=folder_path, append=True)
        self.report({"INFO"}, message)
        return {"FINISHED"}

    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {"RUNNING_MODAL"}


class NODEKIT_OT_Surprise(bpy.types.Operator):
    bl_idname = "nodekit.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        import cProfile
        from deepdiff import DeepDiff
        from .json_nodes.data.blend_data import BlendData
        from .json_nodes.data.file_data import FileData

        return {"FINISHED"}


class NODEKIT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "nodekit.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        attributes = generate_attributes_dict.generate_attributes_dict()
        return {"FINISHED"}


class NODEKIT_OT_Compare(bpy.types.Operator):
    bl_idname = "nodekit.compare"
    bl_label = "Compare"

    def execute(self, context):
        import cProfile
        from deepdiff import DeepDiff
        from .json_nodes.data.blend_data import BlendData
        from .json_nodes.data.file_data import FileData

        blend_data_dicts = BlendData().get_data_dicts()
        file_data_dicts = FileData(
            Path(bpy.path.abspath(bpy.context.scene.node_kit.folder_path))
        ).get_data_dicts()
        print(blend_data_dicts)
        for uuid, blend_data_dict in blend_data_dicts.items():
            file_data_dict = file_data_dicts.get(uuid, {})
            if not file_data_dict:
                print(f"UUID {uuid} not found in file data")
                continue
            if blend_data_dict != file_data_dict:
                print(f"Difference found for node group {blend_data_dict['name']}")
                pprint(DeepDiff(blend_data_dict, file_data_dict))

        return {"FINISHED"}
