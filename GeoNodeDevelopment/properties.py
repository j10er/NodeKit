from bpy.types import PropertyGroup
from bpy.props import StringProperty


class GNDProperties(PropertyGroup):
    json_folder_path: StringProperty(
        name="Folder Path", description="Path to a selected folder", subtype="DIR_PATH"
    )  # type: ignore
