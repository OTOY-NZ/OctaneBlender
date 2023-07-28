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


class OctaneMixMaterialAmount(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialAmount"
    bl_label="Amount"
    color=consts.OctanePinColor.Texture
    octane_default_node_type=consts.NodeType.NT_TEX_FLOAT
    octane_default_node_name="OctaneGreyscaleColor"
    octane_pin_id=consts.PinID.P_AMOUNT
    octane_pin_name="amount"
    octane_pin_type=consts.PinType.PT_TEXTURE
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Mix amount", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMixMaterialMaterial1(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialMaterial1"
    bl_label="First material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL1
    octane_pin_name="material1"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMixMaterialMaterial2(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialMaterial2"
    bl_label="Second material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL2
    octane_pin_name="material2"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMixMaterialDisplacement(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialDisplacement"
    bl_label="Displacement"
    color=consts.OctanePinColor.Displacement
    octane_default_node_type=consts.NodeType.NT_UNKNOWN
    octane_default_node_name=""
    octane_pin_id=consts.PinID.P_DISPLACEMENT
    octane_pin_name="displacement"
    octane_pin_type=consts.PinType.PT_DISPLACEMENT
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=2000000
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneMixMaterialCustomAov(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialCustomAov"
    bl_label="Custom AOV"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV
    octane_pin_name="customAov"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_ENUM
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

class OctaneMixMaterialCustomAovChannel(OctaneBaseSocket):
    bl_idname="OctaneMixMaterialCustomAovChannel"
    bl_label="Custom AOV channel"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CUSTOM_AOV_CHANNEL
    octane_pin_name="customAovChannel"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_ENUM
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

class OctaneMixMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneMixMaterial"
    bl_label="Mix material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneMixMaterialAmount,OctaneMixMaterialMaterial1,OctaneMixMaterialMaterial2,OctaneMixMaterialDisplacement,OctaneMixMaterialCustomAov,OctaneMixMaterialCustomAovChannel,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_MAT_MIX
    octane_socket_list=["Amount", "First material", "Second material", "Displacement", "Custom AOV", "Custom AOV channel", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=6

    def init(self, context):
        self.inputs.new("OctaneMixMaterialAmount", OctaneMixMaterialAmount.bl_label).init()
        self.inputs.new("OctaneMixMaterialMaterial1", OctaneMixMaterialMaterial1.bl_label).init()
        self.inputs.new("OctaneMixMaterialMaterial2", OctaneMixMaterialMaterial2.bl_label).init()
        self.inputs.new("OctaneMixMaterialDisplacement", OctaneMixMaterialDisplacement.bl_label).init()
        self.inputs.new("OctaneMixMaterialCustomAov", OctaneMixMaterialCustomAov.bl_label).init()
        self.inputs.new("OctaneMixMaterialCustomAovChannel", OctaneMixMaterialCustomAovChannel.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneMixMaterialAmount,
    OctaneMixMaterialMaterial1,
    OctaneMixMaterialMaterial2,
    OctaneMixMaterialDisplacement,
    OctaneMixMaterialCustomAov,
    OctaneMixMaterialCustomAovChannel,
    OctaneMixMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
