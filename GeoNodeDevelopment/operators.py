import bpy
from pprint import pprint
from .nodes import exporter, importer
from .nodes import data, file


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"

    def execute(self, context):
        tree = bpy.data.node_groups.get("Testnodes")
        tree_data = data.NodeTreeData.from_tree(tree)
        tree_dict = tree_data.to_dict()
        pprint(tree_dict)
        file.save_tree_dict(tree_dict)
        return {"FINISHED"}


class OBJECT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "object.import_json"
    bl_label = "Import from JSON"

    def execute(self, context):
        tree_dicts = file.load_all()
        for tree_dict in tree_dicts:
            node_tree_data = data.NodeTreeData.from_dict(tree_dict)
            new_tree = node_tree_data.to_tree()
            # bpy.data.node_groups.append(new_tree)
        return {"FINISHED"}


class OBJECT_OT_Surprise(bpy.types.Operator):
    bl_idname = "object.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        tree = bpy.data.node_groups.get("Testnodes")
        interface = tree.interface
        socket = interface.items_tree[0]
        print(socket.subtype)
        return {"FINISHED"}
