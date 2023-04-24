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


class OctanePMCKernelMaxsamples(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxsamples"
    bl_label="Max. samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5000, update=OctaneBaseSocket.update_node_tree, description="The maximum samples per pixel that will be calculated until rendering is stopped", min=1, max=1000000, soft_min=1, soft_max=100000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxDiffuseDepth"
    bl_label="Diffuse depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=104)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxGlossyDepth"
    bl_label="Specular depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=105)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=24, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxScatterDepth"
    bl_label="Scatter depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=464)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which scattering is allowed", min=1, max=256, soft_min=1, soft_max=256, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxOverlappingVolumes"
    bl_label="Maximal overlapping volumes"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=702)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelRayepsilon(OctaneBaseSocket):
    bl_idname="OctanePMCKernelRayepsilon"
    bl_label="Ray epsilon"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Shadow Ray Offset Distance", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelFiltersize(OctaneBaseSocket):
    bl_idname="OctanePMCKernelFiltersize"
    bl_label="Filter size"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.200000, update=OctaneBaseSocket.update_node_tree, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelAlphashadows(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAlphashadows"
    bl_label="Alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelCausticBlur(OctaneBaseSocket):
    bl_idname="OctanePMCKernelCausticBlur"
    bl_label="Caustic blur"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=22)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.010000, update=OctaneBaseSocket.update_node_tree, description="Caustic blur for noise reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelGiClamp(OctaneBaseSocket):
    bl_idname="OctanePMCKernelGiClamp"
    bl_label="GI clamp"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=60)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1000000.000000, update=OctaneBaseSocket.update_node_tree, description="GI clamp reducing fireflies", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=1000000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=2040000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname="OctanePMCKernelNestedDielectrics"
    bl_label="Nested dielectrics"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=571)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")
    octane_hide_value=False
    octane_min_version=10020100
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelIrradiance(OctaneBaseSocket):
    bl_idname="OctanePMCKernelIrradiance"
    bl_label="Irradiance mode"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=381)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render the first surface as a white diffuse material")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxsubdLevel"
    bl_label="Max subdivision level"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=10, update=OctaneBaseSocket.update_node_tree, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelAlphachannel(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAlphachannel"
    bl_label="Alpha channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables a compositing alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname="OctanePMCKernelKeepEnvironment"
    bl_label="Keep environment"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=86)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keeps environment with enabled alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelAiLight(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAiLight"
    bl_label="AI light"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=386)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables AI light")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAiLightUpdate"
    bl_label="AI light update"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=384)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables dynamic AI light update")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname="OctanePMCKernelGlobalLightIdMaskAction"
    bl_label="Light IDs action"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=435)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Disable", "Disable", "", 1),
        ("Enable", "Enable", "", 0),
    ]
    default_value: EnumProperty(default="Disable", update=OctaneBaseSocket.update_node_tree, description="The action to be taken on selected lights IDs", items=items)
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname="OctanePMCKernelGlobalLightIdMask"
    bl_label="Light IDs"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=434)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelLightPassMask(OctaneBaseSocket):
    bl_idname="OctanePMCKernelLightPassMask"
    bl_label="Light linking invert"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelPathTermPower(OctaneBaseSocket):
    bl_idname="OctanePMCKernelPathTermPower"
    bl_label="Path term. power"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=129)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Path may get terminated when ray power is less then this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelExplorationStrength(OctaneBaseSocket):
    bl_idname="OctanePMCKernelExplorationStrength"
    bl_label="Exploration strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=44)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.700000, update=OctaneBaseSocket.update_node_tree, description="Effort on investigating good paths", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelDirectLightImportance(OctaneBaseSocket):
    bl_idname="OctanePMCKernelDirectLightImportance"
    bl_label="Direct light importance"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=32)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Computational effort on direct lighting", min=0.010000, max=1.000000, soft_min=0.010000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelMaxrejects(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxrejects"
    bl_label="Max. rejects"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=107)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=500, update=OctaneBaseSocket.update_node_tree, description="Maximum number of consecutive rejects", min=100, max=10000, soft_min=100, soft_max=10000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelParallelism(OctaneBaseSocket):
    bl_idname="OctanePMCKernelParallelism"
    bl_label="Parallel samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=128)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed.\n\nNOTE: Changing this value restarts rendering", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelWorkChunkSize(OctaneBaseSocket):
    bl_idname="OctanePMCKernelWorkChunkSize"
    bl_label="Work chunk size"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=281)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=8, update=OctaneBaseSocket.update_node_tree, description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value may increase render speed but it will increase system memory usage", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname="OctanePMCKernelWhiteLightSpectrum"
    bl_label="White light spectrum"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=701)
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

class OctanePMCKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname="OctanePMCKernelUseOldColorPipeline"
    bl_label="Use old color pipeline"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")
    octane_hide_value=False
    octane_min_version=11000005
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname="OctanePMCKernelToonShadowAmbient"
    bl_label="Toon shadow ambient"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=368)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The ambient modifier of toon shadowing", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelOldVolumeBehavior(OctaneBaseSocket):
    bl_idname="OctanePMCKernelOldVolumeBehavior"
    bl_label="Emulate old volume behavior"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=448)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Emulate the behavior of emission and scattering of version 4.0 and earlier")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctanePMCKernelAffectRoughness(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAffectRoughness"
    bl_label="Affect roughness"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=487)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000000
    octane_end_version=6000006
    octane_deprecated=True

class OctanePMCKernelAiLightUpdateStrength(OctaneBaseSocket):
    bl_idname="OctanePMCKernelAiLightUpdateStrength"
    bl_label="AI light strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=385)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="The strength for dynamic AI light update", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4000009
    octane_deprecated=True

class OctanePMCKernelMaxdepth(OctaneBaseSocket):
    bl_idname="OctanePMCKernelMaxdepth"
    bl_label="Path depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=103)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=16, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Maximum path depth", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2000002
    octane_deprecated=True

class OctanePMCKernelRrprob(OctaneBaseSocket):
    bl_idname="OctanePMCKernelRrprob"
    bl_label="RR probability"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=205)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Russian Roulette Termination Probability (0=auto)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2100000
    octane_deprecated=True

class OctanePMCKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupQuality"
    bl_label="[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Affect roughness;")

class OctanePMCKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupAlphaChannel"
    bl_label="[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;Keep environment;")

class OctanePMCKernelGroupLight(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupLight"
    bl_label="[OctaneGroupTitle]Light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="AI light;AI light update;Light IDs action;Light IDs;Light linking invert;AI light strength;")

class OctanePMCKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupSampling"
    bl_label="[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Path term. power;Exploration strength;Direct light importance;Max. rejects;Parallel samples;Work chunk size;")

class OctanePMCKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupColor"
    bl_label="[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")

class OctanePMCKernelGroupToonShading(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupToonShading"
    bl_label="[OctaneGroupTitle]Toon Shading"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Toon shadow ambient;")

class OctanePMCKernelGroupCompatibilitySettings(OctaneGroupTitleSocket):
    bl_idname="OctanePMCKernelGroupCompatibilitySettings"
    bl_label="[OctaneGroupTitle]Compatibility settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emulate old volume behavior;")

class OctanePMCKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname="OctanePMCKernel"
    bl_label="PMC kernel"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=23)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Alpha channel;Keep environment;AI light;AI light update;Light IDs action;Light IDs;Light linking invert;Path term. power;Exploration strength;Direct light importance;Max. rejects;Parallel samples;Work chunk size;White light spectrum;Use old color pipeline;Toon shadow ambient;Emulate old volume behavior;Affect roughness;AI light strength;Path depth;RR probability;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=34)

    def init(self, context):
        self.inputs.new("OctanePMCKernelGroupQuality", OctanePMCKernelGroupQuality.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxsamples", OctanePMCKernelMaxsamples.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxDiffuseDepth", OctanePMCKernelMaxDiffuseDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxGlossyDepth", OctanePMCKernelMaxGlossyDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxScatterDepth", OctanePMCKernelMaxScatterDepth.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxOverlappingVolumes", OctanePMCKernelMaxOverlappingVolumes.bl_label).init()
        self.inputs.new("OctanePMCKernelRayepsilon", OctanePMCKernelRayepsilon.bl_label).init()
        self.inputs.new("OctanePMCKernelFiltersize", OctanePMCKernelFiltersize.bl_label).init()
        self.inputs.new("OctanePMCKernelAlphashadows", OctanePMCKernelAlphashadows.bl_label).init()
        self.inputs.new("OctanePMCKernelCausticBlur", OctanePMCKernelCausticBlur.bl_label).init()
        self.inputs.new("OctanePMCKernelGiClamp", OctanePMCKernelGiClamp.bl_label).init()
        self.inputs.new("OctanePMCKernelNestedDielectrics", OctanePMCKernelNestedDielectrics.bl_label).init()
        self.inputs.new("OctanePMCKernelIrradiance", OctanePMCKernelIrradiance.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxsubdLevel", OctanePMCKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctanePMCKernelAffectRoughness", OctanePMCKernelAffectRoughness.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupAlphaChannel", OctanePMCKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctanePMCKernelAlphachannel", OctanePMCKernelAlphachannel.bl_label).init()
        self.inputs.new("OctanePMCKernelKeepEnvironment", OctanePMCKernelKeepEnvironment.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupLight", OctanePMCKernelGroupLight.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLight", OctanePMCKernelAiLight.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLightUpdate", OctanePMCKernelAiLightUpdate.bl_label).init()
        self.inputs.new("OctanePMCKernelGlobalLightIdMaskAction", OctanePMCKernelGlobalLightIdMaskAction.bl_label).init()
        self.inputs.new("OctanePMCKernelGlobalLightIdMask", OctanePMCKernelGlobalLightIdMask.bl_label).init()
        self.inputs.new("OctanePMCKernelLightPassMask", OctanePMCKernelLightPassMask.bl_label).init()
        self.inputs.new("OctanePMCKernelAiLightUpdateStrength", OctanePMCKernelAiLightUpdateStrength.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupSampling", OctanePMCKernelGroupSampling.bl_label).init()
        self.inputs.new("OctanePMCKernelPathTermPower", OctanePMCKernelPathTermPower.bl_label).init()
        self.inputs.new("OctanePMCKernelExplorationStrength", OctanePMCKernelExplorationStrength.bl_label).init()
        self.inputs.new("OctanePMCKernelDirectLightImportance", OctanePMCKernelDirectLightImportance.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxrejects", OctanePMCKernelMaxrejects.bl_label).init()
        self.inputs.new("OctanePMCKernelParallelism", OctanePMCKernelParallelism.bl_label).init()
        self.inputs.new("OctanePMCKernelWorkChunkSize", OctanePMCKernelWorkChunkSize.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupColor", OctanePMCKernelGroupColor.bl_label).init()
        self.inputs.new("OctanePMCKernelWhiteLightSpectrum", OctanePMCKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctanePMCKernelUseOldColorPipeline", OctanePMCKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupToonShading", OctanePMCKernelGroupToonShading.bl_label).init()
        self.inputs.new("OctanePMCKernelToonShadowAmbient", OctanePMCKernelToonShadowAmbient.bl_label).init()
        self.inputs.new("OctanePMCKernelGroupCompatibilitySettings", OctanePMCKernelGroupCompatibilitySettings.bl_label).init()
        self.inputs.new("OctanePMCKernelOldVolumeBehavior", OctanePMCKernelOldVolumeBehavior.bl_label).init()
        self.inputs.new("OctanePMCKernelMaxdepth", OctanePMCKernelMaxdepth.bl_label).init()
        self.inputs.new("OctanePMCKernelRrprob", OctanePMCKernelRrprob.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()


_CLASSES=[
    OctanePMCKernelMaxsamples,
    OctanePMCKernelMaxDiffuseDepth,
    OctanePMCKernelMaxGlossyDepth,
    OctanePMCKernelMaxScatterDepth,
    OctanePMCKernelMaxOverlappingVolumes,
    OctanePMCKernelRayepsilon,
    OctanePMCKernelFiltersize,
    OctanePMCKernelAlphashadows,
    OctanePMCKernelCausticBlur,
    OctanePMCKernelGiClamp,
    OctanePMCKernelNestedDielectrics,
    OctanePMCKernelIrradiance,
    OctanePMCKernelMaxsubdLevel,
    OctanePMCKernelAlphachannel,
    OctanePMCKernelKeepEnvironment,
    OctanePMCKernelAiLight,
    OctanePMCKernelAiLightUpdate,
    OctanePMCKernelGlobalLightIdMaskAction,
    OctanePMCKernelGlobalLightIdMask,
    OctanePMCKernelLightPassMask,
    OctanePMCKernelPathTermPower,
    OctanePMCKernelExplorationStrength,
    OctanePMCKernelDirectLightImportance,
    OctanePMCKernelMaxrejects,
    OctanePMCKernelParallelism,
    OctanePMCKernelWorkChunkSize,
    OctanePMCKernelWhiteLightSpectrum,
    OctanePMCKernelUseOldColorPipeline,
    OctanePMCKernelToonShadowAmbient,
    OctanePMCKernelOldVolumeBehavior,
    OctanePMCKernelAffectRoughness,
    OctanePMCKernelAiLightUpdateStrength,
    OctanePMCKernelMaxdepth,
    OctanePMCKernelRrprob,
    OctanePMCKernelGroupQuality,
    OctanePMCKernelGroupAlphaChannel,
    OctanePMCKernelGroupLight,
    OctanePMCKernelGroupSampling,
    OctanePMCKernelGroupColor,
    OctanePMCKernelGroupToonShading,
    OctanePMCKernelGroupCompatibilitySettings,
    OctanePMCKernel,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


OctanePMCKernelGlobalLightIdMask.octane_default_node_type = "OctaneLightIDBitValue"
OctanePMCKernelLightPassMask.octane_default_node_type = "OctaneLightIDBitValue"

class OctanePMCKernel_Override(OctanePMCKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, True)

utility.override_class(_CLASSES, OctanePMCKernel, OctanePMCKernel_Override)