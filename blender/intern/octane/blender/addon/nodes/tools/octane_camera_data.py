import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCameraData(bpy.types.Node, OctaneBaseNode):
    VIEW_VECTOR_OUT = "View Vector"
    VIEW_Z_DEPTH_OUT = "View Z Depth"
    VIEW_DISTANCE_OUT = "View Distance"
    FRONT_PROJECTION_OUT = "Front Projection"

    CAMERA_DATA_ORBX_PATH_NAME = "CAMERA_DATA_ORBX_PATH"
    CAMERA_DATA_ORBX_REL_PATH = "../../libraries/orbx/CameraData.orbx"
    CAMERA_DATA_ORBX_ABS_PATH = ""
    MAX_Z_DEPTH = "MAX_Z_DEPTH"
    MAX_DISTANCE = "MAX_DISTANCE"
    KEEP_FRONT_PROJECTION = "KEEP_FRONT_PROJECTION"
    USED_IN_ENVIRONMENT = "USED_IN_ENVIRONMENT"

    bl_idname="OctaneCameraData"
    bl_label="Camera Data"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NodeType.NT_BLENDER_NODE_CAMERA_DATA)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)
    
    max_z_depth: FloatProperty(name="Max Z-Depth", default=10, min=0, max=10000000, soft_min=0, soft_max=10000000)
    max_distance: FloatProperty(name="Max Distance", default=100, min=0.001, max=10000000, soft_min=0.001, soft_max=10000000)
    keep_front_projection: BoolProperty(name="Keep Front Projection", default=True)

    def use_mulitple_outputs(self):
        return True

    def init(self, context):
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_VECTOR_OUT).init()
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_Z_DEPTH_OUT).init()
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_DISTANCE_OUT).init()
        self.outputs.new("OctaneProjectionOutSocket", self.FRONT_PROJECTION_OUT).init()

    def sync_custom_data(self, octane_node, octane_graph_node_data, owner_type, scene, is_viewport):
        import os
        super().sync_custom_data(octane_node, octane_graph_node_data, owner_type, scene, is_viewport)
        cur_dir_path = os.path.dirname(os.path.abspath(__file__))
        lib_path = os.path.join(cur_dir_path, self.CAMERA_DATA_ORBX_REL_PATH)
        self.CAMERA_DATA_ORBX_ABS_PATH = os.path.realpath(bpy.path.abspath(lib_path))
        octane_node.set_blender_attribute(self.CAMERA_DATA_ORBX_PATH_NAME, consts.AttributeType.AT_STRING, self.CAMERA_DATA_ORBX_ABS_PATH)
        octane_node.set_blender_attribute(self.MAX_Z_DEPTH, consts.AttributeType.AT_FLOAT, self.max_z_depth)
        octane_node.set_blender_attribute(self.MAX_DISTANCE, consts.AttributeType.AT_FLOAT, self.max_distance)
        octane_node.set_blender_attribute(self.KEEP_FRONT_PROJECTION, consts.AttributeType.AT_BOOL, self.keep_front_projection)
        octane_node.set_blender_attribute(self.USED_IN_ENVIRONMENT, consts.AttributeType.AT_BOOL, owner_type == consts.OctaneNodeTreeIDName.WORLD)       
        
    def draw_buttons(self, context, layout):
        layout.row().prop(self, "max_z_depth")
        layout.row().prop(self, "max_distance")
        layout.row().prop(self, "keep_front_projection")
        
_CLASSES=[
    OctaneCameraData,
]

_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))