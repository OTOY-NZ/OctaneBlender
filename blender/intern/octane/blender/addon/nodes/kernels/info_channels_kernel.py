##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneInfoChannelsKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMaxsamples"
    bl_label = "Max. samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5000, description="The maximum of samples per that will be calculated until rendering is stopped", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelType(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelType"
    bl_label = "Type"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=81)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Geometric normal", "Geometric normal", "", 0),
        ("Smooth normal", "Smooth normal", "", 8),
        ("Shading normal", "Shading normal", "", 1),
        ("Tangent (local) normal", "Tangent (local) normal", "", 15),
        ("Z depth", "Z depth", "", 3),
        ("Position", "Position", "", 2),
        ("Texture coordinate", "Texture coordinate", "", 5),
        ("Texture tangent", "Texture tangent", "", 6),
        ("Motion vector", "Motion vector", "", 11),
        ("Material ID", "Material ID", "", 4),
        ("Object layer ID", "Object layer ID", "", 9),
        ("Object layer color", "Object layer color", "", 24),
        ("Baking group ID", "Baking group ID", "", 17),
        ("Light pass ID", "Light pass ID", "", 14),
        ("Render layer ID", "Render layer ID", "", 12),
        ("Render layer mask", "Render layer mask", "", 13),
        ("Wireframe", "Wireframe", "", 7),
        ("Ambient occlusion (AO)", "Ambient occlusion (AO)", "", 10),
        ("Opacity", "Opacity", "", 16),
        ("Roughness", "Roughness", "", 18),
        ("Index of refraction (IOR)", "Index of refraction (IOR)", "", 19),
        ("Diffuse filter", "Diffuse filter", "", 20),
        ("Reflection filter", "Reflection filter", "", 21),
        ("Refraction filter", "Refraction filter", "", 22),
        ("Transmission filter", "Transmission filter", "", 23),
    ]
    default_value: EnumProperty(default="Wireframe", description="Infochannels kernel type", items=items)

class OctaneInfoChannelsKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelRayepsilon"
    bl_label = "Ray epsilon"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000100, description="Shadow ray offset distance to avoid self-intersection", min=0.000000, max=0.100000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelFiltersize"
    bl_label = "Filter size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.200000, description="Pixel filter radius", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelAodist(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelAodist"
    bl_label = "AO distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=3.000000, description="Ambient occlusion distance", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelAoAlphaShadows(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelAoAlphaShadows"
    bl_label = "AO alpha shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=258)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Take into account alpha maps when calculating ambient occlusion")

class OctaneInfoChannelsKernelOpacity(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelOpacity"
    bl_label = "Opacity threshold"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Geometry with opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelZDepthMax(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelZDepthMax"
    bl_label = "Maximum Z-depth"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=257)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=5.000000, description="The maximum Z-depth value. Background pixels will get this value and and any foreground depths will be clamped at this value. This applies with or without tone mapping, but tone mapping will map the maximum Z-depth to white (0 is mapped to black)", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelUVMax(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelUVMax"
    bl_label = "UV max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=250)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelUvSet(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelUvSet"
    bl_label = "UV coordinate selection"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelMaxSpeed(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMaxSpeed"
    bl_label = "Max speed"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=109)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelSamplingMode(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelSamplingMode"
    bl_label = "Sampling mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=329)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", description="Enables motion blur and depth of field, and sets pixel filtering modes.  'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering. 'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled. 'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render passes except for render layer mask and ambient occlusion", items=items)

class OctaneInfoChannelsKernelBump(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelBump"
    bl_label = "Bump and normal mapping"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Take bump and normal mapping into account for shading normal and texture tangent output and wireframe shading")

class OctaneInfoChannelsKernelHighlightBackfaces(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelHighlightBackfaces"
    bl_label = "Wireframe backface highlighting"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=72)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Show faces seen from the backside of the face normal in a different color in wireframe mode")

class OctaneInfoChannelsKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMaxsubdLevel"
    bl_label = "Max subdivision level"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=10, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelAlphachannel"
    bl_label = "Alpha channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with 'fake shadows' enabled")

class OctaneInfoChannelsKernelParallelSamples(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelParallelSamples"
    bl_label = "Parallel samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=273)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=16, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMaxTileSamples"
    bl_label = "Max. tile samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=267)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=32, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMinimizeNetTraffic"
    bl_label = "Minimize net traffic"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=270)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")

class OctaneInfoChannelsKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelWhiteLightSpectrum"
    bl_label = "White light spectrum"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=701)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("D65", "D65", "", 1),
        ("Legacy/flat", "Legacy/flat", "", 0),
    ]
    default_value: EnumProperty(default="D65", description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, black body emitters). This determines the spectrum that will produce white (before white balance) in the final image. Use D65 to adapt to a reasonable daylight 'white' color. Use Legacy/flat to preserve the appearance of old projects (spectral emitters will appear rather blue)", items=items)

class OctaneInfoChannelsKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelUseOldColorPipeline"
    bl_label = "Use old color pipeline"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")

class OctaneInfoChannelsKernelDeepEnable(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelDeepEnable"
    bl_label = "Deep image"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=263)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render a deep image")

class OctaneInfoChannelsKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelDeepEnablePasses"
    bl_label = "Deep render passes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=446)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Include render passes in deep pixels")

class OctaneInfoChannelsKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelMaxDepthSamples"
    bl_label = "Max. depth samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=266)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernelDepthTolerance(OctaneBaseSocket):
    bl_idname = "OctaneInfoChannelsKernelDepthTolerance"
    bl_label = "Depth tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=264)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.050000, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneInfoChannelsKernel(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneInfoChannelsKernel"
    bl_label = "Info channels kernel"
    octane_node_type: IntProperty(name="Octane Node Type", default=26)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Type;Ray epsilon;Filter size;AO distance;AO alpha shadows;Opacity threshold;Maximum Z-depth;UV max;UV coordinate selection;Max speed;Sampling mode;Bump and normal mapping;Wireframe backface highlighting;Max subdivision level;Alpha channel;Parallel samples;Max. tile samples;Minimize net traffic;White light spectrum;Use old color pipeline;Deep image;Deep render passes;Max. depth samples;Depth tolerance;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneInfoChannelsKernelMaxsamples", OctaneInfoChannelsKernelMaxsamples.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelType", OctaneInfoChannelsKernelType.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelRayepsilon", OctaneInfoChannelsKernelRayepsilon.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelFiltersize", OctaneInfoChannelsKernelFiltersize.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelAodist", OctaneInfoChannelsKernelAodist.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelAoAlphaShadows", OctaneInfoChannelsKernelAoAlphaShadows.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelOpacity", OctaneInfoChannelsKernelOpacity.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelZDepthMax", OctaneInfoChannelsKernelZDepthMax.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelUVMax", OctaneInfoChannelsKernelUVMax.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelUvSet", OctaneInfoChannelsKernelUvSet.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelMaxSpeed", OctaneInfoChannelsKernelMaxSpeed.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelSamplingMode", OctaneInfoChannelsKernelSamplingMode.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelBump", OctaneInfoChannelsKernelBump.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelHighlightBackfaces", OctaneInfoChannelsKernelHighlightBackfaces.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelMaxsubdLevel", OctaneInfoChannelsKernelMaxsubdLevel.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelAlphachannel", OctaneInfoChannelsKernelAlphachannel.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelParallelSamples", OctaneInfoChannelsKernelParallelSamples.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelMaxTileSamples", OctaneInfoChannelsKernelMaxTileSamples.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelMinimizeNetTraffic", OctaneInfoChannelsKernelMinimizeNetTraffic.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelWhiteLightSpectrum", OctaneInfoChannelsKernelWhiteLightSpectrum.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelUseOldColorPipeline", OctaneInfoChannelsKernelUseOldColorPipeline.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelDeepEnable", OctaneInfoChannelsKernelDeepEnable.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelDeepEnablePasses", OctaneInfoChannelsKernelDeepEnablePasses.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelMaxDepthSamples", OctaneInfoChannelsKernelMaxDepthSamples.bl_label)
        self.inputs.new("OctaneInfoChannelsKernelDepthTolerance", OctaneInfoChannelsKernelDepthTolerance.bl_label)
        self.outputs.new("OctaneKernelOutSocket", "Kernel out")


