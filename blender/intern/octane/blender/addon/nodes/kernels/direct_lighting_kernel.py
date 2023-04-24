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


class OctaneDirectLightingKernelMaxsamples(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMaxsamples"
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

class OctaneDirectLightingKernelGIMode(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelGIMode"
    bl_label="Global illumination mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=61)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="GI_mode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 0),
        ("Ambient occlusion", "Ambient occlusion", "", 3),
        ("Diffuse", "Diffuse", "", 4),
    ]
    default_value: EnumProperty(default="Ambient occlusion", update=OctaneBaseSocket.update_node_tree, description="Determines how global illumination is approximated", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelSpeculardepth(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelSpeculardepth"
    bl_label="Specular depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=221)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="speculardepth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=5, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which specular reflections/refractions are allowed", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelGlossydepth(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelGlossydepth"
    bl_label="Glossy depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=66)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="glossydepth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=2, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which glossy reflections are allowed", min=1, max=1024, soft_min=1, soft_max=1024, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelDiffusedepth(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelDiffusedepth"
    bl_label="Diffuse depth"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=29)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="diffusedepth")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=2, update=OctaneBaseSocket.update_node_tree, description="The maximum path depth for which diffuse reflections are allowed", min=1, max=8, soft_min=1, soft_max=8, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelMaxOverlappingVolumes(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMaxOverlappingVolumes"
    bl_label="Maximal overlapping volumes"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=702)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="maxOverlappingVolumes")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=4, update=OctaneBaseSocket.update_node_tree, description="How much space to allocate for overlapping volumes. Ray marching is faster with low values but you can get artefacts where lots of volumes overlap", min=4, max=16, soft_min=4, soft_max=16, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelRayepsilon(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelRayepsilon"
    bl_label="Ray epsilon"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rayepsilon")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Shadow ray offset distance", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelFiltersize(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelFiltersize"
    bl_label="Filter size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=50)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="filtersize")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.200000, update=OctaneBaseSocket.update_node_tree, description="Film splatting width (to reduce aliasing)", min=1.000000, max=8.000000, soft_min=1.000000, soft_max=8.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAodist(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAodist"
    bl_label="AO distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=7)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aodist")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=3.000000, update=OctaneBaseSocket.update_node_tree, description="Maximum distance for environment ambient occlusion", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.010000, soft_max=1024.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAoTexture(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAoTexture"
    bl_label="AO ambient texture"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=326)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aoTexture")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=3030005
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAlphashadows(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAlphashadows"
    bl_label="Alpha shadows"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=3)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="alphashadows")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelNestedDielectrics(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelNestedDielectrics"
    bl_label="Nested dielectrics"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=571)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="nestedDielectrics")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables nested dielectrics. If disabled, the surface IORs not tracked and surface priorities are ignored")
    octane_hide_value=False
    octane_min_version=10020100
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelIrradiance(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelIrradiance"
    bl_label="Irradiance mode"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=381)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="irradiance")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Render the first surface as a white diffuse material")
    octane_hide_value=False
    octane_min_version=3080009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelMaxsubdLevel(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMaxsubdLevel"
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

class OctaneDirectLightingKernelAlphachannel(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAlphachannel"
    bl_label="Alpha channel"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=2)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="alphachannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables a compositing alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelKeepEnvironment(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelKeepEnvironment"
    bl_label="Keep environment"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=86)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="keep_environment")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keeps environment with enabled alpha channel")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAiLight(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAiLight"
    bl_label="AI light"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=386)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aiLight")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enables AI light")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAiLightUpdate(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAiLightUpdate"
    bl_label="AI light update"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=384)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aiLightUpdate")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables dynamic AI light update")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelGlobalLightIdMaskAction(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelGlobalLightIdMaskAction"
    bl_label="Light IDs action"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=435)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="globalLightIdMaskAction")
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

