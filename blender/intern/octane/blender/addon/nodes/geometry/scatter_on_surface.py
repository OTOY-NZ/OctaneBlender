##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneScatterOnSurfaceGeometry(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceGeometry"
    bl_label = "Surface"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterOnSurfaceInput1(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInput1"
    bl_label = "Scattered object 1"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterOnSurfaceInput2(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInput2"
    bl_label = "Scattered object 2"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterOnSurfaceInput3(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInput3"
    bl_label = "Scattered object 3"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=573)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterOnSurfaceInput4(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInput4"
    bl_label = "Scattered object 4"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=574)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterOnSurfaceInputSelectionMethod(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInputSelectionMethod"
    bl_label = "Object selection method"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=575)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Sequential", "Sequential", "", 0),
        ("Random", "Random", "", 1),
        ("Selection map", "Selection map", "", 2),
    ]
    default_value: EnumProperty(default="Sequential", description="The method used to select between source objects for each instance", items=items)

class OctaneScatterOnSurfaceInputSelectionSeed(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInputSelectionSeed"
    bl_label = "Object selection seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=576)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Seed used to randomize the selection of source objects", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInputSelectionMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInputSelectionMap"
    bl_label = "Object selection map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=577)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurfaceInstanceDistributionMethod(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionMethod"
    bl_label = "Distribution on surfaces"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=578)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("One instance per vertex", "One instance per vertex", "", 0),
        ("One instance per edge", "One instance per edge", "", 4),
        ("Evenly spaced instances on edges", "Evenly spaced instances on edges", "", 5),
        ("One instance per polygon", "One instance per polygon", "", 1),
        ("Random instances by relative area", "Random instances by relative area", "", 2),
        ("Random instances by relative density", "Random instances by relative density", "", 3),
        ("Disabled", "Disabled", "", 6),
    ]
    default_value: EnumProperty(default="One instance per vertex", description="The method used to distribute instances on surfaces. - One instance per vertex: an instance is placed at each vertex. - One instance per edge: an instance is placed on each edge using the position value. - Evenly spaced instances on edges: instances are placed along edges using the position and spacing values. - One instance per polygon: an instance is placed at the centroid of each polygon. - Random instances by relative area: instances are placed uniformly over the surface. - Random instances by relative density: the relative density of instances is controlled by a map. - Disabled: no instances are placed on the surface", items=items)

class OctaneScatterOnSurfaceInstanceDistributionMethodParticles(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionMethodParticles"
    bl_label = "Distribution on particles"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=651)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("One instance per particle", "One instance per particle", "", 0),
        ("Disabled", "Disabled", "", 1),
    ]
    default_value: EnumProperty(default="One instance per particle", description="The method used to distribute instances on particles. - One instance per particle: an instance is attached to each particle. - Disabled: no instances are attached to particles", items=items)

class OctaneScatterOnSurfaceInstanceDistributionMethodHair(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionMethodHair"
    bl_label = "Distribution on hair"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=650)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("One instance per hair vertex", "One instance per hair vertex", "", 0),
        ("One instance per hair", "One instance per hair", "", 1),
        ("Evenly spaced instances on hair", "Evenly spaced instances on hair", "", 2),
        ("Disabled", "Disabled", "", 3),
    ]
    default_value: EnumProperty(default="One instance per hair vertex", description="The method used to distribute instances on hair strands. - One instance per hair vertex: an instance is placed at each vertex of each hair strand. - One instance per hair: an instance is placed on each hair strand using the position value. - Evenly spaced instances on hair: instances are placed along hair strands using the position and spacing values. - Disabled: no instances are placed on hair strands", items=items)

class OctaneScatterOnSurfaceInstanceDistributionEdgePosition(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionEdgePosition"
    bl_label = "Position on edge"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=652)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="When scattering on edges this defines the position of instances along the edge", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing"
    bl_label = "Spacing on edges"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=653)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.250000, description="When scattering on edges this defines the spacing between instances along the edge", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterOnSurfacePoissonDiskSampling(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfacePoissonDiskSampling"
    bl_label = "Poisson disk sampling"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=707)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=False, description="When randomly scattering on the surface by area or relative density, enabling this option distributes the instances so that no two instances are too close to each other")

