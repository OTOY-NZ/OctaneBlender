import bpy
from ..utils import consts


class OctaneBaseNodeTree(object):
	@classmethod
	def poll(cls, context):
		return context.scene.render.engine == consts.ENGINE_NAME

