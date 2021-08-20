##### BEGIN OCTANE GENERATED CODE BLOCK #####
import bpy
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from bpy.props import EnumProperty, StringProperty, BoolProperty, IntProperty, FloatProperty, FloatVectorProperty, IntVectorProperty
from ...utils import consts
from ...utils.consts import SocketType
from ..base_node import OctaneBaseNode
from ..base_socket import OctaneBaseSocket, OctaneGroupTitleSocket, OctaneMovableInput, OctaneGroupTitleMovableInputs


class OctaneCustomAOVEnabled(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVEnabled"
    bl_label="Enabled"
    color=consts.OctanePinColor.Bool
    octane_default_node_type="OctaneBoolValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=42)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_BOOL)
    default_value: BoolProperty(default=True, update=OctaneBaseSocket.update_node_tree, description="Enables the render AOV")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOVSubType(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVSubType"
    bl_label="ID"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=703)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("Custom 1", "Custom 1", "", 0),
        ("Custom 2", "Custom 2", "", 1),
        ("Custom 3", "Custom 3", "", 2),
        ("Custom 4", "Custom 4", "", 3),
        ("Custom 5", "Custom 5", "", 4),
        ("Custom 6", "Custom 6", "", 5),
        ("Custom 7", "Custom 7", "", 6),
        ("Custom 8", "Custom 8", "", 7),
        ("Custom 9", "Custom 9", "", 8),
        ("Custom 10", "Custom 10", "", 9),
    ]
    default_value: EnumProperty(default="Custom 1", update=OctaneBaseSocket.update_node_tree, description="The ID or index of the custom AOV", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOVSecondaryRays(OctaneBaseSocket):
    bl_idname="OctaneCustomAOVSecondaryRays"
    bl_label="Visible after"
    color=consts.OctanePinColor.Enum
    octane_default_node_type="OctaneEnumValue"
    octane_pin_id: IntProperty(name="Octane Pin ID", default=631)
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_ENUM)
    items = [
        ("None - primary rays only", "None - primary rays only", "", 0),
        ("Reflections", "Reflections", "", 1),
        ("Refractions", "Refractions", "", 2),
        ("Reflections and refractions", "Reflections and refractions", "", 3),
    ]
    default_value: EnumProperty(default="None - primary rays only", update=None, description="Determines whether secondary bounces should contribute to the custom AOV or not", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCustomAOV(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCustomAOV"
    bl_label="Custom AOV"
    bl_width_default=200
    octane_render_pass_id={0: 501, 1: 502, 2: 503, 3: 504, 4: 505, 5: 506, 6: 507, 7: 508, 8: 509, 9: 510, }
    octane_render_pass_name={0: "Custom AOV 1", 1: "Custom AOV 2", 2: "Custom AOV 3", 3: "Custom AOV 4", 4: "Custom AOV 5", 5: "Custom AOV 6", 6: "Custom AOV 7", 7: "Custom AOV 8", 8: "Custom AOV 9", 9: "Custom AOV 10", }
    octane_render_pass_short_name={0: "Cstm1", 1: "Cstm2", 2: "Cstm3", 3: "Cstm4", 4: "Cstm5", 5: "Cstm6", 6: "Cstm7", 7: "Cstm8", 8: "Cstm9", 9: "Cstm10", }
    octane_render_pass_description={0: "Custom AOV 1", 1: "Custom AOV 2", 2: "Custom AOV 3", 3: "Custom AOV 4", 4: "Custom AOV 5", 5: "Custom AOV 6", 6: "Custom AOV 7", 7: "Custom AOV 8", 8: "Custom AOV 9", 9: "Custom AOV 10", }
    octane_render_pass_sub_type_name="ID"
    octane_min_version=0
    octane_node_type: IntProperty(name="Octane Node Type", default=186)
    octane_socket_list: StringProperty(name="Socket List", default="Enabled;ID;Visible after;")
    octane_attribute_list: StringProperty(name="Attribute List", default="")
    octane_attribute_config_list: StringProperty(name="Attribute Config List", default="")
    octane_static_pin_count: IntProperty(name="Octane Static Pin Count", default=3)

    def init(self, context):
        self.inputs.new("OctaneCustomAOVEnabled", OctaneCustomAOVEnabled.bl_label).init()
        self.inputs.new("OctaneCustomAOVSubType", OctaneCustomAOVSubType.bl_label).init()
        self.inputs.new("OctaneCustomAOVSecondaryRays", OctaneCustomAOVSecondaryRays.bl_label).init()
        self.outputs.new("OctaneRenderAOVsOutSocket", "Render AOVs out").init()


_classes=[
    OctaneCustomAOVEnabled,
    OctaneCustomAOVSubType,
    OctaneCustomAOVSecondaryRays,
    OctaneCustomAOV,
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
