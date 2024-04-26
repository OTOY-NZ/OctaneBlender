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


class OctaneScatterOnSurfaceGeometry(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceGeometry"
    bl_label="Surface"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_GEOMETRY
    octane_pin_name="geometry"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput1(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput1"
    bl_label="Scattered object 1"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT1
    octane_pin_name="input1"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput2(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput2"
    bl_label="Scattered object 2"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT2
    octane_pin_name="input2"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput3(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput3"
    bl_label="Scattered object 3"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT3
    octane_pin_name="input3"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput4(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput4"
    bl_label="Scattered object 4"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT4
    octane_pin_name="input4"
    octane_pin_type=consts.PinType.PT_GEOMETRY
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionMethod(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionMethod"
    bl_label="Object selection method"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INPUT_SELECTION_METHOD
    octane_pin_name="inputSelectionMethod"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Sequential", "Sequential", "", 0),
        ("Random", "Random", "", 1),
        ("Selection map", "Selection map", "", 2),
    ]
    default_value: EnumProperty(default="Sequential", update=OctaneBaseSocket.update_node_tree, description="The method used to select between source objects for each instance", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionSeed(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionSeed"
    bl_label="Object selection seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INPUT_SELECTION_SEED
    octane_pin_name="inputSelectionSeed"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Seed used to randomize the selection of source objects", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionMap"
    bl_label="Object selection map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INPUT_SELECTION_MAP
    octane_pin_name="inputSelectionMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethod(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethod"
    bl_label="Distribution on surfaces"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_METHOD
    octane_pin_name="instanceDistributionMethod"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("One instance per vertex", "One instance per vertex", "", 0),
        ("One instance per edge", "One instance per edge", "", 4),
        ("Evenly spaced instances on edges", "Evenly spaced instances on edges", "", 5),
        ("One instance per polygon", "One instance per polygon", "", 1),
        ("Random instances by relative area", "Random instances by relative area", "", 2),
        ("Random instances by relative density", "Random instances by relative density", "", 3),
        ("Disabled", "Disabled", "", 6),
    ]
    default_value: EnumProperty(default="One instance per vertex", update=OctaneBaseSocket.update_node_tree, description="The method used to distribute instances on surfaces.\n- One instance per vertex: an instance is placed at each vertex.\n- One instance per edge: an instance is placed on each edge using the position value.\n- Evenly spaced instances on edges: instances are placed along edges using the position and spacing values.\n- One instance per polygon: an instance is placed at the centroid of each polygon.\n- Random instances by relative area: instances are placed uniformly over the surface.\n- Random instances by relative density: the relative density of instances is controlled by a map.\n- Disabled: no instances are placed on the surface", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethodParticles(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethodParticles"
    bl_label="Distribution on particles"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_METHOD_PARTICLES
    octane_pin_name="instanceDistributionMethodParticles"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("One instance per particle", "One instance per particle", "", 0),
        ("Disabled", "Disabled", "", 1),
    ]
    default_value: EnumProperty(default="One instance per particle", update=OctaneBaseSocket.update_node_tree, description="The method used to distribute instances on particles.\n- One instance per particle: an instance is attached to each particle.\n- Disabled: no instances are attached to particles", items=items)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethodHair(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethodHair"
    bl_label="Distribution on hair"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_METHOD_HAIR
    octane_pin_name="instanceDistributionMethodHair"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("One instance per hair vertex", "One instance per hair vertex", "", 0),
        ("One instance per hair", "One instance per hair", "", 1),
        ("Evenly spaced instances on hair", "Evenly spaced instances on hair", "", 2),
        ("Disabled", "Disabled", "", 3),
    ]
    default_value: EnumProperty(default="One instance per hair vertex", update=OctaneBaseSocket.update_node_tree, description="The method used to distribute instances on hair strands.\n- One instance per hair vertex: an instance is placed at each vertex of each hair strand.\n- One instance per hair: an instance is placed on each hair strand using the position value.\n- Evenly spaced instances on hair: instances are placed along hair strands using the position and spacing values.\n- Disabled: no instances are placed on hair strands", items=items)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionEdgePosition(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionEdgePosition"
    bl_label="Position on edge"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_EDGE_POSITION
    octane_pin_name="instanceDistributionEdgePosition"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="When scattering on edges this defines the position of instances along the edge", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing"
    bl_label="Spacing on edges"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_EDGE_SPACING
    octane_pin_name="instanceDistributionEdgeSpacing"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.250000, update=OctaneBaseSocket.update_node_tree, description="When scattering on edges this defines the spacing between instances along the edge", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfacePoissonDiskSampling(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfacePoissonDiskSampling"
    bl_label="Poisson disk sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_POISSON_DISK_SAMPLING
    octane_pin_name="poissonDiskSampling"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="When randomly scattering on the surface by area or relative density, enabling this option distributes the instances so that no two instances are too close to each other")
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRelativeDensityMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRelativeDensityMap"
    bl_label="Relative density map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INSTANCE_RELATIVE_DENSITY_MAP
    octane_pin_name="instanceRelativeDensityMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=14
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionHairPosition(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionHairPosition"
    bl_label="Position on hair"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_HAIR_POSITION
    octane_pin_name="instanceDistributionHairPosition"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=15
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="When scattering on hair strands this defines the position of instances along the hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionHairSpacing(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionHairSpacing"
    bl_label="Spacing on hair"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_DISTRIBUTION_HAIR_SPACING
    octane_pin_name="instanceDistributionHairSpacing"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=16
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.250000, update=OctaneBaseSocket.update_node_tree, description="When scattering on hair strands this defines the spacing between instances", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstancePlacementSeed(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstancePlacementSeed"
    bl_label="Seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INSTANCE_PLACEMENT_SEED
    octane_pin_name="instancePlacementSeed"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=17
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=0, update=OctaneBaseSocket.update_node_tree, description="Global seed used to randomize instance placement", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCount(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCount"
    bl_label="Instances"
    color=consts.OctanePinColor.Int
    octane_default_node_type=consts.NodeType.NT_INT
    octane_default_node_name="OctaneIntValue"
    octane_pin_id=consts.PinID.P_INSTANCE_COUNT
    octane_pin_name="instanceCount"
    octane_pin_type=consts.PinType.PT_INT
    octane_pin_index=18
    octane_socket_type=consts.SocketType.ST_INT
    default_value: IntProperty(default=1, update=OctaneBaseSocket.update_node_tree, description="When instances are not attached to discrete geometry elements this defines the maximum number of instances to create", min=0, max=16777216, soft_min=0, soft_max=16777216, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingMap"
    bl_label="Culling map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INSTANCE_CULLING_MAP
    octane_pin_name="instanceCullingMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=19
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingValueMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingValueMin"
    bl_label="Culling min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_CULLING_VALUE_MIN
    octane_pin_name="instanceCullingValueMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=20
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="All instances in areas of the map that have a value below this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingValueMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingValueMax"
    bl_label="Culling max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_CULLING_VALUE_MAX
    octane_pin_name="instanceCullingValueMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=21
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="All instances in areas of the map that have a value above this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingAngleMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingAngleMin"
    bl_label="Culling angle low"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_CULLING_ANGLE_MIN
    octane_pin_name="instanceCullingAngleMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=22
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="All instances on surfaces with a normal too close to the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingAngleMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingAngleMax"
    bl_label="Culling angle high"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_CULLING_ANGLE_MAX
    octane_pin_name="instanceCullingAngleMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=23
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="All instances on surfaces with a normal too far from the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceSmooth(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceSmooth"
    bl_label="Smooth normals"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_SMOOTH
    octane_pin_name="smooth"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=24
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceNormalAlignment(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceNormalAlignment"
    bl_label="Normal align"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_NORMAL_ALIGNMENT
    octane_pin_name="instanceNormalAlignment"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=25
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Blend factor between the reference up direction and the default normal of the instance.\nValues towards 0 align the instance with the reference up direction, values towards 1 align it with the default normal", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontAlignment(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontAlignment"
    bl_label="Front align"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_FRONT_ALIGNMENT
    octane_pin_name="instanceFrontAlignment"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=26
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Blend factor between the reference front direction and the default front of the instance.\nValues towards 0 align the instance with the reference front direction, values towards 1 align it with the default front", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1.000000, precision=2, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceOrientationPriority(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceOrientationPriority"
    bl_label="Orientation priority"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_ORIENTATION_PRIORITY
    octane_pin_name="instanceOrientationPriority"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=27
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Up", "Up", "", 0),
        ("Front", "Front", "", 1),
    ]
    default_value: EnumProperty(default="Up", update=OctaneBaseSocket.update_node_tree, description="If the up and front vector are not orthogonal this option selects which one has priority", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpMode"
    bl_label="Up direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_UP_MODE
    octane_pin_name="instanceUpMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=28
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=OctaneBaseSocket.update_node_tree, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpDirection"
    bl_label="Reference up direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_UP_DIRECTION
    octane_pin_name="instanceUpDirection"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=29
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="When up mode is set to Direction, the reference up vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpPoint"
    bl_label="Reference up point"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_UP_POINT
    octane_pin_name="instanceUpPoint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=30
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="When up mode is set to Point, the reference up vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontMode"
    bl_label="Front direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_FRONT_MODE
    octane_pin_name="instanceFrontMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=31
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=OctaneBaseSocket.update_node_tree, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontDirection"
    bl_label="Reference front direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_FRONT_DIRECTION
    octane_pin_name="instanceFrontDirection"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=32
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="When front mode is set to Direction, the reference front vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1.000000, subtype="DIRECTION", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontPoint"
    bl_label="Reference front point"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_FRONT_POINT
    octane_pin_name="instanceFrontPoint"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=33
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="When front mode is set to Point, the reference front vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMode"
    bl_label="Rotation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_ROTATION_MODE
    octane_pin_name="instanceRotationMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=34
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=OctaneBaseSocket.update_node_tree, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMin"
    bl_label="Rotation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_ROTATION_MIN
    octane_pin_name="instanceRotationMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=35
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Minimum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMax"
    bl_label="Rotation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_ROTATION_MAX
    octane_pin_name="instanceRotationMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=36
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Maximum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationStep"
    bl_label="Rotation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_ROTATION_STEP
    octane_pin_name="instanceRotationStep"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=37
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="When the rotation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMap"
    bl_label="Rotation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INSTANCE_ROTATION_MAP
    octane_pin_name="instanceRotationMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=38
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMode"
    bl_label="Scale mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_SCALE_MODE
    octane_pin_name="instanceScaleMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=39
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=OctaneBaseSocket.update_node_tree, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMin"
    bl_label="Scale min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_SCALE_MIN
    octane_pin_name="instanceScaleMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=40
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Minimum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1.000000, subtype="NONE", precision=3, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMax"
    bl_label="Scale max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_SCALE_MAX
    octane_pin_name="instanceScaleMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=41
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Maximum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1.000000, subtype="NONE", precision=3, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleStep"
    bl_label="Scale step"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_SCALE_STEP
    octane_pin_name="instanceScaleStep"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=42
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="When the scale mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMap"
    bl_label="Scale map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INSTANCE_SCALE_MAP
    octane_pin_name="instanceScaleMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=43
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMode"
    bl_label="Translation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_INSTANCE_TRANSLATION_MODE
    octane_pin_name="instanceTranslationMode"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=44
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=OctaneBaseSocket.update_node_tree, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMin"
    bl_label="Translation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_TRANSLATION_MIN
    octane_pin_name="instanceTranslationMin"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=45
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Minimum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMax"
    bl_label="Translation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_TRANSLATION_MAX
    octane_pin_name="instanceTranslationMax"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=46
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=OctaneBaseSocket.update_node_tree, description="Maximum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationStep"
    bl_label="Translation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_INSTANCE_TRANSLATION_STEP
    octane_pin_name="instanceTranslationStep"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=47
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000000, update=OctaneBaseSocket.update_node_tree, description="When the translation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMap"
    bl_label="Translation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_INSTANCE_TRANSLATION_MAP
    octane_pin_name="instanceTranslationMap"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=48
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceGroupGeometry(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupGeometry"
    bl_label="[OctaneGroupTitle]Geometry"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Surface;")

class OctaneScatterOnSurfaceGroupObjects(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupObjects"
    bl_label="[OctaneGroupTitle]Objects"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;")

class OctaneScatterOnSurfaceGroupDistribution(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupDistribution"
    bl_label="[OctaneGroupTitle]Distribution"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Distribution on surfaces;Distribution on particles;Distribution on hair;Position on edge;Spacing on edges;Poisson disk sampling;Relative density map;Position on hair;Spacing on hair;Seed;")

class OctaneScatterOnSurfaceGroupDensity(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupDensity"
    bl_label="[OctaneGroupTitle]Density"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Instances;Culling map;Culling min;Culling max;Culling angle low;Culling angle high;")

class OctaneScatterOnSurfaceGroupInstanceOrientation(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupInstanceOrientation"
    bl_label="[OctaneGroupTitle]Instance orientation"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Smooth normals;Normal align;Front align;Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;")

class OctaneScatterOnSurfaceGroupInstanceTransform(OctaneGroupTitleSocket):
    bl_idname="OctaneScatterOnSurfaceGroupInstanceTransform"
    bl_label="[OctaneGroupTitle]Instance transform"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")

class OctaneScatterOnSurface(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneScatterOnSurface"
    bl_label="Scatter on surface"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneScatterOnSurfaceGroupGeometry,OctaneScatterOnSurfaceGeometry,OctaneScatterOnSurfaceGroupObjects,OctaneScatterOnSurfaceInput1,OctaneScatterOnSurfaceInput2,OctaneScatterOnSurfaceInput3,OctaneScatterOnSurfaceInput4,OctaneScatterOnSurfaceInputSelectionMethod,OctaneScatterOnSurfaceInputSelectionSeed,OctaneScatterOnSurfaceInputSelectionMap,OctaneScatterOnSurfaceGroupDistribution,OctaneScatterOnSurfaceInstanceDistributionMethod,OctaneScatterOnSurfaceInstanceDistributionMethodParticles,OctaneScatterOnSurfaceInstanceDistributionMethodHair,OctaneScatterOnSurfaceInstanceDistributionEdgePosition,OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing,OctaneScatterOnSurfacePoissonDiskSampling,OctaneScatterOnSurfaceInstanceRelativeDensityMap,OctaneScatterOnSurfaceInstanceDistributionHairPosition,OctaneScatterOnSurfaceInstanceDistributionHairSpacing,OctaneScatterOnSurfaceInstancePlacementSeed,OctaneScatterOnSurfaceGroupDensity,OctaneScatterOnSurfaceInstanceCount,OctaneScatterOnSurfaceInstanceCullingMap,OctaneScatterOnSurfaceInstanceCullingValueMin,OctaneScatterOnSurfaceInstanceCullingValueMax,OctaneScatterOnSurfaceInstanceCullingAngleMin,OctaneScatterOnSurfaceInstanceCullingAngleMax,OctaneScatterOnSurfaceGroupInstanceOrientation,OctaneScatterOnSurfaceSmooth,OctaneScatterOnSurfaceInstanceNormalAlignment,OctaneScatterOnSurfaceInstanceFrontAlignment,OctaneScatterOnSurfaceInstanceOrientationPriority,OctaneScatterOnSurfaceInstanceUpMode,OctaneScatterOnSurfaceInstanceUpDirection,OctaneScatterOnSurfaceInstanceUpPoint,OctaneScatterOnSurfaceInstanceFrontMode,OctaneScatterOnSurfaceInstanceFrontDirection,OctaneScatterOnSurfaceInstanceFrontPoint,OctaneScatterOnSurfaceGroupInstanceTransform,OctaneScatterOnSurfaceInstanceRotationMode,OctaneScatterOnSurfaceInstanceRotationMin,OctaneScatterOnSurfaceInstanceRotationMax,OctaneScatterOnSurfaceInstanceRotationStep,OctaneScatterOnSurfaceInstanceRotationMap,OctaneScatterOnSurfaceInstanceScaleMode,OctaneScatterOnSurfaceInstanceScaleMin,OctaneScatterOnSurfaceInstanceScaleMax,OctaneScatterOnSurfaceInstanceScaleStep,OctaneScatterOnSurfaceInstanceScaleMap,OctaneScatterOnSurfaceInstanceTranslationMode,OctaneScatterOnSurfaceInstanceTranslationMin,OctaneScatterOnSurfaceInstanceTranslationMax,OctaneScatterOnSurfaceInstanceTranslationStep,OctaneScatterOnSurfaceInstanceTranslationMap,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_SCATTER_SURFACE
    octane_socket_list=["Surface", "Scattered object 1", "Scattered object 2", "Scattered object 3", "Scattered object 4", "Object selection method", "Object selection seed", "Object selection map", "Distribution on surfaces", "Distribution on particles", "Distribution on hair", "Position on edge", "Spacing on edges", "Poisson disk sampling", "Relative density map", "Position on hair", "Spacing on hair", "Seed", "Instances", "Culling map", "Culling min", "Culling max", "Culling angle low", "Culling angle high", "Smooth normals", "Normal align", "Front align", "Orientation priority", "Up direction mode", "Reference up direction", "Reference up point", "Front direction mode", "Reference front direction", "Reference front point", "Rotation mode", "Rotation min", "Rotation max", "Rotation step", "Rotation map", "Scale mode", "Scale min", "Scale max", "Scale step", "Scale map", "Translation mode", "Translation min", "Translation max", "Translation step", "Translation map", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=49

    def init(self, context):
        self.inputs.new("OctaneScatterOnSurfaceGroupGeometry", OctaneScatterOnSurfaceGroupGeometry.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGeometry", OctaneScatterOnSurfaceGeometry.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGroupObjects", OctaneScatterOnSurfaceGroupObjects.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInput1", OctaneScatterOnSurfaceInput1.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInput2", OctaneScatterOnSurfaceInput2.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInput3", OctaneScatterOnSurfaceInput3.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInput4", OctaneScatterOnSurfaceInput4.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionMethod", OctaneScatterOnSurfaceInputSelectionMethod.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionSeed", OctaneScatterOnSurfaceInputSelectionSeed.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionMap", OctaneScatterOnSurfaceInputSelectionMap.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGroupDistribution", OctaneScatterOnSurfaceGroupDistribution.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethod", OctaneScatterOnSurfaceInstanceDistributionMethod.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethodParticles", OctaneScatterOnSurfaceInstanceDistributionMethodParticles.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethodHair", OctaneScatterOnSurfaceInstanceDistributionMethodHair.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionEdgePosition", OctaneScatterOnSurfaceInstanceDistributionEdgePosition.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing", OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfacePoissonDiskSampling", OctaneScatterOnSurfacePoissonDiskSampling.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRelativeDensityMap", OctaneScatterOnSurfaceInstanceRelativeDensityMap.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionHairPosition", OctaneScatterOnSurfaceInstanceDistributionHairPosition.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionHairSpacing", OctaneScatterOnSurfaceInstanceDistributionHairSpacing.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstancePlacementSeed", OctaneScatterOnSurfaceInstancePlacementSeed.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGroupDensity", OctaneScatterOnSurfaceGroupDensity.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCount", OctaneScatterOnSurfaceInstanceCount.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingMap", OctaneScatterOnSurfaceInstanceCullingMap.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingValueMin", OctaneScatterOnSurfaceInstanceCullingValueMin.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingValueMax", OctaneScatterOnSurfaceInstanceCullingValueMax.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingAngleMin", OctaneScatterOnSurfaceInstanceCullingAngleMin.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingAngleMax", OctaneScatterOnSurfaceInstanceCullingAngleMax.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGroupInstanceOrientation", OctaneScatterOnSurfaceGroupInstanceOrientation.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceSmooth", OctaneScatterOnSurfaceSmooth.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceNormalAlignment", OctaneScatterOnSurfaceInstanceNormalAlignment.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontAlignment", OctaneScatterOnSurfaceInstanceFrontAlignment.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceOrientationPriority", OctaneScatterOnSurfaceInstanceOrientationPriority.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpMode", OctaneScatterOnSurfaceInstanceUpMode.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpDirection", OctaneScatterOnSurfaceInstanceUpDirection.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpPoint", OctaneScatterOnSurfaceInstanceUpPoint.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontMode", OctaneScatterOnSurfaceInstanceFrontMode.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontDirection", OctaneScatterOnSurfaceInstanceFrontDirection.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontPoint", OctaneScatterOnSurfaceInstanceFrontPoint.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceGroupInstanceTransform", OctaneScatterOnSurfaceGroupInstanceTransform.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMode", OctaneScatterOnSurfaceInstanceRotationMode.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMin", OctaneScatterOnSurfaceInstanceRotationMin.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMax", OctaneScatterOnSurfaceInstanceRotationMax.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationStep", OctaneScatterOnSurfaceInstanceRotationStep.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMap", OctaneScatterOnSurfaceInstanceRotationMap.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMode", OctaneScatterOnSurfaceInstanceScaleMode.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMin", OctaneScatterOnSurfaceInstanceScaleMin.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMax", OctaneScatterOnSurfaceInstanceScaleMax.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleStep", OctaneScatterOnSurfaceInstanceScaleStep.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMap", OctaneScatterOnSurfaceInstanceScaleMap.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMode", OctaneScatterOnSurfaceInstanceTranslationMode.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMin", OctaneScatterOnSurfaceInstanceTranslationMin.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMax", OctaneScatterOnSurfaceInstanceTranslationMax.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationStep", OctaneScatterOnSurfaceInstanceTranslationStep.bl_label).init()
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMap", OctaneScatterOnSurfaceInstanceTranslationMap.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneScatterOnSurfaceGeometry,
    OctaneScatterOnSurfaceInput1,
    OctaneScatterOnSurfaceInput2,
    OctaneScatterOnSurfaceInput3,
    OctaneScatterOnSurfaceInput4,
    OctaneScatterOnSurfaceInputSelectionMethod,
    OctaneScatterOnSurfaceInputSelectionSeed,
    OctaneScatterOnSurfaceInputSelectionMap,
    OctaneScatterOnSurfaceInstanceDistributionMethod,
    OctaneScatterOnSurfaceInstanceDistributionMethodParticles,
    OctaneScatterOnSurfaceInstanceDistributionMethodHair,
    OctaneScatterOnSurfaceInstanceDistributionEdgePosition,
    OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing,
    OctaneScatterOnSurfacePoissonDiskSampling,
    OctaneScatterOnSurfaceInstanceRelativeDensityMap,
    OctaneScatterOnSurfaceInstanceDistributionHairPosition,
    OctaneScatterOnSurfaceInstanceDistributionHairSpacing,
    OctaneScatterOnSurfaceInstancePlacementSeed,
    OctaneScatterOnSurfaceInstanceCount,
    OctaneScatterOnSurfaceInstanceCullingMap,
    OctaneScatterOnSurfaceInstanceCullingValueMin,
    OctaneScatterOnSurfaceInstanceCullingValueMax,
    OctaneScatterOnSurfaceInstanceCullingAngleMin,
    OctaneScatterOnSurfaceInstanceCullingAngleMax,
    OctaneScatterOnSurfaceSmooth,
    OctaneScatterOnSurfaceInstanceNormalAlignment,
    OctaneScatterOnSurfaceInstanceFrontAlignment,
    OctaneScatterOnSurfaceInstanceOrientationPriority,
    OctaneScatterOnSurfaceInstanceUpMode,
    OctaneScatterOnSurfaceInstanceUpDirection,
    OctaneScatterOnSurfaceInstanceUpPoint,
    OctaneScatterOnSurfaceInstanceFrontMode,
    OctaneScatterOnSurfaceInstanceFrontDirection,
    OctaneScatterOnSurfaceInstanceFrontPoint,
    OctaneScatterOnSurfaceInstanceRotationMode,
    OctaneScatterOnSurfaceInstanceRotationMin,
    OctaneScatterOnSurfaceInstanceRotationMax,
    OctaneScatterOnSurfaceInstanceRotationStep,
    OctaneScatterOnSurfaceInstanceRotationMap,
    OctaneScatterOnSurfaceInstanceScaleMode,
    OctaneScatterOnSurfaceInstanceScaleMin,
    OctaneScatterOnSurfaceInstanceScaleMax,
    OctaneScatterOnSurfaceInstanceScaleStep,
    OctaneScatterOnSurfaceInstanceScaleMap,
    OctaneScatterOnSurfaceInstanceTranslationMode,
    OctaneScatterOnSurfaceInstanceTranslationMin,
    OctaneScatterOnSurfaceInstanceTranslationMax,
    OctaneScatterOnSurfaceInstanceTranslationStep,
    OctaneScatterOnSurfaceInstanceTranslationMap,
    OctaneScatterOnSurfaceGroupGeometry,
    OctaneScatterOnSurfaceGroupObjects,
    OctaneScatterOnSurfaceGroupDistribution,
    OctaneScatterOnSurfaceGroupDensity,
    OctaneScatterOnSurfaceGroupInstanceOrientation,
    OctaneScatterOnSurfaceGroupInstanceTransform,
    OctaneScatterOnSurface,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
from octane import core

OctaneScatterOnSurfaceGeometry.octane_default_node_name = "OctaneObjectData"
OctaneScatterOnSurfaceInput1.octane_default_node_name = "OctaneObjectData"
OctaneScatterOnSurfaceInput2.octane_default_node_name = "OctaneObjectData"
OctaneScatterOnSurfaceInput3.octane_default_node_name = "OctaneObjectData"
OctaneScatterOnSurfaceInput4.octane_default_node_name = "OctaneObjectData"