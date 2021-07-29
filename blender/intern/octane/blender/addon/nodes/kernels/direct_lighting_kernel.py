##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneDirectLightingKernelMaxsamples(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMaxsamples"
    bl_label = "Max. samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=108)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5000, description="The maximum of samples per that will be calculated until rendering is stopped", min=1, max=100000, soft_min=1, soft_max=1000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelGIMode(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelGIMode"
    bl_label = "Global illumination mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=61)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("None", "None", "", 0),
        ("Ambient occlusion", "Ambient occlusion", "", 3),
        ("Diffuse", "Diffuse", "", 4),
    ]
    default_value: EnumProperty(default="Ambient occlusion", description="Determines how global illumination is approximated", items=items)

class OctaneDirectLightingKernelSpeculardepth(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelSpeculardepth"
    bl_label = "Specular depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=221)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=5, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelGlossydepth(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelGlossydepth"
    bl_label = "Glossy depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=66)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=2, description="The maximum path depth for which glossy reflections are allowed", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelDiffusedepth(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelDiffusedepth"
    bl_label = "Diffuse depth"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=29)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=2, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMaxOverlappingVolumes"
    bl_label = "Maximal overlapping volumes"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=702)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=4, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelRayepsilon(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelRayepsilon"
    bl_label = "Ray epsilon"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000100, description="Shadow ray offset distance", min=0.000000, max=0.100000, soft_min=0.000000, soft_max=1000.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelFiltersize(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelFiltersize"
    bl_label = "Filter size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.200000, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelAodist(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAodist"
    bl_label = "AO distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=3.000000, description="Maximum distance for environment ambient occlusion", min=0.000000, max=1024.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelAoTexture(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAoTexture"
    bl_label = "AO ambient texture"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=326)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneDirectLightingKernelAlphashadows(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAlphashadows"
    bl_label = "Alpha shadows"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with 'fake shadows' enabled")

class OctaneDirectLightingKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelNestedDielectrics"
    bl_label = "Nested dielectrics"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=571)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")

class OctaneDirectLightingKernelIrradiance(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelIrradiance"
    bl_label = "Irradiance mode"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=381)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render the first surface as a white diffuse material")

class OctaneDirectLightingKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMaxsubdLevel"
    bl_label = "Max subdivision level"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=495)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=10, description="The maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision", min=0, max=10, soft_min=0, soft_max=10, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelAlphachannel(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAlphachannel"
    bl_label = "Alpha channel"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables a compositing alpha channel")

class OctaneDirectLightingKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelKeepEnvironment"
    bl_label = "Keep environment"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=86)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Keeps environment with enabled alpha channel")

class OctaneDirectLightingKernelAiLight(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAiLight"
    bl_label = "AI light"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=386)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Enables AI light")

class OctaneDirectLightingKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAiLightUpdate"
    bl_label = "AI light update"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=384)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="Enables dynamic AI light update")

class OctaneDirectLightingKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelGlobalLightIdMaskAction"
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

class OctaneDirectLightingKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelGlobalLightIdMask"
    bl_label = "Light IDs"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=434)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDirectLightingKernelLightPassMask(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelLightPassMask"
    bl_label = "Light linking invert"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=31)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneDirectLightingKernelPathTermPower(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelPathTermPower"
    bl_label = "Path term. power"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=129)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.300000, description="Path may get terminated when ray power is less then this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelCoherentRatio(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelCoherentRatio"
    bl_label = "Coherent ratio"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=25)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelStaticNoise(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelStaticNoise"
    bl_label = "Static noise"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=223)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, the noise patterns are kept stable between frames")

class OctaneDirectLightingKernelParallelSamples(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelParallelSamples"
    bl_label = "Parallel samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=273)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=16, description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMaxTileSamples"
    bl_label = "Max. tile samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=267)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=32, description="The maximum samples we calculate until we switch to a new tile", min=1, max=64, soft_min=1, soft_max=64, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMinimizeNetTraffic"
    bl_label = "Minimize net traffic"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=270)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="If enabled, the work is distributed to the network render nodes in such a way to minimize the amount of data that is sent to the network render master")

class OctaneDirectLightingKernelAdaptiveSampling(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAdaptiveSampling"
    bl_label = "Adaptive sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=347)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image parts")

