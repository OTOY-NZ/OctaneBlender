##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneProceduralEffectsOperationType(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsOperationType"
    bl_label = "Type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=613)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Combustible Voronoi", "Combustible Voronoi", "", 0),
        ("Fractal", "Fractal", "", 1),
        ("Kaleidoscope", "Kaleidoscope", "", 2),
        ("Neon stripes", "Neon stripes", "", 3),
        ("Paint colors", "Paint colors", "", 4),
        ("Particles", "Particles", "", 5),
        ("Star scroller", "Star scroller", "", 6),
        ("Wavey colors", "Wavey colors", "", 7),
    ]
    default_value: EnumProperty(default="Combustible Voronoi", description="The effect to generate", items=items)

class OctaneProceduralEffectsTime(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsTime"
    bl_label = "Time"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=241)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The animation timestamp", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneProceduralEffectsTransform(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsTransform"
    bl_label = "UV transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneProceduralEffectsProjection(OctaneBaseSocket):
    bl_idname = "OctaneProceduralEffectsProjection"
    bl_label = "Projection"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=141)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=21)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneProceduralEffects(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneProceduralEffects"
    bl_label = "Procedural effects"
    octane_node_type: IntProperty(name="Octane Node Type", default=262)
    octane_socket_list: StringProperty(name="Socket List", default="Type;Time;UV transform;Projection;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneProceduralEffectsOperationType", OctaneProceduralEffectsOperationType.bl_label)
        self.inputs.new("OctaneProceduralEffectsTime", OctaneProceduralEffectsTime.bl_label)
        self.inputs.new("OctaneProceduralEffectsTransform", OctaneProceduralEffectsTransform.bl_label)
        self.inputs.new("OctaneProceduralEffectsProjection", OctaneProceduralEffectsProjection.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneProceduralEffectsOperationType)
    register_class(OctaneProceduralEffectsTime)
    register_class(OctaneProceduralEffectsTransform)
    register_class(OctaneProceduralEffectsProjection)
    register_class(OctaneProceduralEffects)

def unregister():
    unregister_class(OctaneProceduralEffects)
    unregister_class(OctaneProceduralEffectsProjection)
    unregister_class(OctaneProceduralEffectsTransform)
    unregister_class(OctaneProceduralEffectsTime)
    unregister_class(OctaneProceduralEffectsOperationType)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
