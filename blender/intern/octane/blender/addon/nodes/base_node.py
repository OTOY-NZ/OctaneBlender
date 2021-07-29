import bpy
from ..utils import consts


class OctaneBaseNode(object):
	"""Base class for Octane nodes"""

	bl_label = ""
	@classmethod
	def poll(cls, tree):
		pass


class OctaneBaseCompositeNode(OctaneBaseNode, bpy.types.Node):
	"""Base class for Octane composite nodes"""

	bl_label = ""
	@classmethod
	def poll(cls, tree):
		return tree.bl_idname in [consts.NODE_TREE_IDNAME_COMPOSITE, ] 
