##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import consts, runtime_globals, utility
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_lut import OctaneBaseLutNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneStarFieldDensity(OctaneBaseSocket):
    bl_idname="OctaneStarFieldDensity"
    bl_label="Density"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DENSITY
    octane_pin_name="density"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.001000, update=OctaneBaseSocket.update_node_tree, description="The density of the star field", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldIntensityFalloff(OctaneBaseSocket):
    bl_idname="OctaneStarFieldIntensityFalloff"
    bl_label="Falloff"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INTENSITY_FALLOFF
    octane_pin_name="intensityFalloff"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="How quickly the star brightness falls off. This affects the apparent size of the stars", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldIntensity(OctaneBaseSocket):
    bl_idname="OctaneStarFieldIntensity"
    bl_label="Intensity"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INTENSITY
    octane_pin_name="intensity"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10.000000, update=OctaneBaseSocket.update_node_tree, description="The brightness of the stars", min=0.000000, max=1000.000000, soft_min=0.000000, soft_max=1000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldSpectral(OctaneBaseSocket):
    bl_idname="OctaneStarFieldSpectral"
    bl_label="Spectral"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SPECTRAL
    octane_pin_name="spectral"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enable to shift the color of more distant stars towards the red spectrum")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldTemperatureMin(OctaneBaseSocket):
    bl_idname="OctaneStarFieldTemperatureMin"
    bl_label="Temperature (min)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TEMPERATURE_MIN
    octane_pin_name="temperatureMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=2500.000000, update=OctaneBaseSocket.update_node_tree, description="The minimum temperature, in Kelvin, used to determine the range of colors in spectral mode", min=500.000000, max=50000.000000, soft_min=500.000000, soft_max=50000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldTemperatureMax(OctaneBaseSocket):
    bl_idname="OctaneStarFieldTemperatureMax"
    bl_label="Temperature (max)"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TEMPERATURE_MAX
    octane_pin_name="temperatureMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=10000.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum temperature, in Kelvin, used to determine the range of colors in spectral mode", min=500.000000, max=50000.000000, soft_min=500.000000, soft_max=50000.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=12000008
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldTransform(OctaneBaseSocket):
    bl_idname="OctaneStarFieldTransform"
    bl_label="UVW transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarFieldProjection(OctaneBaseSocket):
    bl_idname="OctaneStarFieldProjection"
    bl_label="Projection"
    color=consts.OctanePinColor.Projection
    octane_default_node_type=consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name="OctaneXYZToUVW"
    octane_pin_id=consts.PinID.P_PROJECTION
    octane_pin_name="projection"
    octane_pin_type=consts.PinType.PT_PROJECTION
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneStarField(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneStarField"
    bl_label="Star field"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneStarFieldDensity,OctaneStarFieldIntensityFalloff,OctaneStarFieldIntensity,OctaneStarFieldSpectral,OctaneStarFieldTemperatureMin,OctaneStarFieldTemperatureMax,OctaneStarFieldTransform,OctaneStarFieldProjection,]
    octane_min_version=12000005
    octane_node_type=consts.NodeType.NT_TEX_STAR_FIELD
    octane_socket_list=["Density", "Falloff", "Intensity", "Spectral", "Temperature (min)", "Temperature (max)", "UVW transform", "Projection", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=8

    def init(self, context):
        self.inputs.new("OctaneStarFieldDensity", OctaneStarFieldDensity.bl_label).init()
        self.inputs.new("OctaneStarFieldIntensityFalloff", OctaneStarFieldIntensityFalloff.bl_label).init()
        self.inputs.new("OctaneStarFieldIntensity", OctaneStarFieldIntensity.bl_label).init()
        self.inputs.new("OctaneStarFieldSpectral", OctaneStarFieldSpectral.bl_label).init()
        self.inputs.new("OctaneStarFieldTemperatureMin", OctaneStarFieldTemperatureMin.bl_label).init()
        self.inputs.new("OctaneStarFieldTemperatureMax", OctaneStarFieldTemperatureMax.bl_label).init()
        self.inputs.new("OctaneStarFieldTransform", OctaneStarFieldTransform.bl_label).init()
        self.inputs.new("OctaneStarFieldProjection", OctaneStarFieldProjection.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneStarFieldDensity,
    OctaneStarFieldIntensityFalloff,
    OctaneStarFieldIntensity,
    OctaneStarFieldSpectral,
    OctaneStarFieldTemperatureMin,
    OctaneStarFieldTemperatureMax,
    OctaneStarFieldTransform,
    OctaneStarFieldProjection,
    OctaneStarField,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
