##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCompositeTextureClamp(OctaneBaseSocket):
    bl_idname="OctaneCompositeTextureClamp"
    bl_label="Clamp"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=628)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="Clamp the result of blending each layer to [0,1] (ignored when used as a normal map)")
    octane_hide_value=False
    octane_min_version=10020600
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeTexture(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCompositeTexture"
    bl_label="Composite texture"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=176)
    octane_socket_list: StringProperty(name="Socket List", default="Clamp;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_layer_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    a_layer_count: IntProperty(name="Layer count", default=0, update=None, description="The number of layers. Changing this value and evaluating the node will update the number of layers. New layers will be added to the front of the dynamic pin list")

    def init(self, context):
        self.inputs.new("OctaneCompositeTextureClamp", OctaneCompositeTextureClamp.bl_label).init()
        self.outputs.new("OctaneTextureOutSocket", "Texture out").init()


_CLASSES=[
    OctaneCompositeTextureClamp,
    OctaneCompositeTexture,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####

from ...utils import utility


class OctaneCompositeTextureMovableTextureLayerInput(OctaneMovableInput):
    bl_idname="OctaneCompositeTextureMovableTextureLayerInput"
    bl_label="Layer"
    octane_movable_input_count_attribute_name="a_layer_count"
    octane_input_pattern=r"Layer \d+"
    octane_input_format_pattern="Layer {}"
    octane_reversed_input_sockets=True
    color=consts.OctanePinColor.CompositeTextureLayer
    octane_default_node_type="OctaneCompositeTextureLayer"
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)    


class OctaneCompositeTextureGroupTextureLayers(OctaneGroupTitleMovableInputs):
    bl_idname="OctaneCompositeTextureGroupTextureLayers"
    bl_label="[OctaneGroupTitle]Layer"
    octane_group_sockets: StringProperty(name="Group Sockets", default="")


class OctaneCompositeTexture_Override(OctaneCompositeTexture):
    MAX_LAYER_COUNT = 16
    DEFAULT_LAYER_COUNT = 2   

    def init(self, context):
        super().init(context)
        self.inputs.new("OctaneCompositeTextureGroupTextureLayers", OctaneCompositeTextureGroupTextureLayers.bl_label).init(cls=OctaneCompositeTextureMovableTextureLayerInput, max_num=self.MAX_LAYER_COUNT)        
        self.init_movable_inputs(context, OctaneCompositeTextureMovableTextureLayerInput, self.DEFAULT_LAYER_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneCompositeTextureMovableTextureLayerInput, self.MAX_LAYER_COUNT)


_ADDED_CLASSES = [OctaneCompositeTextureMovableTextureLayerInput, OctaneCompositeTextureGroupTextureLayers]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneCompositeTexture, OctaneCompositeTexture_Override)    