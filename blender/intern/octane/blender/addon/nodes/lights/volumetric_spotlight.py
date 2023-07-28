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


class OctaneVolumetricSpotlightThrowDistance(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightThrowDistance"
    bl_label="Throw distance"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_THROW_DISTANCE
    octane_pin_name="throwDistance"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightConeWidth(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightConeWidth"
    bl_label="Cone width"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_CONE_WIDTH
    octane_pin_name="coneWidth"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightHardness(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightHardness"
    bl_label="Cone hardness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_HARDNESS
    octane_pin_name="hardness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.700000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=12000004
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightMedium(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightMedium"
    bl_label="Light medium"
    color=consts.OctanePinColor.Medium
    octane_default_node_type=consts.NodeType.NT_MED_SCATTERING
    octane_default_node_name="OctaneScattering"
    octane_pin_id=consts.PinID.P_MEDIUM
    octane_pin_name="medium"
    octane_pin_type=consts.PinType.PT_MEDIUM
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightEmitterMaterial(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightEmitterMaterial"
    bl_label="Emitter material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_EMITTER_MATERIAL
    octane_pin_name="emitterMaterial"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoorsMaterial(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoorsMaterial"
    bl_label="Barn doors material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_BARN_DOORS_MATERIAL
    octane_pin_name="barnDoorsMaterial"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id=consts.PinID.P_OBJECT_LAYER
    octane_pin_name="objectLayer"
    octane_pin_type=consts.PinType.PT_OBJECTLAYER
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightTransform(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightTransform"
    bl_label="Light transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightEnableBarnDoors(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightEnableBarnDoors"
    bl_label="Enable barn doors"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_ENABLE_BARN_DOORS
    octane_pin_name="enableBarnDoors"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoorsSize(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoorsSize"
    bl_label="Barn doors size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BARN_DOORS_SIZE
    octane_pin_name="barnDoorsSize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.080000, update=OctaneBaseSocket.update_node_tree, description="", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor1Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor1Angle"
    bl_label="Barn door 1 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BARN_DOOR_1_ANGLE
    octane_pin_name="barnDoor1Angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor2Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor2Angle"
    bl_label="Barn door 2 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BARN_DOOR_2_ANGLE
    octane_pin_name="barnDoor2Angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor3Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor3Angle"
    bl_label="Barn door 3 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BARN_DOOR_3_ANGLE
    octane_pin_name="barnDoor3Angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightBarnDoor4Angle(OctaneBaseSocket):
    bl_idname="OctaneVolumetricSpotlightBarnDoor4Angle"
    bl_label="Barn door 4 angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_BARN_DOOR_4_ANGLE
    octane_pin_name="barnDoor4Angle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.750000, update=OctaneBaseSocket.update_node_tree, description="", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-1.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVolumetricSpotlightGroupBarnDoors(OctaneGroupTitleSocket):
    bl_idname="OctaneVolumetricSpotlightGroupBarnDoors"
    bl_label="[OctaneGroupTitle]Barn doors"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Enable barn doors;Barn doors size;Barn door 1 angle;Barn door 2 angle;Barn door 3 angle;Barn door 4 angle;")

class OctaneVolumetricSpotlight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneVolumetricSpotlight"
    bl_label="Volumetric spotlight"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneVolumetricSpotlightThrowDistance,OctaneVolumetricSpotlightConeWidth,OctaneVolumetricSpotlightHardness,OctaneVolumetricSpotlightMedium,OctaneVolumetricSpotlightEmitterMaterial,OctaneVolumetricSpotlightBarnDoorsMaterial,OctaneVolumetricSpotlightObjectLayer,OctaneVolumetricSpotlightTransform,OctaneVolumetricSpotlightGroupBarnDoors,OctaneVolumetricSpotlightEnableBarnDoors,OctaneVolumetricSpotlightBarnDoorsSize,OctaneVolumetricSpotlightBarnDoor1Angle,OctaneVolumetricSpotlightBarnDoor2Angle,OctaneVolumetricSpotlightBarnDoor3Angle,OctaneVolumetricSpotlightBarnDoor4Angle,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_LIGHT_VOLUME_SPOT
    octane_socket_list=["Throw distance", "Cone width", "Cone hardness", "Light medium", "Emitter material", "Barn doors material", "Object layer", "Light transform", "Enable barn doors", "Barn doors size", "Barn door 1 angle", "Barn door 2 angle", "Barn door 3 angle", "Barn door 4 angle", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=14

    def init(self, context):
        self.inputs.new("OctaneVolumetricSpotlightThrowDistance", OctaneVolumetricSpotlightThrowDistance.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightConeWidth", OctaneVolumetricSpotlightConeWidth.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightHardness", OctaneVolumetricSpotlightHardness.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightMedium", OctaneVolumetricSpotlightMedium.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightEmitterMaterial", OctaneVolumetricSpotlightEmitterMaterial.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsMaterial", OctaneVolumetricSpotlightBarnDoorsMaterial.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightObjectLayer", OctaneVolumetricSpotlightObjectLayer.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightTransform", OctaneVolumetricSpotlightTransform.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightGroupBarnDoors", OctaneVolumetricSpotlightGroupBarnDoors.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightEnableBarnDoors", OctaneVolumetricSpotlightEnableBarnDoors.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoorsSize", OctaneVolumetricSpotlightBarnDoorsSize.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor1Angle", OctaneVolumetricSpotlightBarnDoor1Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor2Angle", OctaneVolumetricSpotlightBarnDoor2Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor3Angle", OctaneVolumetricSpotlightBarnDoor3Angle.bl_label).init()
        self.inputs.new("OctaneVolumetricSpotlightBarnDoor4Angle", OctaneVolumetricSpotlightBarnDoor4Angle.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneVolumetricSpotlightThrowDistance,
    OctaneVolumetricSpotlightConeWidth,
    OctaneVolumetricSpotlightHardness,
    OctaneVolumetricSpotlightMedium,
    OctaneVolumetricSpotlightEmitterMaterial,
    OctaneVolumetricSpotlightBarnDoorsMaterial,
    OctaneVolumetricSpotlightObjectLayer,
    OctaneVolumetricSpotlightTransform,
    OctaneVolumetricSpotlightEnableBarnDoors,
    OctaneVolumetricSpotlightBarnDoorsSize,
    OctaneVolumetricSpotlightBarnDoor1Angle,
    OctaneVolumetricSpotlightBarnDoor2Angle,
    OctaneVolumetricSpotlightBarnDoor3Angle,
    OctaneVolumetricSpotlightBarnDoor4Angle,
    OctaneVolumetricSpotlightGroupBarnDoors,
    OctaneVolumetricSpotlight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
import math

class OctaneVolumetricSpotlight_Override(OctaneVolumetricSpotlight):
    items = [
        ("Automatic", "Automatic", "Calculate the cone width from the shape in the OpenGL viewport", 0),
        ("Manual", "Manual", "Set the cone width in the node manually", 1),
    ]
    source_type: EnumProperty(name="Cone Width Source type", default="Automatic", update=OctaneBaseNode.update_node_tree, description="Determines the data source type of the cone width", items=items)    

    def init(self, context):
        super().init(context)
        self.inputs[OctaneVolumetricSpotlightObjectLayer.bl_label].hide = True
        self.inputs[OctaneVolumetricSpotlightTransform.bl_label].hide = True

    def draw_buttons(self, context, layout):
        layout.row().prop(self, "source_type")

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        super().sync_custom_data(octane_node, octane_graph_node_data, depsgraph)
        transform_node_name = octane_node.name + "[Transform]"
        _3d_transform_node = octane_node.get_subnode(transform_node_name, consts.NodeType.NT_TRANSFORM_3D)
        rotation = [90, 0, 0]        
        _3d_transform_node.set_pin_id(consts.PinID.P_ROTATION, False, "", rotation)
        octane_node.set_pin_id(consts.PinID.P_TRANSFORM, True, transform_node_name, "")
        if self.source_type == "Manual":
            return
        spotlight = None
        for light in bpy.data.lights:
            if light.type == "SPOT" and light.node_tree is self.id_data.original:
                spotlight = light.evaluated_get(depsgraph)
                break
        if spotlight is not None:
            distance = self.inputs[OctaneVolumetricSpotlightThrowDistance.bl_label].default_value
            cone_size_socket = self.inputs[OctaneVolumetricSpotlightConeWidth.bl_label]
            try:
                cone_size = max(0, math.tan(spotlight.spot_size / 2) * distance)
            except:
                cone_size = 0
            octane_node.set_pin_id(consts.PinID.P_CONE_WIDTH, False, "", cone_size)


utility.override_class(_CLASSES, OctaneVolumetricSpotlight, OctaneVolumetricSpotlight_Override)