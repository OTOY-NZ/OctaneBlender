#
# Copyright 2011-2013 Blender Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# <pep8 compliant>

import bpy
from octane import core
if not core.EXCLUSIVE_OCTANE_ADDON_CLIENT_MODE:
    import _octane


def osl_compile(node, identifier, osl_path, osl_code, report):
    # ok = _octane.osl_compile(input_path, output_path)    
    # print('osl identifier: ', identifier)
    # print('osl_path: \n', osl_path)
    # print('osl_code: \n', osl_code)
    import _octane    
    scene = bpy.context.scene
    oct_scene = scene.octane   
    ok, compile_msg = _octane.osl_compile(identifier, node.id_data.as_pointer(), node.as_pointer(), osl_path, osl_code)  

    if ok:
        report({'INFO'}, "OSL shader compilation succeeded")
    else:
        report({'ERROR'}, "OSL script compilation error: %s" % compile_msg)

    return ok, compile_msg


def update_script_node(node, report):
    """compile and update shader script node"""
    def resolve_identifier(identifier):
        return "[OSL COMPILE NODE]" + identifier

    import os
    import shutil
    import tempfile

    ok = False
    identifier = ''
    compile_msg = ''

    if node.mode == 'EXTERNAL':
        # compile external script file
        script_path = bpy.path.abspath(node.filepath, library=node.id_data.library)

        if len(script_path):
            # compile .osl file
            identifier = resolve_identifier(script_path)
            ok, compile_msg = osl_compile(node, identifier, script_path, "", report)
        else:
            # unknown
            report({'ERROR'}, "No valid osl file, nothing to compile")
    elif node.mode == 'INTERNAL' and node.script:
        # internal script, we will store bytecode in the node
        script = node.script
        osl_path = bpy.path.abspath(script.filepath, library=script.library)

        if script.is_in_memory or script.is_dirty or script.is_modified or not os.path.exists(osl_path):
            identifier = resolve_identifier(script.name)
            ok, compile_msg = osl_compile(node, identifier, "", script.as_string(), report) 
        else:
            # compile text datablock from disk directly
            try:
                osl_file = open(osl_path, 'r')
                osl_code = osl_file.read()
                osl_file.close()          
                identifier = resolve_identifier(script.name)
                ok, compile_msg = osl_compile(node, identifier, "", osl_code, report)
            except:
                report({'ERROR'}, "No valid osl file, nothing to compile")             
    else:
        report({'WARNING'}, "No text or file specified in node, nothing to compile")
        return

    if ok:
        # now update node with new sockets
        data = bpy.data.as_pointer()
        ok = _octane.osl_update_node(data, identifier, node.id_data.as_pointer(), node.as_pointer())
        # trick to trigger node update
        node.width = node.width

    if not ok:
        report({'ERROR'}, "OSL script compilation failed, see console for errors")     
        report({'ERROR'}, compile_msg)   

    return ok
