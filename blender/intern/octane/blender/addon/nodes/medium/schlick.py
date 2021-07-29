##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneSchlickScatteringDirection(OctaneBaseSocket):
    bl_idname = "OctaneSchlickScatteringDirection"
    bl_label = "Scattering direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=210)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Scattering direction, negative values means backward scattering, 0 means equal scattering in all direction (isotropic) and positive means forward scattering", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneSchlick(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSchlick"
    bl_label = "Schlick"
    octane_node_type: IntProperty(name="Octane Node Type", default=60)
    octane_socket_list: StringProperty(name="Socket List", default="Scattering direction;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneSchlickScatteringDirection", OctaneSchlickScatteringDirection.bl_label)
        self.outputs.new("OctanePhaseFunctionOutSocket", "Phase function out")


def register():
    register_class(OctaneSchlickScatteringDirection)
    register_class(OctaneSchlick)

def unregister():
    unregister_class(OctaneSchlick)
    unregister_class(OctaneSchlickScatteringDirection)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
