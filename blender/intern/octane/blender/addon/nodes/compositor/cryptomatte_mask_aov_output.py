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


class OctaneCryptomatteMaskAOVOutputCryptomatteType(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteMaskAOVOutputCryptomatteType"
    bl_label="Type"
    color=consts.OctanePinColor.Enum
    octane_default_node_type=consts.NodeType.NT_ENUM
    octane_default_node_name="OctaneEnumValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_TYPE
    octane_pin_name="cryptomatteType"
    octane_pin_type=consts.PinType.PT_ENUM
    octane_pin_index=0
    octane_socket_type=consts.SocketType.ST_ENUM
    items = [
        ("Material node", "Material node", "", 2006),
        ("Material node name", "Material node name", "", 2001),
        ("Material pin name", "Material pin name", "", 2002),
        ("Object node", "Object node", "", 2004),
        ("Object node name", "Object node name", "", 2003),
        ("Object pin name", "Object pin name", "", 2007),
        ("Instance", "Instance", "", 2005),
        ("Geometry node name", "Geometry node name", "", 2008),
        ("Render layer", "Render layer", "", 2009),
        ("User instance ID", "User instance ID", "", 2010),
    ]
    default_value: EnumProperty(default="Material node", update=OctaneBaseSocket.update_node_tree, description="The type of cryptomatte render AOV from which to extract mattes", items=items)
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteMaskAOVOutputCryptomatteMattes(OctaneBaseSocket):
    bl_idname="OctaneCryptomatteMaskAOVOutputCryptomatteMattes"
    bl_label="Mattes"
    color=consts.OctanePinColor.String
    octane_default_node_type=consts.NodeType.NT_STRING
    octane_default_node_name="OctaneStringValue"
    octane_pin_id=consts.PinID.P_CRYPTOMATTE_MATTES
    octane_pin_name="cryptomatteMattes"
    octane_pin_type=consts.PinType.PT_STRING
    octane_pin_index=1
    octane_socket_type=consts.SocketType.ST_STRING
    default_value: StringProperty(default="", update=OctaneBaseSocket.update_node_tree, description="List of selected matte names, one per line.\n\nSome characters have special meaning:\n    * is a wildcard that matches any sequence of characters.\n    - at the start of a line excludes any mattes matched by that line.\n    ? on a line by itself matches mattes with blank names.\n    \ prevents the next character being treated as a special character.\n\nBlank lines are ignored. When a matte name is included by one line and excluded by another, whichever line comes last takes precedence. For example,\n    Car_*\n    -*dirt*\n    Car_wheel_dirt\nwill include \"Car_windows\" and \"Car_wheel_dirt\", but not \"Ground\" or \"Car_door_dirt\"")
    octane_hide_value=False
    octane_min_version=0
    octane_end_version=4294967295
    octane_deprecated=False

class OctaneCryptomatteMaskAOVOutput(bpy.types.Node, OctaneBaseNode):
    bl_idname="OctaneCryptomatteMaskAOVOutput"
    bl_label="Cryptomatte mask output AOV"
    bl_width_default=200
    octane_render_pass_id=-1
    octane_render_pass_name=""
    octane_render_pass_short_name=""
    octane_render_pass_description=""
    octane_render_pass_sub_type_name=""
    octane_socket_class_list=[OctaneCryptomatteMaskAOVOutputCryptomatteType,OctaneCryptomatteMaskAOVOutputCryptomatteMattes,]
    octane_min_version=12000003
    octane_node_type=consts.NodeType.NT_OUTPUT_AOV_CRYPTOMATTE_MASK
    octane_socket_list=["Type", "Mattes", ]
    octane_attribute_list=[]
    octane_attribute_config={}
    octane_static_pin_count=2

    def init(self, context):
        self.inputs.new("OctaneCryptomatteMaskAOVOutputCryptomatteType", OctaneCryptomatteMaskAOVOutputCryptomatteType.bl_label).init()
        self.inputs.new("OctaneCryptomatteMaskAOVOutputCryptomatteMattes", OctaneCryptomatteMaskAOVOutputCryptomatteMattes.bl_label).init()
        self.outputs.new("OctaneAOVOutputOutSocket", "Output AOV out").init()

    @classmethod
    def poll(cls, node_tree):
        return OctaneBaseNode.poll(node_tree)


_CLASSES=[
    OctaneCryptomatteMaskAOVOutputCryptomatteType,
    OctaneCryptomatteMaskAOVOutputCryptomatteMattes,
    OctaneCryptomatteMaskAOVOutput,
]

_SOCKET_INTERFACE_CLASSES = []

def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)

def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))

##### END OCTANE GENERATED CODE BLOCK #####


