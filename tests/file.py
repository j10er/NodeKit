import bpy
import os
import shutil


def open_blend(blend_path: str, nodes_path: str):
    clear_folder(nodes_path)
    bpy.ops.wm.open_mainfile(filepath=blend_path)
    bpy.context.scene.node_kit.folder_path = nodes_path


def clear_folder(folder_path: str):
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.makedirs(folder_path)


def new(nodes_path: str):
    bpy.ops.wm.read_homefile(use_empty=True)
    bpy.context.scene.node_kit.folder_path = nodes_path
