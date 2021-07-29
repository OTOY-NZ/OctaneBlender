##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctanePathTracingKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxsamples"
    bl_label = "Max. samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5000, description="The maximum of samples per that will be calculated until rendering is stopped", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelMaxDiffuseDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxDiffuseDepth"
    bl_label = "Diffuse depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=104)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")

class OctanePathTracingKernelMaxGlossyDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxGlossyDepth"
    bl_label = "Specular depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=105)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=24, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=2048, soft_min=1, soft_max=2048, step=1, subtype="FACTOR")

class OctanePathTracingKernelMaxScatterDepth(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxScatterDepth"
    bl_label = "Scatter depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=464)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="The maximum path depth for which scattering is allowed", min=1, max=256, soft_min=1, soft_max=256, step=1, subtype="FACTOR")

class OctanePathTracingKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxOverlappingVolumes"
    bl_label = "Maximal overlapping volumes"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=702)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype="FACTOR")

class OctanePathTracingKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelRayepsilon"
    bl_label = "Ray epsilon"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000100, description="Shadow Ray Offset Distance", min=0.000000, max=0.100000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelFiltersize"
    bl_label = "Filter size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.200000, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAlphashadows"
    bl_label = "Alpha shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with 'fake shadows' enabled")

class OctanePathTracingKernelCausticBlur(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelCausticBlur"
    bl_label = "Caustic blur"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=22)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.010000, description="Caustic blur for noise reduction", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelGiClamp(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGiClamp"
    bl_label = "GI clamp"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=60)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1000000.000000, description="GI clamp reducing fireflies", min=0.001000, max=1000000.000000, soft_min=0.001000, soft_max=1000000.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelNestedDielectrics"
    bl_label = "Nested dielectrics"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=571)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")

class OctanePathTracingKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelIrradiance"
    bl_label = "Irradiance mode"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=381)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render the first surface as a white diffuse material")

class OctanePathTracingKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxsubdLevel"
    bl_label = "Max subdivision level"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=10, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")

class OctanePathTracingKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAlphachannel"
    bl_label = "Alpha channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables a compositing alpha channel")

class OctanePathTracingKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelKeepEnvironment"
    bl_label = "Keep environment"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=86)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Keeps environment with enabled alpha channel")

class OctanePathTracingKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAiLight"
    bl_label = "AI light"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=386)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables AI light")

class OctanePathTracingKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAiLightUpdate"
    bl_label = "AI light update"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=384)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables dynamic AI light update")

class OctanePathTracingKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGlobalLightIdMaskAction"
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

class OctanePathTracingKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelGlobalLightIdMask"
    bl_label = "Light IDs"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=434)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePathTracingKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelLightPassMask"
    bl_label = "Light linking invert"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctanePathTracingKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelPathTermPower"
    bl_label = "Path term. power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=129)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.300000, description="Path may get terminated when ray power is less then this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelCoherentRatio(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelCoherentRatio"
    bl_label = "Coherent ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=25)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelStaticNoise(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelStaticNoise"
    bl_label = "Static noise"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=223)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the noise patterns are kept stable between frames")

class OctanePathTracingKernelParallelSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelParallelSamples"
    bl_label = "Parallel samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=273)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=16, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctanePathTracingKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxTileSamples"
    bl_label = "Max. tile samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=267)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=32, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")

class OctanePathTracingKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMinimizeNetTraffic"
    bl_label = "Minimize net traffic"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=270)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")

class OctanePathTracingKernelAdaptiveSampling(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSampling"
    bl_label = "Adaptive sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=347)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image parts")

