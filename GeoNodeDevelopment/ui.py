import bpy

addon_name = "GeoNodeDevelopment"


class VIEW3D_PT_SidePanel(bpy.types.Panel):

    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = addon_name
    bl_label = addon_name

    def draw(self, context):

        layout = self.layout
        layout.operator("object.export_json")
        layout.operator("object.import_json")
        layout.operator("object.surprise")
        layout.operator("object.generate_default_values")