class OCTANE_OT_BaseCryptomattePicker(bpy.types.Operator):
    IS_PICKER_ADD = True

    @classmethod
    def poll(cls, context):
        node = getattr(context, "node", None)
        return node is not None

    def modal(self, context, event):
        if event.type in {'MIDDLEMOUSE', 'WHEELUPMOUSE', 'WHEELDOWNMOUSE'}:            
            return {'PASS_THROUGH'}        
        elif event.type in {'LEFTMOUSE', 'PRESS'}:
            print("event.mouse_x", event.mouse_x)
            print("event.mouse_y", event.mouse_y)
            print("event.mouse_region_x", event.mouse_region_x)
            print("event.mouse_region_y", event.mouse_region_y)
            print("context.area", context.area, context.area.type)
            context.window.cursor_set("DEFAULT")
            import _octane
            from octane.core.octane_node import OctaneRpcNode, OctaneRpcNodeType
            import xml.etree.ElementTree as ET
            node = self.node
            octane_rpc_node = OctaneRpcNode(OctaneRpcNodeType.SYNC_NODE)
            octane_rpc_node.set_name("OctaneCryptomattePicker[%s]" % node.name)
            octane_rpc_node.set_node_type(node.octane_node_type)
            x_view3d_offset = 0
            y_view3d_offset = 0
            for area in bpy.context.screen.areas:
                if area.type != "VIEW_3D":
                    continue
                for space in area.spaces:
                    if space.type != "VIEW_3D":
                        continue
                    if space.shading.type == "RENDERED":
                        x_view3d_offset = area.x
                        y_view3d_offset = area.y
                        break
            octane_rpc_node.set_attribute("mouse_x", consts.AttributeType.AT_INT, event.mouse_x - x_view3d_offset)
            octane_rpc_node.set_attribute("mouse_y", consts.AttributeType.AT_INT, event.mouse_y - y_view3d_offset)
            render_pass_id = utility.get_enum_int_value(node.inputs["Type"], "default_value", 2006)
            octane_rpc_node.set_attribute("render_pass_id", consts.AttributeType.AT_INT, render_pass_id)
            octane_rpc_node.set_attribute("is_add", consts.AttributeType.AT_BOOL, self.IS_PICKER_ADD)
            current_mattes = node.inputs["Mattes"].default_value
            octane_rpc_node.set_attribute("mattes", consts.AttributeType.AT_STRING, current_mattes)
            # node.sync_data(octane_rpc_node, None, consts.OctaneNodeTreeIDName.GENERAL)
            header_data = "[COMMAND]CRYPTOMATTE_PICKER"        
            body_data = octane_rpc_node.get_xml_data()
            response_data = _octane.update_octane_custom_node(header_data, body_data)
            if len(response_data):
                root = ET.fromstring(response_data)
                custom_data_et = root.find("custom_data")
                error = custom_data_et.findtext("error")
                if len(error):
                    self.report({'ERROR'}, error)
                else:
                    mattes = custom_data_et.findtext("mattes")
                    node.inputs["Mattes"].default_value = mattes
            return {'FINISHED'}
        elif event.type in {'RIGHTMOUSE', 'ESC'}:
            context.window.cursor_set("DEFAULT")
            return {'CANCELLED'}
        return {'RUNNING_MODAL'}

    def invoke(self, context, event):
        print("context.node", context.node)
        self.node = context.node
        from octane import engine                     
        if engine.IS_RENDERING:
            context.window.cursor_set("EYEDROPPER")
            context.window_manager.modal_handler_add(self)
            return {'RUNNING_MODAL'}
        else:
            self.report({'ERROR'}, "Please activate the viewport rendering when using the cryptomatte picker")
            return {'CANCELLED'}


class OCTANE_OT_CryptomattePickerAddMatte(OCTANE_OT_BaseCryptomattePicker):
    """Add mattes by picking in the rendering viewport"""
    bl_idname = "octane.cryptomatte_picker_add_matte"
    bl_label = "Add Matte"
    IS_PICKER_ADD = True


class OCTANE_OT_CryptomattePickerRemoveMatte(OCTANE_OT_BaseCryptomattePicker):
    """Remove mattes by picking in the rendering viewport"""
    bl_idname = "octane.cryptomatte_picker_remove_matte"
    bl_label = "Remove Matte"
    IS_PICKER_ADD = False


class OctaneCryptomatteMaskAOVOutput_Override(OctaneCryptomatteMaskAOVOutput):

    def draw_buttons(self, context, layout):
        row = layout.row()
        row.column().operator("octane.cryptomatte_picker_add_matte", icon="ADD", text="")
        row.column().operator("octane.cryptomatte_picker_remove_matte", icon="REMOVE", text="")


_CLASSES.extend([OCTANE_OT_CryptomattePickerAddMatte, OCTANE_OT_CryptomattePickerRemoveMatte])
utility.override_class(_CLASSES, OctaneCryptomatteMaskAOVOutput, OctaneCryptomatteMaskAOVOutput_Override)