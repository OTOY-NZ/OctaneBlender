import nodeitems_utils
from . import (
	base_node, 
	base_socket, 
	base_output_socket, 
	base_output_node,
	base_image,
	base_color_ramp,
	base_kernel,
	base_osl,	
	base_node_tree,
	node_trees, 
	node_items
)
from . import render_settings

from . import cameras
from . import compositor
from . import displacement
from . import emission
from . import environments
from . import geometry
from . import kernels
from . import lights
from . import material_layers
from . import materials
from . import medium
from . import object_layer
from . import other
from . import projection
from . import render_aovs
from . import render_settings
from . import render_target
from . import round_edges
from . import textures
from . import transforms
from . import values
from . import tools


def register():
	# Basic nodes
	node_items.register()
	base_node.register()
	base_socket.register()
	base_output_socket.register()
	base_output_node.register()	
	base_osl.register()
	base_image.register()
	base_kernel.register()
	base_color_ramp.register()
	base_node_tree.register()
	node_trees.register()
	# Octane auto generated code
	cameras.register()
	compositor.register()
	displacement.register()
	emission.register()
	environments.register()
	geometry.register()
	kernels.register()
	lights.register()
	material_layers.register()
	materials.register()
	medium.register()
	object_layer.register()
	other.register()
	projection.register()
	render_aovs.register()
	render_settings.register()
	render_target.register()
	round_edges.register()
	textures.register()
	transforms.register()
	values.register()	
	tools.register()

def unregister():	
	# Octane auto generated code
	cameras.unregister()
	compositor.unregister()
	displacement.unregister()
	emission.unregister()
	environments.unregister()
	geometry.unregister()
	kernels.unregister()
	lights.unregister()
	material_layers.unregister()
	materials.unregister()
	medium.unregister()
	object_layer.unregister()
	other.unregister()
	projection.unregister()
	render_aovs.unregister()
	render_settings.unregister()
	render_target.unregister()
	round_edges.unregister()
	textures.unregister()
	transforms.unregister()
	values.unregister()	
	tools.unregister()
	# Basic nodes
	node_items.unregister()
	base_node.unregister()
	base_node_tree.unregister()
	base_output_node.unregister()
	base_output_socket.unregister()
	base_osl.unregister()
	base_kernel.unregister()
	base_color_ramp.unregister()
	base_image.unregister()
	base_socket.unregister()
	node_trees.unregister()