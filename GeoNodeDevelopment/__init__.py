# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
from . import operators
from . import ui, properties
import logging

classes = [
    ui.VIEW3D_PT_SidePanel,
    operators.OBJECT_OT_ExportJSON,
    operators.OBJECT_OT_ImportJSON,
    operators.OBJECT_OT_Surprise,
    operators.OBJECT_OT_GenerateDefaultValues,
    properties.GNDProperties,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.gnd_props = bpy.props.PointerProperty(type=properties.GNDProperties)
    if operators.save_handler not in bpy.app.handlers.save_post:
        bpy.app.handlers.save_post.append(operators.save_handler)

    logging.basicConfig(
        level=logging.DEBUG,
        format="[%(levelname)s] %(message)s",
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.gnd_props