class OctaneDirectLightingKernelNoiseThreshold(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelNoiseThreshold"
    bl_label = "Noise threshold"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=349)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.020000, description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelMinAdaptiveSamples(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMinAdaptiveSamples"
    bl_label = "Min. adaptive samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=351)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=512, description="Minimum number of samples per pixel until adaptive sampling kicks in. Set it to a higher value if you notice that the error estimate is incorrect and stops sampling pixels too early resulting in artifacts. Only valid if adaptive sampling is enabled", min=2, max=100000, soft_min=2, soft_max=1000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelAdaptiveSamplingPixelGroup(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAdaptiveSamplingPixelGroup"
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

class OctaneDirectLightingKernelAdaptiveSamplingExposure(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelAdaptiveSamplingExposure"
    bl_label = "Expected exposure"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=353)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="The expected exposure should be approximately the same value as the exposure in the imager or 0 to ignore this settings. It's used by adaptive sampling to determine which pixels are bright and which are dark, which obviously depends on the exposure setting in the imaging settings. Adaptive sampling tweaks/reduces the noise estimate of very dark areas of the image. It also increases the min. adaptive samples limit for very dark areas which tend to find paths to light sources only very irregularly and thus have a too optimistic noise estimate", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=4096.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelWhiteLightSpectrum"
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

class OctaneDirectLightingKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelUseOldColorPipeline"
    bl_label = "Use old color pipeline"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=708)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Use the old behavior for converting colors to and from spectra and for applying white balance. Use this to preserve the appearance of old projects (textures with colors outside the sRGB gamut will be rendered inaccurately)")

class OctaneDirectLightingKernelDeepEnable(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelDeepEnable"
    bl_label = "Deep image"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=263)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Render a deep image")

class OctaneDirectLightingKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelDeepEnablePasses"
    bl_label = "Deep render passes"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=446)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="Include render passes in deep pixels")

class OctaneDirectLightingKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelMaxDepthSamples"
    bl_label = "Max. depth samples"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=266)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=8, description="Maximum number of depth samples per pixels", min=1, max=32, soft_min=1, soft_max=32, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelDepthTolerance(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelDepthTolerance"
    bl_label = "Depth tolerance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=264)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.050000, description="Depth samples whose relative depth difference falls below the tolerance value are merged together", min=0.001000, max=1.000000, soft_min=0.001000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneDirectLightingKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname = "OctaneDirectLightingKernelToonShadowAmbient"
    bl_label = "Toon shadow ambient"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=368)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=9)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), description="The ambient modifier of toon shadowing", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", size=3)

