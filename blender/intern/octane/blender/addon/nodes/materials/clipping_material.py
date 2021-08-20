##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneClippingMaterialEnabled(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=None, description="If true, geometries located inside the clipping material will be clipped away")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneClippingMaterialIntersectionMaterial(OctaneBaseSocket):
    bl_idname="OctaneClippingMaterialIntersectionMaterial"
    bl_label="Intersection"
    color=consts.OctanePinColor.Material
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=658)
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
    octane_default_node_type="OctaneIntValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=564)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_INT)
    default_value: IntProperty(default=100, update=None, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=11000001
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
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;Intersection;Priority;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneClippingMaterialEnabled", OctaneClippingMaterialEnabled.bl_label).init()
        self.inputs.new("OctaneClippingMaterialIntersectionMaterial", OctaneClippingMaterialIntersectionMaterial.bl_label).init()
        self.inputs.new("OctaneClippingMaterialPriority", OctaneClippingMaterialPriority.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()


_classes=[
    OctaneClippingMaterialEnabled,
    OctaneClippingMaterialIntersectionMaterial,
    OctaneClippingMaterialPriority,
    OctaneClippingMaterial,
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
