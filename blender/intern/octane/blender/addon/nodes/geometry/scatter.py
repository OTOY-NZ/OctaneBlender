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


class OctaneScatterGeometry(OctaneBaseSocket):
    bl_idname = "OctaneScatterGeometry"
    bl_label = "Geometry"
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


class OctaneScatter(bpy.types.Node, OctaneBaseNode):
    bl_idname = "OctaneScatter"
    bl_label = "Scatter"
    bl_width_default = 200
    octane_render_pass_id = -1
    octane_render_pass_name = ""
    octane_render_pass_short_name = ""
    octane_render_pass_description = ""
    octane_render_pass_sub_type_name = ""
    octane_socket_class_list = [OctaneScatterGeometry, ]
    octane_min_version = 0
    octane_node_type = consts.NodeType.NT_GEO_SCATTER
    octane_socket_list = ["Geometry", ]
    octane_attribute_list = ["a_filename", "a_reload", "a_geoimp_scale_unit", "a_inherit", "a_user_instance_ids", ]
    octane_attribute_config = {"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_geoimp_scale_unit": [consts.AttributeID.A_GEOIMP_SCALE_UNIT, "scaleUnitType", consts.AttributeType.AT_INT], "a_transforms": [consts.AttributeID.A_TRANSFORMS, "transforms", consts.AttributeType.AT_MATRIX], "a_inherit": [consts.AttributeID.A_INHERIT, "inherit", consts.AttributeType.AT_BOOL], "a_user_instance_ids": [consts.AttributeID.A_USER_INSTANCE_IDS, "userInstanceIds", consts.AttributeType.AT_INT], }
    octane_static_pin_count = 1

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the CSV file to load the transforms from. After loading successfully the A_TRANSFORMS and A_USER_INSTANCE_IDS attributes will be replaced by the file contents, otherwise the A_TRANSFORMS and AT_FILENAME and A_USER_INSTANCE_IDS attributes are reverted to their original value", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_geoimp_scale_unit: IntProperty(name="Geoimp scale unit", default=4, update=OctaneBaseNode.update_node_tree, description="Defines the length unit used to create the transform matrices. This applies to the rightmost column of the transform matrix, which defines the translation component. (see Octane::GeometryImportScale)")
    a_inherit: BoolProperty(name="Inherit", default=True, update=OctaneBaseNode.update_node_tree, description="If enabled the transforms are relative to the object space of the destination node, otherwise they are absolute transforms from world space to object space")
    a_user_instance_ids: IntProperty(name="User instance ids", default=0, update=OctaneBaseNode.update_node_tree, description="An array of identifiers for the instances, The instance IDs are assigned to transform nodes in the array index order. If this array is empty and for any unassigned instances, IDs are set to invalid. A valid ID should be a non-negative number. It's a non-unique ID, multiple nodes can have the same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):  # noqa
        self.inputs.new("OctaneScatterGeometry", OctaneScatterGeometry.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES = [
    OctaneScatterGeometry,
    OctaneScatter,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

# END OCTANE GENERATED CODE BLOCK #