class OctaneDirectLightingKernel(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneDirectLightingKernel"
    bl_label = "Direct lighting kernel"
    octane_node_type: IntProperty(name="Octane Node Type", default=24)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Global illumination mode;Specular depth;Glossy depth;Diffuse depth;Maximal overlapping volumes;Ray epsilon;Filter size;AO distance;AO ambient texture;Alpha shadows;Nested dielectrics;Irradiance mode;Max subdivision level;Alpha channel;Keep environment;AI light;AI light update;Light IDs action;Light IDs;Light linking invert;Path term. power;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;White light spectrum;Use old color pipeline;Deep image;Deep render passes;Max. depth samples;Depth tolerance;Toon shadow ambient;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneDirectLightingKernelMaxsamples", OctaneDirectLightingKernelMaxsamples.bl_label)
        self.inputs.new("OctaneDirectLightingKernelGIMode", OctaneDirectLightingKernelGIMode.bl_label)
        self.inputs.new("OctaneDirectLightingKernelSpeculardepth", OctaneDirectLightingKernelSpeculardepth.bl_label)
        self.inputs.new("OctaneDirectLightingKernelGlossydepth", OctaneDirectLightingKernelGlossydepth.bl_label)
        self.inputs.new("OctaneDirectLightingKernelDiffusedepth", OctaneDirectLightingKernelDiffusedepth.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMaxOverlappingVolumes", OctaneDirectLightingKernelMaxOverlappingVolumes.bl_label)
        self.inputs.new("OctaneDirectLightingKernelRayepsilon", OctaneDirectLightingKernelRayepsilon.bl_label)
        self.inputs.new("OctaneDirectLightingKernelFiltersize", OctaneDirectLightingKernelFiltersize.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAodist", OctaneDirectLightingKernelAodist.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAoTexture", OctaneDirectLightingKernelAoTexture.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAlphashadows", OctaneDirectLightingKernelAlphashadows.bl_label)
        self.inputs.new("OctaneDirectLightingKernelNestedDielectrics", OctaneDirectLightingKernelNestedDielectrics.bl_label)
        self.inputs.new("OctaneDirectLightingKernelIrradiance", OctaneDirectLightingKernelIrradiance.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMaxsubdLevel", OctaneDirectLightingKernelMaxsubdLevel.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAlphachannel", OctaneDirectLightingKernelAlphachannel.bl_label)
        self.inputs.new("OctaneDirectLightingKernelKeepEnvironment", OctaneDirectLightingKernelKeepEnvironment.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAiLight", OctaneDirectLightingKernelAiLight.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAiLightUpdate", OctaneDirectLightingKernelAiLightUpdate.bl_label)
        self.inputs.new("OctaneDirectLightingKernelGlobalLightIdMaskAction", OctaneDirectLightingKernelGlobalLightIdMaskAction.bl_label)
        self.inputs.new("OctaneDirectLightingKernelGlobalLightIdMask", OctaneDirectLightingKernelGlobalLightIdMask.bl_label)
        self.inputs.new("OctaneDirectLightingKernelLightPassMask", OctaneDirectLightingKernelLightPassMask.bl_label)
        self.inputs.new("OctaneDirectLightingKernelPathTermPower", OctaneDirectLightingKernelPathTermPower.bl_label)
        self.inputs.new("OctaneDirectLightingKernelCoherentRatio", OctaneDirectLightingKernelCoherentRatio.bl_label)
        self.inputs.new("OctaneDirectLightingKernelStaticNoise", OctaneDirectLightingKernelStaticNoise.bl_label)
        self.inputs.new("OctaneDirectLightingKernelParallelSamples", OctaneDirectLightingKernelParallelSamples.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMaxTileSamples", OctaneDirectLightingKernelMaxTileSamples.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMinimizeNetTraffic", OctaneDirectLightingKernelMinimizeNetTraffic.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSampling", OctaneDirectLightingKernelAdaptiveSampling.bl_label)
        self.inputs.new("OctaneDirectLightingKernelNoiseThreshold", OctaneDirectLightingKernelNoiseThreshold.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMinAdaptiveSamples", OctaneDirectLightingKernelMinAdaptiveSamples.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSamplingPixelGroup", OctaneDirectLightingKernelAdaptiveSamplingPixelGroup.bl_label)
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSamplingExposure", OctaneDirectLightingKernelAdaptiveSamplingExposure.bl_label)
        self.inputs.new("OctaneDirectLightingKernelWhiteLightSpectrum", OctaneDirectLightingKernelWhiteLightSpectrum.bl_label)
        self.inputs.new("OctaneDirectLightingKernelUseOldColorPipeline", OctaneDirectLightingKernelUseOldColorPipeline.bl_label)
        self.inputs.new("OctaneDirectLightingKernelDeepEnable", OctaneDirectLightingKernelDeepEnable.bl_label)
        self.inputs.new("OctaneDirectLightingKernelDeepEnablePasses", OctaneDirectLightingKernelDeepEnablePasses.bl_label)
        self.inputs.new("OctaneDirectLightingKernelMaxDepthSamples", OctaneDirectLightingKernelMaxDepthSamples.bl_label)
        self.inputs.new("OctaneDirectLightingKernelDepthTolerance", OctaneDirectLightingKernelDepthTolerance.bl_label)
        self.inputs.new("OctaneDirectLightingKernelToonShadowAmbient", OctaneDirectLightingKernelToonShadowAmbient.bl_label)
        self.outputs.new("OctaneKernelOutSocket", "Kernel out")


def register():
    register_class(OctaneDirectLightingKernelMaxsamples)
    register_class(OctaneDirectLightingKernelGIMode)
    register_class(OctaneDirectLightingKernelSpeculardepth)
    register_class(OctaneDirectLightingKernelGlossydepth)
    register_class(OctaneDirectLightingKernelDiffusedepth)
    register_class(OctaneDirectLightingKernelMaxOverlappingVolumes)
    register_class(OctaneDirectLightingKernelRayepsilon)
    register_class(OctaneDirectLightingKernelFiltersize)
    register_class(OctaneDirectLightingKernelAodist)
    register_class(OctaneDirectLightingKernelAoTexture)
    register_class(OctaneDirectLightingKernelAlphashadows)
    register_class(OctaneDirectLightingKernelNestedDielectrics)
    register_class(OctaneDirectLightingKernelIrradiance)
    register_class(OctaneDirectLightingKernelMaxsubdLevel)
    register_class(OctaneDirectLightingKernelAlphachannel)
    register_class(OctaneDirectLightingKernelKeepEnvironment)
    register_class(OctaneDirectLightingKernelAiLight)
    register_class(OctaneDirectLightingKernelAiLightUpdate)
    register_class(OctaneDirectLightingKernelGlobalLightIdMaskAction)
    register_class(OctaneDirectLightingKernelGlobalLightIdMask)
    register_class(OctaneDirectLightingKernelLightPassMask)
    register_class(OctaneDirectLightingKernelPathTermPower)
    register_class(OctaneDirectLightingKernelCoherentRatio)
    register_class(OctaneDirectLightingKernelStaticNoise)
    register_class(OctaneDirectLightingKernelParallelSamples)
    register_class(OctaneDirectLightingKernelMaxTileSamples)
    register_class(OctaneDirectLightingKernelMinimizeNetTraffic)
    register_class(OctaneDirectLightingKernelAdaptiveSampling)
    register_class(OctaneDirectLightingKernelNoiseThreshold)
    register_class(OctaneDirectLightingKernelMinAdaptiveSamples)
    register_class(OctaneDirectLightingKernelAdaptiveSamplingPixelGroup)
    register_class(OctaneDirectLightingKernelAdaptiveSamplingExposure)
    register_class(OctaneDirectLightingKernelWhiteLightSpectrum)
    register_class(OctaneDirectLightingKernelUseOldColorPipeline)
    register_class(OctaneDirectLightingKernelDeepEnable)
    register_class(OctaneDirectLightingKernelDeepEnablePasses)
    register_class(OctaneDirectLightingKernelMaxDepthSamples)
    register_class(OctaneDirectLightingKernelDepthTolerance)
    register_class(OctaneDirectLightingKernelToonShadowAmbient)
    register_class(OctaneDirectLightingKernel)

def unregister():
    unregister_class(OctaneDirectLightingKernel)
    unregister_class(OctaneDirectLightingKernelToonShadowAmbient)
    unregister_class(OctaneDirectLightingKernelDepthTolerance)
    unregister_class(OctaneDirectLightingKernelMaxDepthSamples)
    unregister_class(OctaneDirectLightingKernelDeepEnablePasses)
    unregister_class(OctaneDirectLightingKernelDeepEnable)
    unregister_class(OctaneDirectLightingKernelUseOldColorPipeline)
    unregister_class(OctaneDirectLightingKernelWhiteLightSpectrum)
    unregister_class(OctaneDirectLightingKernelAdaptiveSamplingExposure)
    unregister_class(OctaneDirectLightingKernelAdaptiveSamplingPixelGroup)
    unregister_class(OctaneDirectLightingKernelMinAdaptiveSamples)
    unregister_class(OctaneDirectLightingKernelNoiseThreshold)
    unregister_class(OctaneDirectLightingKernelAdaptiveSampling)
    unregister_class(OctaneDirectLightingKernelMinimizeNetTraffic)
    unregister_class(OctaneDirectLightingKernelMaxTileSamples)
    unregister_class(OctaneDirectLightingKernelParallelSamples)
    unregister_class(OctaneDirectLightingKernelStaticNoise)
    unregister_class(OctaneDirectLightingKernelCoherentRatio)
    unregister_class(OctaneDirectLightingKernelPathTermPower)
    unregister_class(OctaneDirectLightingKernelLightPassMask)
    unregister_class(OctaneDirectLightingKernelGlobalLightIdMask)
    unregister_class(OctaneDirectLightingKernelGlobalLightIdMaskAction)
    unregister_class(OctaneDirectLightingKernelAiLightUpdate)
    unregister_class(OctaneDirectLightingKernelAiLight)
    unregister_class(OctaneDirectLightingKernelKeepEnvironment)
    unregister_class(OctaneDirectLightingKernelAlphachannel)
    unregister_class(OctaneDirectLightingKernelMaxsubdLevel)
    unregister_class(OctaneDirectLightingKernelIrradiance)
    unregister_class(OctaneDirectLightingKernelNestedDielectrics)
    unregister_class(OctaneDirectLightingKernelAlphashadows)
    unregister_class(OctaneDirectLightingKernelAoTexture)
    unregister_class(OctaneDirectLightingKernelAodist)
    unregister_class(OctaneDirectLightingKernelFiltersize)
    unregister_class(OctaneDirectLightingKernelRayepsilon)
    unregister_class(OctaneDirectLightingKernelMaxOverlappingVolumes)
    unregister_class(OctaneDirectLightingKernelDiffusedepth)
    unregister_class(OctaneDirectLightingKernelGlossydepth)
    unregister_class(OctaneDirectLightingKernelSpeculardepth)
    unregister_class(OctaneDirectLightingKernelGIMode)
    unregister_class(OctaneDirectLightingKernelMaxsamples)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
