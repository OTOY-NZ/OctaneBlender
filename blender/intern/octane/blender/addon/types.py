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
    ('CUBEMAP', "Cube map", ""),
    ('CUBEMAPPX', "Cube map (+X)", ""),
    ('CUBEMAPMX', "Cube map (-X)", ""),
    ('CUBEMAPPY', "Cube map (+Y)", ""),
    ('CUBEMAPMY', "Cube map (-Y)", ""),
    ('CUBEMAPPZ', "Cube map (+Z)", ""),
    ('CUBEMAPMZ', "Cube map (-Z)", ""),
    )

camera_stereo_modes = (
    ('1', "Off axis", ""),
    ('2', "Parallel", ""),
    )

camera_stereo_outs = (
    ('0', "Disabled", ""),
    ('1', "Left eye", ""),
    ('2', "Right eye", ""),
    ('3', "Side by side", ""),
    ('4', "Anaglyphic", ""),
    ('5', "Over-under", ""),
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

anim_modes = (
    ('0', "Full", ""),
    ('1', "Movable proxies", ""),
    ('2', "Camera only", ""),
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
    ('9', "Object layer ID", ""),
    ('10',"Ambient occlusion", ""),
    )

mb_types = (
    ('0', "Internal", ""),
    ('1', "Subframe", ""),
    )

mb_directions = (
    ('0', "After", ""),
    ('1', "Before", ""),
    ('2', "Symmetric", ""),
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
    ('3', "Reshapable proxy", ""),
    )

meshes_render_types = (
    ('0', "Global", ""),
    ('1', "Scatter", ""),
    ('2', "Movable", ""),
    ('3', "Reshapable", ""),
    ('4', "As is", ""),
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

bound_interp = (
    ('1', "None", ""),
    ('2', "Edge only", ""),
    ('3', "Edge and corner", ""),
    ('4', "Always sharp", ""),
    )

subd_scheme = (
    ('1', "Catmull Clark", ""),
    ('2', "Loop", ""),
    ('3', "Bilinear", ""),
    )

pass_types = (
    ('0', "Combined", "Combined pass"),

    ('1', "Emitters", "Emitters pass"),
    ('2', "Environment", "Environment pass"),
    ('3', "Diffuse direct", "Diffuse direct pass"),
    ('4', "Diffuse indirect", "Diffuse indirect pass"),
    ('5', "Reflection direct", "Reflection direct pass"),
    ('6', "Reflection indirect", "Reflection indirect pass"),
    ('7', "Refraction", "Refraction pass pass"),
    ('8', "Transmission", "Transmission pass"),
    ('9', "Subsurface scattering", "Subsurface scattering pass"),
    ('10', "Post processing", "Post processing pass"),

    ('11', "Layer shadows", "Layer shadows pass"),
    ('12', "Layer black shadows", "Layer black shadows pass"),
    ('13', "Layer color shadows", "Layer color shadows pass"),
    ('14', "Layer reflections", "Layer reflections pass"),

    ('15', "Ambient light", "Ambient light pass"),
    ('16', "Sunlight", "Sunlight pass"),
    ('17', "Light pass 1", "Light pass 1 pass"),
    ('18', "Light pass 2", "Light pass 2 pass"),
    ('19', "Light pass 3", "Light pass 3 pass"),
    ('20', "Light pass 4", "Light pass 4 pass"),
    ('21', "Light pass 5", "Light pass 5 pass"),
    ('22', "Light pass 6", "Light pass 6 pass"),
    ('23', "Light pass 7", "Light pass 7 pass"),
    ('24', "Light pass 8", "Light pass 8 pass"),

    ('100000', "Geometric normals", "Geometric normals pass"),
    ('100001', "Shading normals", "Shading normals pass"),
    ('100002', "Position", "Position pass"),
    ('100003', "Z-depth", "Z-depth pass"),
    ('100004', "Material id", "Material id pass"),
    ('100005', "UV coordinates", "UV coordinates pass"),
    ('100006', "Tangents", "Tangents pass"),
    ('100007', "Wireframe", "Wireframe pass"),
    ('100008', "Vertex normals", "Vertex normals pass"),
    ('100009', "Object id", "Object id pass"),
    ('100010', "Ambient occlusion", "Ambient occlusion pass"),
    ('100011', "Motion vector", "Motion vector pass"),
    ('100012', "Layer ID", "Layer ID pass"),
    ('100013', "Layer mask", "Layer mask pass"),
    ('100014', "Light pass ID", "Light pass ID pass"),
    )

pass_dir_subtype = (
    ('0', "Direct", ""),
    ('1', "Indirect", ""),
    )

pass_refl_subtype = (
    ('0', "Direct", ""),
    ('1', "Indirect", ""),
    ('2', "Layers", ""),
    )

pass_shadows_subtype = (
    ('0', "Shadows", ""),
    ('1', "Black shadows", ""),
    ('2', "Colored shadows", ""),
    )

pass_normal_subtype = (
    ('0', "Geomenty", ""),
    ('1', "Shading", ""),
    ('2', "Vertex", ""),
    )

winding_orders = (
    ('0', "Clockwise", ""),
    ('1', "Counterclockwise", ""),
    )

layer_modes = (
    ('0', "Normal", ""),
    ('1', "Hide inactive layers", ""),
    ('2', "Only side effects", ""),
    ('3', "Hide from camera", ""),
    )

hair_interpolations = (
    ('0', "Hair length", ""),
    ('1', "Segment count", ""),
    ('2', "Use hair Ws", ""),
    )

pass_sampling_modes = (
    ('0', "Distributed rays", ""),
    ('1', "Non-distributed with pixel filtering", ""),
    ('2', "Non-distributed without pixel filtering", ""),
    )
