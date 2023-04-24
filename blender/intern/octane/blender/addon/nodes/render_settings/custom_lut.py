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


class OctaneCustomLUTStrength(OctaneBaseSocket):
    bl_idname="OctaneCustomLUTStrength"
    bl_label="Strength"
    color=consts.OctanePinColor.Float
    octane_default_node_type=6
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=230)
    octane_pin_name: StringProperty(name="Octane Pin Name", default="strength")
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_FLOAT)
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="The amount how much the LUT should be applied", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomLUT(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCustomLUT"
    bl_label="Custom LUT"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=103)
    octane_socket_list: StringProperty(name="Socket List", default="Strength;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_filename;a_reload;a_title;a_domain_min_1d;a_domain_max_1d;a_values_1d;a_domain_min_3d;a_domain_max_3d;a_values_3d;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="11;1;10;8;8;8;8;8;8;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="Stores the CSV file to load the transforms from. After loading successfully the A_TRANSFORMS and A_USER_INSTANCE_IDS attributes will be replaced by the file contents, otherwise the A_TRANSFORMS and AT_FILENAME and A_USER_INSTANCE_IDS attributes are reverted to their original value", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_title: StringProperty(name="Title", default="", update=OctaneBaseNode.update_node_tree, description="The title stored in the LUT file")
    a_domain_min_1d: FloatVectorProperty(name="Domain min 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 1D look up table")
    a_domain_max_1d: FloatVectorProperty(name="Domain max 1d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 1D look up table")
    a_values_1d: FloatVectorProperty(name="Values 1d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The (XYZ or RGB) output values of the 1D look up table corresponding to input values that are equidistantly distributed between the A_DOMAIN_MIN_1D and A_DOMAIN_MAX_1D.\n\nNeeds to have a size >= 2")
    a_domain_min_3d: FloatVectorProperty(name="Domain min 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The minimum of the input domain of the 3D look up table")
    a_domain_max_3d: FloatVectorProperty(name="Domain max 3d", default=(1.000000, 1.000000, 1.000000), size=3, update=OctaneBaseNode.update_node_tree, description="The maximum of the input domain of the 3D look up table")
    a_values_3d: FloatVectorProperty(name="Values 3d", default=(0.000000, 0.000000, 0.000000), size=3, update=OctaneBaseNode.update_node_tree, description="Array storing the 3D LUT cube. Its size must be the cube of an integral number.\nThe order of the grid values is that the first dimension (X or red) changes fastest and the last dimension (Z or blue) changes slowest.\n\nNeeds to have a size >= 8")

    def init(self, context):
        self.inputs.new("OctaneCustomLUTStrength", OctaneCustomLUTStrength.bl_label).init()
        self.outputs.new("OctaneLUTOutSocket", "LUT out").init()


_CLASSES=[
    OctaneCustomLUTStrength,
    OctaneCustomLUT,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_class(reversed(_SOCKET_INTERFACE_CLASSES))
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
