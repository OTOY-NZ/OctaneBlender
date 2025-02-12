# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom  # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_lut import OctaneBaseLutNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneClippingMaterialEnabled(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialEnabled"
    bl_label = "Enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_ENABLED
    octane_pin_name = "enabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If true, geometries located inside the clipping material will be clipped away")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterialShadingEnabled(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialShadingEnabled"
    bl_label = "Shading enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_SHADING_ENABLED
    octane_pin_name = "shadingEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="If true, the clipping material will try to shade the gap with the material it has clipped or the intersection material,otherwise the clipping material will just leave the gap unfilled")
    octane_hide_value = False
    octane_min_version = 11000400
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterialIntersectionMaterial(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialIntersectionMaterial"
    bl_label = "Intersection"
    color = consts.OctanePinColor.Material
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_INTERSECTION_MATERIAL
    octane_pin_name = "intersectionMaterial"
    octane_pin_type = consts.PinType.PT_MATERIAL
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 11000003
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterialPriority(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialPriority"
    bl_label = "Priority"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_INT
    octane_default_node_name = "OctaneIntValue"
    octane_pin_id = consts.PinID.P_PRIORITY
    octane_pin_name = "priority"
    octane_pin_type = consts.PinType.PT_INT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_INT
    default_value: IntProperty(default=100, update=OctaneBaseSocket.update_node_tree, description="The material priority for this surface material", min=-100, max=100, soft_min=-100, soft_max=100, step=1, subtype=runtime_globals.FACTOR_PROPERTY_SUBTYPE)
    octane_hide_value = False
    octane_min_version = 11000001
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterialRayepsilon(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialRayepsilon"
    bl_label = "Custom ray epsilon"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_RAY_EPSILON
    octane_pin_name = "rayepsilon"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.000100, update=OctaneBaseSocket.update_node_tree, description="Clipping material offset distance", min=0.000000, max=1000.000000, soft_min=0.000001, soft_max=0.100000, step=0.000100, precision=4, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 11000014
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterialRayEpsilonCustomEnabled(OctaneBaseSocket):
    bl_idname = "OctaneClippingMaterialRayEpsilonCustomEnabled"
    bl_label = "Custom ray epsilon enabled"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_BOOL
    octane_default_node_name = "OctaneBoolValue"
    octane_pin_id = consts.PinID.P_RAY_EPSILON_CUSTOM_ENABLED
    octane_pin_name = "rayEpsilonCustomEnabled"
    octane_pin_type = consts.PinType.PT_BOOL
    octane_pin_index = 5
    octane_socket_type = consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="If true, the clipping material uses the specified custom ray epsilon instead of the global ray epsilon in kernel node")
    octane_hide_value = False
    octane_min_version = 11000014
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneClippingMaterial(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneClippingMaterial"
    bl_label = "Clipping material"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneClippingMaterialEnabled, OctaneClippingMaterialShadingEnabled, OctaneClippingMaterialIntersectionMaterial, OctaneClippingMaterialPriority, OctaneClippingMaterialRayepsilon, OctaneClippingMaterialRayEpsilonCustomEnabled, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_MAT_CLIPPING
    octane_socket_list = ["Enabled", "Shading enabled", "Intersection", "Priority", "Custom ray epsilon", "Custom ray epsilon enabled", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 6

    def init(self, context):  # noqa
        self.inputs.new("OctaneClippingMaterialEnabled", OctaneClippingMaterialEnabled.bl_label).init()
        self.inputs.new("OctaneClippingMaterialShadingEnabled", OctaneClippingMaterialShadingEnabled.bl_label).init()
        self.inputs.new("OctaneClippingMaterialIntersectionMaterial", OctaneClippingMaterialIntersectionMaterial.bl_label).init()
        self.inputs.new("OctaneClippingMaterialPriority", OctaneClippingMaterialPriority.bl_label).init()
        self.inputs.new("OctaneClippingMaterialRayepsilon", OctaneClippingMaterialRayepsilon.bl_label).init()
        self.inputs.new("OctaneClippingMaterialRayEpsilonCustomEnabled", OctaneClippingMaterialRayEpsilonCustomEnabled.bl_label).init()
        self.outputs.new("OctaneMaterialOutSocket", "Material out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneClippingMaterialEnabled,
    OctaneClippingMaterialShadingEnabled,
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
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
