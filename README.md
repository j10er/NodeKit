# NodeDev

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Blender](https://img.shields.io/badge/Blender-4.3%2B-orange.svg)](https://www.blender.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green.svg)](https://www.python.org/)

A comprehensive Blender addon for developing, testing, and managing Geometry Node Trees. This addon provides tools for exporting node trees to JSON format, importing them back into Blender, and maintaining a robust development workflow for geometry nodes.


# Notes

### File Organization

Exported files follow this structure:
```
JSON_FOLDER/
├── GeometryNodeTree/
│   ├── Assets/
│   ├── Groups/
│   │   ├── MyNodeGroup.json
│   │   └── AnotherGroup.json
│   ├── Test-Assets/
│   └── Tests/
│       └── test_MyTest.json
└── {other_tree_types}/
```

### JSON Structure

Each exported file contains:
```json
{
  "name": "NodeTreeName",
  "tree": {
    "name": "NodeTreeName",
    "bl_idname": "GeometryNodeTree",
    "uuid": "unique-identifier",
    "nodes": { /* node data */ },
    "interface_items": [ /* interface definitions */ ]
  },
  "blender_version": "4.3.2",
  "tree_type": "GeometryNodeTree",
  "category": "Groups"
}
```


# Workflow
## First Setup
### From empty json storage, empty blend:
- create empty folder, open with
-
## Path Setup
On changing the directory path:
- validate path and folder contents, if anything other than jsons cancel
- message popup:
  - if contains jsons:
    - ask if import or overwrite existing node trees
  - if is empty:
    - continue
  - ask if export is wanted
## Exporting
- check if node trees are in the files that arent in the blend
## Importing
- Create empty node trees with interfaces
- add nodes and set their attributes (includes item lists in eg. foreach)
- connect paired nodes (of zones)
- connect nodes with links
- set default values of interface items
- set attributes (here: only default_value) on node sockets



# TODO
## Path Management/Workflow
- determine setup workflow
- integration with git workflow

## Only sync changed trees

## Assets
### Export
- asset:
  - Object
  - Collection
  - Material
  - Texture

- determine all assets
- set a uuid for each used asset
- store uuid of asset in node
- export asset to separate file with uuid as filename
What to do if asset is used in multiple contexts? collection with objects, but objects also used on its own
### Import
- Find file with correct uuid
- append to current scene, extra collection?
- set asset pointer as attribute

## Tests
### Based on attributes_dict
- find way to genericallý create each data type

- for each class (except nodetree):
  - create nodetree
  - add this item
  - for each attribute:
    - set random attribute for this datatype
      - int/float: trivial
      - str: random, except filepaths?
      - vector: store size in attributes_dict?
      - enum: ??
      - bpy_collection: find type of collection, add 3 items
      - assets/other objets: future
=> attributes_dict wouldn't be backwards compatible
### Test the behavior of a complex tree
- needs node tester
### Manually
- find key features/node types
- useful?