import bpy
import os
import json

from . import file


def import_groups():

    group_dicts = file.load()
