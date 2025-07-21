# NodeKit

[![Blender](https://img.shields.io/badge/Blender-4.3%2B-orange)](https://www.blender.org/)
[![License](https://img.shields.io/badge/License-GPL%202.0-blue.svg)](LICENSE)
[![Release](https://img.shields.io/github/v/release/j10er/NodeKit?include_prereleases)](https://github.com/j10er/NodeKit/releases)

> Tools for building better Blender node trees

## About

NodeKit is a Blender addon designed for developing, testing, and managing Geometry Node Trees with version control in mind. The addon lets you export node trees to JSON format and import them back into Blender, allowing to easily share them.

**Key Features:**
- Export/Import Geometry Node Trees as JSON
- Asset management for node tree dependencies
- Version control friendly workflow
- In development: Testing framework for geometry nodes

> ⚠️ **Development Status**: This add-on is under active development and may contain bugs in the importer and exporter. Use with caution in production projects.

### Settings
- Export on Save: Whether node groups should be exported automatically to the specified location whenever the blend file is saved

## Installation

### Method 1: Download from Releases
1. Download the latest `NodeKit.zip` from the [Releases page](https://github.com/j10er/NodeKit/releases)
2. In Blender, go to **Edit** → **Preferences** → **Add-ons**
3. Click **Install** and select the downloaded `NodeKit.zip` file
4. Enable the "NodeKit" addon in the list

### Method 2: Drag and Drop
1. Download `NodeKit.zip` from releases
2. Simply drag the zip file into your Blender viewport
3. Confirm the installation when prompted

## Usage

### Getting Started

1. **Set up a project folder**: NodeKit works with a dedicated folder structure to organize JSON files and assets
2. **Export your first node tree**: Select an empty folder and export your geometry nodes to it
3. **Version control**: Add your project folder to Git or your preferred VCS

### Basic Workflow

```
Create Node Tree → Export to JSON → Commit to Git → Share/Collaborate → Import JSON → Continue Development
```

### Important Notes

- **Import Warning**: Using "Import from JSON" will delete all other node groups in the current scene
- **Safe Addition**: Use the "Append" function to add node groups without affecting existing ones
- **Project Structure**: Always work with a dedicated project folder for each set of related node trees

## Export Structure

### Folder Structure

```
MyProject/
├── GeometryNodeTree/           # Exported geometry node trees (JSON)
│   ├── Groups/                 # Main geometry node groups
│   │   ├── MyNodeGroup1.json
│   │   ├── MyNodeGroup2.json
│   │   └── ...
│   └── Tests/                  # Test geometry node groups (prefix: ".test: ")
│       ├── .test: TestGroup1.json
│       ├── .test: TestGroup2.json
│       └── ...
└── Assets/                     # Referenced assets and dependencies
    ├── Objects/                # 3D objects and meshes
    ├── Collections/            # Blender collections
    ├── Materials/              # Material definitions
    └── Images/                 # Textures and image assets
```

### JSON Structure

Here is an example of the typical structure of a Geometry Node Tree json file

```json
{
    "name": "Geometry Nodes",
    "tree": {
        "bl_idname": "GeometryNodeTree",
        "name": "Geometry Nodes",
        "is_modifier": true,
        "uuid": "06ddc5a6-a930-45b3-bc3e-63b782202223",
        "nodes": {
            "Group Input": {
                "bl_idname": "NodeGroupInput",
                "location": [
                    -685.4281616210938,
                    61.29835891723633
                ],
                "name": "Group Input",
                "outputs": [
                    {
                        "bl_idname": "NodeSocketGeometry",
                        "name": "Geometry",
                        "to_socket_index": [
                            0
                        ],
                        "to_node": [
                            "Set Position"
                        ],
                        "index": 0
                    }
                ]
            },
            "Group Output": {
                "bl_idname": "NodeGroupOutput",
                "location": [
                    53.52098083496094,
                    35.02762985229492
                ],
                "name": "Group Output"
            },
            "Set Position": {
                "bl_idname": "GeometryNodeSetPosition",
                "location": [
                    -250.32614135742188,
                    87.569091796875
                ],
                "name": "Set Position",
                "inputs": [
                    {
                        "bl_idname": "NodeSocketBool",
                        "name": "Selection",
                        "default_value": true,
                        "index": 1
                    },
                    {
                        "bl_idname": "NodeSocketVector",
                        "name": "Position",
                        "index": 2
                    },
                    {
                        "bl_idname": "NodeSocketVectorTranslation",
                        "name": "Offset",
                        "index": 3
                    }
                ],
                "outputs": [
                    {
                        "bl_idname": "NodeSocketGeometry",
                        "name": "Geometry",
                        "to_socket_index": [
                            0
                        ],
                        "to_node": [
                            "Group Output"
                        ],
                        "index": 0
                    }
                ]
            },
            "Vector": {
                "bl_idname": "FunctionNodeInputVector",
                "location": [
                    -505.98858642578125,
                    -47.92365264892578
                ],
                "name": "Vector",
                "vector": [
                    1.0,
                    2.0,
                    3.0
                ],
                "outputs": [
                    {
                        "bl_idname": "NodeSocketVector",
                        "name": "Vector",
                        "to_socket_index": [
                            3
                        ],
                        "to_node": [
                            "Set Position"
                        ],
                        "index": 0
                    }
                ]
            }
        },
        "interface_items": [
            {
                "name": "Geometry",
                "in_out": "OUTPUT",
                "socket_type": "NodeSocketGeometry",
                "bl_idname": "NodeTreeInterfaceSocketGeometry"
            },
            {
                "name": "Geometry",
                "socket_type": "NodeSocketGeometry",
                "bl_idname": "NodeTreeInterfaceSocketGeometry"
            }
        ]
    },
    "blender_version": "4.5.0",
    "tree_type": "GeometryNodeTree",
    "category": "Groups"
}
```

## Development

### Building from Source

```bash
# Clone the repository
git clone https://github.com/your-username/NodeKit.git
cd NodeKit

# Build the addon
python dev.py build

# Run tests
python dev.py test
```

### Project Structure

```
NodeKit/
├── dev.py                    # Development script
├── README.md
├── NodeKit/                  # Main addon code
│   ├── __init__.py
│   ├── blender_manifest.toml
│   ├── operators.py          # Blender operators
│   ├── ui.py                # User interface
│   ├── properties.py        # Addon properties
│   └── json_nodes/          # Core JSON export/import logic
│       ├── import_export.py
│       ├── assets.py
│       ├── attributes/
│       └── representations/
└── tests/                   # Test suite
    ├── test_trees.py
    └── test_trees.blend
```

## Future Roadmap

- Support for other node tree types like Shader and Compositor nodes
- Build a comprehensive testing framework for geometry nodes
- Improve asset management and linking between projects
- Optimize performance for large node tree exports and imports
- Enhance the user interface and overall workflow experience
