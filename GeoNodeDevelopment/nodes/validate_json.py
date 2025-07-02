import bpy
import os
import json
import logging
from typing import Any, Dict, List, Tuple, Optional
from .attributes.attributes_dict import DEFAULTS
from . import file

log = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom exception for validation errors"""

    pass


class JSONValidator:
    """Validator for Geometry Node JSON exports"""

    def __init__(self):
        self.current_blender_version = bpy.app.version_string
        self.allowed_tree_types = ["GeometryNodeTree"]
        self.allowed_categories = ["Groups", "Tests"]

    def validate_data_dict(self, data_dict: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """
        Validate a complete data dictionary from export.

        Args:
            data_dict: Dictionary containing exported tree data

        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []

        try:
            # Check top-level structure
            required_keys = ["name", "tree", "blender_version", "tree_type", "category"]
            for key in required_keys:
                if key not in data_dict:
                    errors.append(f"Missing required top-level key: {key}")

            if errors:
                return False, errors

            # Validate blender version
            if not self._validate_blender_version(data_dict["blender_version"]):
                errors.append(
                    f"Blender version mismatch. Expected: {self.current_blender_version}, Got: {data_dict['blender_version']}"
                )

            # Validate tree type
            if data_dict["tree_type"] not in self.allowed_tree_types:
                errors.append(
                    f"Invalid tree_type: {data_dict['tree_type']}. Allowed: {self.allowed_tree_types}"
                )

            # Validate category
            if data_dict["category"] not in self.allowed_categories:
                errors.append(
                    f"Invalid category: {data_dict['category']}. Allowed: {self.allowed_categories}"
                )

            # Validate tree structure
            tree_valid, tree_errors = self._validate_tree_dict(data_dict["tree"])
            if not tree_valid:
                errors.extend([f"Tree validation: {err}" for err in tree_errors])

        except Exception as e:
            errors.append(f"Validation failed with exception: {str(e)}")

        return len(errors) == 0, errors

    def validate_json_file(self, filepath: str) -> Tuple[bool, List[str]]:
        """
        Validate a JSON file containing exported tree data.

        Args:
            filepath: Path to the JSON file

        Returns:
            Tuple of (is_valid, list_of_errors)
        """
        errors = []

        try:
            if not os.path.exists(filepath):
                return False, [f"File does not exist: {filepath}"]

            with open(filepath, "r") as f:
                data_dict = json.load(f)

            return self.validate_data_dict(data_dict)

        except json.JSONDecodeError as e:
            return False, [f"Invalid JSON syntax: {str(e)}"]
        except Exception as e:
            return False, [f"Error reading file: {str(e)}"]

    def _validate_blender_version(self, version: str) -> bool:
        """Check if blender version matches current version"""
        return version == self.current_blender_version

    def _validate_tree_dict(self, tree_dict: Dict[str, Any]) -> Tuple[bool, List[str]]:
        """Validate the tree dictionary structure"""
        errors = []

        try:
            # Check required tree keys
            required_keys = ["bl_idname", "uuid", "nodes", "interface_items"]
            for key in required_keys:
                if key not in tree_dict:
                    errors.append(f"Missing required tree key: {key}")

            if errors:
                return False, errors

            # Validate tree attributes against defaults
            tree_bl_idname = tree_dict.get("bl_idname", "GeometryNodeTree")
            tree_errors = self._validate_attributes(tree_dict, tree_bl_idname)
            if tree_errors:
                errors.extend([f"Tree attributes: {err}" for err in tree_errors])

            # Validate nodes
            if "nodes" in tree_dict:
                for node_name, node_dict in tree_dict["nodes"].items():
                    node_errors = self._validate_node_dict(node_dict)
                    if node_errors:
                        errors.extend(
                            [f"Node '{node_name}': {err}" for err in node_errors]
                        )

            # Validate interface items
            if "interface_items" in tree_dict:
                for i, item_dict in enumerate(tree_dict["interface_items"]):
                    item_errors = self._validate_interface_item(item_dict)
                    if item_errors:
                        errors.extend(
                            [f"Interface item {i}: {err}" for err in item_errors]
                        )

        except Exception as e:
            errors.append(f"Tree validation failed: {str(e)}")

        return len(errors) == 0, errors

    def _validate_node_dict(self, node_dict: Dict[str, Any]) -> List[str]:
        """Validate a single node dictionary"""
        errors = []

        if "bl_idname" not in node_dict:
            errors.append("Missing bl_idname")
            return errors

        # Validate node attributes
        node_bl_idname = node_dict["bl_idname"]
        attr_errors = self._validate_attributes(node_dict, node_bl_idname, "Node")
        errors.extend(attr_errors)

        # Validate sockets
        for socket_type in ["inputs", "outputs"]:
            if socket_type in node_dict:
                for i, socket_dict in enumerate(node_dict[socket_type]):
                    socket_errors = self._validate_socket_dict(socket_dict)
                    if socket_errors:
                        errors.extend(
                            [f"{socket_type}[{i}]: {err}" for err in socket_errors]
                        )

        return errors

    def _validate_socket_dict(self, socket_dict: Dict[str, Any]) -> List[str]:
        """Validate a socket dictionary"""
        errors = []

        if "bl_idname" not in socket_dict:
            errors.append("Missing bl_idname")
            return errors

        socket_bl_idname = socket_dict["bl_idname"]
        attr_errors = self._validate_attributes(
            socket_dict, socket_bl_idname, "NodeSocket"
        )
        errors.extend(attr_errors)

        return errors

    def _validate_interface_item(self, item_dict: Dict[str, Any]) -> List[str]:
        """Validate an interface item dictionary"""
        errors = []

        if "bl_idname" not in item_dict:
            errors.append("Missing bl_idname")
            return errors

        item_bl_idname = item_dict["bl_idname"]
        attr_errors = self._validate_attributes(
            item_dict, item_bl_idname, "NodeTreeInterfaceItem"
        )
        errors.extend(attr_errors)

        # Validate nested items for panels
        if "items" in item_dict:
            for i, nested_item in enumerate(item_dict["items"]):
                nested_errors = self._validate_interface_item(nested_item)
                if nested_errors:
                    errors.extend([f"item[{i}]: {err}" for err in nested_errors])

        return errors

    def _validate_attributes(
        self, obj_dict: Dict[str, Any], bl_idname: str, base_class: str = "Element"
    ) -> List[str]:
        """
        Validate that all attributes in the dictionary are allowed according to DEFAULTS.

        Args:
            obj_dict: Dictionary containing object attributes
            bl_idname: Blender class identifier
            base_class: Base class for attribute lookup

        Returns:
            List of validation errors
        """
        errors = []

        try:
            # Get allowed attributes for this class
            allowed_attributes = self._get_allowed_attributes(bl_idname, base_class)

            if not allowed_attributes:
                errors.append(f"No attribute defaults found for class {bl_idname}")
                return errors

            # Check each attribute in the object
            for attr_name, attr_value in obj_dict.items():
                # Skip meta attributes that aren't in DEFAULTS
                if attr_name in [
                    "bl_idname",
                    "uuid",
                    "nodes",
                    "interface_items",
                    "inputs",
                    "outputs",
                    "items",
                    "index",
                    "to_socket_index",
                    "to_node",
                    "parent_index",
                ]:
                    continue

                if attr_name not in allowed_attributes:
                    errors.append(
                        f"Unknown attribute '{attr_name}' for class {bl_idname}"
                    )
                    continue

                # Validate attribute type
                expected_type, default_value = allowed_attributes[attr_name]
                type_error = self._validate_attribute_type(
                    attr_name, attr_value, expected_type
                )
                if type_error:
                    errors.append(type_error)

        except Exception as e:
            errors.append(f"Attribute validation failed: {str(e)}")

        return errors

    def _get_allowed_attributes(
        self, bl_idname: str, base_class: str = "Element"
    ) -> Dict[str, Tuple[str, Any]]:
        """Get allowed attributes for a given class from DEFAULTS"""
        try:
            # Find the class path in DEFAULTS
            class_path = self._find_class_path(bl_idname)
            if not class_path:
                class_path = self._find_class_path(base_class)

            if not class_path:
                return {}

            # Navigate to the class and collect attributes
            current_subtype = DEFAULTS["Element"]
            allowed_attributes = {}

            # Start with base Element attributes
            allowed_attributes.update(current_subtype[0])

            # Navigate through the class path and merge attributes
            for subtype_name in class_path:
                if len(current_subtype) < 2 or subtype_name not in current_subtype[1]:
                    break
                current_subtype = current_subtype[1][subtype_name]
                if len(current_subtype) > 0:
                    allowed_attributes.update(current_subtype[0])

            return allowed_attributes

        except Exception as e:
            log.warning(f"Error getting allowed attributes for {bl_idname}: {e}")
            return {}

    def _find_class_path(
        self, target_name: str, subtype=None, path=None
    ) -> Optional[List[str]]:
        """Find the path to a class in the DEFAULTS hierarchy"""
        if subtype is None:
            subtype = DEFAULTS["Element"]
        if path is None:
            path = []

        try:
            for name, subtype_data in subtype[1].items() if len(subtype) > 1 else []:
                if name == target_name:
                    return path + [name]
                result = self._find_class_path(target_name, subtype_data, path + [name])
                if result:
                    return result
        except (IndexError, KeyError, TypeError):
            pass

        return None

    def _validate_attribute_type(
        self, attr_name: str, value: Any, expected_type: str
    ) -> Optional[str]:
        """Validate that an attribute value matches its expected type"""
        try:
            if expected_type == "STRING" and not isinstance(value, str):
                return f"Attribute '{attr_name}' should be string, got {type(value).__name__}"
            elif expected_type == "INT" and not isinstance(value, int):
                return (
                    f"Attribute '{attr_name}' should be int, got {type(value).__name__}"
                )
            elif expected_type == "FLOAT" and not isinstance(value, (int, float)):
                return f"Attribute '{attr_name}' should be float, got {type(value).__name__}"
            elif expected_type == "BOOLEAN" and not isinstance(value, bool):
                return f"Attribute '{attr_name}' should be bool, got {type(value).__name__}"
            elif expected_type == "LIST" and not isinstance(value, list):
                return f"Attribute '{attr_name}' should be list, got {type(value).__name__}"
            elif expected_type == "COLLECTION" and not isinstance(value, list):
                return f"Attribute '{attr_name}' should be collection (list), got {type(value).__name__}"
            elif (
                expected_type in ["NODE", "NODETREE", "NONE"]
                and value is not None
                and not isinstance(value, str)
            ):
                return f"Attribute '{attr_name}' should be string or None, got {type(value).__name__}"
        except Exception as e:
            return f"Type validation error for '{attr_name}': {str(e)}"

        return None


