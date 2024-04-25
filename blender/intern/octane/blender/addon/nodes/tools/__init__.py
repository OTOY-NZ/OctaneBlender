from . import octane_camera_data
from . import octane_object_data
from . import octane_proxy
from . import octane_script_graph


def register():
    octane_camera_data.register()
    octane_object_data.register()
    octane_proxy.register()
    octane_script_graph.register()
    

def unregister():
    octane_camera_data.unregister()
    octane_object_data.unregister()
    octane_proxy.unregister()
    octane_script_graph.unregister()