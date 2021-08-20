##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneScatterOnSurfaceGeometry(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceGeometry"
    bl_label="Surface"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput1(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput1"
    bl_label="Scattered object 1"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput2(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput2"
    bl_label="Scattered object 2"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput3(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput3"
    bl_label="Scattered object 3"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=573)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInput4(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInput4"
    bl_label="Scattered object 4"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=574)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionMethod(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionMethod"
    bl_label="Object selection method"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=575)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Sequential", "Sequential", "", 0),
        ("Random", "Random", "", 1),
        ("Selection map", "Selection map", "", 2),
    ]
    default_value: EnumProperty(default="Sequential", update=None, description="The method used to select between source objects for each instance", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionSeed(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionSeed"
    bl_label="Object selection seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=576)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="Seed used to randomize the selection of source objects", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInputSelectionMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInputSelectionMap"
    bl_label="Object selection map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=577)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethod(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethod"
    bl_label="Distribution on surfaces"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=578)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("One instance per vertex", "One instance per vertex", "", 0),
        ("One instance per edge", "One instance per edge", "", 4),
        ("Evenly spaced instances on edges", "Evenly spaced instances on edges", "", 5),
        ("One instance per polygon", "One instance per polygon", "", 1),
        ("Random instances by relative area", "Random instances by relative area", "", 2),
        ("Random instances by relative density", "Random instances by relative density", "", 3),
        ("Disabled", "Disabled", "", 6),
    ]
    default_value: EnumProperty(default="One instance per vertex", update=None, description="The method used to distribute instances on surfaces.\n- One instance per vertex: an instance is placed at each vertex.\n- One instance per edge: an instance is placed on each edge using the position value.\n- Evenly spaced instances on edges: instances are placed along edges using the position and spacing values.\n- One instance per polygon: an instance is placed at the centroid of each polygon.\n- Random instances by relative area: instances are placed uniformly over the surface.\n- Random instances by relative density: the relative density of instances is controlled by a map.\n- Disabled: no instances are placed on the surface", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethodParticles(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethodParticles"
    bl_label="Distribution on particles"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=651)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("One instance per particle", "One instance per particle", "", 0),
        ("Disabled", "Disabled", "", 1),
    ]
    default_value: EnumProperty(default="One instance per particle", update=None, description="The method used to distribute instances on particles.\n- One instance per particle: an instance is attached to each particle.\n- Disabled: no instances are attached to particles", items=items)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionMethodHair(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionMethodHair"
    bl_label="Distribution on hair"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=650)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("One instance per hair vertex", "One instance per hair vertex", "", 0),
        ("One instance per hair", "One instance per hair", "", 1),
        ("Evenly spaced instances on hair", "Evenly spaced instances on hair", "", 2),
        ("Disabled", "Disabled", "", 3),
    ]
    default_value: EnumProperty(default="One instance per hair vertex", update=None, description="The method used to distribute instances on hair strands.\n- One instance per hair vertex: an instance is placed at each vertex of each hair strand.\n- One instance per hair: an instance is placed on each hair strand using the position value.\n- Evenly spaced instances on hair: instances are placed along hair strands using the position and spacing values.\n- Disabled: no instances are placed on hair strands", items=items)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionEdgePosition(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionEdgePosition"
    bl_label="Position on edge"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=652)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="When scattering on edges this defines the position of instances along the edge", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing"
    bl_label="Spacing on edges"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=653)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.250000, update=None, description="When scattering on edges this defines the spacing between instances along the edge", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfacePoissonDiskSampling(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfacePoissonDiskSampling"
    bl_label="Poisson disk sampling"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=707)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="When randomly scattering on the surface by area or relative density, enabling this option distributes the instances so that no two instances are too close to each other")
    octane_hide_value=False
    octane_min_version=11000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRelativeDensityMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRelativeDensityMap"
    bl_label="Relative density map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=579)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionHairPosition(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionHairPosition"
    bl_label="Position on hair"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=654)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.500000, update=None, description="When scattering on hair strands this defines the position of instances along the hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceDistributionHairSpacing(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceDistributionHairSpacing"
    bl_label="Spacing on hair"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=655)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.250000, update=None, description="When scattering on hair strands this defines the spacing between instances", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstancePlacementSeed(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstancePlacementSeed"
    bl_label="Seed"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=581)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=0, update=None, description="Global seed used to randomize instance placement", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCount(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCount"
    bl_label="Instances"
    color=consts.OctanePinColor.Int
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=582)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=1, update=None, description="When instances are not attached to discrete geometry elements this defines the maximum number of instances to create", min=0, max=16777216, soft_min=0, soft_max=16777216, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingMap"
    bl_label="Culling map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=583)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingValueMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingValueMin"
    bl_label="Culling min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=584)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="All instances in areas of the map that have a value below this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingValueMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingValueMax"
    bl_label="Culling max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=585)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="All instances in areas of the map that have a value above this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingAngleMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingAngleMin"
    bl_label="Culling angle low"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=586)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="All instances on surfaces with a normal too close to the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceCullingAngleMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceCullingAngleMax"
    bl_label="Culling angle high"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=587)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="All instances on surfaces with a normal too far from the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceSmooth(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceSmooth"
    bl_label="Smooth normals"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceNormalAlignment(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceNormalAlignment"
    bl_label="Normal align"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=588)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Blend factor between the reference up direction and the default normal of the instance.\nValues towards 0 align the instance with the reference up direction, values towards 1 align it with the default normal", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontAlignment(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontAlignment"
    bl_label="Front align"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=656)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Blend factor between the reference front direction and the default front of the instance.\nValues towards 0 align the instance with the reference front direction, values towards 1 align it with the default front", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceOrientationPriority(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceOrientationPriority"
    bl_label="Orientation priority"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=589)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Up", "Up", "", 0),
        ("Front", "Front", "", 1),
    ]
    default_value: EnumProperty(default="Up", update=None, description="If the up and front vector are not orthogonal this option selects which one has priority", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpMode"
    bl_label="Up direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=590)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=None, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpDirection"
    bl_label="Reference up direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=591)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), update=None, description="When up mode is set to Direction, the reference up vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceUpPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceUpPoint"
    bl_label="Reference up point"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=592)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="When up mode is set to Point, the reference up vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontMode"
    bl_label="Front direction mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=593)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", update=None, description="Selects between the use of a reference direction or a reference point", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontDirection(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontDirection"
    bl_label="Reference front direction"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=594)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), update=None, description="When front mode is set to Direction, the reference front vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="DIRECTION", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceFrontPoint(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceFrontPoint"
    bl_label="Reference front point"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=595)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="When front mode is set to Point, the reference front vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMode"
    bl_label="Rotation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=596)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMin"
    bl_label="Rotation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=597)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Minimum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMax"
    bl_label="Rotation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=598)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Maximum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationStep"
    bl_label="Rotation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=609)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the rotation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceRotationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceRotationMap"
    bl_label="Rotation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=599)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMode"
    bl_label="Scale mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=600)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMin"
    bl_label="Scale min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=601)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Minimum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMax"
    bl_label="Scale max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=602)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), update=None, description="Maximum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleStep"
    bl_label="Scale step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=610)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the scale mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceScaleMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceScaleMap"
    bl_label="Scale map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=603)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMode(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMode"
    bl_label="Translation mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=604)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", update=None, description="", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMin(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMin"
    bl_label="Translation min"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=605)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Minimum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMax(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMax"
    bl_label="Translation max"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=606)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT3)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), update=None, description="Maximum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationStep(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationStep"
    bl_label="Translation step"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=611)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="When the translation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatterOnSurfaceInstanceTranslationMap(OctaneBaseSocket):
    bl_idname="OctaneScatterOnSurfaceInstanceTranslationMap"
    bl_label="Translation map"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=607)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
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
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=164)
    octane_socket_list: StringProperty(name="Socket List", default="Surface;Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;Distribution on surfaces;Distribution on particles;Distribution on hair;Position on edge;Spacing on edges;Poisson disk sampling;Relative density map;Position on hair;Spacing on hair;Seed;Instances;Culling map;Culling min;Culling max;Culling angle low;Culling angle high;Smooth normals;Normal align;Front align;Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_module_graph_storage;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="10;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=49)

    a_module_graph_storage: StringProperty(name="Module graph storage", default="", update=None, description="Data stored by the wrapped module node graph. Will be updated after every evaluation of the graph")

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


_classes=[
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

def register():
    from bpy.utils import register_class
    for _class in _classes:
        register_class(_class)

def unregister():
    from bpy.utils import unregister_class
    for _class in reversed(_classes):
        unregister_class(_class)

##### END OCTANE GENERATED CODE BLOCK #####

OctaneScatterOnSurfaceGeometry.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterOnSurfaceInput1.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterOnSurfaceInput2.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterOnSurfaceInput3.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"
OctaneScatterOnSurfaceInput4.octane_default_node_type = "ShaderNodeOctObjectData:OutGeo"