class OctaneScatterOnSurfaceInstanceRelativeDensityMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRelativeDensityMap"
    bl_label = "Relative density map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=579)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurfaceInstanceDistributionHairPosition(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionHairPosition"
    bl_label = "Position on hair"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=654)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="When scattering on hair strands this defines the position of instances along the hair", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceDistributionHairSpacing(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceDistributionHairSpacing"
    bl_label = "Spacing on hair"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=655)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.250000, description="When scattering on hair strands this defines the spacing between instances", min=0.001000, max=340282346638528859811704183484516925440.000000, soft_min=0.001000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInstancePlacementSeed(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstancePlacementSeed"
    bl_label = "Seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=581)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Global seed used to randomize instance placement", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInstanceCount(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCount"
    bl_label = "Instances"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=582)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=1, description="When instances are not attached to discrete geometry elements this defines the maximum number of instances to create", min=0, max=16777216, soft_min=0, soft_max=16777216, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceCullingMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCullingMap"
    bl_label = "Culling map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=583)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurfaceInstanceCullingValueMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCullingValueMin"
    bl_label = "Culling min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=584)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="All instances in areas of the map that have a value below this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceCullingValueMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCullingValueMax"
    bl_label = "Culling max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=585)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="All instances in areas of the map that have a value above this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceCullingAngleMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCullingAngleMin"
    bl_label = "Culling angle low"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=586)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="All instances on surfaces with a normal too close to the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceCullingAngleMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceCullingAngleMax"
    bl_label = "Culling angle high"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=587)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="All instances on surfaces with a normal too far from the reference up vector are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceSmooth(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceSmooth"
    bl_label = "Smooth normals"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=218)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneScatterOnSurfaceInstanceNormalAlignment(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceNormalAlignment"
    bl_label = "Normal align"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=588)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Blend factor between the reference up direction and the default normal of the instance. Values towards 0 align the instance with the reference up direction, values towards 1 align it with the default normal", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceFrontAlignment(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceFrontAlignment"
    bl_label = "Front align"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=656)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="Blend factor between the reference front direction and the default front of the instance. Values towards 0 align the instance with the reference front direction, values towards 1 align it with the default front", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterOnSurfaceInstanceOrientationPriority(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceOrientationPriority"
    bl_label = "Orientation priority"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=589)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Up", "Up", "", 0),
        ("Front", "Front", "", 1),
    ]
    default_value: EnumProperty(default="Up", description="If the up and front vector are not orthogonal this option selects which one has priority", items=items)

class OctaneScatterOnSurfaceInstanceUpMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceUpMode"
    bl_label = "Up direction mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=590)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", description="Selects between the use of a reference direction or a reference point", items=items)

class OctaneScatterOnSurfaceInstanceUpDirection(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceUpDirection"
    bl_label = "Reference up direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=591)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="When up mode is set to Direction, the reference up vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceUpPoint(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceUpPoint"
    bl_label = "Reference up point"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=592)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="When up mode is set to Point, the reference up vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceFrontMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceFrontMode"
    bl_label = "Front direction mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=593)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Direction", "Direction", "", 0),
        ("Point", "Point", "", 1),
    ]
    default_value: EnumProperty(default="Direction", description="Selects between the use of a reference direction or a reference point", items=items)

class OctaneScatterOnSurfaceInstanceFrontDirection(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceFrontDirection"
    bl_label = "Reference front direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=594)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), description="When front mode is set to Direction, the reference front vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceFrontPoint(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceFrontPoint"
    bl_label = "Reference front point"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=595)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="When front mode is set to Point, the reference front vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceRotationMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRotationMode"
    bl_label = "Rotation mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=596)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", description="", items=items)

class OctaneScatterOnSurfaceInstanceRotationMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRotationMin"
    bl_label = "Rotation min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=597)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Minimum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceRotationMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRotationMax"
    bl_label = "Rotation max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=598)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Maximum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceRotationStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRotationStep"
    bl_label = "Rotation step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=609)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the rotation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInstanceRotationMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceRotationMap"
    bl_label = "Rotation map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=599)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurfaceInstanceScaleMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceScaleMode"
    bl_label = "Scale mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=600)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", description="", items=items)

