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


class OctaneInfoChannelsKernelMaxsamples(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMaxsamples"
    bl_label="Max. samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maxsamples")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5000, update=OctaneBaseSocket.update_node_tree, description="The maximum samples per pixel that will be calculated until rendering is stopped", min=1, max=1000000, soft_min=1, soft_max=100000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelType(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=81)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="type")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
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
    default_value: EnumProperty(default="Wireframe", update=OctaneBaseSocket.update_node_tree, description="Infochannels kernel type", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelRayepsilon(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelRayepsilon"
    bl_label="Ray epsilon"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rayepsilon")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Shadow ray offset distance to avoid self-intersection", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelFiltersize(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelFiltersize"
    bl_label="Filter size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filtersize")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.200000, update=OctaneBaseSocket.update_node_tree, description="Pixel filter radius", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelAodist(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelAodist"
    bl_label="AO distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aodist")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="Ambient occlusion distance", min=0.010000, max=1024.000000, soft_min=0.010000, soft_max=1024.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelAoAlphaShadows(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelAoAlphaShadows"
    bl_label="AO alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=258)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aoAlphaShadows")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take into account alpha maps when calculating ambient occlusion")
    octane_hide_value=False
    octane_min_version=3000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelOpacity(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelOpacity"
    bl_label="Opacity threshold"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=125)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="opacity")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Geometry with opacity higher or equal to this value is treated as totally opaque", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelZDepthMax(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelZDepthMax"
    bl_label="Maximum Z-depth"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=257)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="Z_depth_max")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=5.000000, update=OctaneBaseSocket.update_node_tree, description="The maximum Z-depth value. Background pixels will get this value and and any foreground depths will be clamped at this value. This applies with or without tone mapping, but tone mapping will map the maximum Z-depth to white (0 is mapped to black)", min=0.001000, max=100000.000000, soft_min=0.001000, soft_max=100000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelUVMax(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelUVMax"
    bl_label="UV max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=250)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="UV_max")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="UV coordinate value mapped to maximum intensity", min=0.000010, max=1000.000000, soft_min=0.000010, soft_max=1000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelUvSet(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelUvSet"
    bl_label="UV coordinate selection"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=249)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="uvSet")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="Determines which set of UV coordinates to use", min=1, max=3, soft_min=1, soft_max=3, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2200000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelMaxSpeed(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMaxSpeed"
    bl_label="Max speed"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=109)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maxSpeed")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval", min=0.000010, max=10000.000000, soft_min=0.000010, soft_max=10000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2130000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelSamplingMode(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelSamplingMode"
    bl_label="Sampling mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=329)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="samplingMode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Distributed rays", "Distributed rays", "", 0),
        ("Non-distributed with pixel filtering", "Non-distributed with pixel filtering", "", 1),
        ("Non-distributed without pixel filtering", "Non-distributed without pixel filtering", "", 2),
    ]
    default_value: EnumProperty(default="Distributed rays", update=OctaneBaseSocket.update_node_tree, description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n'Distributed rays': Enables motion blur and DOF, and also enables pixel filtering.\n'Non-distributed with pixel filtering': Disables motion blur and DOF, but leaves pixel filtering enabled.\n'Non-distributed without pixel filtering': Disables motion blur and DOF, and disables pixel filtering for all render AOVs except for render layer mask and ambient occlusion", items=items)
    octane_hide_value=False
    octane_min_version=3050100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelBump(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelBump"
    bl_label="Bump and normal mapping"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=18)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="bump")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take bump and normal mapping into account for shading normal and texture tangent output and wireframe shading")
    octane_hide_value=False
    octane_min_version=1250000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelHighlightBackfaces(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelHighlightBackfaces"
    bl_label="Wireframe backface highlighting"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=72)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="highlightBackfaces")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Show faces seen from the backside of the face normal in a different color in wireframe mode")
    octane_hide_value=False
    octane_min_version=1210000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMaxsubdLevel"
    bl_label="Max subdivision level"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="MaxsubdLevel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelAlphachannel(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelAlphachannel"
    bl_label="Alpha channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="alphachannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelParallelSamples(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelParallelSamples"
    bl_label="Parallel samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=273)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="parallelSamples")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMaxTileSamples"
    bl_label="Max. tile samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=267)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maxTileSamples")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=32, update=OctaneBaseSocket.update_node_tree, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMinimizeNetTraffic"
    bl_label="Minimize net traffic"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=270)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="minimizeNetTraffic")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelWhiteLightSpectrum"
    bl_label="White light spectrum"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=701)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="whiteLightSpectrum")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("D65", "D65", "", 1),
        ("Legacy/flat", "Legacy/flat", "", 0),
    ]
    default_value: EnumProperty(default="D65", update=OctaneBaseSocket.update_node_tree, description="Controls the appearance of colors produced by spectral emitters (e.g. daylight environment, black body emitters). This determines the spectrum that will produce white (before white balance) in the final image. Use D65 to adapt to a reasonable daylight \"white\" color. Use Legacy/flat to preserve the appearance of old projects (spectral emitters will appear rather blue)", items=items)
    octane_hide_value=False
    octane_min_version=11000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelUseOldColorPipeline"
    bl_label="Use old color pipeline"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="useOldColorPipeline")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")
    octane_hide_value=False
    octane_min_version=11000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelDeepEnable(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelDeepEnable"
    bl_label="Deep image"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=263)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="deepEnable")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render a deep image")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelDeepEnablePasses"
    bl_label="Deep render AOVs"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=446)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="deepEnablePasses")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Include render AOVs in deep pixels")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelMaxDepthSamples"
    bl_label="Max. depth samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=266)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maxDepthSamples")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelDepthTolerance(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelDepthTolerance"
    bl_label="Depth tolerance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=264)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="depthTolerance")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.050000, update=OctaneBaseSocket.update_node_tree, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneInfoChannelsKernelDistributedTracing(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelDistributedTracing"
    bl_label="Distributed ray tracing"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=36)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="distributedTracing")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enable depth of field and motion blur")
    octane_hide_value=False
    octane_min_version=1340000
    octane_end_version=3050100
    octane_deprecated=True