def validate_json_file(filepath: str) -> Tuple[bool, List[str]]:
    """
    Convenience function to validate a single JSON file.

    Args:
        filepath: Path to the JSON file to validate

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    validator = JSONValidator()
    return validator.validate_json_file(filepath)


def validate_data_dict(data_dict: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """
    Convenience function to validate a data dictionary.

    Args:
        data_dict: Dictionary containing exported tree data

    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    validator = JSONValidator()
    return validator.validate_data_dict(data_dict)


def validate_folder(folder_path: str) -> Dict[str, Tuple[bool, List[str]]]:
    """
    Validate all JSON files in a folder and its subfolders.

    Args:
        folder_path: Path to the folder containing JSON files

    Returns:
        Dictionary mapping file paths to (is_valid, list_of_errors) tuples
    """
    validator = JSONValidator()
    results = {}

    if not os.path.exists(folder_path):
        return {"error": (False, [f"Folder does not exist: {folder_path}"])}

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".json"):
                filepath = os.path.join(root, file)
                relative_path = os.path.relpath(filepath, folder_path)
                results[relative_path] = validator.validate_json_file(filepath)

    return results


def validate_exported_files() -> Dict[str, Tuple[bool, List[str]]]:
    """
    Validate all exported JSON files in the configured export folder.

    Returns:
        Dictionary mapping file paths to (is_valid, list_of_errors) tuples
    """
    if not file.path_is_valid():
        return {"error": (False, ["Export folder path is not configured or invalid"])}

    return validate_folder(file.get_folder_path())