class OctanePathTracingKernelNoiseThreshold(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelNoiseThreshold"
    bl_label = "Noise threshold"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=349)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.020000, description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelMinAdaptiveSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMinAdaptiveSamples"
    bl_label = "Min. adaptive samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=351)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=512, description="Minimum number of samples per pixel until adaptive sampling kicks in. Set it to a higher value if you notice that the error estimate is incorrect and stops sampling pixels too early resulting in artifacts. Only valid if adaptive sampling is enabled", min=2, max=100000, soft_min=2, soft_max=1000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelAdaptiveSamplingPixelGroup(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSamplingPixelGroup"
    bl_label = "Pixel grouping"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=350)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 1),
        ("2 x 2", "2 x 2", "", 2),
        ("4 x 4", "4 x 4", "", 4),
    ]
    default_value: EnumProperty(default="2 x 2", description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not", items=items)

class OctanePathTracingKernelAdaptiveSamplingExposure(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelAdaptiveSamplingExposure"
    bl_label = "Expected exposure"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=353)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The expected exposure should be approximately the same value as the exposure in the imager or 0 to ignore this settings. It's used by adaptive sampling to determine which pixels are bright and which are dark, which obviously depends on the exposure setting in the imaging settings. Adaptive sampling tweaks/reduces the noise estimate of very dark areas of the image. It also increases the min. adaptive samples limit for very dark areas which tend to find paths to light sources only very irregularly and thus have a too optimistic noise estimate", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=4096.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelWhiteLightSpectrum"
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

class OctanePathTracingKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelUseOldColorPipeline"
    bl_label = "Use old color pipeline"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")

class OctanePathTracingKernelDeepEnable(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDeepEnable"
    bl_label = "Deep image"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=263)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render a deep image")

class OctanePathTracingKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDeepEnablePasses"
    bl_label = "Deep render passes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=446)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Include render passes in deep pixels")

class OctanePathTracingKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelMaxDepthSamples"
    bl_label = "Max. depth samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=266)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctanePathTracingKernelDepthTolerance(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelDepthTolerance"
    bl_label = "Depth tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=264)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.050000, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctanePathTracingKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctanePathTracingKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=368)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="The ambient modifier of toon shadowing", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctanePathTracingKernel(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctanePathTracingKernel"
    bl_label = "Path tracing kernel"
    octane_node_type: IntProperty(name="Octane Node Type", default=25)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Diffuse depth;Specular depth;Scatter depth;Maximal overlapping volumes;Ray epsilon;Filter size;Alpha shadows;Caustic blur;GI clamp;Nested dielectrics;Irradiance mode;Max subdivision level;Alpha channel;Keep environment;AI light;AI light update;Light IDs action;Light IDs;Light linking invert;Path term. power;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;White light spectrum;Use old color pipeline;Deep image;Deep render passes;Max. depth samples;Depth tolerance;Toon shadow ambient;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctanePathTracingKernelMaxsamples", OctanePathTracingKernelMaxsamples.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxDiffuseDepth", OctanePathTracingKernelMaxDiffuseDepth.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxGlossyDepth", OctanePathTracingKernelMaxGlossyDepth.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxScatterDepth", OctanePathTracingKernelMaxScatterDepth.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxOverlappingVolumes", OctanePathTracingKernelMaxOverlappingVolumes.bl_label)
        self.inputs.new("OctanePathTracingKernelRayepsilon", OctanePathTracingKernelRayepsilon.bl_label)
        self.inputs.new("OctanePathTracingKernelFiltersize", OctanePathTracingKernelFiltersize.bl_label)
        self.inputs.new("OctanePathTracingKernelAlphashadows", OctanePathTracingKernelAlphashadows.bl_label)
        self.inputs.new("OctanePathTracingKernelCausticBlur", OctanePathTracingKernelCausticBlur.bl_label)
        self.inputs.new("OctanePathTracingKernelGiClamp", OctanePathTracingKernelGiClamp.bl_label)
        self.inputs.new("OctanePathTracingKernelNestedDielectrics", OctanePathTracingKernelNestedDielectrics.bl_label)
        self.inputs.new("OctanePathTracingKernelIrradiance", OctanePathTracingKernelIrradiance.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxsubdLevel", OctanePathTracingKernelMaxsubdLevel.bl_label)
        self.inputs.new("OctanePathTracingKernelAlphachannel", OctanePathTracingKernelAlphachannel.bl_label)
        self.inputs.new("OctanePathTracingKernelKeepEnvironment", OctanePathTracingKernelKeepEnvironment.bl_label)
        self.inputs.new("OctanePathTracingKernelAiLight", OctanePathTracingKernelAiLight.bl_label)
        self.inputs.new("OctanePathTracingKernelAiLightUpdate", OctanePathTracingKernelAiLightUpdate.bl_label)
        self.inputs.new("OctanePathTracingKernelGlobalLightIdMaskAction", OctanePathTracingKernelGlobalLightIdMaskAction.bl_label)
        self.inputs.new("OctanePathTracingKernelGlobalLightIdMask", OctanePathTracingKernelGlobalLightIdMask.bl_label)
        self.inputs.new("OctanePathTracingKernelLightPassMask", OctanePathTracingKernelLightPassMask.bl_label)
        self.inputs.new("OctanePathTracingKernelPathTermPower", OctanePathTracingKernelPathTermPower.bl_label)
        self.inputs.new("OctanePathTracingKernelCoherentRatio", OctanePathTracingKernelCoherentRatio.bl_label)
        self.inputs.new("OctanePathTracingKernelStaticNoise", OctanePathTracingKernelStaticNoise.bl_label)
        self.inputs.new("OctanePathTracingKernelParallelSamples", OctanePathTracingKernelParallelSamples.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxTileSamples", OctanePathTracingKernelMaxTileSamples.bl_label)
        self.inputs.new("OctanePathTracingKernelMinimizeNetTraffic", OctanePathTracingKernelMinimizeNetTraffic.bl_label)
        self.inputs.new("OctanePathTracingKernelAdaptiveSampling", OctanePathTracingKernelAdaptiveSampling.bl_label)
        self.inputs.new("OctanePathTracingKernelNoiseThreshold", OctanePathTracingKernelNoiseThreshold.bl_label)
        self.inputs.new("OctanePathTracingKernelMinAdaptiveSamples", OctanePathTracingKernelMinAdaptiveSamples.bl_label)
        self.inputs.new("OctanePathTracingKernelAdaptiveSamplingPixelGroup", OctanePathTracingKernelAdaptiveSamplingPixelGroup.bl_label)
        self.inputs.new("OctanePathTracingKernelAdaptiveSamplingExposure", OctanePathTracingKernelAdaptiveSamplingExposure.bl_label)
        self.inputs.new("OctanePathTracingKernelWhiteLightSpectrum", OctanePathTracingKernelWhiteLightSpectrum.bl_label)
        self.inputs.new("OctanePathTracingKernelUseOldColorPipeline", OctanePathTracingKernelUseOldColorPipeline.bl_label)
        self.inputs.new("OctanePathTracingKernelDeepEnable", OctanePathTracingKernelDeepEnable.bl_label)
        self.inputs.new("OctanePathTracingKernelDeepEnablePasses", OctanePathTracingKernelDeepEnablePasses.bl_label)
        self.inputs.new("OctanePathTracingKernelMaxDepthSamples", OctanePathTracingKernelMaxDepthSamples.bl_label)
        self.inputs.new("OctanePathTracingKernelDepthTolerance", OctanePathTracingKernelDepthTolerance.bl_label)
        self.inputs.new("OctanePathTracingKernelToonShadowAmbient", OctanePathTracingKernelToonShadowAmbient.bl_label)
        self.outputs.new("OctaneKernelOutSocket", "Kernel out")


def register():
    register_class(OctanePathTracingKernelMaxsamples)
    register_class(OctanePathTracingKernelMaxDiffuseDepth)
    register_class(OctanePathTracingKernelMaxGlossyDepth)
    register_class(OctanePathTracingKernelMaxScatterDepth)
    register_class(OctanePathTracingKernelMaxOverlappingVolumes)
    register_class(OctanePathTracingKernelRayepsilon)
    register_class(OctanePathTracingKernelFiltersize)
    register_class(OctanePathTracingKernelAlphashadows)
    register_class(OctanePathTracingKernelCausticBlur)
    register_class(OctanePathTracingKernelGiClamp)
    register_class(OctanePathTracingKernelNestedDielectrics)
    register_class(OctanePathTracingKernelIrradiance)
    register_class(OctanePathTracingKernelMaxsubdLevel)
    register_class(OctanePathTracingKernelAlphachannel)
    register_class(OctanePathTracingKernelKeepEnvironment)
    register_class(OctanePathTracingKernelAiLight)
    register_class(OctanePathTracingKernelAiLightUpdate)
    register_class(OctanePathTracingKernelGlobalLightIdMaskAction)
    register_class(OctanePathTracingKernelGlobalLightIdMask)
    register_class(OctanePathTracingKernelLightPassMask)
    register_class(OctanePathTracingKernelPathTermPower)
    register_class(OctanePathTracingKernelCoherentRatio)
    register_class(OctanePathTracingKernelStaticNoise)
    register_class(OctanePathTracingKernelParallelSamples)
    register_class(OctanePathTracingKernelMaxTileSamples)
    register_class(OctanePathTracingKernelMinimizeNetTraffic)
    register_class(OctanePathTracingKernelAdaptiveSampling)
    register_class(OctanePathTracingKernelNoiseThreshold)
    register_class(OctanePathTracingKernelMinAdaptiveSamples)
    register_class(OctanePathTracingKernelAdaptiveSamplingPixelGroup)
    register_class(OctanePathTracingKernelAdaptiveSamplingExposure)
    register_class(OctanePathTracingKernelWhiteLightSpectrum)
    register_class(OctanePathTracingKernelUseOldColorPipeline)
    register_class(OctanePathTracingKernelDeepEnable)
    register_class(OctanePathTracingKernelDeepEnablePasses)
    register_class(OctanePathTracingKernelMaxDepthSamples)
    register_class(OctanePathTracingKernelDepthTolerance)
    register_class(OctanePathTracingKernelToonShadowAmbient)
    register_class(OctanePathTracingKernel)

def unregister():
    unregister_class(OctanePathTracingKernel)
    unregister_class(OctanePathTracingKernelToonShadowAmbient)
    unregister_class(OctanePathTracingKernelDepthTolerance)
    unregister_class(OctanePathTracingKernelMaxDepthSamples)
    unregister_class(OctanePathTracingKernelDeepEnablePasses)
    unregister_class(OctanePathTracingKernelDeepEnable)
    unregister_class(OctanePathTracingKernelUseOldColorPipeline)
    unregister_class(OctanePathTracingKernelWhiteLightSpectrum)
    unregister_class(OctanePathTracingKernelAdaptiveSamplingExposure)
    unregister_class(OctanePathTracingKernelAdaptiveSamplingPixelGroup)
    unregister_class(OctanePathTracingKernelMinAdaptiveSamples)
    unregister_class(OctanePathTracingKernelNoiseThreshold)
    unregister_class(OctanePathTracingKernelAdaptiveSampling)
    unregister_class(OctanePathTracingKernelMinimizeNetTraffic)
    unregister_class(OctanePathTracingKernelMaxTileSamples)
    unregister_class(OctanePathTracingKernelParallelSamples)
    unregister_class(OctanePathTracingKernelStaticNoise)
    unregister_class(OctanePathTracingKernelCoherentRatio)
    unregister_class(OctanePathTracingKernelPathTermPower)
    unregister_class(OctanePathTracingKernelLightPassMask)
    unregister_class(OctanePathTracingKernelGlobalLightIdMask)
    unregister_class(OctanePathTracingKernelGlobalLightIdMaskAction)
    unregister_class(OctanePathTracingKernelAiLightUpdate)
    unregister_class(OctanePathTracingKernelAiLight)
    unregister_class(OctanePathTracingKernelKeepEnvironment)
    unregister_class(OctanePathTracingKernelAlphachannel)
    unregister_class(OctanePathTracingKernelMaxsubdLevel)
    unregister_class(OctanePathTracingKernelIrradiance)
    unregister_class(OctanePathTracingKernelNestedDielectrics)
    unregister_class(OctanePathTracingKernelGiClamp)
    unregister_class(OctanePathTracingKernelCausticBlur)
    unregister_class(OctanePathTracingKernelAlphashadows)
    unregister_class(OctanePathTracingKernelFiltersize)
    unregister_class(OctanePathTracingKernelRayepsilon)
    unregister_class(OctanePathTracingKernelMaxOverlappingVolumes)
    unregister_class(OctanePathTracingKernelMaxScatterDepth)
    unregister_class(OctanePathTracingKernelMaxGlossyDepth)
    unregister_class(OctanePathTracingKernelMaxDiffuseDepth)
    unregister_class(OctanePathTracingKernelMaxsamples)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
