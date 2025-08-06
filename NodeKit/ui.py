import logging

import bpy

from . import config

log = logging.getLogger(__name__)
addon_name = __package__.split(".")[-1]


class NODEKIT_PT_MainPanel(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = addon_name
    bl_label = addon_name

    def draw(self, context):

        layout = self.layout
        layout.prop(context.scene.node_kit, "folder_path", text="Folder Path")
        if context.scene.node_kit.directory_error:
            box = layout.box()
            box.label(text=context.scene.node_kit.directory_error, icon="ERROR")
        layout.operator("nodekit.import_json")
        layout.operator("nodekit.export_json")
        layout.operator("nodekit.export_update_assets")
        layout.separator()
        layout.operator("nodekit.append_json", text="Append JSON from")

        if config.DEBUG:
            layout.separator()
            layout.operator("nodekit.surprise")
            layout.operator("nodekit.generate_default_values")
            layout.operator("nodekit.compare")
