##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneScatterInVolumeInput1(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInput1"
    bl_label = "Scattered object 1"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=527)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterInVolumeInput2(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInput2"
    bl_label = "Scattered object 2"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=528)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterInVolumeInput3(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInput3"
    bl_label = "Scattered object 3"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=573)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterInVolumeInput4(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInput4"
    bl_label = "Scattered object 4"
    color = (1.00, 0.74, 0.95, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=574)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=12)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneScatterInVolumeInputSelectionMethod(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInputSelectionMethod"
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

class OctaneScatterInVolumeInputSelectionSeed(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInputSelectionSeed"
    bl_label = "Object selection seed"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=576)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=3)
    default_value: IntProperty(default=0, description="Seed used to randomize the selection of source objects", min=0, max=2147483647, soft_min=0, soft_max=2147483647, step=1, subtype="NONE")

class OctaneScatterInVolumeInputSelectionMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInputSelectionMap"
    bl_label = "Object selection map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=577)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterInVolumeDimensions(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeDimensions"
    bl_label = "Dimension"
    color = (1.00, 0.84, 0.17, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=31)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=3)
    octane_socket_type: IntProperty(name="Socket Type", default=5)
    default_value: IntVectorProperty(default=(3, 3, 3), description="Number of instances along each dimension", min=1, max=1000, soft_min=1, soft_max=1000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeOffset(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeOffset"
    bl_label = "Offsets"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=122)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Offset between instances along each dimension", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeShape(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeShape"
    bl_label = "Shape"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=608)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Box", "Box", "", 0),
        ("Sphere", "Sphere", "", 1),
        ("Cylinder", "Cylinder", "", 2),
        ("Cone", "Cone", "", 3),
    ]
    default_value: EnumProperty(default="Box", description="", items=items)

class OctaneScatterInVolumeInstanceCullingMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceCullingMap"
    bl_label = "Culling map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=583)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterInVolumeInstanceCullingValueMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceCullingValueMin"
    bl_label = "Culling min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=584)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="All instances in areas of the map that have a value below this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterInVolumeInstanceCullingValueMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceCullingValueMax"
    bl_label = "Culling max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=585)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="All instances in areas of the map that have a value above this threshold are removed", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, subtype="FACTOR")

class OctaneScatterInVolumeInstanceOrientationPriority(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceOrientationPriority"
    bl_label = "Orientation priority"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=589)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=16)
    octane_socket_type: IntProperty(name="Socket Type", default=2)
    items = [
        ("Up", "Up", "", 0),
        ("Front", "Front", "", 1),
    ]
    default_value: EnumProperty(default="Up", description="If the up and front vector are not orthogonal, selects which one has priority", items=items)

class OctaneScatterInVolumeInstanceUpMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceUpMode"
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

class OctaneScatterInVolumeInstanceUpDirection(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceUpDirection"
    bl_label = "Reference up direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=591)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 1.000000, 0.000000), description="When up mode is set to Direction, the reference up vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceUpPoint(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceUpPoint"
    bl_label = "Reference up point"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=592)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="When up mode is set to Point, the reference up vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceFrontMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceFrontMode"
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

class OctaneScatterInVolumeInstanceFrontDirection(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceFrontDirection"
    bl_label = "Reference front direction"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=594)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 1.000000), description="When front mode is set to Direction, the reference front vector will point in this direction", min=-1.000000, max=1.000000, soft_min=-1.000000, soft_max=1.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceFrontPoint(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceFrontPoint"
    bl_label = "Reference front point"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=595)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="When front mode is set to Point, the reference front vector will point towards this location", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceRotationMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceRotationMode"
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

class OctaneScatterInVolumeInstanceRotationMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceRotationMin"
    bl_label = "Rotation min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=597)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Minimum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceRotationMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceRotationMax"
    bl_label = "Rotation max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=598)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Maximum rotation of the instance", min=-360.000000, max=360.000000, soft_min=-360.000000, soft_max=360.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceRotationStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceRotationStep"
    bl_label = "Rotation step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=609)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the rotation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterInVolumeInstanceRotationMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceRotationMap"
    bl_label = "Rotation map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=599)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterInVolumeInstanceScaleMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceScaleMode"
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

class OctaneScatterInVolumeInstanceScaleMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceScaleMin"
    bl_label = "Scale min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=601)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Minimum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceScaleMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceScaleMax"
    bl_label = "Scale max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=602)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(1.000000, 1.000000, 1.000000), description="Maximum scale of the instance", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceScaleStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceScaleStep"
    bl_label = "Scale step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=610)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the scale mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterInVolumeInstanceScaleMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceScaleMap"
    bl_label = "Scale map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=603)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterInVolumeInstanceTranslationMode(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceTranslationMode"
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

