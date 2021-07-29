import bpy
from ..utils import consts


class OctaneBaseSocket(object):
	"""Base class for Octane sockets"""

	bl_label = ""
	color = consts.SOCKET_COLOR_DEFAULT
	octane_pin_id = consts.P_UNKNOWN

	def draw(self, context, layout):
		pass