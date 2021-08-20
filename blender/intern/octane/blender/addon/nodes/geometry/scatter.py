##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneScatterGeometry(OctaneBaseSocket):
    bl_idname="OctaneScatterGeometry"
    bl_label="Geometry"
    color=consts.OctanePinColor.Geometry
    octane_default_node_type=""
    octane_pin_id: IntProperty(name="Octane Pin ID", default=59)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)
    octane_hide_value=True
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneScatter(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneScatter"
    bl_label="Scatter"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=5)
    octane_socket_list: StringProperty(name="Socket List", default="Geometry;")
    octane_attribute_list: StringProperty(name="Attribute List", default="a_reload;a_geoimp_scale_unit;a_inherit;a_user_instance_ids;")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="1;2;1;2;")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=1)

    a_reload: BoolProperty(name="Reload", default=False, update=None, description="Set it to TRUE if the file needs a reload. After the node was evaluated the attribute will be false again")
    a_geoimp_scale_unit: IntProperty(name="Geoimp scale unit", default=4, update=None, description="Defines the length unit used to create the transform matrices. This applies to the rightmost column of the transform matrix, which defines the translation component. (see Octane::GeometryImportScale)")
    a_inherit: BoolProperty(name="Inherit", default=True, update=None, description="If enabled the transforms are relative to the object space of the destination node, otherwise they are absolute transforms from world space to object space")
    a_user_instance_ids: IntProperty(name="User instance ids", default=0, update=None, description="An array of identifiers for the instances, The instance IDs are assigned to transform nodes in the array index order. If this array is empty and for any unassigned instances, IDs are set to invalid. A valid ID should be a non-negative number. It's a non-unique ID, multiple nodes can have the same ID, so it's a user responsibility to set unique ID if needed. In a tree hierarchy, the ID of current node will override the input geometry node's ID")

    def init(self, context):
        self.inputs.new("OctaneScatterGeometry", OctaneScatterGeometry.bl_label).init()
        self.outputs.new("OctaneGeometryOutSocket", "Geometry out").init()


_classes=[
    OctaneScatterGeometry,
    OctaneScatter,
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
