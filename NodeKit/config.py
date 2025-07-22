from typing import TypedDict, Any


class ExportDict(TypedDict):
    name: str
    tree: dict
    blender_version: str
    tree_type: str
    category: str


ASSET_TYPES = {
    "Object": "objects",
    "Material": "materials",
    "Image": "images",
    "Collection": "collections",
}

# Node tree types
SUPPORTED_TREE_TYPES = "GeometryNodeTree"

# File categories
CATEGORY_TESTS = "Tests"
CATEGORY_GROUPS = "Groups"

# Test identification
TEST_PREFIX = ".test: "

# Folder and collection names
ASSETS_FOLDER = "Assets"
ASSETS_COLLECTION_NAME = "Assets"

# JSON structure keys
JSON_KEY_FILE_TYPE = "file_type"
JSON_KEY_NAME = "name"
JSON_KEY_TREE = "tree"
JSON_KEY_BLENDER_VERSION = "blender_version"
JSON_KEY_TREE_TYPE = "tree_type"
JSON_KEY_CATEGORY = "category"
JSON_KEY_UUID = "uuid"
JSON_KEY_INDEX = "index"


# Filename sanitization
INVALID_FILENAME_CHARS = r'[<>:"/\\|?*\n\r\t ]'
FILENAME_REPLACEMENT_CHAR = "_"

DEBUG = True