class OctaneScatterOnSurfaceInstanceScaleMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceScaleMin"
    bl_label = "Scale min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=601)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Minimum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceScaleMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceScaleMax"
    bl_label = "Scale max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=602)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Maximum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceScaleStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceScaleStep"
    bl_label = "Scale step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=610)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the scale mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInstanceScaleMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceScaleMap"
    bl_label = "Scale map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=603)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurfaceInstanceTranslationMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceTranslationMode"
    bl_label = "Translation mode"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=604)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Fixed", "Fixed", "", 0),
        ("Randomized with independent axes", "Randomized with independent axes", "", 1),
        ("Randomized with coupled axes", "Randomized with coupled axes", "", 2),
        ("Map", "Map", "", 3),
    ]
    default_value: EnumProperty(default="Fixed", description="", items=items)

class OctaneScatterOnSurfaceInstanceTranslationMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceTranslationMin"
    bl_label = "Translation min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=605)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Minimum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceTranslationMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceTranslationMax"
    bl_label = "Translation max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=606)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Maximum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterOnSurfaceInstanceTranslationStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceTranslationStep"
    bl_label = "Translation step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=611)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the translation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterOnSurfaceInstanceTranslationMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterOnSurfaceInstanceTranslationMap"
    bl_label = "Translation map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=607)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterOnSurface(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneScatterOnSurface"
    bl_label = "Scatter on surface"
    octane_node_type: IntProperty(name="Octane Node Type", default=164)
    octane_socket_list: StringProperty(name="Socket List", default="Surface;Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;Distribution on surfaces;Distribution on particles;Distribution on hair;Position on edge;Spacing on edges;Poisson disk sampling;Relative density map;Position on hair;Spacing on hair;Seed;Instances;Culling map;Culling min;Culling max;Culling angle low;Culling angle high;Smooth normals;Normal align;Front align;Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneScatterOnSurfaceGeometry", OctaneScatterOnSurfaceGeometry.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInput1", OctaneScatterOnSurfaceInput1.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInput2", OctaneScatterOnSurfaceInput2.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInput3", OctaneScatterOnSurfaceInput3.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInput4", OctaneScatterOnSurfaceInput4.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionMethod", OctaneScatterOnSurfaceInputSelectionMethod.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionSeed", OctaneScatterOnSurfaceInputSelectionSeed.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInputSelectionMap", OctaneScatterOnSurfaceInputSelectionMap.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethod", OctaneScatterOnSurfaceInstanceDistributionMethod.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethodParticles", OctaneScatterOnSurfaceInstanceDistributionMethodParticles.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionMethodHair", OctaneScatterOnSurfaceInstanceDistributionMethodHair.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionEdgePosition", OctaneScatterOnSurfaceInstanceDistributionEdgePosition.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing", OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing.bl_label)
        self.inputs.new("OctaneScatterOnSurfacePoissonDiskSampling", OctaneScatterOnSurfacePoissonDiskSampling.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRelativeDensityMap", OctaneScatterOnSurfaceInstanceRelativeDensityMap.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionHairPosition", OctaneScatterOnSurfaceInstanceDistributionHairPosition.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceDistributionHairSpacing", OctaneScatterOnSurfaceInstanceDistributionHairSpacing.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstancePlacementSeed", OctaneScatterOnSurfaceInstancePlacementSeed.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCount", OctaneScatterOnSurfaceInstanceCount.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingMap", OctaneScatterOnSurfaceInstanceCullingMap.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingValueMin", OctaneScatterOnSurfaceInstanceCullingValueMin.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingValueMax", OctaneScatterOnSurfaceInstanceCullingValueMax.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingAngleMin", OctaneScatterOnSurfaceInstanceCullingAngleMin.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceCullingAngleMax", OctaneScatterOnSurfaceInstanceCullingAngleMax.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceSmooth", OctaneScatterOnSurfaceSmooth.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceNormalAlignment", OctaneScatterOnSurfaceInstanceNormalAlignment.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontAlignment", OctaneScatterOnSurfaceInstanceFrontAlignment.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceOrientationPriority", OctaneScatterOnSurfaceInstanceOrientationPriority.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpMode", OctaneScatterOnSurfaceInstanceUpMode.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpDirection", OctaneScatterOnSurfaceInstanceUpDirection.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceUpPoint", OctaneScatterOnSurfaceInstanceUpPoint.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontMode", OctaneScatterOnSurfaceInstanceFrontMode.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontDirection", OctaneScatterOnSurfaceInstanceFrontDirection.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceFrontPoint", OctaneScatterOnSurfaceInstanceFrontPoint.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMode", OctaneScatterOnSurfaceInstanceRotationMode.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMin", OctaneScatterOnSurfaceInstanceRotationMin.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMax", OctaneScatterOnSurfaceInstanceRotationMax.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationStep", OctaneScatterOnSurfaceInstanceRotationStep.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceRotationMap", OctaneScatterOnSurfaceInstanceRotationMap.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMode", OctaneScatterOnSurfaceInstanceScaleMode.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMin", OctaneScatterOnSurfaceInstanceScaleMin.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMax", OctaneScatterOnSurfaceInstanceScaleMax.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleStep", OctaneScatterOnSurfaceInstanceScaleStep.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceScaleMap", OctaneScatterOnSurfaceInstanceScaleMap.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMode", OctaneScatterOnSurfaceInstanceTranslationMode.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMin", OctaneScatterOnSurfaceInstanceTranslationMin.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMax", OctaneScatterOnSurfaceInstanceTranslationMax.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationStep", OctaneScatterOnSurfaceInstanceTranslationStep.bl_label)
        self.inputs.new("OctaneScatterOnSurfaceInstanceTranslationMap", OctaneScatterOnSurfaceInstanceTranslationMap.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneScatterOnSurfaceGeometry)
    register_class(OctaneScatterOnSurfaceInput1)
    register_class(OctaneScatterOnSurfaceInput2)
    register_class(OctaneScatterOnSurfaceInput3)
    register_class(OctaneScatterOnSurfaceInput4)
    register_class(OctaneScatterOnSurfaceInputSelectionMethod)
    register_class(OctaneScatterOnSurfaceInputSelectionSeed)
    register_class(OctaneScatterOnSurfaceInputSelectionMap)
    register_class(OctaneScatterOnSurfaceInstanceDistributionMethod)
    register_class(OctaneScatterOnSurfaceInstanceDistributionMethodParticles)
    register_class(OctaneScatterOnSurfaceInstanceDistributionMethodHair)
    register_class(OctaneScatterOnSurfaceInstanceDistributionEdgePosition)
    register_class(OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing)
    register_class(OctaneScatterOnSurfacePoissonDiskSampling)
    register_class(OctaneScatterOnSurfaceInstanceRelativeDensityMap)
    register_class(OctaneScatterOnSurfaceInstanceDistributionHairPosition)
    register_class(OctaneScatterOnSurfaceInstanceDistributionHairSpacing)
    register_class(OctaneScatterOnSurfaceInstancePlacementSeed)
    register_class(OctaneScatterOnSurfaceInstanceCount)
    register_class(OctaneScatterOnSurfaceInstanceCullingMap)
    register_class(OctaneScatterOnSurfaceInstanceCullingValueMin)
    register_class(OctaneScatterOnSurfaceInstanceCullingValueMax)
    register_class(OctaneScatterOnSurfaceInstanceCullingAngleMin)
    register_class(OctaneScatterOnSurfaceInstanceCullingAngleMax)
    register_class(OctaneScatterOnSurfaceSmooth)
    register_class(OctaneScatterOnSurfaceInstanceNormalAlignment)
    register_class(OctaneScatterOnSurfaceInstanceFrontAlignment)
    register_class(OctaneScatterOnSurfaceInstanceOrientationPriority)
    register_class(OctaneScatterOnSurfaceInstanceUpMode)
    register_class(OctaneScatterOnSurfaceInstanceUpDirection)
    register_class(OctaneScatterOnSurfaceInstanceUpPoint)
    register_class(OctaneScatterOnSurfaceInstanceFrontMode)
    register_class(OctaneScatterOnSurfaceInstanceFrontDirection)
    register_class(OctaneScatterOnSurfaceInstanceFrontPoint)
    register_class(OctaneScatterOnSurfaceInstanceRotationMode)
    register_class(OctaneScatterOnSurfaceInstanceRotationMin)
    register_class(OctaneScatterOnSurfaceInstanceRotationMax)
    register_class(OctaneScatterOnSurfaceInstanceRotationStep)
    register_class(OctaneScatterOnSurfaceInstanceRotationMap)
    register_class(OctaneScatterOnSurfaceInstanceScaleMode)
    register_class(OctaneScatterOnSurfaceInstanceScaleMin)
    register_class(OctaneScatterOnSurfaceInstanceScaleMax)
    register_class(OctaneScatterOnSurfaceInstanceScaleStep)
    register_class(OctaneScatterOnSurfaceInstanceScaleMap)
    register_class(OctaneScatterOnSurfaceInstanceTranslationMode)
    register_class(OctaneScatterOnSurfaceInstanceTranslationMin)
    register_class(OctaneScatterOnSurfaceInstanceTranslationMax)
    register_class(OctaneScatterOnSurfaceInstanceTranslationStep)
    register_class(OctaneScatterOnSurfaceInstanceTranslationMap)
    register_class(OctaneScatterOnSurface)

