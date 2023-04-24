##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneWCoordinateTranslation(OctaneBaseSocket):
    bl_idname="OctaneWCoordinateTranslation"
    bl_label="Translation"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=244)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000000, update=None, description="Translation", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWCoordinateScale(OctaneBaseSocket):
    bl_idname="OctaneWCoordinateScale"
    bl_label="Scale"
    color=consts.OctanePinColor.Float
    octane_default_node_type="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=209)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=None, description="Scale", min=0.001000, max=1000.000000, soft_min=0.001000, soft_max=1000.000000, step=1, precision=3, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWCoordinateBorderModeWCoord(OctaneBaseSocket):
    bl_idname="OctaneWCoordinateBorderModeWCoord"
    bl_label="Border mode"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=699)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 0),
        ("Wrap around", "Wrap around", "", 1),
        ("Mirror", "Mirror", "", 2),
        ("Clamp value", "Clamp value", "", 3),
    ]
    default_value: EnumProperty(default="None", update=None, description="Determines the lookup behavior when the W coordinate falls outside of [0,1]", items=items)
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWCoordinateInvert(OctaneBaseSocket):
    bl_idname="OctaneWCoordinateInvert"
    bl_label="Invert"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=83)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=None, description="Invert")
    octane_hide_value=False
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneWCoordinate(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneWCoordinate"
    bl_label="W coordinate"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=104)
    octane_socket_list: StringProperty(name="Socket List", default="Translation;Scale;Border mode;Invert;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=4)

    def init(self, context):
        self.inputs.new("OctaneWCoordinateTranslation", OctaneWCoordinateTranslation.bl_label).init()
        self.inputs.new("OctaneWCoordinateScale", OctaneWCoordinateScale.bl_label).init()
        self.inputs.new("OctaneWCoordinateBorderModeWCoord", OctaneWCoordinateBorderModeWCoord.bl_label).init()
        self.inputs.new("OctaneWCoordinateInvert", OctaneWCoordinateInvert.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneWCoordinateTranslation,
    OctaneWCoordinateScale,
    OctaneWCoordinateBorderModeWCoord,
    OctaneWCoordinateInvert,
    OctaneWCoordinate,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
