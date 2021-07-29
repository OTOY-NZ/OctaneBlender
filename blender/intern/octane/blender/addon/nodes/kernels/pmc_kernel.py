##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePMCKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxsamples"
    bl_label = "Max. samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5000, description="The maximum of samples per that will be calculated until rendering is stopped", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")

class OctanePMCKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxDiffuseDepth"
    bl_label = "Diffuse depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=104)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")

class OctanePMCKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxGlossyDepth"
    bl_label = "Specular depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=105)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=24, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")

class OctanePMCKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxScatterDepth"
    bl_label = "Scatter depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=464)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The maximum path depth for which scattering is allowed", min=1, max=256, soft_min=1, soft_max=256, step=1, subtype="FACTOR")

class OctanePMCKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxOverlappingVolumes"
    bl_label = "Maximal overlapping volumes"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=702)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype="FACTOR")

class OctanePMCKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelRayepsilon"
    bl_label = "Ray epsilon"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000100, description="Shadow Ray Offset Distance", min=0.000000, max=0.100000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctanePMCKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelFiltersize"
    bl_label = "Filter size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.200000, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctanePMCKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAlphashadows"
    bl_label = "Alpha shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with 'fake shadows' enabled")

class OctanePMCKernelCausticBlur(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelCausticBlur"
    bl_label = "Caustic blur"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=22)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.010000, description="Caustic blur for noise reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePMCKernelGiClamp(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGiClamp"
    bl_label = "GI clamp"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=60)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1000000.000000, description="GI clamp reducing fireflies", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctanePMCKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelNestedDielectrics"
    bl_label = "Nested dielectrics"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=571)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")

class OctanePMCKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelIrradiance"
    bl_label = "Irradiance mode"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=381)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render the first surface as a white diffuse material")

class OctanePMCKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxsubdLevel"
    bl_label = "Max subdivision level"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=10, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")

class OctanePMCKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAlphachannel"
    bl_label = "Alpha channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables a compositing alpha channel")

class OctanePMCKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelKeepEnvironment"
    bl_label = "Keep environment"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=86)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Keeps environment with enabled alpha channel")

class OctanePMCKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAiLight"
    bl_label = "AI light"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=386)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables AI light")

class OctanePMCKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelAiLightUpdate"
    bl_label = "AI light update"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=384)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables dynamic AI light update")

class OctanePMCKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGlobalLightIdMaskAction"
    bl_label = "Light IDs action"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=435)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Disable", "Disable", "", 1),
        ("Enable", "Enable", "", 0),
    ]
    default_value: EnumProperty(default="Disable", description="The action to be taken on selected lights IDs", items=items)

class OctanePMCKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelGlobalLightIdMask"
    bl_label = "Light IDs"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=434)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePMCKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelLightPassMask"
    bl_label = "Light linking invert"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePMCKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelPathTermPower"
    bl_label = "Path term. power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=129)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.300000, description="Path may get terminated when ray power is less then this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePMCKernelExplorationStrength(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelExplorationStrength"
    bl_label = "Exploration strength"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=44)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.700000, description="Effort on investigating good paths", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePMCKernelDirectLightImportance(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelDirectLightImportance"
    bl_label = "Direct light importance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=32)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.100000, description="Computational effort on direct lighting", min=0.010000, max=1.000000, soft_min=0.010000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePMCKernelMaxrejects(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelMaxrejects"
    bl_label = "Max. rejects"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=107)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=500, description="Maximum number of consecutive rejects", min=100, max=10000, soft_min=100, soft_max=10000, step=1, subtype="FACTOR")

