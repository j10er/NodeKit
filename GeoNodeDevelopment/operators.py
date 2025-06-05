import bpy
from pprint import pprint
from .nodes import exporter, importer
from .nodes import data, file


class OBJECT_OT_ExportJSON(bpy.types.Operator):
    bl_idname = "object.export_json"
    bl_label = "Export to JSON"

    def execute(self, context):
        node_group = bpy.data.node_groups.get("Testnodes")
        tree_data = data.NodeTreeData(node_group)
        tree_dict = tree_data.as_dict()
        pprint(tree_dict)
        file.save_tree_dict(tree_dict)
        return {"FINISHED"}


class OBJECT_OT_ImportJSON(bpy.types.Operator):
    bl_idname = "object.import_json"
    bl_label = "Import from JSON"

    def execute(self, context):
        tree_dicts = file.load_all()
        for tree_dict in tree_dicts:
            node_tree_data = data.NodeTreeData(tree_dict=tree_dict)
            new_tree = node_tree_data.as_tree()
            # bpy.data.node_groups.append(new_tree)
        return {"FINISHED"}


class OBJECT_OT_Surprise(bpy.types.Operator):
    bl_idname = "object.surprise"
    bl_label = "Surprise"

    def execute(self, context):
        node_group = bpy.data.node_groups.get("Testnodes")
        # node_group["uuid"] = "1234567890"
        node = node_group.nodes.get("Cube")

        links = node_group.links
        link = links[0]
        print(dir(link))
        print(link.from_node["uuid"])
        print(link.to_socket.name)
        # print(node.inputs[0])
        # print(list(offset.default_value))
        # pprint(type(node_group))
        # print(node_group.bl_idname)
        return {"FINISHED"}
