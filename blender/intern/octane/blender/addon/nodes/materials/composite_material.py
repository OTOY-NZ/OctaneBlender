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


class OctaneCompositeMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneCompositeMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=34)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="displacement")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneCompositeMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=632)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="customAov")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None", "None", "", 4096),
        ("Custom AOV 1", "Custom AOV 1", "", 0),
        ("Custom AOV 2", "Custom AOV 2", "", 1),
        ("Custom AOV 3", "Custom AOV 3", "", 2),
        ("Custom AOV 4", "Custom AOV 4", "", 3),
        ("Custom AOV 5", "Custom AOV 5", "", 4),
        ("Custom AOV 6", "Custom AOV 6", "", 5),
        ("Custom AOV 7", "Custom AOV 7", "", 6),
        ("Custom AOV 8", "Custom AOV 8", "", 7),
        ("Custom AOV 9", "Custom AOV 9", "", 8),
        ("Custom AOV 10", "Custom AOV 10", "", 9),
        ("Custom AOV 11", "Custom AOV 11", "", 10),
        ("Custom AOV 12", "Custom AOV 12", "", 11),
        ("Custom AOV 13", "Custom AOV 13", "", 12),
        ("Custom AOV 14", "Custom AOV 14", "", 13),
        ("Custom AOV 15", "Custom AOV 15", "", 14),
        ("Custom AOV 16", "Custom AOV 16", "", 15),
        ("Custom AOV 17", "Custom AOV 17", "", 16),
        ("Custom AOV 18", "Custom AOV 18", "", 17),
        ("Custom AOV 19", "Custom AOV 19", "", 18),
        ("Custom AOV 20", "Custom AOV 20", "", 19),
    ]
    default_value: EnumProperty(default="None", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, it will write a mask to it where the material is visible", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneCompositeMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=57
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=633)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="customAovChannel")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("All", "All", "", 0),
        ("Red", "Red", "", 1),
        ("Green", "Green", "", 2),
        ("Blue", "Blue", "", 3),
    ]
    default_value: EnumProperty(default="All", update=OctaneBaseSocket.update_node_tree, description="If a custom AOV is selected, the selected channel(s) will receive the mask", items=items)
    octane_hide_value=False
    octane_min_version=11000002
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCompositeMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCompositeMaterial"
    bl_label="Composite material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=138)
    octane_socket_list: StringProperty(name="Socket List", default="Displacement;Custom AOV;Custom AOV channel;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_material_count;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    a_material_count: IntProperty(name="Material count", default=0, update=OctaneBaseNode.update_node_tree, description="The number of materials to mix. Two pins per new material are created and appended to the end")

    def init(self, context):
        self.inputs.new("OctaneCompositeMaterialDisplacement", OctaneCompositeMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneCompositeMaterialCustomAov", OctaneCompositeMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneCompositeMaterialCustomAovChannel", OctaneCompositeMaterialCustomAovChannel.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_CLASSES=[
    OctaneCompositeMaterialDisplacement,
    OctaneCompositeMaterialCustomAov,
    OctaneCompositeMaterialCustomAovChannel,
    OctaneCompositeMaterial,
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
from ..base_socket import OctanePatternInput


class OctaneCompositeMaterialMaterialMaskMovableInput(OctanePatternInput):
    bl_idname="OctaneCompositeMaterialMaterialMaskMovableInput"
    bl_label="Material Mask"
    octane_input_pattern=r"Material \d+ mask"
    octane_input_format_pattern="Material {} mask"
    color=consts.OctanePinColor.Texture
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneCompositeMaterialMaterialMovableInput(OctaneMovableInput):
    bl_idname="OctaneCompositeMaterialMaterialMovableInput"
    bl_label="Material"
    octane_movable_input_count_attribute_name="a_material_count"
    octane_input_pattern=r"Material \d+"
    octane_input_format_pattern="Material {}"
    octane_sub_movable_inputs=[OctaneCompositeMaterialMaterialMaskMovableInput, ]
    color=consts.OctanePinColor.Material
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneCompositeMaterial_Override(OctaneCompositeMaterial):
    MAX_MATERIAL_COUNT = 16
    DEFAULT_MATERIAL_COUNT = 2

    def init(self, context):
        super().init(context)
        self.init_movable_inputs(context, OctaneCompositeMaterialMaterialMovableInput, self.DEFAULT_MATERIAL_COUNT)

    def draw_buttons(self, context, layout):
        self.draw_movable_inputs(context, layout, OctaneCompositeMaterialMaterialMovableInput, self.MAX_MATERIAL_COUNT)


_ADDED_CLASSES = [OctaneCompositeMaterialMaterialMaskMovableInput, OctaneCompositeMaterialMaterialMovableInput, ]
_CLASSES = _ADDED_CLASSES + _CLASSES
utility.override_class(_CLASSES, OctaneCompositeMaterial, OctaneCompositeMaterial_Override)   