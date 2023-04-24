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


class OctaneVectronMaterial1(OctaneBaseSocket):
    bl_idname="OctaneVectronMaterial1"
    bl_label="Geometry material"
    color=consts.OctanePinColor.Material
    octane_default_node_type=consts.NodeType.NT_MAT_DIFFUSE
    octane_default_node_name="OctaneDiffuseMaterial"
    octane_pin_id=consts.PinID.P_MATERIAL1
    octane_pin_name="material1"
    octane_pin_type=consts.PinType.PT_MATERIAL
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVectronSize(OctaneBaseSocket):
    bl_idname="OctaneVectronSize"
    bl_label="Bounds"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SIZE
    octane_pin_name="size"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT3
    default_value: FloatVectorProperty(default=(10.000000, 10.000000, 10.000000), update=OctaneBaseSocket.update_node_tree, description="Bounds of the geometry in meters", min=0.000000, max=340282346638528859811704183484516925440.000000, soft_min=0.000000, soft_max=340282346638528859811704183484516925440.000000, step=1, subtype="NONE", precision=2, size=3)
    octane_hide_value=False
    octane_min_version=4000009
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneVectron(bpy.types.Node, OctaneScriptNode):
    bl_idname="OctaneVectron"
    bl_label="Vectron®"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneVectronMaterial1,OctaneVectronSize,]
    octane_min_version=0
    octane_node_type=consts.NodeType.NT_GEO_OSL
    octane_socket_list=["Geometry material", "Bounds", ]
    octane_attribute_list=["a_filename", "a_reload", "a_shader_code", "a_result", ]
    octane_attribute_config={"a_package": [consts.AttributeID.A_PACKAGE, "package", consts.AttributeType.AT_FILENAME], "a_filename": [consts.AttributeID.A_FILENAME, "filename", consts.AttributeType.AT_FILENAME], "a_reload": [consts.AttributeID.A_RELOAD, "reload", consts.AttributeType.AT_BOOL], "a_shader_code": [consts.AttributeID.A_SHADER_CODE, "shaderCode", consts.AttributeType.AT_STRING], "a_errors": [consts.AttributeID.A_ERRORS, "errors", consts.AttributeType.AT_STRING], "a_result": [consts.AttributeID.A_RESULT, "result", consts.AttributeType.AT_INT], }
    octane_static_pin_count=2

    a_filename: StringProperty(name="Filename", default="", update=OctaneBaseNode.update_node_tree, description="The file where the OSL shader is stored. If set, A_SHADER_CODE will be replaced with the content of the file", subtype="FILE_PATH")
    a_reload: BoolProperty(name="Reload", default=False, update=OctaneBaseNode.update_node_tree, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_shader_code: StringProperty(name="Shader code", default="#include <octane-oslintrin.h>\n\nshader Vectron(\n    float radius = 1 [[float min = 0, float slidermax = 1e4, float sliderexponent = 4]],\n    vector translate = 0,\n    output _sdf out = _SDFDEF)\n{\n    out.dist = distance(P, translate) - radius;\n}\n", update=OctaneBaseNode.update_node_tree, description="The OSL code for this node")
    a_result: IntProperty(name="Result", default=0, update=OctaneBaseNode.update_node_tree, description="The OSL code for this node. If set to COMPILE_NONE, the shader code will be recompiled at the next evaluation. If set to COMPILE_FORCE, the code will be recompiled even if it didn't change")

    def init(self, context):
        self.inputs.new("OctaneVectronMaterial1", OctaneVectronMaterial1.bl_label).init()
        self.inputs.new("OctaneVectronSize", OctaneVectronSize.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_CLASSES=[
    OctaneVectronMaterial1,
    OctaneVectronSize,
    OctaneVectron,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
