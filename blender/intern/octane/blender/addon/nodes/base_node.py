import bpy
from ..utils import consts


class OctaneBaseNode(object):	
    """Base class for Octane nodes"""

    bl_label = ""
    @classmethod
    def poll(cls, tree):
        pass    

    def add_input(self, type, name, default, enabled=True):
        input = self.inputs.new(type, name)
        if hasattr(input, "default_value"):
            input.default_value = default        
        input.enabled = enabled
        return input        


class OctaneBaseCompositeNode(OctaneBaseNode):
    """Base class for Octane composite nodes"""

    bl_label = ""
    @classmethod
    def poll(cls, tree):
        return tree.bl_idname in [consts.NODE_TREE_IDNAME_COMPOSITE, ] 


class OctaneBaseRenderAOVNode(OctaneBaseNode):
    """Base class for Octane render aov nodes"""

    bl_label = ""
    @classmethod
    def poll(cls, tree):
        return tree.bl_idname in [consts.NODE_TREE_IDNAME_RENDER_AOV, ]