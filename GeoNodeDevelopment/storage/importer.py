import bpy
import os
import json

from .data import NodeTreeData, NodeData, SocketData
from . import file


def import_groups():

    group_dicts = file.load()
