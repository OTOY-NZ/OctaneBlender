# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom # noqa
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes import base_switch_input_socket  # noqa
from octane.nodes.base_color_ramp import OctaneBaseRampNode  # noqa
from octane.nodes.base_curve import OctaneBaseCurveNode  # noqa
from octane.nodes.base_image import OctaneBaseImageNode  # noqa
from octane.nodes.base_kernel import OctaneBaseKernelNode  # noqa
from octane.nodes.base_node import OctaneBaseNode  # noqa
from octane.nodes.base_osl import OctaneScriptNode  # noqa
from octane.nodes.base_switch import OctaneBaseSwitchNode  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs  # noqa


class OctaneSDFDomainTransformGeometry(OctaneBaseSocket):
    bl_idname = "OctaneSDFDomainTransformGeometry"
    bl_label = "SDF"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_default_node_name = ""
    octane_pin_id = consts.PinID.P_GEOMETRY
    octane_pin_name = "geometry"
    octane_pin_type = consts.PinType.PT_GEOMETRY
    octane_pin_index = 0
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFDomainTransformTransform(OctaneBaseSocket):
    bl_idname = "OctaneSDFDomainTransformTransform"
    bl_label = "P transform"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name = "Octane3DTransformation"
    octane_pin_id = consts.PinID.P_TRANSFORM
    octane_pin_name = "transform"
    octane_pin_type = consts.PinType.PT_TRANSFORM
    octane_pin_index = 1
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFDomainTransformProjection(OctaneBaseSocket):
    bl_idname = "OctaneSDFDomainTransformProjection"
    bl_label = "Projection"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_PROJ_LINEAR
    octane_default_node_name = "OctaneXYZToUVW"
    octane_pin_id = consts.PinID.P_PROJECTION
    octane_pin_name = "projection"
    octane_pin_type = consts.PinType.PT_PROJECTION
    octane_pin_index = 2
    octane_socket_type = consts.SocketType.ST_LINK
    octane_hide_value = True
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFDomainTransformSize(OctaneBaseSocket):
    bl_idname = "OctaneSDFDomainTransformSize"
    bl_label = "Bounds"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_SIZE
    octane_pin_name = "size"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 3
    octane_socket_type = consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(10.000000, 10.000000, 10.000000), update=OctaneBaseSocket.update_node_tree, description="Bounds of the geometry in meters, if no node is connected this is derived from the nodes connected to the input", min=-340282346638528859811704183484516925440.000000, max=340282346638528859811704183484516925440.000000, soft_min=-340282346638528859811704183484516925440.000000, soft_max=340282346638528859811704183484516925440.000000, step=1.000000, subtype="NONE", precision=2, size=3)
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFDomainTransformStepScale(OctaneBaseSocket):
    bl_idname = "OctaneSDFDomainTransformStepScale"
    bl_label = "Step scale"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_FLOAT
    octane_default_node_name = "OctaneFloatValue"
    octane_pin_id = consts.PinID.P_STEP_SCALE
    octane_pin_name = "stepScale"
    octane_pin_type = consts.PinType.PT_FLOAT
    octane_pin_index = 4
    octane_socket_type = consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Scale factor applied to the marching step. If the distance field is distorted a lot, use a lower value to avoid too steep gradients in the result", min=0.010000, max=1.000000, soft_min=0.010000, soft_max=1.000000, step=1.000000, precision=2, subtype="NONE")
    octane_hide_value = False
    octane_min_version = 0
    octane_end_version = 4294967295
    octane_deprecated = False


class OctaneSDFDomainTransform(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneSDFDomainTransform"
    bl_label = "Domain transform"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneSDFDomainTransformGeometry, OctaneSDFDomainTransformTransform, OctaneSDFDomainTransformProjection, OctaneSDFDomainTransformSize, OctaneSDFDomainTransformStepScale, ]
    octane_min_version = 12000001
    octane_node_type = consts.NodeType.NT_GEO_SDF_DOMAIN
    octane_socket_list = ["SDF", "P transform", "Projection", "Bounds", "Step scale", ]
    octane_attribute_list = []
    octane_attribute_config = {}
    octane_static_pin_count = 5

    def init(self, context):  # noqa
        self.inputs.new("OctaneSDFDomainTransformGeometry", OctaneSDFDomainTransformGeometry.bl_label).init()
        self.inputs.new("OctaneSDFDomainTransformTransform", OctaneSDFDomainTransformTransform.bl_label).init()
        self.inputs.new("OctaneSDFDomainTransformProjection", OctaneSDFDomainTransformProjection.bl_label).init()
        self.inputs.new("OctaneSDFDomainTransformSize", OctaneSDFDomainTransformSize.bl_label).init()
        self.inputs.new("OctaneSDFDomainTransformStepScale", OctaneSDFDomainTransformStepScale.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneSDFDomainTransformGeometry,
    OctaneSDFDomainTransformTransform,
    OctaneSDFDomainTransformProjection,
    OctaneSDFDomainTransformSize,
    OctaneSDFDomainTransformStepScale,
    OctaneSDFDomainTransform,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