class OctaneInfoChannelsKernelAlphashadows(OctaneBaseSocket):
    bl_idname="OctaneInfoChannelsKernelAlphashadows"
    bl_label="AO alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="alphashadows")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Take into account alpha maps when calculating ambient occlusion")
    octane_hide_value=False
    octane_min_version=2130000
    octane_end_version=3000001
    octane_deprecated=True

class OctaneInfoChannelsKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname="OctaneInfoChannelsKernelGroupQuality"
    bl_label="[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Type;Ray epsilon;Filter size;AO distance;AO alpha shadows;Opacity threshold;Maximum Z-depth;UV max;UV coordinate selection;Max speed;Sampling mode;Bump and normal mapping;Wireframe backface highlighting;Max subdivision level;Distributed ray tracing;AO alpha shadows;")

class OctaneInfoChannelsKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname="OctaneInfoChannelsKernelGroupAlphaChannel"
    bl_label="[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;")

class OctaneInfoChannelsKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname="OctaneInfoChannelsKernelGroupSampling"
    bl_label="[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Parallel samples;Max. tile samples;Minimize net traffic;")

class OctaneInfoChannelsKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname="OctaneInfoChannelsKernelGroupColor"
    bl_label="[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")

class OctaneInfoChannelsKernelGroupDeepImage(OctaneGroupTitleSocket):
    bl_idname="OctaneInfoChannelsKernelGroupDeepImage"
    bl_label="[OctaneGroupTitle]Deep image"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;")

class OctaneInfoChannelsKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname="OctaneInfoChannelsKernel"
    bl_label="Info channels kernel"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=26)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Type;Ray epsilon;Filter size;AO distance;AO alpha shadows;Opacity threshold;Maximum Z-depth;UV max;UV coordinate selection;Max speed;Sampling mode;Bump and normal mapping;Wireframe backface highlighting;Max subdivision level;Alpha channel;Parallel samples;Max. tile samples;Minimize net traffic;White light spectrum;Use old color pipeline;Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;Distributed ray tracing;AO alpha shadows;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=27)

    def init(self, context):
        self.inputs.new("OctaneInfoChannelsKernelGroupQuality", OctaneInfoChannelsKernelGroupQuality.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMaxsamples", OctaneInfoChannelsKernelMaxsamples.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelType", OctaneInfoChannelsKernelType.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelRayepsilon", OctaneInfoChannelsKernelRayepsilon.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelFiltersize", OctaneInfoChannelsKernelFiltersize.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelAodist", OctaneInfoChannelsKernelAodist.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelAoAlphaShadows", OctaneInfoChannelsKernelAoAlphaShadows.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelOpacity", OctaneInfoChannelsKernelOpacity.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelZDepthMax", OctaneInfoChannelsKernelZDepthMax.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelUVMax", OctaneInfoChannelsKernelUVMax.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelUvSet", OctaneInfoChannelsKernelUvSet.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMaxSpeed", OctaneInfoChannelsKernelMaxSpeed.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelSamplingMode", OctaneInfoChannelsKernelSamplingMode.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelBump", OctaneInfoChannelsKernelBump.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelHighlightBackfaces", OctaneInfoChannelsKernelHighlightBackfaces.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMaxsubdLevel", OctaneInfoChannelsKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelDistributedTracing", OctaneInfoChannelsKernelDistributedTracing.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelAlphashadows", OctaneInfoChannelsKernelAlphashadows.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelGroupAlphaChannel", OctaneInfoChannelsKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelAlphachannel", OctaneInfoChannelsKernelAlphachannel.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelGroupSampling", OctaneInfoChannelsKernelGroupSampling.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelParallelSamples", OctaneInfoChannelsKernelParallelSamples.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMaxTileSamples", OctaneInfoChannelsKernelMaxTileSamples.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMinimizeNetTraffic", OctaneInfoChannelsKernelMinimizeNetTraffic.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelGroupColor", OctaneInfoChannelsKernelGroupColor.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelWhiteLightSpectrum", OctaneInfoChannelsKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelUseOldColorPipeline", OctaneInfoChannelsKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelGroupDeepImage", OctaneInfoChannelsKernelGroupDeepImage.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelDeepEnable", OctaneInfoChannelsKernelDeepEnable.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelDeepEnablePasses", OctaneInfoChannelsKernelDeepEnablePasses.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelMaxDepthSamples", OctaneInfoChannelsKernelMaxDepthSamples.bl_label).init()
        self.inputs.new("OctaneInfoChannelsKernelDepthTolerance", OctaneInfoChannelsKernelDepthTolerance.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()


_CLASSES=[
    OctaneInfoChannelsKernelMaxsamples,
    OctaneInfoChannelsKernelType,
    OctaneInfoChannelsKernelRayepsilon,
    OctaneInfoChannelsKernelFiltersize,
    OctaneInfoChannelsKernelAodist,
    OctaneInfoChannelsKernelAoAlphaShadows,
    OctaneInfoChannelsKernelOpacity,
    OctaneInfoChannelsKernelZDepthMax,
    OctaneInfoChannelsKernelUVMax,
    OctaneInfoChannelsKernelUvSet,
    OctaneInfoChannelsKernelMaxSpeed,
    OctaneInfoChannelsKernelSamplingMode,
    OctaneInfoChannelsKernelBump,
    OctaneInfoChannelsKernelHighlightBackfaces,
    OctaneInfoChannelsKernelMaxsubdLevel,
    OctaneInfoChannelsKernelAlphachannel,
    OctaneInfoChannelsKernelParallelSamples,
    OctaneInfoChannelsKernelMaxTileSamples,
    OctaneInfoChannelsKernelMinimizeNetTraffic,
    OctaneInfoChannelsKernelWhiteLightSpectrum,
    OctaneInfoChannelsKernelUseOldColorPipeline,
    OctaneInfoChannelsKernelDeepEnable,
    OctaneInfoChannelsKernelDeepEnablePasses,
    OctaneInfoChannelsKernelMaxDepthSamples,
    OctaneInfoChannelsKernelDepthTolerance,
    OctaneInfoChannelsKernelDistributedTracing,
    OctaneInfoChannelsKernelAlphashadows,
    OctaneInfoChannelsKernelGroupQuality,
    OctaneInfoChannelsKernelGroupAlphaChannel,
    OctaneInfoChannelsKernelGroupSampling,
    OctaneInfoChannelsKernelGroupColor,
    OctaneInfoChannelsKernelGroupDeepImage,
    OctaneInfoChannelsKernel,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OctaneInfoChannelsKernel_Override(OctaneInfoChannelsKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, False)

utility.override_class(_CLASSES, OctaneInfoChannelsKernel, OctaneInfoChannelsKernel_Override)