from . import (
    base_node,
    base_socket,
    base_output_socket,
    base_output_node,
    base_switch_input_socket,
    base_image,
    base_lut,
    base_color_ramp,
    base_curve,
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
from . import other
from . import output_aovs
from . import projection
from . import render_aovs
from . import render_settings
from . import render_target
from . import round_edges
from . import texture_layers
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
    base_switch_input_socket.register()
    base_osl.register()
    base_image.register()
    base_kernel.register()
    base_color_ramp.register()
    base_curve.register()
    base_lut.register()
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
    other.register()
    output_aovs.register()
    projection.register()
    render_aovs.register()
    render_settings.register()
    render_target.register()
    round_edges.register()
    textures.register()
    texture_layers.register()
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
    other.unregister()
    output_aovs.unregister()
    projection.unregister()
    render_aovs.unregister()
    render_settings.unregister()
    render_target.unregister()
    round_edges.unregister()
    textures.unregister()
    texture_layers.unregister()
    transforms.unregister()
    values.unregister()
    tools.unregister()
    # Basic nodes
    node_items.unregister()
    base_node.unregister()
    base_node_tree.unregister()
    base_switch_input_socket.unregister()
    base_output_node.unregister()
    base_output_socket.unregister()
    base_osl.unregister()
    base_kernel.unregister()
    base_color_ramp.unregister()
    base_curve.unregister()
    base_lut.unregister()
    base_image.unregister()
    base_socket.unregister()
    node_trees.unregister()
