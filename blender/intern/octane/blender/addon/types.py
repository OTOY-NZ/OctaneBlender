#
# Copyright 2011, Blender Foundation.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#

# <pep8 compliant>

import bpy
from . import engine

class OctaneRender(bpy.types.RenderEngine):
    bl_idname = 'octane'
    bl_label = "OctaneRender"
    bl_use_shading_nodes = True
    bl_use_preview = True
    session = 0

    def __init__(self):
        #engine.init()
        if OctaneRender.session:
            self.busy = True
        else:
            self.busy = False

    def __del__(self):
        if hasattr(self, 'busy') and self.busy:
            return
        engine.free(OctaneRender, self)

    # final render
    def update(self, data, scene):
        if self.busy:
            return
            
        if self.is_preview:
            if not OctaneRender.session:
                engine.create(OctaneRender, self, data, scene, None, None, None)
            else:
                engine.reset(OctaneRender, self, data, scene)
                self.busy = True
        else:
            if not OctaneRender.session:
                engine.create(OctaneRender, self, data, scene)
            else:
                engine.reset(OctaneRender, self, data, scene)
                self.busy = True
        engine.update(OctaneRender, self, data, scene)

    def render(self, scene):
        if self.busy:
            return
        engine.render(OctaneRender, self)

    # preview render
    # def preview_update(self, context, id):
    #    pass
    #
    # def preview_render(self):
    #    pass

    # viewport render
    def view_update(self, context):
        if self.busy:
            return

        if not OctaneRender.session:
            engine.create(OctaneRender, self, context.blend_data, context.scene, context.region, context.space_data, context.region_data)
        engine.update(OctaneRender, self, context.blend_data, context.scene)

    def view_draw(self, context):
        if self.busy:
            return
        engine.draw(OctaneRender, self, context.region, context.space_data, context.region_data)


filter_types = (
    ('BOX', "Box", "Box filter"),
    ('GAUSSIAN', "Gaussian", "Gaussian filter"),
    )

aperture_types = (
    ('RADIUS', "Radius", "Directly change the size of the aperture"),
    ('FSTOP', "F/stop", "Change the size of the aperture by f/stops"),
    )

panorama_types = (
    ('EQUIRECTANGULAR', "Equirectangular", "Render the scene with a spherical camera, also known as Lat Long panorama"),
    ('FISHEYE_EQUIDISTANT', "Fisheye Equidistant", "Ideal for fulldomes, ignore the sensor dimensions"),
    ('FISHEYE_EQUISOLID', "Fisheye Equisolid", "Similar to most fisheye modern lens, take sensor dimensions into consideration"),
    )

camera_pan_modes = (
    ('SPHERE', "Spherical", ""),
    ('CYLINDER', "Cylindrical", ""),
    )

response_types = (
    ('99', "Agfacolor_Futura_100CD", ""),
    ('100', "Agfacolor_Futura_200CD", ""),
    ('101', "Agfacolor_Futura_400CD", ""),
    ('102', "Agfacolor_Futura_II_100CD", ""),
    ('103', "Agfacolor_Futura_II_200CD", ""),
    ('104', "Agfacolor_Futura_II_400CD", ""),
    ('105', "Agfacolor_HDC_100_plusCD", ""),
    ('106', "Agfacolor_HDC_200_plusCD", ""),
    ('107', "Agfacolor_HDC_400_plusCD", ""),
    ('108', "Agfacolor_Optima_II_100CD", ""),
    ('109', "Agfacolor_Optima_II_200CD", ""),
    ('110', "Agfacolor_ultra_050_CD", ""),
    ('111', "Agfacolor_Vista_100CD", ""),
    ('112', "Agfacolor_Vista_200CD", ""),
    ('113', "Agfacolor_Vista_400CD", ""),
    ('114', "Agfacolor_Vista_800CD", ""),
    ('115', "Agfachrome_CT_precisa_100CD", ""),
    ('116', "Agfachrome_CT_precisa_200CD", ""),
    ('117', "Agfachrome_RSX2_050CD", ""),
    ('118', "Agfachrome_RSX2_100CD", ""),
    ('119', "Agfachrome_RSX2_200CD", ""),
    ('201', "Advantix_100CD", ""),
    ('202', "Advantix_200CD", ""),
    ('203', "Advantix_400CD", ""),
    ('204', "Gold_100CD", ""),
    ('205', "Gold_200CD", ""),
    ('206', "Max_Zoom_800CD", ""),
    ('207', "Portra_100TCD", ""),
    ('208', "Portra_160NCCD", ""),
    ('209', "Portra_160VCCD", ""),
    ('210', "Portra_800CD", ""),
    ('211', "Portra_400VCCD", ""),
    ('212', "Portra_400NCCD", ""),
    ('213', "Ektachrome_100_plusCD", ""),
    ('214', "Ektachrome_320TCD", ""),
    ('215', "Ektachrome_400XCD", ""),
    ('216', "Ektachrome_64CD", ""),
    ('217', "Ektachrome_64TCD", ""),
    ('218', "Ektachrome_E100SCD", ""),
    ('219', "Ektachrome_100CD", ""),
    ('220', "Kodachrome_200CD", ""),
    ('221', "Kodachrome_25", ""),
    ('222', "Kodachrome_64CD", ""),
    ('301', "F125CD", ""),
    ('302', "F250CD", ""),
    ('303', "F400CD", ""),
    ('304', "FCICD", ""),
    ('305', "DSCS315_1", ""),
    ('306', "DSCS315_2", ""),
    ('307', "DSCS315_3", ""),
    ('308', "DSCS315_4", ""),
    ('309', "DSCS315_5", ""),
    ('310', "DSCS315_6", ""),
    ('311', "FP2900Z", ""),
    ('400', "Linear", ""),
    )

gi_modes = (
    ('0', "None", ""),
    ('1', "Ambient", ""),
    ('2', "Sample environment", ""),
    ('3', "Ambient occlusion", ""),
    ('4', "Diffuse", ""),
    )

info_channel_types = (
    ('0', "Geometric normals", ""),
    ('1', "Shading normals", ""),
    ('2', "Position", ""),
    ('3', "Z-Depth", ""),
    ('4', "Material ID", ""),
    ('5', "Textures coordinates", ""),
    ('7', "Wireframe", ""),
    ('8', "Interpolated vertex normals", ""),
    )

kernel_types = (
    ('0', "Default", ""),
    ('1', "Direct light", ""),
    ('2', "Path trace", ""),
    ('3', "PMC", ""),
    ('4', "Info-channel", ""),
    )

mesh_types = (
    ('0', "Global", ""),
    ('1', "Scatter", ""),
    ('2', "Movable proxy", ""),
    )

meshes_render_types = (
    ('0', "Global", ""),
    ('1', "Scatter", ""),
    ('2', "Movable proxy", ""),
    ('3', "As is", ""),
    )

environment_types = (
    ('0', "Texture", ""),
    ('1', "Daylight", ""),
    )

environment_daylight_types = (
    ('0', "Direction", ""),
    ('1', "Daylight system", ""),
    )

environment_daylight_models = (
    ('0', "Old", ""),
    ('1', "New", ""),
    )
