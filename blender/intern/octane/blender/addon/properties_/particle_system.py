# <pep8 compliant>

import bpy
from bpy.props import FloatProperty, PointerProperty
from bpy.utils import register_class, unregister_class
from octane.properties_.common import OctanePropertyGroup
from octane import core


class OctaneHairPropertyGroup(OctanePropertyGroup):
    def update_hair_setting(self, _context):
        # Need to trigger an update here
        if not core.ENABLE_OCTANE_ADDON_CLIENT:
            self.id_data.update_tag()
    root_width: FloatProperty(
        name="Root thickness",
        description="Hair thickness at root",
        min=0.0, max=1000.0,
        default=0.001,
        precision=3,
        step=0.1,
        update=update_hair_setting,
    )
    tip_width: FloatProperty(
        name="Tip thickness",
        description="Hair thickness at tip",
        min=0.0, max=1000.0,
        default=0.001,
        precision=3,
        step=0.1,
        update=update_hair_setting,
    )
    min_curvature: FloatProperty(
        name="Minimal curvature (deg.)",
        description="Hair points having angle deviation from previous point less than this value will be skipped",
        min=0.0, max=180.0,
        default=0.0,
        update=update_hair_setting,
    )
    w_min: FloatProperty(
        name="Min. W",
        description="W coordinate of the root of a hair: it represents a position on a color gradient for roots of "
                    "all hairs of this particle system",
        min=0.0, max=1.0,
        default=0.0,
        update=update_hair_setting,
    )
    w_max: FloatProperty(
        name="Max. W",
        description="W coordinate of the tip of a hair: it represents a position on a color gradient for tips of all "
                    "hairs of this particle system",
        min=0.0, max=1.0,
        default=1.0,
        update=update_hair_setting,
    )

    @classmethod
    def register(cls):
        bpy.types.ParticleSettings.octane = PointerProperty(
            name="Octane Hair Settings",
            description="Octane hair settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.ParticleSettings.octane


_CLASSES = [
    OctaneHairPropertyGroup,
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
