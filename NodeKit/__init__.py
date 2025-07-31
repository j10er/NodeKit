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
from . import operators, ui, properties, config
import logging

classes = [
    properties.NodeKitProperties,
    properties.NodeKitPreferences,
    operators.NODEKIT_OT_ExportJSON,
    operators.NODEKIT_OT_ExportUpdateAssets,
    operators.NODEKIT_OT_ImportJSON,
    operators.NODEKIT_OT_AppendJSON,
    operators.NODEKIT_OT_Surprise,
    operators.NODEKIT_OT_GenerateDefaultValues,
    operators.NODEKIT_OT_TestConversion,
    ui.NODEKIT_PT_MainPanel,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.node_kit = bpy.props.PointerProperty(
        type=properties.NodeKitProperties
    )
    if bpy.context.preferences.addons[__package__].preferences.export_on_save:
        if properties.save_handler not in bpy.app.handlers.save_post:
            bpy.app.handlers.save_post.append(properties.save_handler)

    logging.basicConfig(
        level=logging.DEBUG if config.DEBUG else logging.INFO,
        format="[%(levelname)s] %(message)s",
    )


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.node_kit
