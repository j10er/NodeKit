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
        socket = tree.interface.new_socket("a")
        all_attributes = set(bpy.types.NodeTreeInterfaceSocket.bl_rna.properties.keys())
        socket_attributes = dir(socket)
        print(socket.bl_rna.properties.keys())
        print(set(socket_attributes) - set(all_attributes))
        return {"FINISHED"}


class OBJECT_OT_GenerateDefaultValues(bpy.types.Operator):
    bl_idname = "object.generate_default_values"
    bl_label = "Generate Default Values"

    def execute(self, context):
        # Define the socket types to analyze
        socket_types = (
            "NodeSocketString",
            "NodeSocketBool",
            "NodeSocketMaterial",
            "NodeSocketVector",
            "NodeSocketInt",
            "NodeSocketMenu",
            "NodeSocketCollection",
            "NodeSocketGeometry",
            "NodeSocketTexture",
            "NodeSocketFloat",
            "NodeSocketColor",
            "NodeSocketObject",
            "NodeSocketRotation",
            "NodeSocketMatrix",
            "NodeSocketImage",
        )

        # Create a temporary node tree
        tree = bpy.data.node_groups.new(
            name="SocketAnalysis",
            type="GeometryNodeTree",
        )

        try:
            interface = tree.interface
            socket_attributes = {}

            # Get the base socket class attributes to exclude them later
            base_socket_class = None
            base_socket_attrs = set()
            if hasattr(bpy.types, "NodeTreeInterfaceSocket"):
                base_socket_class = bpy.types.NodeTreeInterfaceSocket
                base_socket_attrs = set(dir(base_socket_class))

            for socket_type in socket_types:
                try:
                    # Create a socket of this type
                    socket = interface.new_socket(
                        name=socket_type, socket_type=socket_type
                    )

                    # Get all attributes of this socket
                    all_attrs = set(dir(socket))

                    # Filter out base class attributes and private/system attributes
                    unique_attrs = all_attrs - base_socket_attrs

                    # Additional filtering with explicit superclass check
                    filtered_attrs = set()
                    for attr in unique_attrs:
                        if (
                            not attr.startswith("_")
                            and not attr.startswith("bl_")
                            and not callable(getattr(socket, attr, None))
                        ):

                            # Extra check: ensure attribute is not available in superclass
                            if base_socket_class is None or not hasattr(
                                base_socket_class, attr
                            ):
                                filtered_attrs.add(attr)

                    unique_attrs = filtered_attrs

                    # Extract attribute values
                    socket_data = {}
                    for attr in unique_attrs:
                        try:
                            value = getattr(socket, attr)
                            # Convert complex types to serializable formats
                            if hasattr(value, "__iter__") and not isinstance(
                                value, str
                            ):
                                try:
                                    socket_data[attr] = list(value)
                                except:
                                    socket_data[attr] = str(value)
                            else:
                                socket_data[attr] = value
                        except Exception as e:
                            socket_data[attr] = f"Error accessing attribute: {str(e)}"

                    socket_attributes[socket_type] = socket_data
                    print(
                        f"Analyzed {socket_type}: {len(socket_data)} unique attributes"
                    )

                except Exception as e:
                    socket_attributes[socket_type] = f"Error creating socket: {str(e)}"
                    print(f"Error with {socket_type}: {str(e)}")

            # Print the results
            print("\n" + "=" * 60)
            print("NODE TREE INTERFACE SOCKET ATTRIBUTES AND DEFAULT VALUES")
            print("=" * 60)
            pprint(socket_attributes)

        finally:
            # Clean up the temporary tree
            bpy.data.node_groups.remove(tree, do_unlink=True)

        return {"FINISHED"}