def unregister():
    unregister_class(OctaneScatterOnSurface)
    unregister_class(OctaneScatterOnSurfaceInstanceTranslationMap)
    unregister_class(OctaneScatterOnSurfaceInstanceTranslationStep)
    unregister_class(OctaneScatterOnSurfaceInstanceTranslationMax)
    unregister_class(OctaneScatterOnSurfaceInstanceTranslationMin)
    unregister_class(OctaneScatterOnSurfaceInstanceTranslationMode)
    unregister_class(OctaneScatterOnSurfaceInstanceScaleMap)
    unregister_class(OctaneScatterOnSurfaceInstanceScaleStep)
    unregister_class(OctaneScatterOnSurfaceInstanceScaleMax)
    unregister_class(OctaneScatterOnSurfaceInstanceScaleMin)
    unregister_class(OctaneScatterOnSurfaceInstanceScaleMode)
    unregister_class(OctaneScatterOnSurfaceInstanceRotationMap)
    unregister_class(OctaneScatterOnSurfaceInstanceRotationStep)
    unregister_class(OctaneScatterOnSurfaceInstanceRotationMax)
    unregister_class(OctaneScatterOnSurfaceInstanceRotationMin)
    unregister_class(OctaneScatterOnSurfaceInstanceRotationMode)
    unregister_class(OctaneScatterOnSurfaceInstanceFrontPoint)
    unregister_class(OctaneScatterOnSurfaceInstanceFrontDirection)
    unregister_class(OctaneScatterOnSurfaceInstanceFrontMode)
    unregister_class(OctaneScatterOnSurfaceInstanceUpPoint)
    unregister_class(OctaneScatterOnSurfaceInstanceUpDirection)
    unregister_class(OctaneScatterOnSurfaceInstanceUpMode)
    unregister_class(OctaneScatterOnSurfaceInstanceOrientationPriority)
    unregister_class(OctaneScatterOnSurfaceInstanceFrontAlignment)
    unregister_class(OctaneScatterOnSurfaceInstanceNormalAlignment)
    unregister_class(OctaneScatterOnSurfaceSmooth)
    unregister_class(OctaneScatterOnSurfaceInstanceCullingAngleMax)
    unregister_class(OctaneScatterOnSurfaceInstanceCullingAngleMin)
    unregister_class(OctaneScatterOnSurfaceInstanceCullingValueMax)
    unregister_class(OctaneScatterOnSurfaceInstanceCullingValueMin)
    unregister_class(OctaneScatterOnSurfaceInstanceCullingMap)
    unregister_class(OctaneScatterOnSurfaceInstanceCount)
    unregister_class(OctaneScatterOnSurfaceInstancePlacementSeed)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionHairSpacing)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionHairPosition)
    unregister_class(OctaneScatterOnSurfaceInstanceRelativeDensityMap)
    unregister_class(OctaneScatterOnSurfacePoissonDiskSampling)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionEdgeSpacing)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionEdgePosition)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionMethodHair)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionMethodParticles)
    unregister_class(OctaneScatterOnSurfaceInstanceDistributionMethod)
    unregister_class(OctaneScatterOnSurfaceInputSelectionMap)
    unregister_class(OctaneScatterOnSurfaceInputSelectionSeed)
    unregister_class(OctaneScatterOnSurfaceInputSelectionMethod)
    unregister_class(OctaneScatterOnSurfaceInput4)
    unregister_class(OctaneScatterOnSurfaceInput3)
    unregister_class(OctaneScatterOnSurfaceInput2)
    unregister_class(OctaneScatterOnSurfaceInput1)
    unregister_class(OctaneScatterOnSurfaceGeometry)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
