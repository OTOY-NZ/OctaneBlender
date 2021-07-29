##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneCaptureToCustomAOVTexture(OctaneBaseSocket):
    bl_idname = "OctaneCaptureToCustomAOVTexture"
    bl_label = "Capture texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=240)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneCaptureToCustomAOVCustomAov(OctaneBaseSocket):
    bl_idname = "OctaneCaptureToCustomAOVCustomAov"
    bl_label = "Custom AOV"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
    ]
    default_value: EnumProperty(default="None", description="If a custom AOV is selected, it will write the captured (or the overwrite) texture to the selected AOV", items=items)

class OctaneCaptureToCustomAOVOverrideTexture(OctaneBaseSocket):
    bl_idname = "OctaneCaptureToCustomAOVOverrideTexture"
    bl_label = "Override texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=644)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneCaptureToCustomAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneCaptureToCustomAOV"
    bl_label = "Capture to custom AOV"
    octane_node_type: IntProperty(name="Octane Node Type", default=323)
    octane_socket_list: StringProperty(name="Socket List", default="Capture texture;Custom AOV;Override texture;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneCaptureToCustomAOVTexture", OctaneCaptureToCustomAOVTexture.bl_label)
        self.inputs.new("OctaneCaptureToCustomAOVCustomAov", OctaneCaptureToCustomAOVCustomAov.bl_label)
        self.inputs.new("OctaneCaptureToCustomAOVOverrideTexture", OctaneCaptureToCustomAOVOverrideTexture.bl_label)
        self.outputs.new("OctaneTextureOutSocket", "Texture out")


def register():
    register_class(OctaneCaptureToCustomAOVTexture)
    register_class(OctaneCaptureToCustomAOVCustomAov)
    register_class(OctaneCaptureToCustomAOVOverrideTexture)
    register_class(OctaneCaptureToCustomAOV)

def unregister():
    unregister_class(OctaneCaptureToCustomAOV)
    unregister_class(OctaneCaptureToCustomAOVOverrideTexture)
    unregister_class(OctaneCaptureToCustomAOVCustomAov)
    unregister_class(OctaneCaptureToCustomAOVTexture)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
