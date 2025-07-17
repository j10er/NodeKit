# NodeDev

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Blender](https://img.shields.io/badge/Blender-4.3%2B-orange.svg)](https://www.blender.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green.svg)](https://www.python.org/)

A Blender addon for developing, testing, and managing Geometry Node Trees. This addon provides tools for exporting node trees to JSON format, importing them back into Blender, and maintaining a robust development workflow for geometry nodes.


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




## Object Naming
- How to handle invalid characters for filenames?
1. replace, but keep actual name in blend file or JSON

# TODO
# Node Features
- MenuSwitch Item Description
## Path Management/Workflow
- test with git

## Assets
- What to do if asset is used in multiple contexts? collection with objects, but objects also used on its own
- what to do if assset has geometry nodes
## Tests
### Test the behavior
- All basic tests: recieve a point at (0,0,0) as input, test successful if it now is at (0,0,1), otherwise wrong
