import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


shader_osl_code_view_vector = """
shader OctaneBlender_CameraData_ViewVector(
    output color c = 0
)
{
    c = normalize(I);
}
"""

shader_osl_code_view_distance = """
shader OctaneBlender_CameraData_ViewDistance(
    float dmax = 100[[float min=0.0010, float max=100000.0, float sliderexponent=4]],
    output color c = 0
)
{
    point pCam = transform("common", "camera", P);
    float len = length(pCam) / dmax;
    c = color(len, len, len);
}
"""

shader_osl_code_zdepth = """
shader OctaneBlender_CameraData_ZDepth(
    float dmax = 10[[float min=0.0010, float max=100000.0, float sliderexponent=4]],
    output color c = 0)
{
    point pCam = transform("common", "camera", P);
    c = -pCam[2] / dmax;
}
"""

shader_osl_code_front_projection = """
shader OctaneBlender_CameraData_FrontProjection(
  int env_mode = 0[[string label = "Environment Mode",string widget = "boolean"]],
  int blender_camera_mode = 0[[string label = "Blender Camera Mode",string widget = "boolean"]],
  float blender_camera_center_x = 0[[string label = "Center X",string widget = "float"]],
  float blender_camera_center_y = 0[[string label = "Center Y",string widget = "float"]],
  int blender_camera_region_x = 0[[string label = "Region Width",string widget = "int"]],
  int blender_camera_region_y = 0[[string label = "Region Height",string widget = "int"]],
  output point uvw = 0)
{
    float fov;
    int res[2];
    getattribute("camera:fov", fov);
    getattribute("camera:resolution", res);
    if (env_mode) {
        vector p = transform("camera", I);
        if (blender_camera_mode) {
            uvw[0] = blender_camera_center_x + 0.5 * p[0] / p[2] / tan(fov / 2) * res[0] / blender_camera_region_x;
            uvw[1] = blender_camera_center_y - 0.5 * p[1] / p[2] / tan(fov / 2) * res[0] / blender_camera_region_y;
        } else {            
            uvw[0] = 0.5 + 0.5 * p[0] / p[2] / tan(fov / 2) ;
            uvw[1] = 0.5 - 0.5 * p[1] / p[2] / tan(fov / 2) * res[0] / res[1];
        }
    } else {
        vector p = transform("camera", P);
        if (blender_camera_mode) {
            uvw[0] = blender_camera_center_x - 0.5 * p[0] / p[2] / tan(fov / 2) * res[0] / blender_camera_region_x;
            uvw[1] = blender_camera_center_y - 0.5 * p[1] / p[2] / tan(fov / 2) * res[0] / blender_camera_region_y;
        } else {
            uvw[0] = 0.5 - 0.5 * p[0] / p[2] / tan(fov / 2) ;
            uvw[1] = 0.5 - 0.5 * p[1] / p[2] / tan(fov / 2) * res[0] / res[1];
        }
    }
}
"""


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
    octane_node_type=consts.NodeType.NT_BLENDER_NODE_CAMERA_DATA
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=0)
    
    max_z_depth: FloatProperty(name="Max Z-Depth", default=10, min=0, max=10000000, soft_min=0, soft_max=10000000, update=OctaneBaseNode.update_node_tree)
    max_distance: FloatProperty(name="Max Distance", default=100, min=0.001, max=10000000, soft_min=0.001, soft_max=10000000, update=OctaneBaseNode.update_node_tree)
    keep_front_projection: BoolProperty(name="Keep Front Projection", default=True, update=OctaneBaseNode.update_node_tree)

    def use_mulitple_outputs(self):
        return True

    def init(self, context):
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_VECTOR_OUT).init()
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_Z_DEPTH_OUT).init()
        self.outputs.new("OctaneTextureOutSocket", self.VIEW_DISTANCE_OUT).init()
        self.outputs.new("OctaneProjectionOutSocket", self.FRONT_PROJECTION_OUT).init()

    def sync_custom_data(self, octane_node, octane_graph_node_data, depsgraph):
        from octane.nodes.base_osl import OctaneScriptNode
        octane_node.clear_all_subnodes()
        octane_name = octane_node.name
        if octane_name.endswith(self.VIEW_VECTOR_OUT):
            subnode_name = octane_name
            subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_TEX_OSL)
            subnode.set_attribute_id(consts.AttributeID.A_RELOAD, True)
            subnode.set_attribute_id(consts.AttributeID.A_SHADER_CODE, shader_osl_code_view_vector)
        elif octane_name.endswith(self.VIEW_DISTANCE_OUT):
            subnode_name = octane_name
            subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_TEX_OSL)
            subnode.set_attribute_id(consts.AttributeID.A_RELOAD, True)
            subnode.set_attribute_id(consts.AttributeID.A_SHADER_CODE, shader_osl_code_view_distance)
            OctaneScriptNode.set_osl_pin(subnode, 0, "dmax", consts.SocketType.ST_FLOAT, consts.PinType.PT_FLOAT, consts.NodeType.NT_FLOAT, False, "", self.max_distance)
        elif octane_name.endswith(self.VIEW_Z_DEPTH_OUT):
            subnode_name = octane_name
            subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_TEX_OSL)
            subnode.set_attribute_id(consts.AttributeID.A_RELOAD, True)
            subnode.set_attribute_id(consts.AttributeID.A_SHADER_CODE, shader_osl_code_zdepth)
            OctaneScriptNode.set_osl_pin(subnode, 0, "dmax", consts.SocketType.ST_FLOAT, consts.PinType.PT_FLOAT, consts.NodeType.NT_FLOAT, False, "", self.max_z_depth)
        elif octane_name.endswith(self.FRONT_PROJECTION_OUT):
            subnode_name = octane_name
            if self.keep_front_projection:
                subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_PROJ_OSL)
                subnode.set_attribute_id(consts.AttributeID.A_RELOAD, True)
                subnode.set_attribute_id(consts.AttributeID.A_SHADER_CODE, shader_osl_code_front_projection)
                is_environment_node = (getattr(octane_graph_node_data, "owner_type", consts.OctaneNodeTreeIDName.MATERIAL) == consts.OctaneNodeTreeIDName.WORLD)
                OctaneScriptNode.set_osl_pin(subnode, 0, "env_mode", consts.SocketType.ST_BOOL, consts.PinType.PT_BOOL, consts.NodeType.NT_BOOL, False, "", is_environment_node)
                OctaneScriptNode.set_osl_pin(subnode, 1, "blender_camera_mode", consts.SocketType.ST_BOOL, consts.PinType.PT_BOOL, consts.NodeType.NT_BOOL, True, consts.OCTANE_BLENDER_CAMERA_MODE, False)
                OctaneScriptNode.set_osl_pin(subnode, 2, "blender_camera_center_x", consts.SocketType.ST_FLOAT, consts.PinType.PT_FLOAT, consts.NodeType.NT_FLOAT, True, consts.OCTANE_BLENDER_CAMERA_CENTER_X, 0)
                OctaneScriptNode.set_osl_pin(subnode, 3, "blender_camera_center_y", consts.SocketType.ST_FLOAT, consts.PinType.PT_FLOAT, consts.NodeType.NT_FLOAT, True, consts.OCTANE_BLENDER_CAMERA_CENTER_Y, 0)
                OctaneScriptNode.set_osl_pin(subnode, 4, "blender_camera_region_x", consts.SocketType.ST_INT, consts.PinType.PT_INT, consts.NodeType.NT_INT, True, consts.OCTANE_BLENDER_CAMERA_REGION_WIDTH, 0)
                OctaneScriptNode.set_osl_pin(subnode, 5, "blender_camera_region_y", consts.SocketType.ST_INT, consts.PinType.PT_INT, consts.NodeType.NT_INT, True, consts.OCTANE_BLENDER_CAMERA_REGION_HEIGHT, 0)
            else:
                subnode = octane_node.get_subnode(subnode_name, consts.NodeType.NT_PROJ_PERSPECTIVE)
                subnode.set_pin_id(consts.PinID.P_POSITION_TYPE, False, "", 1) # World space
                subnode.set_pin_id(consts.PinID.P_TRANSFORM, True, consts.OCTANE_BLENDER_STATIC_FRONT_PROJECTION_TRANSFORM, "")

    def load_custom_legacy_node(self, legacy_node, node_tree, context, report=None):
        if report is not None:
            if legacy_node.inputs["Max Z-Depth"].is_linked:
                report({"WARNING"}, "Outer links of the 'Max Z-Depth' socket are not supported in the Addon CameraData node anymore. So the link of the 'Max Z-Depth' socket in Node %s is discarded" % (legacy_node.name))
            if legacy_node.inputs["Max Distance"].is_linked:
                report({"WARNING"}, "Outer links of the 'Max Distance' socket are not supported in the Addon CameraData node anymore. So the link of the 'Max Distance' socket in Node %s is discarded" % (legacy_node.name))
            if legacy_node.inputs["Keep Front Projection"].is_linked:
                report({"WARNING"}, "Outer links of the 'Keep Front Projection' socket are not supported in the Addon CameraData node anymore. So the link of the 'Keep Front Projection' socket in Node %s is discarded" % (legacy_node.name))
        self.max_z_depth = legacy_node.inputs["Max Z-Depth"].default_value
        self.max_distance = legacy_node.inputs["Max Distance"].default_value
        self.keep_front_projection = legacy_node.inputs["Keep Front Projection"].default_value        
        outputs_mapping = {
            "Octane View Vector": "View Vector",
            "Octane View Z Depth": "View Z Depth",
            "Octane View Distance": "View Distance",
            "Octane Front Projection": "Front Projection",
        }
        for legacy_output_name, current_output_name in outputs_mapping.items():
            for link in legacy_node.outputs[legacy_output_name].links:                
                node_tree.links.new(self.outputs[current_output_name], link.to_socket)

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