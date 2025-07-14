import bpy

addon_name = "NodeDev"


class VIEW3D_PT_SidePanel(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = addon_name
    bl_label = addon_name

    def draw(self, context):

        layout = self.layout
        layout.operator("nodedev.export_json")
        layout.operator("nodedev.import_json")
        layout.operator("nodedev.surprise")
        layout.operator("nodedev.generate_default_values")
        layout.prop(context.scene.gnd_props, "folder_path", text="Nodes Path")
        if context.scene.gnd_props.directory_error:
            box = layout.box()
            box.label(text=context.scene.gnd_props.directory_error, icon="ERROR")
