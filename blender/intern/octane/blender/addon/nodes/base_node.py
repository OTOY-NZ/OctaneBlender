import bpy
from bpy.props import IntProperty, StringProperty
from ..utils import consts


class OctaneBaseNode(object):	
    """Base class for Octane nodes"""

    bl_label = ""
    octane_node_type: IntProperty(name="Octane Node Type", default=consts.NT_UNKNOWN)
    octane_socket_list: StringProperty(name="Socket List", default="")
    octane_attribute_list: StringProperty(name="Attribute List", default="")

    @classmethod
    def poll(cls, tree):
        pass    

    def add_input(self, type, name, default, enabled=True):
        input = self.inputs.new(type, name)
        if hasattr(input, "default_value"):
            input.default_value = default        
        input.enabled = enabled
        return input        

    def update(self):
        pass   