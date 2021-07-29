##### BEGIN OCTANE AUTO GENERATED CODE BLOCK #####
import bpy
from bpy.utils import register_class, unregister_class
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket


class OctaneVolumetricSpotlightThrowDistance(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightThrowDistance"
    bl_label = "Throw distance"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=516)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=1.000000, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneVolumetricSpotlightConeWidth(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightConeWidth"
    bl_label = "Cone width"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=517)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.500000, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneVolumetricSpotlightMedium(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightMedium"
    bl_label = "Light medium"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=110)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=13)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumetricSpotlightEmitterMaterial(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightEmitterMaterial"
    bl_label = "Emitter material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=518)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumetricSpotlightBarnDoorsMaterial(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoorsMaterial"
    bl_label = "Barn doors material"
    color = (1.00, 0.95, 0.74, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=519)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=7)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumetricSpotlightObjectLayer(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightObjectLayer"
    bl_label = "Object layer"
    color = (1.00, 1.00, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=328)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=17)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumetricSpotlightTransform(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightTransform"
    bl_label = "Light transform"
    color = (0.75, 0.87, 1.00, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=243)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=4)
    octane_socket_type: IntProperty(name="Socket Type", default=11)

class OctaneVolumetricSpotlightEnableBarnDoors(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightEnableBarnDoors"
    bl_label = "Enable barn doors"
    color = (0.87, 0.66, 0.83, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=520)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=1)
    octane_socket_type: IntProperty(name="Socket Type", default=1)
    default_value: BoolProperty(default=True, description="")

class OctaneVolumetricSpotlightBarnDoorsSize(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoorsSize"
    bl_label = "Barn doors size"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=521)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.080000, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE")

class OctaneVolumetricSpotlightBarnDoor1Angle(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoor1Angle"
    bl_label = "Barn door 1 angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=522)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneVolumetricSpotlightBarnDoor2Angle(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoor2Angle"
    bl_label = "Barn door 2 angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=523)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneVolumetricSpotlightBarnDoor3Angle(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoor3Angle"
    bl_label = "Barn door 3 angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=524)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneVolumetricSpotlightBarnDoor4Angle(OctaneBaseSocket):
    bl_idname = "OctaneVolumetricSpotlightBarnDoor4Angle"
    bl_label = "Barn door 4 angle"
    color = (0.50, 0.70, 0.90, 0.70)
    octane_pin_id: IntProperty(name="Octane Pin ID", default=525)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=2)
    octane_socket_type: IntProperty(name="Socket Type", default=6)
    default_value: FloatProperty(default=0.750000, description="", min=-340282346638528859811704183484516925440.000000, max=1.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="FACTOR")

class OctaneVolumetricSpotlight(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneVolumetricSpotlight"
    bl_label = "Volumetric spotlight"
    octane_node_type: IntProperty(name="Octane Node Type", default=152)
    octane_socket_list: StringProperty(name="Socket List", default="Throw distance;Cone width;Light medium;Emitter material;Barn doors material;Object layer;Light transform;Enable barn doors;Barn doors size;Barn door 1 angle;Barn door 2 angle;Barn door 3 angle;Barn door 4 angle;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    bl_width_default = 160

    def init(self, context):
        self.inputs.new("OctaneVolumetricSpotlightThrowDistance", OctaneVolumetricSpotlightThrowDistance.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightConeWidth", OctaneVolumetricSpotlightConeWidth.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightMedium", OctaneVolumetricSpotlightMedium.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightEmitterMaterial", OctaneVolumetricSpotlightEmitterMaterial.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsMaterial", OctaneVolumetricSpotlightBarnDoorsMaterial.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightObjectLayer", OctaneVolumetricSpotlightObjectLayer.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightTransform", OctaneVolumetricSpotlightTransform.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightEnableBarnDoors", OctaneVolumetricSpotlightEnableBarnDoors.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsSize", OctaneVolumetricSpotlightBarnDoorsSize.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor1Angle", OctaneVolumetricSpotlightBarnDoor1Angle.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor2Angle", OctaneVolumetricSpotlightBarnDoor2Angle.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor3Angle", OctaneVolumetricSpotlightBarnDoor3Angle.bl_label)
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor4Angle", OctaneVolumetricSpotlightBarnDoor4Angle.bl_label)
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out")


def register():
    register_class(OctaneVolumetricSpotlightThrowDistance)
    register_class(OctaneVolumetricSpotlightConeWidth)
    register_class(OctaneVolumetricSpotlightMedium)
    register_class(OctaneVolumetricSpotlightEmitterMaterial)
    register_class(OctaneVolumetricSpotlightBarnDoorsMaterial)
    register_class(OctaneVolumetricSpotlightObjectLayer)
    register_class(OctaneVolumetricSpotlightTransform)
    register_class(OctaneVolumetricSpotlightEnableBarnDoors)
    register_class(OctaneVolumetricSpotlightBarnDoorsSize)
    register_class(OctaneVolumetricSpotlightBarnDoor1Angle)
    register_class(OctaneVolumetricSpotlightBarnDoor2Angle)
    register_class(OctaneVolumetricSpotlightBarnDoor3Angle)
    register_class(OctaneVolumetricSpotlightBarnDoor4Angle)
    register_class(OctaneVolumetricSpotlight)

def unregister():
    unregister_class(OctaneVolumetricSpotlight)
    unregister_class(OctaneVolumetricSpotlightBarnDoor4Angle)
    unregister_class(OctaneVolumetricSpotlightBarnDoor3Angle)
    unregister_class(OctaneVolumetricSpotlightBarnDoor2Angle)
    unregister_class(OctaneVolumetricSpotlightBarnDoor1Angle)
    unregister_class(OctaneVolumetricSpotlightBarnDoorsSize)
    unregister_class(OctaneVolumetricSpotlightEnableBarnDoors)
    unregister_class(OctaneVolumetricSpotlightTransform)
    unregister_class(OctaneVolumetricSpotlightObjectLayer)
    unregister_class(OctaneVolumetricSpotlightBarnDoorsMaterial)
    unregister_class(OctaneVolumetricSpotlightEmitterMaterial)
    unregister_class(OctaneVolumetricSpotlightMedium)
    unregister_class(OctaneVolumetricSpotlightConeWidth)
    unregister_class(OctaneVolumetricSpotlightThrowDistance)

##### END OCTANE AUTO GENERATED CODE BLOCK #####