class OctaneScatterInVolumeInstanceTranslationMin(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceTranslationMin"
    bl_label = "Translation min"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=605)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Minimum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceTranslationMax(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceTranslationMax"
    bl_label = "Translation max"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=606)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=8)
    default_value: FloatVectorProperty(default=(0.000000, 0.000000, 0.000000), description="Maximum translation of the instance", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", size=3)

class OctaneScatterInVolumeInstanceTranslationStep(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceTranslationStep"
    bl_label = "Translation step"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=611)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.000000, description="When the translation mode is random or map and this value is different from zero the values will be aliased to the nearest step", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneScatterInVolumeInstanceTranslationMap(OctaneBaseSocket):
    bl_idname = "OctaneScatterInVolumeInstanceTranslationMap"
    bl_label = "Translation map"
    color = (0.75, 1.00, 0.87, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=607)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=5)
    octane_socket_type: IntProperty(name="Socket Type", default=11)
    
class OctaneScatterInVolume(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneScatterInVolume"
    bl_label = "Scatter in volume"
    octane_node_type: IntProperty(name="Octane Node Type", default=165)
    octane_socket_list: StringProperty(name="Socket List", default="Scattered object 1;Scattered object 2;Scattered object 3;Scattered object 4;Object selection method;Object selection seed;Object selection map;Dimension;Offsets;Shape;Culling map;Culling min;Culling max;Orientation priority;Up direction mode;Reference up direction;Reference up point;Front direction mode;Reference front direction;Reference front point;Rotation mode;Rotation min;Rotation max;Rotation step;Rotation map;Scale mode;Scale min;Scale max;Scale step;Scale map;Translation mode;Translation min;Translation max;Translation step;Translation map;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneScatterInVolumeInput1", OctaneScatterInVolumeInput1.bl_label)
        self.inputs.new("OctaneScatterInVolumeInput2", OctaneScatterInVolumeInput2.bl_label)
        self.inputs.new("OctaneScatterInVolumeInput3", OctaneScatterInVolumeInput3.bl_label)
        self.inputs.new("OctaneScatterInVolumeInput4", OctaneScatterInVolumeInput4.bl_label)
        self.inputs.new("OctaneScatterInVolumeInputSelectionMethod", OctaneScatterInVolumeInputSelectionMethod.bl_label)
        self.inputs.new("OctaneScatterInVolumeInputSelectionSeed", OctaneScatterInVolumeInputSelectionSeed.bl_label)
        self.inputs.new("OctaneScatterInVolumeInputSelectionMap", OctaneScatterInVolumeInputSelectionMap.bl_label)
        self.inputs.new("OctaneScatterInVolumeDimensions", OctaneScatterInVolumeDimensions.bl_label)
        self.inputs.new("OctaneScatterInVolumeOffset", OctaneScatterInVolumeOffset.bl_label)
        self.inputs.new("OctaneScatterInVolumeShape", OctaneScatterInVolumeShape.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceCullingMap", OctaneScatterInVolumeInstanceCullingMap.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceCullingValueMin", OctaneScatterInVolumeInstanceCullingValueMin.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceCullingValueMax", OctaneScatterInVolumeInstanceCullingValueMax.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceOrientationPriority", OctaneScatterInVolumeInstanceOrientationPriority.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceUpMode", OctaneScatterInVolumeInstanceUpMode.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceUpDirection", OctaneScatterInVolumeInstanceUpDirection.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceUpPoint", OctaneScatterInVolumeInstanceUpPoint.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceFrontMode", OctaneScatterInVolumeInstanceFrontMode.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceFrontDirection", OctaneScatterInVolumeInstanceFrontDirection.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceFrontPoint", OctaneScatterInVolumeInstanceFrontPoint.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMode", OctaneScatterInVolumeInstanceRotationMode.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMin", OctaneScatterInVolumeInstanceRotationMin.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMax", OctaneScatterInVolumeInstanceRotationMax.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceRotationStep", OctaneScatterInVolumeInstanceRotationStep.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceRotationMap", OctaneScatterInVolumeInstanceRotationMap.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMode", OctaneScatterInVolumeInstanceScaleMode.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMin", OctaneScatterInVolumeInstanceScaleMin.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMax", OctaneScatterInVolumeInstanceScaleMax.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceScaleStep", OctaneScatterInVolumeInstanceScaleStep.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceScaleMap", OctaneScatterInVolumeInstanceScaleMap.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMode", OctaneScatterInVolumeInstanceTranslationMode.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMin", OctaneScatterInVolumeInstanceTranslationMin.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMax", OctaneScatterInVolumeInstanceTranslationMax.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationStep", OctaneScatterInVolumeInstanceTranslationStep.bl_label)
        self.inputs.new("OctaneScatterInVolumeInstanceTranslationMap", OctaneScatterInVolumeInstanceTranslationMap.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneScatterInVolumeInput1)
    register_class(OctaneScatterInVolumeInput2)
    register_class(OctaneScatterInVolumeInput3)
    register_class(OctaneScatterInVolumeInput4)
    register_class(OctaneScatterInVolumeInputSelectionMethod)
    register_class(OctaneScatterInVolumeInputSelectionSeed)
    register_class(OctaneScatterInVolumeInputSelectionMap)
    register_class(OctaneScatterInVolumeDimensions)
    register_class(OctaneScatterInVolumeOffset)
    register_class(OctaneScatterInVolumeShape)
    register_class(OctaneScatterInVolumeInstanceCullingMap)
    register_class(OctaneScatterInVolumeInstanceCullingValueMin)
    register_class(OctaneScatterInVolumeInstanceCullingValueMax)
    register_class(OctaneScatterInVolumeInstanceOrientationPriority)
    register_class(OctaneScatterInVolumeInstanceUpMode)
    register_class(OctaneScatterInVolumeInstanceUpDirection)
    register_class(OctaneScatterInVolumeInstanceUpPoint)
    register_class(OctaneScatterInVolumeInstanceFrontMode)
    register_class(OctaneScatterInVolumeInstanceFrontDirection)
    register_class(OctaneScatterInVolumeInstanceFrontPoint)
    register_class(OctaneScatterInVolumeInstanceRotationMode)
    register_class(OctaneScatterInVolumeInstanceRotationMin)
    register_class(OctaneScatterInVolumeInstanceRotationMax)
    register_class(OctaneScatterInVolumeInstanceRotationStep)
    register_class(OctaneScatterInVolumeInstanceRotationMap)
    register_class(OctaneScatterInVolumeInstanceScaleMode)
    register_class(OctaneScatterInVolumeInstanceScaleMin)
    register_class(OctaneScatterInVolumeInstanceScaleMax)
    register_class(OctaneScatterInVolumeInstanceScaleStep)
    register_class(OctaneScatterInVolumeInstanceScaleMap)
    register_class(OctaneScatterInVolumeInstanceTranslationMode)
    register_class(OctaneScatterInVolumeInstanceTranslationMin)
    register_class(OctaneScatterInVolumeInstanceTranslationMax)
    register_class(OctaneScatterInVolumeInstanceTranslationStep)
    register_class(OctaneScatterInVolumeInstanceTranslationMap)
    register_class(OctaneScatterInVolume)

def unregister():
    unregister_class(OctaneScatterInVolume)
    unregister_class(OctaneScatterInVolumeInstanceTranslationMap)
    unregister_class(OctaneScatterInVolumeInstanceTranslationStep)
    unregister_class(OctaneScatterInVolumeInstanceTranslationMax)
    unregister_class(OctaneScatterInVolumeInstanceTranslationMin)
    unregister_class(OctaneScatterInVolumeInstanceTranslationMode)
    unregister_class(OctaneScatterInVolumeInstanceScaleMap)
    unregister_class(OctaneScatterInVolumeInstanceScaleStep)
    unregister_class(OctaneScatterInVolumeInstanceScaleMax)
    unregister_class(OctaneScatterInVolumeInstanceScaleMin)
    unregister_class(OctaneScatterInVolumeInstanceScaleMode)
    unregister_class(OctaneScatterInVolumeInstanceRotationMap)
    unregister_class(OctaneScatterInVolumeInstanceRotationStep)
    unregister_class(OctaneScatterInVolumeInstanceRotationMax)
    unregister_class(OctaneScatterInVolumeInstanceRotationMin)
    unregister_class(OctaneScatterInVolumeInstanceRotationMode)
    unregister_class(OctaneScatterInVolumeInstanceFrontPoint)
    unregister_class(OctaneScatterInVolumeInstanceFrontDirection)
    unregister_class(OctaneScatterInVolumeInstanceFrontMode)
    unregister_class(OctaneScatterInVolumeInstanceUpPoint)
    unregister_class(OctaneScatterInVolumeInstanceUpDirection)
    unregister_class(OctaneScatterInVolumeInstanceUpMode)
    unregister_class(OctaneScatterInVolumeInstanceOrientationPriority)
    unregister_class(OctaneScatterInVolumeInstanceCullingValueMax)
    unregister_class(OctaneScatterInVolumeInstanceCullingValueMin)
    unregister_class(OctaneScatterInVolumeInstanceCullingMap)
    unregister_class(OctaneScatterInVolumeShape)
    unregister_class(OctaneScatterInVolumeOffset)
    unregister_class(OctaneScatterInVolumeDimensions)
    unregister_class(OctaneScatterInVolumeInputSelectionMap)
    unregister_class(OctaneScatterInVolumeInputSelectionSeed)
    unregister_class(OctaneScatterInVolumeInputSelectionMethod)
    unregister_class(OctaneScatterInVolumeInput4)
    unregister_class(OctaneScatterInVolumeInput3)
    unregister_class(OctaneScatterInVolumeInput2)
    unregister_class(OctaneScatterInVolumeInput1)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