class OctanePMCKernelParallelism(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelParallelism"
    bl_label = "Parallel samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=128)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed.  NOTE: Changing this value restarts rendering", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")

class OctanePMCKernelWorkChunkSize(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelWorkChunkSize"
    bl_label = "Work chunk size"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=281)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value increases the memory usage on the system, but doesn't affect memory usage on the system and may increase render speed", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")

class OctanePMCKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelWhiteLightSpectrum"
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

class OctanePMCKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelUseOldColorPipeline"
    bl_label = "Use old color pipeline"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")

class OctanePMCKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctanePMCKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=368)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="The ambient modifier of toon shadowing", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctanePMCKernel(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePMCKernel"
    bl_label = "PMC kernel"
    octane_node_type: IntProperty(name="Octane Node Type", default=23)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Alpha channel;Keep environment;AI light;AI light update;Light IDs action;Light IDs;Light linking invert;Path term. power;Exploration strength;Direct light importance;Max. rejects;Parallel samples;Work chunk size;White light spectrum;Use old color pipeline;Toon shadow ambient;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePMCKernelMaxsamples", OctanePMCKernelMaxsamples.bl_label)
        self.inputs.new("OctanePMCKernelMaxDiffuseDepth", OctanePMCKernelMaxDiffuseDepth.bl_label)
        self.inputs.new("OctanePMCKernelMaxGlossyDepth", OctanePMCKernelMaxGlossyDepth.bl_label)
        self.inputs.new("OctanePMCKernelMaxScatterDepth", OctanePMCKernelMaxScatterDepth.bl_label)
        self.inputs.new("OctanePMCKernelMaxOverlappingVolumes", OctanePMCKernelMaxOverlappingVolumes.bl_label)
        self.inputs.new("OctanePMCKernelRayepsilon", OctanePMCKernelRayepsilon.bl_label)
        self.inputs.new("OctanePMCKernelFiltersize", OctanePMCKernelFiltersize.bl_label)
        self.inputs.new("OctanePMCKernelAlphashadows", OctanePMCKernelAlphashadows.bl_label)
        self.inputs.new("OctanePMCKernelCausticBlur", OctanePMCKernelCausticBlur.bl_label)
        self.inputs.new("OctanePMCKernelGiClamp", OctanePMCKernelGiClamp.bl_label)
        self.inputs.new("OctanePMCKernelNestedDielectrics", OctanePMCKernelNestedDielectrics.bl_label)
        self.inputs.new("OctanePMCKernelIrradiance", OctanePMCKernelIrradiance.bl_label)
        self.inputs.new("OctanePMCKernelMaxsubdLevel", OctanePMCKernelMaxsubdLevel.bl_label)
        self.inputs.new("OctanePMCKernelAlphachannel", OctanePMCKernelAlphachannel.bl_label)
        self.inputs.new("OctanePMCKernelKeepEnvironment", OctanePMCKernelKeepEnvironment.bl_label)
        self.inputs.new("OctanePMCKernelAiLight", OctanePMCKernelAiLight.bl_label)
        self.inputs.new("OctanePMCKernelAiLightUpdate", OctanePMCKernelAiLightUpdate.bl_label)
        self.inputs.new("OctanePMCKernelGlobalLightIdMaskAction", OctanePMCKernelGlobalLightIdMaskAction.bl_label)
        self.inputs.new("OctanePMCKernelGlobalLightIdMask", OctanePMCKernelGlobalLightIdMask.bl_label)
        self.inputs.new("OctanePMCKernelLightPassMask", OctanePMCKernelLightPassMask.bl_label)
        self.inputs.new("OctanePMCKernelPathTermPower", OctanePMCKernelPathTermPower.bl_label)
        self.inputs.new("OctanePMCKernelExplorationStrength", OctanePMCKernelExplorationStrength.bl_label)
        self.inputs.new("OctanePMCKernelDirectLightImportance", OctanePMCKernelDirectLightImportance.bl_label)
        self.inputs.new("OctanePMCKernelMaxrejects", OctanePMCKernelMaxrejects.bl_label)
        self.inputs.new("OctanePMCKernelParallelism", OctanePMCKernelParallelism.bl_label)
        self.inputs.new("OctanePMCKernelWorkChunkSize", OctanePMCKernelWorkChunkSize.bl_label)
        self.inputs.new("OctanePMCKernelWhiteLightSpectrum", OctanePMCKernelWhiteLightSpectrum.bl_label)
        self.inputs.new("OctanePMCKernelUseOldColorPipeline", OctanePMCKernelUseOldColorPipeline.bl_label)
        self.inputs.new("OctanePMCKernelToonShadowAmbient", OctanePMCKernelToonShadowAmbient.bl_label)
        self.outputs.new("OctaneKernelOutSocket", "Kernel out")


def register():
    register_class(OctanePMCKernelMaxsamples)
    register_class(OctanePMCKernelMaxDiffuseDepth)
    register_class(OctanePMCKernelMaxGlossyDepth)
    register_class(OctanePMCKernelMaxScatterDepth)
    register_class(OctanePMCKernelMaxOverlappingVolumes)
    register_class(OctanePMCKernelRayepsilon)
    register_class(OctanePMCKernelFiltersize)
    register_class(OctanePMCKernelAlphashadows)
    register_class(OctanePMCKernelCausticBlur)
    register_class(OctanePMCKernelGiClamp)
    register_class(OctanePMCKernelNestedDielectrics)
    register_class(OctanePMCKernelIrradiance)
    register_class(OctanePMCKernelMaxsubdLevel)
    register_class(OctanePMCKernelAlphachannel)
    register_class(OctanePMCKernelKeepEnvironment)
    register_class(OctanePMCKernelAiLight)
    register_class(OctanePMCKernelAiLightUpdate)
    register_class(OctanePMCKernelGlobalLightIdMaskAction)
    register_class(OctanePMCKernelGlobalLightIdMask)
    register_class(OctanePMCKernelLightPassMask)
    register_class(OctanePMCKernelPathTermPower)
    register_class(OctanePMCKernelExplorationStrength)
    register_class(OctanePMCKernelDirectLightImportance)
    register_class(OctanePMCKernelMaxrejects)
    register_class(OctanePMCKernelParallelism)
    register_class(OctanePMCKernelWorkChunkSize)
    register_class(OctanePMCKernelWhiteLightSpectrum)
    register_class(OctanePMCKernelUseOldColorPipeline)
    register_class(OctanePMCKernelToonShadowAmbient)
    register_class(OctanePMCKernel)

def unregister():
    unregister_class(OctanePMCKernel)
    unregister_class(OctanePMCKernelToonShadowAmbient)
    unregister_class(OctanePMCKernelUseOldColorPipeline)
    unregister_class(OctanePMCKernelWhiteLightSpectrum)
    unregister_class(OctanePMCKernelWorkChunkSize)
    unregister_class(OctanePMCKernelParallelism)
    unregister_class(OctanePMCKernelMaxrejects)
    unregister_class(OctanePMCKernelDirectLightImportance)
    unregister_class(OctanePMCKernelExplorationStrength)
    unregister_class(OctanePMCKernelPathTermPower)
    unregister_class(OctanePMCKernelLightPassMask)
    unregister_class(OctanePMCKernelGlobalLightIdMask)
    unregister_class(OctanePMCKernelGlobalLightIdMaskAction)
    unregister_class(OctanePMCKernelAiLightUpdate)
    unregister_class(OctanePMCKernelAiLight)
    unregister_class(OctanePMCKernelKeepEnvironment)
    unregister_class(OctanePMCKernelAlphachannel)
    unregister_class(OctanePMCKernelMaxsubdLevel)
    unregister_class(OctanePMCKernelIrradiance)
    unregister_class(OctanePMCKernelNestedDielectrics)
    unregister_class(OctanePMCKernelGiClamp)
    unregister_class(OctanePMCKernelCausticBlur)
    unregister_class(OctanePMCKernelAlphashadows)
    unregister_class(OctanePMCKernelFiltersize)
    unregister_class(OctanePMCKernelRayepsilon)
    unregister_class(OctanePMCKernelMaxOverlappingVolumes)
    unregister_class(OctanePMCKernelMaxScatterDepth)
    unregister_class(OctanePMCKernelMaxGlossyDepth)
    unregister_class(OctanePMCKernelMaxDiffuseDepth)
    unregister_class(OctanePMCKernelMaxsamples)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
