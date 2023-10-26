##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from octane.utils import utility, consts
from octane.nodes import base_switch_input_socket
from octane.nodes.base_color_ramp import OctaneBaseRampNode
from octane.nodes.base_curve import OctaneBaseCurveNode
from octane.nodes.base_image import OctaneBaseImageNode
from octane.nodes.base_kernel import OctaneBaseKernelNode
from octane.nodes.base_node import OctaneBaseNode
from octane.nodes.base_osl import OctaneScriptNode
from octane.nodes.base_switch import OctaneBaseSwitchNode
from octane.nodes.base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneAnalyticLightAnalyticLightType(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightAnalyticLightType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_ANALYTIC_LIGHT_TYPE
    octane_pin_name="analyticLightType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Quad", "Quad", "", 0),
        ("Disk", "Disk", "", 1),
        ("Sphere", "Sphere", "", 3),
        ("Tube", "Tube", "", 4),
    ]
    default_value: EnumProperty(default="Quad", update=OctaneBaseSocket.update_node_tree, description="Type of the analytic light", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightAnalyticLightSpreadAngle(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightAnalyticLightSpreadAngle"
    bl_label="Spread angle"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANALYTIC_LIGHT_SPREAD_ANGLE
    octane_pin_name="analyticLightSpreadAngle"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=60.000000, update=OctaneBaseSocket.update_node_tree, description="Spread angle in degrees for quad and disk lights", min=0.000000, max=180.000000, soft_min=0.000000, soft_max=180.000000, step=10, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightAnalyticLightSpreadCutoffHardness(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightAnalyticLightSpreadCutoffHardness"
    bl_label="Spread cutoff hardness"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANALYTIC_LIGHT_SPREAD_CUTOFF_HARDNESS
    octane_pin_name="analyticLightSpreadCutoffHardness"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=2
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.500000, update=OctaneBaseSocket.update_node_tree, description="Spread cutoff hardness for quad and disk lights", min=0.000000, max=1.000000, soft_min=0.000000, soft_max=1.000000, step=1, precision=2, subtype="FACTOR")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightNormalize(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightNormalize"
    bl_label="Normalize power"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_NORMALIZE
    octane_pin_name="normalize"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=3
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Keep the emitted power constant if the angle changes")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightAnalyticLightFalloffRadius(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightAnalyticLightFalloffRadius"
    bl_label="Falloff radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_ANALYTIC_LIGHT_FALLOFF_RADIUS
    octane_pin_name="analyticLightFalloffRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=4
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=100000.000000, update=OctaneBaseSocket.update_node_tree, description="Falloff radius for quad, disk, tube and sphere lights", min=0.000100, max=100000.000000, soft_min=0.000100, soft_max=100000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightUseInPostVolume(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightUseInPostVolume"
    bl_label="Use in post volume"
    color=consts.OctanePinColor.Bool
    octane_default_node_type=consts.NodeType.NT_BOOL
    octane_default_node_name="OctaneBoolValue"
    octane_pin_id=consts.PinID.P_USE_IN_POST_VOLUME
    octane_pin_name="useInPostVolume"
    octane_pin_type=consts.PinType.PT_BOOL
    octane_pin_index=5
    octane_socket_type=consts.SocketType.ST_BOOL
    default_value: BoolProperty(default=False, update=OctaneBaseSocket.update_node_tree, description="Enable or disable this analytic light in post volume rendering")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightEmission(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightEmission"
    bl_label="Emission"
    color=consts.OctanePinColor.Emission
    octane_default_node_type=consts.NodeType.NT_EMIS_TEXTURE
    octane_default_node_name="OctaneTextureEmission"
    octane_pin_id=consts.PinID.P_EMISSION
    octane_pin_name="emission"
    octane_pin_type=consts.PinType.PT_EMISSION
    octane_pin_index=6
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightTransform(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightTransform"
    bl_label="Transform"
    color=consts.OctanePinColor.Transform
    octane_default_node_type=consts.NodeType.NT_TRANSFORM_3D
    octane_default_node_name="Octane3DTransformation"
    octane_pin_id=consts.PinID.P_TRANSFORM
    octane_pin_name="transform"
    octane_pin_type=consts.PinType.PT_TRANSFORM
    octane_pin_index=7
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightObjectLayer(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightObjectLayer"
    bl_label="Object layer"
    color=consts.OctanePinColor.ObjectLayer
    octane_default_node_type=consts.NodeType.NT_OBJECTLAYER
    octane_default_node_name="OctaneObjectLayer"
    octane_pin_id=consts.PinID.P_OBJECT_LAYER
    octane_pin_name="objectLayer"
    octane_pin_type=consts.PinType.PT_OBJECTLAYER
    octane_pin_index=8
    octane_socket_type=consts.SocketType.ST_LINK
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightQuadAnalyticLightSize(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightQuadAnalyticLightSize"
    bl_label="Quad size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_QUAD_ANALYTIC_LIGHT_SIZE
    octane_pin_name="quadAnalyticLightSize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=9
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Size of the quad. The quad light is always centered around the origin in the XY plane with the +Z axis as normal", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=1000000.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightDiskAnalyticLightSize(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightDiskAnalyticLightSize"
    bl_label="Disk size"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_DISK_ANALYTIC_LIGHT_SIZE
    octane_pin_name="diskAnalyticLightSize"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=10
    octane_socket_type=consts.SocketType.ST_FLOAT2
    default_value: FloatVectorProperty(default=(1.000000, 1.000000), update=OctaneBaseSocket.update_node_tree, description="Major and minor lengths of the disk. The disk light is always centered around the origin in the XY plane with the +Z axis as normal", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=1000000.000000, step=1, subtype="NONE", precision=2, size=2)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightSphereAnalyticLightRadius(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightSphereAnalyticLightRadius"
    bl_label="Sphere radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_SPHERE_ANALYTIC_LIGHT_RADIUS
    octane_pin_name="sphereAnalyticLightRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=11
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Sphere light's radius", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=1000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightTubeAnalyticLightCapRadius(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightTubeAnalyticLightCapRadius"
    bl_label="Tube cap radius"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TUBE_ANALYTIC_LIGHT_CAP_RADIUS
    octane_pin_name="tubeAnalyticLightCapRadius"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=12
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=0.100000, update=OctaneBaseSocket.update_node_tree, description="Tube light's cap radius", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=1000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightTubeAnalyticLightLength(OctaneBaseSocket):
    bl_idname="OctaneAnalyticLightTubeAnalyticLightLength"
    bl_label="Tube length"
    color=consts.OctanePinColor.Float
    octane_default_node_type=consts.NodeType.NT_FLOAT
    octane_default_node_name="OctaneFloatValue"
    octane_pin_id=consts.PinID.P_TUBE_ANALYTIC_LIGHT_LENGTH
    octane_pin_name="tubeAnalyticLightLength"
    octane_pin_type=consts.PinType.PT_FLOAT
    octane_pin_index=13
    octane_socket_type=consts.SocketType.ST_FLOAT
    default_value: FloatProperty(default=1.000000, update=OctaneBaseSocket.update_node_tree, description="Tube light's length. The tube is always centered around the origin with length being the vertical distance from end to end", min=0.000000, max=1000000.000000, soft_min=0.000000, soft_max=1000000.000000, step=1, precision=2, subtype="NONE")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneAnalyticLightGroupQuad(OctaneGroupTitleSocket):
    bl_idname="OctaneAnalyticLightGroupQuad"
    bl_label="[OctaneGroupTitle]Quad"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Quad size;")

class OctaneAnalyticLightGroupDisk(OctaneGroupTitleSocket):
    bl_idname="OctaneAnalyticLightGroupDisk"
    bl_label="[OctaneGroupTitle]Disk"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Disk size;")

class OctaneAnalyticLightGroupSphere(OctaneGroupTitleSocket):
    bl_idname="OctaneAnalyticLightGroupSphere"
    bl_label="[OctaneGroupTitle]Sphere"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Sphere radius;")

class OctaneAnalyticLightGroupTube(OctaneGroupTitleSocket):
    bl_idname="OctaneAnalyticLightGroupTube"
    bl_label="[OctaneGroupTitle]Tube"
    octane_group_sockets: StringProperty(name="Group Sockets", default="Tube cap radius;Tube length;")

class OctaneAnalyticLight(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneAnalyticLight"
    bl_label="Analytic light"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneAnalyticLightAnalyticLightType,OctaneAnalyticLightAnalyticLightSpreadAngle,OctaneAnalyticLightAnalyticLightSpreadCutoffHardness,OctaneAnalyticLightNormalize,OctaneAnalyticLightAnalyticLightFalloffRadius,OctaneAnalyticLightUseInPostVolume,OctaneAnalyticLightEmission,OctaneAnalyticLightTransform,OctaneAnalyticLightObjectLayer,OctaneAnalyticLightGroupQuad,OctaneAnalyticLightQuadAnalyticLightSize,OctaneAnalyticLightGroupDisk,OctaneAnalyticLightDiskAnalyticLightSize,OctaneAnalyticLightGroupSphere,OctaneAnalyticLightSphereAnalyticLightRadius,OctaneAnalyticLightGroupTube,OctaneAnalyticLightTubeAnalyticLightCapRadius,OctaneAnalyticLightTubeAnalyticLightLength,]
    octane_min_version=13000000
    octane_node_type=consts.NodeType.NT_LIGHT_ANALYTIC
    octane_socket_list=["Type", "Spread angle", "Spread cutoff hardness", "Normalize power", "Falloff radius", "Use in post volume", "Emission", "Transform", "Object layer", "Quad size", "Disk size", "Sphere radius", "Tube cap radius", "Tube length", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=14

    def init(self, context):
        self.inputs.new("OctaneAnalyticLightAnalyticLightType", OctaneAnalyticLightAnalyticLightType.bl_label).init()
        self.inputs.new("OctaneAnalyticLightAnalyticLightSpreadAngle", OctaneAnalyticLightAnalyticLightSpreadAngle.bl_label).init()
        self.inputs.new("OctaneAnalyticLightAnalyticLightSpreadCutoffHardness", OctaneAnalyticLightAnalyticLightSpreadCutoffHardness.bl_label).init()
        self.inputs.new("OctaneAnalyticLightNormalize", OctaneAnalyticLightNormalize.bl_label).init()
        self.inputs.new("OctaneAnalyticLightAnalyticLightFalloffRadius", OctaneAnalyticLightAnalyticLightFalloffRadius.bl_label).init()
        self.inputs.new("OctaneAnalyticLightUseInPostVolume", OctaneAnalyticLightUseInPostVolume.bl_label).init()
        self.inputs.new("OctaneAnalyticLightEmission", OctaneAnalyticLightEmission.bl_label).init()
        self.inputs.new("OctaneAnalyticLightTransform", OctaneAnalyticLightTransform.bl_label).init()
        self.inputs.new("OctaneAnalyticLightObjectLayer", OctaneAnalyticLightObjectLayer.bl_label).init()
        self.inputs.new("OctaneAnalyticLightGroupQuad", OctaneAnalyticLightGroupQuad.bl_label).init()
        self.inputs.new("OctaneAnalyticLightQuadAnalyticLightSize", OctaneAnalyticLightQuadAnalyticLightSize.bl_label).init()
        self.inputs.new("OctaneAnalyticLightGroupDisk", OctaneAnalyticLightGroupDisk.bl_label).init()
        self.inputs.new("OctaneAnalyticLightDiskAnalyticLightSize", OctaneAnalyticLightDiskAnalyticLightSize.bl_label).init()
        self.inputs.new("OctaneAnalyticLightGroupSphere", OctaneAnalyticLightGroupSphere.bl_label).init()
        self.inputs.new("OctaneAnalyticLightSphereAnalyticLightRadius", OctaneAnalyticLightSphereAnalyticLightRadius.bl_label).init()
        self.inputs.new("OctaneAnalyticLightGroupTube", OctaneAnalyticLightGroupTube.bl_label).init()
        self.inputs.new("OctaneAnalyticLightTubeAnalyticLightCapRadius", OctaneAnalyticLightTubeAnalyticLightCapRadius.bl_label).init()
        self.inputs.new("OctaneAnalyticLightTubeAnalyticLightLength", OctaneAnalyticLightTubeAnalyticLightLength.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneAnalyticLightAnalyticLightType,
    OctaneAnalyticLightAnalyticLightSpreadAngle,
    OctaneAnalyticLightAnalyticLightSpreadCutoffHardness,
    OctaneAnalyticLightNormalize,
    OctaneAnalyticLightAnalyticLightFalloffRadius,
    OctaneAnalyticLightUseInPostVolume,
    OctaneAnalyticLightEmission,
    OctaneAnalyticLightTransform,
    OctaneAnalyticLightObjectLayer,
    OctaneAnalyticLightQuadAnalyticLightSize,
    OctaneAnalyticLightDiskAnalyticLightSize,
    OctaneAnalyticLightSphereAnalyticLightRadius,
    OctaneAnalyticLightTubeAnalyticLightCapRadius,
    OctaneAnalyticLightTubeAnalyticLightLength,
    OctaneAnalyticLightGroupQuad,
    OctaneAnalyticLightGroupDisk,
    OctaneAnalyticLightGroupSphere,
    OctaneAnalyticLightGroupTube,
    OctaneAnalyticLight,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####
