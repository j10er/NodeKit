import bpy
import os
import pytest
import shutil

from bl_ext.user_default.nodekit.json_nodes.data.blend_data import BlendData

from abc import ABC
from pathlib import Path
from deepdiff import DeepDiff


class TestNodeKit(ABC):
    """Base class for NodeKit tests."""

    test_tree_names: list[str]
    other_tree_names: list[str]
    nodes_path: str
    blend_path: str

    def open_blend_file(self):
        self.clear_folder(self.nodes_path)
        bpy.ops.wm.open_mainfile(filepath=self.blend_path)
        bpy.context.scene.node_kit.folder_path = self.nodes_path

    def clear_folder(self):
        if os.path.exists(self.nodes_path):
            shutil.rmtree(self.nodes_path)
        os.makedirs(self.nodes_path)

    def new_file(self):
        bpy.ops.wm.read_homefile(use_empty=True)
        bpy.context.scene.node_kit.folder_path = self.nodes_path

    @pytest.fixture(scope="module")
    def fixture_export_import(self):
        self.open_blend_file()
        bpy.ops.nodekit.export_json()

        self.new_file()
        bpy.ops.nodekit.import_json()

        yield

        self.new_file()

    def test_original_trees_exist(self):
        """Test if the fixture is imported correctly."""
        self.open_blend_file()
        for tree_name in self.other_tree_names:
            assert (
                tree_name in bpy.data.node_groups
            ), f"{tree_name} should be in the node groups"

    @pytest.fixture(scope="module")
    def capture_original_data(self, request):
        self.open_blend_file()
        data_dicts = BlendData().get_data_dicts()
        bpy.ops.nodekit.export_json()
        self.new_file()
        bpy.ops.nodekit.import_json()

        yield data_dicts

        self.new_file()

    @pytest.mark.parametrize("tree_name", test_tree_names)
    def test_imported_tree_data(self, capture_original_data, tree_name):
        """Test that the imported node tree data matches the expected structure."""
        old_data_dicts = capture_original_data
        new_data_dicts = BlendData().get_data_dicts()
        uuid = next(
            (
                uuid
                for uuid, data_dict in old_data_dicts.items()
                if data_dict["name"] == tree_name
            ),
            None,
        )
        assert uuid, f"{tree_name} not found in old data dicts"
        assert uuid in new_data_dicts, f"{tree_name} not found in new data dicts"

        old_data_dict = old_data_dicts[uuid]
        new_data_dict = new_data_dicts[uuid]

        # Compare the two dictionaries
        diff = DeepDiff(old_data_dict, new_data_dict)
        assert diff == {}, f"Difference found in {tree_name}: {diff}"

    @pytest.mark.parametrize("tree_name", test_tree_names)
    def test_twice_imported_tree_data(self, capture_original_data, tree_name):
        """Test that the imported node tree data matches the expected structure."""
        old_data_dicts = capture_original_data
        bpy.ops.nodekit.import_json()
        new_data_dicts = BlendData().get_data_dicts()
        uuid = next(
            (
                uuid
                for uuid, data_dict in old_data_dicts.items()
                if data_dict["name"] == tree_name
            ),
            None,
        )
        assert uuid, f"{tree_name} not found in old data dicts"
        assert uuid in new_data_dicts, f"{tree_name} not found in new data dicts"

        old_data_dict = old_data_dicts[uuid]
        new_data_dict = new_data_dicts[uuid]

        # Compare the two dictionaries
        diff = DeepDiff(old_data_dict, new_data_dict)
        assert diff == {}, f"Difference found in {tree_name}: {diff}"
