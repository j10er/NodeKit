# GeoNodeDevelopment

[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)
[![Blender](https://img.shields.io/badge/Blender-4.3%2B-orange.svg)](https://www.blender.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B-green.svg)](https://www.python.org/)

A comprehensive Blender addon for developing, testing, and managing Geometry Node Trees. This addon provides tools for exporting node trees to JSON format, importing them back into Blender, and maintaining a robust development workflow for geometry nodes.

## Features

### 🔄 Import/Export System
- **Export to JSON**: Convert Geometry Node Trees to structured JSON files
- **Import from JSON**: Recreate node trees from JSON data with full fidelity
- **Automatic File Organization**: Organizes exported files by tree type and category
- **Version Tracking**: Includes Blender version information in exports

### 🧩 Node Tree Management
- **Complete Tree Serialization**: Preserves all node properties, connections, and interface items
- **Socket Management**: Handles all socket types including custom attributes
- **Interface Preservation**: Maintains input/output panels and their organization
- **UUID Tracking**: Automatic UUID assignment for consistent tree identification

### 🔧 Development Tools
- **Attribute Dictionary Generation**: Automatically generates type definitions for all Blender node types
- **Modern Python Typing**: Uses Python 3.9+ type hints with modern syntax
- **Extensible Architecture**: Modular design for easy extension and customization
- **Auto-save Integration**: Optional automatic export on file save

### 🧪 Testing Framework
- **Automated Testing**: Pytest-based test suite for reliability
- **Multi-version Support**: Tests against multiple Blender versions
- **CI/CD Ready**: Automated build and test pipeline

## Installation

### Method 1: From Release
1. Download the latest `GeoNodeDevelopment.zip` from the releases page
2. In Blender, go to `Edit > Preferences > Add-ons`
3. Click `Install` and select the downloaded zip file
4. Enable the "GeoNodeDevelopment" addon

### Method 2: Development Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/GeoNodeDevelopment.git
   cd GeoNodeDevelopment
   ```

2. Build the addon:
   ```bash
   python dev.py build
   ```

3. Install in Blender using the generated `GeoNodeDevelopment.zip`

## Usage

### Basic Workflow

1. **Set Export Path**: In the 3D Viewport sidebar (N key), find the GeoNodeDevelopment panel and set your JSON folder path

2. **Export Node Trees**:
   - Click "Export to JSON" to export all Geometry Node Trees in your current file
   - Files are organized as: `{tree_type}/{category}/{tree_name}.json`
   - Test trees (starting with ".test: ") are categorized separately

3. **Import Node Trees**:
   - Click "Import from JSON" to recreate all node trees from the JSON folder
   - Existing trees with the same UUID will be updated

### Panel Controls

- **Export to JSON**: Exports all geometry node trees to the specified folder
- **Import from JSON**: Imports all node trees from JSON files in the folder
- **Generate Default Values**: Regenerates the internal attribute dictionary
- **JSON Folder Path**: Set the directory for import/export operations

### File Organization

Exported files follow this structure:
```
JSON_FOLDER/
├── GeometryNodeTree/
│   ├── Groups/
│   │   ├── MyNodeGroup.json
│   │   └── AnotherGroup.json
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


# Procedure
## Exporting
## Importing
- Create empty node trees with interfaces
- add nodes and set their attributes (includes item lists in eg. foreach)
- connect paired nodes (of zones)
- connect nodes with links
- set default values of interface items
- set attributes (here: only default_value) on node sockets