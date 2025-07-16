import bpy
import logging

log = logging.getLogger(__name__)
addon_name = "NodeKit"


class VIEW3D_PT_SidePanel(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = addon_name
    bl_label = addon_name

    def draw(self, context):

        layout = self.layout
        layout.prop(context.scene.node_kit, "folder_path", text="Nodes Path")
        if context.scene.node_kit.directory_error:
            box = layout.box()
            box.label(text=context.scene.node_kit.directory_error, icon="ERROR")
        layout.operator("nodekit.import_json")
        layout.operator("nodekit.export_json")
        layout.separator()
        if log.isEnabledFor(logging.DEBUG):
            layout.operator("nodekit.surprise")
            layout.operator("nodekit.generate_default_values")
