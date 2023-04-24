import bpy
import xml.etree.ElementTree as ET
from bpy.props import IntProperty, FloatProperty, BoolProperty, StringProperty, EnumProperty, PointerProperty, FloatVectorProperty, IntVectorProperty, BoolVectorProperty, CollectionProperty
from bpy.utils import register_class, unregister_class
from octane.properties_ import common
from octane.utils import consts, ocio, utility


class OctaneHairSettings(bpy.types.PropertyGroup):
    root_width: FloatProperty(
        name="Root thickness",
        description="Hair thickness at root",
        min=0.0, max=1000.0,
        default=0.001,
    )
    tip_width: FloatProperty(
        name="Tip thickness",
        description="Hair thickness at tip",
        min=0.0, max=1000.0,
        default=0.001,
    )
    min_curvature: FloatProperty(
        name="Minimal curvature (deg.)",
        description="Hair points having angle deviation from previous point less than this value will be skipped",
        min=0.0, max=180.0,
        default=0.0,
    )
    w_min: FloatProperty(
        name="Min. W",
        description="W coordinate of the root of a hair: it represents a position on a color gradient for roots of all hairs of this particle system",
        min=0.0, max=1.0,
        default=0.0,
    )
    w_max: FloatProperty(
        name="Max. W",
        description="W coordinate of the tip of a hair: it represents a position on a color gradient for tips of all hairs of this particle system",
        min=0.0, max=1.0,
        default=1.0,
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
    OctaneHairSettings,
]


def register(): 
    for cls in _CLASSES:
        register_class(cls)

def unregister():
    for cls in _CLASSES:
        unregister_class(cls)