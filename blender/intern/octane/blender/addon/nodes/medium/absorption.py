##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneAbsorptionScale(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionScale"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=100.000000, update=OctaneBaseSocket.update_node_tree, description="Absorption scale", min=0.000100, max=10000.000000, soft_min=0.000100, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionRayMarchStepLength"
    bl_label="Volume step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=274)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3030001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionShadowRayMarchStepLength(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionShadowRayMarchStepLength"
    bl_label="Vol. shadow ray step length"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=496)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=4.000000, update=OctaneBaseSocket.update_node_tree, description="Step length that is used by the shadow ray for marching through volumes", min=0.000010, max=1000000.000000, soft_min=0.010000, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionUseRayStepLengthForShadowRays(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionUseRayStepLengthForShadowRays"
    bl_label="Use Vol. step length for Vol. shadow ray step length"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=515)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Uses Volume step length as Volume shadow ray step length as well")
    octane_hide_value=False
    octane_min_version=8000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionDisplacement(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionDisplacement"
    bl_label="Sample position displacement"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=7000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionAbsorption(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionAbsorption"
    bl_label="Absorption"
    color=consts.OctanePinColor.Texture
    octane_default_node_type="OctaneRGBColor"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=1)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="Absorption cross section. Determines how quickly light is absorbed while traveling through this medium", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="COLOR", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionInvertAbsorption(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionInvertAbsorption"
    bl_label="Invert absorption"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=302)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Inverts the absorption color so that the absorption channel becomes a transparency channel. This helps visualizing the effect of the specified color since a neutral background shining through the medium will appear approximately in that color")
    octane_hide_value=False
    octane_min_version=3000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAbsorptionLockStepLength(OctaneBaseSocket):
    bl_idname="OctaneAbsorptionLockStepLength"
    bl_label="Lock step length pins"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=500)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Locks volume step length and shadow step length pins. So if the value of one is changed then the other one is also changed automatically")
    octane_hide_value=False
    octane_min_version=7000000
    octane_end_version=8000005
    octane_deprecated=True

class OctaneAbsorptionGroupAbsorption(OctaneGroupTitleSocket):
    bl_idname="OctaneAbsorptionGroupAbsorption"
    bl_label="[OctaneGroupTitle]Absorption"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Absorption;Invert absorption;")

class OctaneAbsorption(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAbsorption"
    bl_label="Absorption"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=58)
    octane_socket_list: StringProperty(name="Socket List", default="Density;Volume step length;Vol. shadow ray step length;Use Vol. step length for Vol. shadow ray step length;Sample position displacement;Absorption;Invert absorption;Lock step length pins;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=8)

    def init(self, context):
        self.inputs.new("OctaneAbsorptionScale", OctaneAbsorptionScale.bl_label).init()
        self.inputs.new("OctaneAbsorptionRayMarchStepLength", OctaneAbsorptionRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneAbsorptionShadowRayMarchStepLength", OctaneAbsorptionShadowRayMarchStepLength.bl_label).init()
        self.inputs.new("OctaneAbsorptionUseRayStepLengthForShadowRays", OctaneAbsorptionUseRayStepLengthForShadowRays.bl_label).init()
        self.inputs.new("OctaneAbsorptionDisplacement", OctaneAbsorptionDisplacement.bl_label).init()
        self.inputs.new("OctaneAbsorptionGroupAbsorption", OctaneAbsorptionGroupAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionAbsorption", OctaneAbsorptionAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionInvertAbsorption", OctaneAbsorptionInvertAbsorption.bl_label).init()
        self.inputs.new("OctaneAbsorptionLockStepLength", OctaneAbsorptionLockStepLength.bl_label).init()
        self.outputs.new("OctaneMediumOutSocket", "Medium out").init()


_CLASSES=[
    OctaneAbsorptionScale,
    OctaneAbsorptionRayMarchStepLength,
    OctaneAbsorptionShadowRayMarchStepLength,
    OctaneAbsorptionUseRayStepLengthForShadowRays,
    OctaneAbsorptionDisplacement,
    OctaneAbsorptionAbsorption,
    OctaneAbsorptionInvertAbsorption,
    OctaneAbsorptionLockStepLength,
    OctaneAbsorptionGroupAbsorption,
    OctaneAbsorption,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
