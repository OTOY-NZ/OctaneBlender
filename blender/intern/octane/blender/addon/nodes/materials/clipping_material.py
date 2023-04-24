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


class OctaneClippingMaterialEnabled(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="enabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If true, geometries located inside the clipping material will be clipped away")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterialIntersectionMaterial(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialIntersectionMaterial"
    bl_label="Intersection"
    color=consts.OctanePinColor.Material
    octane_default_node_type=0
    octane_default_node_name=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=658)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="intersectionMaterial")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=11000003
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterialPriority(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialPriority"
    bl_label="Priority"
    color=consts.OctanePinColor.Int
    octane_default_node_type=9
    octane_default_node_name="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="priority")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=100, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000001
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterialRayepsilon(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialRayepsilon"
    bl_label="Custom ray epsilon"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=144)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rayepsilon")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Clipping material offset distance", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=11000014
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterialRayEpsilonCustomEnabled(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialRayEpsilonCustomEnabled"
    bl_label="Custom ray epsilon enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=11
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=744)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="rayEpsilonCustomEnabled")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If true, the clipping material uses the specified custom ray epsilon instead of the global ray epsilon in kernel node")
    octane_hide_value=False
    octane_min_version=11000014
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneClippingMaterial"
    bl_label="Clipping material"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=178)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Intersection;Priority;Custom ray epsilon;Custom ray epsilon enabled;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_name_list: StringProperty(name="Attribute Name List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=5)

    def init(self, context):
        self.inputs.new("OctaneClippingMaterialEnabled", OctaneClippingMaterialEnabled.bl_label).init()
        self.inputs.new("OctaneClippingMaterialIntersectionMaterial", OctaneClippingMaterialIntersectionMaterial.bl_label).init()
        self.inputs.new("OctaneClippingMaterialPriority", OctaneClippingMaterialPriority.bl_label).init()
        self.inputs.new("OctaneClippingMaterialRayepsilon", OctaneClippingMaterialRayepsilon.bl_label).init()
        self.inputs.new("OctaneClippingMaterialRayEpsilonCustomEnabled", OctaneClippingMaterialRayEpsilonCustomEnabled.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_CLASSES=[
    OctaneClippingMaterialEnabled,
    OctaneClippingMaterialIntersectionMaterial,
    OctaneClippingMaterialPriority,
    OctaneClippingMaterialRayepsilon,
    OctaneClippingMaterialRayEpsilonCustomEnabled,
    OctaneClippingMaterial,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