class OctaneDirectLightingKernelGlobalLightIdMask(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelGlobalLightIdMask"
    bl_label="Light IDs"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type=132
    octane_default_node_name="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=434)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="globalLightIdMask")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelLightPassMask(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelLightPassMask"
    bl_label="Light linking invert"
    color=consts.OctanePinColor.BitMask
    octane_default_node_type=132
    octane_default_node_name="OctaneBitValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=433)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="lightPassMask")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=4000013
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelPathTermPower(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelPathTermPower"
    bl_label="Path term. power"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=129)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="pathTermPower")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.300000, update=OctaneBaseSocket.update_node_tree, description="Path may get terminated when ray power is less then this value", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelCoherentRatio(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelCoherentRatio"
    bl_label="Coherent ratio"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=25)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coherentRatio")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=2140000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelStaticNoise(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelStaticNoise"
    bl_label="Static noise"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=223)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="staticNoise")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, the noise patterns are kept stable between frames")
    octane_hide_value=False
    octane_min_version=2110002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelParallelSamples(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelParallelSamples"
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

class OctaneDirectLightingKernelMaxTileSamples(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMaxTileSamples"
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

class OctaneDirectLightingKernelMinimizeNetTraffic(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMinimizeNetTraffic"
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

class OctaneDirectLightingKernelAdaptiveSampling(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAdaptiveSampling"
    bl_label="Adaptive sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=347)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="adaptiveSampling")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image parts")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelNoiseThreshold(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelNoiseThreshold"
    bl_label="Noise threshold"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=349)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="noiseThreshold")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.020000, update=OctaneBaseSocket.update_node_tree, description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelMinAdaptiveSamples(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMinAdaptiveSamples"
    bl_label="Min. adaptive samples"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=351)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="minAdaptiveSamples")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=512, update=OctaneBaseSocket.update_node_tree, description="Minimum number of samples per pixel until adaptive sampling kicks in. Set it to a higher value if you notice that the error estimate is incorrect and stops sampling pixels too early resulting in artifacts.\nOnly valid if adaptive sampling is enabled", min=2, max=1000000, soft_min=2, soft_max=100000, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAdaptiveSamplingPixelGroup(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAdaptiveSamplingPixelGroup"
    bl_label="Pixel grouping"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=350)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="adaptiveSamplingPixelGroup")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 1),
        ("2 x 2", "2 x 2", "", 2),
        ("4 x 4", "4 x 4", "", 4),
    ]
    default_value: EnumProperty(default="2 x 2", update=OctaneBaseSocket.update_node_tree, description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not", items=items)
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAdaptiveSamplingExposure(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAdaptiveSamplingExposure"
    bl_label="Expected exposure"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=353)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="adaptiveSamplingExposure")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The expected exposure should be approximately the same value as the exposure in the imager or 0 to ignore this settings.\nIt's used by adaptive sampling to determine which pixels are bright and which are dark, which obviously depends on the exposure setting in the imaging settings. Adaptive sampling tweaks/reduces the noise estimate of very dark areas of the image. It also increases the min. adaptive samples limit for very dark areas which tend to find paths to light sources only very irregularly and thus have a too optimistic noise estimate", min=0.000000, max=4096.000000, soft_min=0.000000, soft_max=4096.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=3060002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelWhiteLightSpectrum(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelWhiteLightSpectrum"
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