def register():
    register_class(OctaneInfoChannelsKernelMaxsamples)
    register_class(OctaneInfoChannelsKernelType)
    register_class(OctaneInfoChannelsKernelRayepsilon)
    register_class(OctaneInfoChannelsKernelFiltersize)
    register_class(OctaneInfoChannelsKernelAodist)
    register_class(OctaneInfoChannelsKernelAoAlphaShadows)
    register_class(OctaneInfoChannelsKernelOpacity)
    register_class(OctaneInfoChannelsKernelZDepthMax)
    register_class(OctaneInfoChannelsKernelUVMax)
    register_class(OctaneInfoChannelsKernelUvSet)
    register_class(OctaneInfoChannelsKernelMaxSpeed)
    register_class(OctaneInfoChannelsKernelSamplingMode)
    register_class(OctaneInfoChannelsKernelBump)
    register_class(OctaneInfoChannelsKernelHighlightBackfaces)
    register_class(OctaneInfoChannelsKernelMaxsubdLevel)
    register_class(OctaneInfoChannelsKernelAlphachannel)
    register_class(OctaneInfoChannelsKernelParallelSamples)
    register_class(OctaneInfoChannelsKernelMaxTileSamples)
    register_class(OctaneInfoChannelsKernelMinimizeNetTraffic)
    register_class(OctaneInfoChannelsKernelWhiteLightSpectrum)
    register_class(OctaneInfoChannelsKernelUseOldColorPipeline)
    register_class(OctaneInfoChannelsKernelDeepEnable)
    register_class(OctaneInfoChannelsKernelDeepEnablePasses)
    register_class(OctaneInfoChannelsKernelMaxDepthSamples)
    register_class(OctaneInfoChannelsKernelDepthTolerance)
    register_class(OctaneInfoChannelsKernel)

def unregister():
    unregister_class(OctaneInfoChannelsKernel)
    unregister_class(OctaneInfoChannelsKernelDepthTolerance)
    unregister_class(OctaneInfoChannelsKernelMaxDepthSamples)
    unregister_class(OctaneInfoChannelsKernelDeepEnablePasses)
    unregister_class(OctaneInfoChannelsKernelDeepEnable)
    unregister_class(OctaneInfoChannelsKernelUseOldColorPipeline)
    unregister_class(OctaneInfoChannelsKernelWhiteLightSpectrum)
    unregister_class(OctaneInfoChannelsKernelMinimizeNetTraffic)
    unregister_class(OctaneInfoChannelsKernelMaxTileSamples)
    unregister_class(OctaneInfoChannelsKernelParallelSamples)
    unregister_class(OctaneInfoChannelsKernelAlphachannel)
    unregister_class(OctaneInfoChannelsKernelMaxsubdLevel)
    unregister_class(OctaneInfoChannelsKernelHighlightBackfaces)
    unregister_class(OctaneInfoChannelsKernelBump)
    unregister_class(OctaneInfoChannelsKernelSamplingMode)
    unregister_class(OctaneInfoChannelsKernelMaxSpeed)
    unregister_class(OctaneInfoChannelsKernelUvSet)
    unregister_class(OctaneInfoChannelsKernelUVMax)
    unregister_class(OctaneInfoChannelsKernelZDepthMax)
    unregister_class(OctaneInfoChannelsKernelOpacity)
    unregister_class(OctaneInfoChannelsKernelAoAlphaShadows)
    unregister_class(OctaneInfoChannelsKernelAodist)
    unregister_class(OctaneInfoChannelsKernelFiltersize)
    unregister_class(OctaneInfoChannelsKernelRayepsilon)
    unregister_class(OctaneInfoChannelsKernelType)
    unregister_class(OctaneInfoChannelsKernelMaxsamples)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