class OctaneDirectLightingKernelUseOldColorPipeline(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelUseOldColorPipeline"
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

class OctaneDirectLightingKernelDeepEnable(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelDeepEnable"
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
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelDeepEnablePasses(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelDeepEnablePasses"
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

class OctaneDirectLightingKernelMaxDepthSamples(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelMaxDepthSamples"
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
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelDepthTolerance(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelDepthTolerance"
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
    octane_min_version=3000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelToonShadowAmbient(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelToonShadowAmbient"
    bl_label="Toon shadow ambient"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=368)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="toonShadowAmbient")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_RGBA)
    default_value: FloatVectorProperty(default=(0.500000, 0.500000, 0.500000), update=OctaneBaseSocket.update_node_tree, description="The ambient modifier of toon shadowing", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="COLOR", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=3080000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelOldVolumeBehavior(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelOldVolumeBehavior"
    bl_label="Emulate old volume behavior"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=448)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="oldVolumeBehavior")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Emulate the behavior of emission and scattering of version 4.0 and earlier")
    octane_hide_value=False
    octane_min_version=5000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneDirectLightingKernelAffectRoughness(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAffectRoughness"
    bl_label="Affect roughness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=487)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="affectRoughness")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="The percentage of roughness affecting subsequent layers' roughness", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=6000000
    octane_end_version=6000006
    octane_deprecated=True

class OctaneDirectLightingKernelAiLightUpdateStrength(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAiLightUpdateStrength"
    bl_label="AI light strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=385)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="aiLightUpdateStrength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.800000, update=OctaneBaseSocket.update_node_tree, description="The strength for dynamic AI light update", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=4000000
    octane_end_version=4000009
    octane_deprecated=True

class OctaneDirectLightingKernelCoherentMode(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelCoherentMode"
    bl_label="Coherent mode"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=24)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="coherentMode")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts")
    octane_hide_value=False
    octane_min_version=2100000
    octane_end_version=2140000
    octane_deprecated=True

class OctaneDirectLightingKernelRrprob(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelRrprob"
    bl_label="RR probability"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=205)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rrprob")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="(deprecated) Russian roulette termination probability (0=auto)", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=2100000
    octane_deprecated=True

class OctaneDirectLightingKernelAdaptiveStrength(OctaneBaseSocket):
    bl_idname="OctaneDirectLightingKernelAdaptiveStrength"
    bl_label="Adaptive strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=352)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="adaptiveStrength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The strength with which the adaptive sampling is applied. Lower the values will increase render time. Only valid if adaptive sampling is enabled", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=3060000
    octane_end_version=3060001
    octane_deprecated=True

class OctaneDirectLightingKernelGroupQuality(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupQuality"
    bl_label="[OctaneGroupTitle]Quality"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Max. samples;Global illumination mode;Specular depth;Glossy depth;Diffuse depth;Maximal overlapping volumes;Ray epsilon;Filter size;AO distance;AO ambient texture;Alpha shadows;Nested dielectrics;Irradiance mode;Max subdivision level;Affect roughness;")

class OctaneDirectLightingKernelGroupAlphaChannel(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupAlphaChannel"
    bl_label="[OctaneGroupTitle]Alpha channel"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Alpha channel;Keep environment;")

class OctaneDirectLightingKernelGroupLight(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupLight"
    bl_label="[OctaneGroupTitle]Light"
    octane_group_sockets: StringProperty(name="Group Sockets", default="AI light;AI light update;Light IDs action;Light IDs;Light linking invert;AI light strength;")

class OctaneDirectLightingKernelGroupSampling(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupSampling"
    bl_label="[OctaneGroupTitle]Sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Path term. power;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;")

class OctaneDirectLightingKernelGroupAdaptiveSampling(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupAdaptiveSampling"
    bl_label="[OctaneGroupTitle]Adaptive sampling"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;Adaptive strength;")

class OctaneDirectLightingKernelGroupColor(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupColor"
    bl_label="[OctaneGroupTitle]Color"
    octane_group_sockets: StringProperty(name="Group Sockets", default="White light spectrum;Use old color pipeline;")

class OctaneDirectLightingKernelGroupDeepImage(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupDeepImage"
    bl_label="[OctaneGroupTitle]Deep image"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;")

class OctaneDirectLightingKernelGroupToonShading(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupToonShading"
    bl_label="[OctaneGroupTitle]Toon Shading"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Toon shadow ambient;")

class OctaneDirectLightingKernelGroupCompatibilitySettings(OctaneGroupTitleSocket):
    bl_idname="OctaneDirectLightingKernelGroupCompatibilitySettings"
    bl_label="[OctaneGroupTitle]Compatibility settings"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Emulate old volume behavior;")

class OctaneDirectLightingKernel(bpy.types.Node, OctaneBaseKernelNode):
    bl_idname="OctaneDirectLightingKernel"
    bl_label="Direct lighting kernel"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=24)
    octane_socket_list: StringProperty(name="Socket List", default="Max. samples;Global illumination mode;Specular depth;Glossy depth;Diffuse depth;Maximal overlapping volumes;Ray epsilon;Filter size;AO distance;AO ambient texture;Alpha shadows;Nested dielectrics;Irradiance mode;Max subdivision level;Alpha channel;Keep environment;AI light;AI light update;Light IDs action;Light IDs;Light linking invert;Path term. power;Coherent ratio;Static noise;Parallel samples;Max. tile samples;Minimize net traffic;Adaptive sampling;Noise threshold;Min. adaptive samples;Pixel grouping;Expected exposure;White light spectrum;Use old color pipeline;Deep image;Deep render AOVs;Max. depth samples;Depth tolerance;Toon shadow ambient;Emulate old volume behavior;Affect roughness;AI light strength;Coherent mode;RR probability;Adaptive strength;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=45)

    def init(self, context):
        self.inputs.new("OctaneDirectLightingKernelGroupQuality", OctaneDirectLightingKernelGroupQuality.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMaxsamples", OctaneDirectLightingKernelMaxsamples.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGIMode", OctaneDirectLightingKernelGIMode.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelSpeculardepth", OctaneDirectLightingKernelSpeculardepth.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGlossydepth", OctaneDirectLightingKernelGlossydepth.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelDiffusedepth", OctaneDirectLightingKernelDiffusedepth.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMaxOverlappingVolumes", OctaneDirectLightingKernelMaxOverlappingVolumes.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelRayepsilon", OctaneDirectLightingKernelRayepsilon.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelFiltersize", OctaneDirectLightingKernelFiltersize.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAodist", OctaneDirectLightingKernelAodist.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAoTexture", OctaneDirectLightingKernelAoTexture.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAlphashadows", OctaneDirectLightingKernelAlphashadows.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelNestedDielectrics", OctaneDirectLightingKernelNestedDielectrics.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelIrradiance", OctaneDirectLightingKernelIrradiance.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMaxsubdLevel", OctaneDirectLightingKernelMaxsubdLevel.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAffectRoughness", OctaneDirectLightingKernelAffectRoughness.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupAlphaChannel", OctaneDirectLightingKernelGroupAlphaChannel.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAlphachannel", OctaneDirectLightingKernelAlphachannel.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelKeepEnvironment", OctaneDirectLightingKernelKeepEnvironment.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupLight", OctaneDirectLightingKernelGroupLight.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAiLight", OctaneDirectLightingKernelAiLight.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAiLightUpdate", OctaneDirectLightingKernelAiLightUpdate.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGlobalLightIdMaskAction", OctaneDirectLightingKernelGlobalLightIdMaskAction.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGlobalLightIdMask", OctaneDirectLightingKernelGlobalLightIdMask.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelLightPassMask", OctaneDirectLightingKernelLightPassMask.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAiLightUpdateStrength", OctaneDirectLightingKernelAiLightUpdateStrength.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupSampling", OctaneDirectLightingKernelGroupSampling.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelPathTermPower", OctaneDirectLightingKernelPathTermPower.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelCoherentRatio", OctaneDirectLightingKernelCoherentRatio.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelStaticNoise", OctaneDirectLightingKernelStaticNoise.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelParallelSamples", OctaneDirectLightingKernelParallelSamples.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMaxTileSamples", OctaneDirectLightingKernelMaxTileSamples.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMinimizeNetTraffic", OctaneDirectLightingKernelMinimizeNetTraffic.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupAdaptiveSampling", OctaneDirectLightingKernelGroupAdaptiveSampling.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSampling", OctaneDirectLightingKernelAdaptiveSampling.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelNoiseThreshold", OctaneDirectLightingKernelNoiseThreshold.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMinAdaptiveSamples", OctaneDirectLightingKernelMinAdaptiveSamples.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSamplingPixelGroup", OctaneDirectLightingKernelAdaptiveSamplingPixelGroup.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAdaptiveSamplingExposure", OctaneDirectLightingKernelAdaptiveSamplingExposure.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelAdaptiveStrength", OctaneDirectLightingKernelAdaptiveStrength.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupColor", OctaneDirectLightingKernelGroupColor.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelWhiteLightSpectrum", OctaneDirectLightingKernelWhiteLightSpectrum.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelUseOldColorPipeline", OctaneDirectLightingKernelUseOldColorPipeline.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupDeepImage", OctaneDirectLightingKernelGroupDeepImage.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelDeepEnable", OctaneDirectLightingKernelDeepEnable.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelDeepEnablePasses", OctaneDirectLightingKernelDeepEnablePasses.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelMaxDepthSamples", OctaneDirectLightingKernelMaxDepthSamples.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelDepthTolerance", OctaneDirectLightingKernelDepthTolerance.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupToonShading", OctaneDirectLightingKernelGroupToonShading.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelToonShadowAmbient", OctaneDirectLightingKernelToonShadowAmbient.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelGroupCompatibilitySettings", OctaneDirectLightingKernelGroupCompatibilitySettings.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelOldVolumeBehavior", OctaneDirectLightingKernelOldVolumeBehavior.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelCoherentMode", OctaneDirectLightingKernelCoherentMode.bl_label).init()
        self.inputs.new("OctaneDirectLightingKernelRrprob", OctaneDirectLightingKernelRrprob.bl_label).init()
        self.outputs.new("OctaneKernelOutSocket", "Kernel out").init()


_CLASSES=[
    OctaneDirectLightingKernelMaxsamples,
    OctaneDirectLightingKernelGIMode,
    OctaneDirectLightingKernelSpeculardepth,
    OctaneDirectLightingKernelGlossydepth,
    OctaneDirectLightingKernelDiffusedepth,
    OctaneDirectLightingKernelMaxOverlappingVolumes,
    OctaneDirectLightingKernelRayepsilon,
    OctaneDirectLightingKernelFiltersize,
    OctaneDirectLightingKernelAodist,
    OctaneDirectLightingKernelAoTexture,
    OctaneDirectLightingKernelAlphashadows,
    OctaneDirectLightingKernelNestedDielectrics,
    OctaneDirectLightingKernelIrradiance,
    OctaneDirectLightingKernelMaxsubdLevel,
    OctaneDirectLightingKernelAlphachannel,
    OctaneDirectLightingKernelKeepEnvironment,
    OctaneDirectLightingKernelAiLight,
    OctaneDirectLightingKernelAiLightUpdate,
    OctaneDirectLightingKernelGlobalLightIdMaskAction,
    OctaneDirectLightingKernelGlobalLightIdMask,
    OctaneDirectLightingKernelLightPassMask,
    OctaneDirectLightingKernelPathTermPower,
    OctaneDirectLightingKernelCoherentRatio,
    OctaneDirectLightingKernelStaticNoise,
    OctaneDirectLightingKernelParallelSamples,
    OctaneDirectLightingKernelMaxTileSamples,
    OctaneDirectLightingKernelMinimizeNetTraffic,
    OctaneDirectLightingKernelAdaptiveSampling,
    OctaneDirectLightingKernelNoiseThreshold,
    OctaneDirectLightingKernelMinAdaptiveSamples,
    OctaneDirectLightingKernelAdaptiveSamplingPixelGroup,
    OctaneDirectLightingKernelAdaptiveSamplingExposure,
    OctaneDirectLightingKernelWhiteLightSpectrum,
    OctaneDirectLightingKernelUseOldColorPipeline,
    OctaneDirectLightingKernelDeepEnable,
    OctaneDirectLightingKernelDeepEnablePasses,
    OctaneDirectLightingKernelMaxDepthSamples,
    OctaneDirectLightingKernelDepthTolerance,
    OctaneDirectLightingKernelToonShadowAmbient,
    OctaneDirectLightingKernelOldVolumeBehavior,
    OctaneDirectLightingKernelAffectRoughness,
    OctaneDirectLightingKernelAiLightUpdateStrength,
    OctaneDirectLightingKernelCoherentMode,
    OctaneDirectLightingKernelRrprob,
    OctaneDirectLightingKernelAdaptiveStrength,
    OctaneDirectLightingKernelGroupQuality,
    OctaneDirectLightingKernelGroupAlphaChannel,
    OctaneDirectLightingKernelGroupLight,
    OctaneDirectLightingKernelGroupSampling,
    OctaneDirectLightingKernelGroupAdaptiveSampling,
    OctaneDirectLightingKernelGroupColor,
    OctaneDirectLightingKernelGroupDeepImage,
    OctaneDirectLightingKernelGroupToonShading,
    OctaneDirectLightingKernelGroupCompatibilitySettings,
    OctaneDirectLightingKernel,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

OctaneDirectLightingKernelGlobalLightIdMask.octane_default_node_name = "OctaneLightIDBitValue"
OctaneDirectLightingKernelLightPassMask.octane_default_node_name = "OctaneLightIDBitValue"

class OctaneDirectLightingKernel_Override(OctaneDirectLightingKernel):

    def init(self, context):
        super().init(context)
        self.init_octane_kernel(context, True)

utility.override_class(_CLASSES, OctaneDirectLightingKernel, OctaneDirectLightingKernel_Override)