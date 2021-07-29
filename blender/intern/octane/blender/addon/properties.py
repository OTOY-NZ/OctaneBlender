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
from bpy.app.handlers import persistent
from bpy.props import (
    BoolProperty,
    EnumProperty,
    FloatProperty,
    IntProperty,
    PointerProperty,
    StringProperty,
    FloatVectorProperty,
    BoolVectorProperty,
    CollectionProperty
)

from math import pi
import nodeitems_utils
from . import nodeitems_octane


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
    ('1', "Off axis", '', 1),
    ('2', "Parallel", '', 2),
    )

camera_stereo_outs = (
    ('0', "Disabled", ""),
    ('1', "Left eye", ""),
    ('2', "Right eye", ""),
    ('3', "Side by side", ""),
    ('4', "Anaglyphic", ""),
    ('5', "Over-under", ""),
    )

camera_imager_orders = (
    ('0', "Response,Gamma,LUT", '', 0),
    ('1', "Gamma,Response,LUT", '', 1),
    ('2', "LUT,Response,Gamma", '', 2),
    ('3', "LUT,Gamma,Response", '', 3),
    ('4', "Response,LUT,Gamma", '', 4),
    ('5', "Gamma,LUT,Response", '', 5),        
    )

default_material_orders = (
    ('0', "Diffuse", '', 0),
    ('1', "Glossy", '', 1),
    ('2', "Specular", '', 2),
    ('3', "Mix", '', 3), 
    ('4', "Portal", '', 4), 
    ('5', "Toon", '', 5),
    ('6', "Metal", '', 6),
    ('7', "Universal", '', 7), 
    ('8', "ShadowCatcher", '', 8), 
    ('9', "Layered", '', 9), 
    ('10', "Composite", '', 10), 
    )

texture_node_layouts = (
    ('0', "Default", '', 0),
    ('1', "Octane", '', 1),    
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
    ('400', "Linear/Off", "",),
    ('401', "sRGB", "",),
    ('402', "Gamma1.8", "",),
    ('403', "Gamma2.2", "",),
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
    ('0', "Geometric normals", "", 0),
    ('1', "Shading normals", "", 1),
    ('2', "Position", "", 2),
    ('3', "Z-Depth", "", 3),
    ('4', "Material ID", "", 4),
    ('5', "Textures coordinates", "", 5),
    ('6',"Texture tangent", "", 6),
    ('7', "Wireframe", "", 7),
    ('8', "Smooth normals", "", 8),
    ('9', "Object layer ID", "", 9),
    ('10',"Ambient occlusion", "", 10),
    ('11',"Motion vector", "", 11),
    ('12',"Render layer ID", "", 12),
    ('13',"Render layer Mask", "", 13),
    ('14',"Light pass ID", "", 14),
    ('15',"Tangent normal", "", 15),
    ('16',"Opacity", "", 16),
    ('17',"Baking group ID", "", 17),
    ('18',"Roughness", "", 18),
    ('19',"Index of reflection", "", 19),
    ('20',"Diffuse filter color", "", 20),
    ('21',"Reflection filter color", "", 21),
    ('22',"Refraction filter color", "", 22),
    ('23',"Transmission filter color", "", 23),
    ('24',"Object layer color", "", 24),
    )

octane_render_pass_types = (
    ('0', "Combined", "Combined pass", 0),

    ('1', "Emitters", "Emitters pass", 1),
    ('2', "Environment", "Environment pass", 2),

    ('3', "Diffuse", "Diffuse pass", 3),
    ('4', "Diffuse direct", "Diffuse direct pass", 4),
    ('5', "Diffuse indirect", "Diffuse indirect pass", 5),
    ('6', "Diffuse filter", "Diffuse filter pass", 6),

    ('7', "Reflection", "Reflection pass", 7),
    ('8', "Reflection direct", "Reflection direct pass", 8),
    ('9', "Reflection indirect", "Reflection indirect pass", 9),
    ('10', "Reflection filter", "Reflection filter pass", 10),

    ('11', "Refraction", "Refraction pass pass", 11),
    ('12', "Refraction filter", "Refraction filter pass pass", 12),
    ('13', "Transmission", "Transmission pass", 13),
    ('14', "Transmission filter", "Transmission filter pass", 14),

    ('15', "Subsurface scattering", "Subsurface scattering pass", 15),
    ('16', "Post processing", "Post processing pass", 16),

    ('17', "Layer shadows", "Layer shadows pass", 17),
    ('18', "Layer black shadows", "Layer black shadows pass", 18),
    ('20', "Layer reflections", "Layer reflections pass", 20),

    ('21', "Ambient light", "Ambient light pass", 21),
    ('22', "Sunlight", "Sunlight pass", 22),
    ('23', "Light pass 1", "Light pass 1", 23),
    ('24', "Light pass 2", "Light pass 2", 24),
    ('25', "Light pass 3", "Light pass 3", 25),
    ('26', "Light pass 4", "Light pass 4", 26),
    ('27', "Light pass 5", "Light pass 5", 27),
    ('28', "Light pass 6", "Light pass 6", 28),
    ('29', "Light pass 7", "Light pass 7", 29),
    ('30', "Light pass 8", "Light pass 8", 30),
    ('31', "Noise", "Noise pass", 31),
    ('32', "Shadow", "Shadow pass", 32),
    ('33', "Irradiance", "Irradiance pass", 33),
    ('34', "Light Direction", "Light Direction pass", 34),
    ('35', "Volume", "Volume pass", 35),
    ('36', "Volume Mask", "Volume Mask pass", 36),
    ('37', "Volume Emission", "Volume Emission pass", 37),
    ('38', "Volume Z-Depth Front", "Volume Z-Depth Front pass", 38),
    ('39', "Volume Z-Depth Back", "Volume Z-Depth Back pass", 39),

    ('43', "Denoiser Beauty", "Denoiser Beauty pass", 43),
    ('44', "Denoiser DiffDir", "Denoiser Diffuse Direct pass", 44),
    ('45', "Denoiser DiffIndir", "Denoiser Diffuse Indirect pass", 45),
    ('46', "Denoiser ReflectDir", "Denoiser Reflection Direct pass", 46),
    ('47', "Denoiser ReflectIndir", "Denoiser Reflection Indirect pass", 47),
    #('48', "Denoiser Refraction", "Denoiser Refraction pass"),
    ('49', "Denoiser Remainder", "Denoiser Remainder pass", 49),
    ('76', "Denoiser Emission", "Denoiser Emission pass", 76),
    ('74', "Denoiser Volume", "Denoiser Volume pass", 74),
    ('75', "Denoiser Volume Emission", "Denoiser Volume Emission pass", 75),

    ('54', "Ambient light direct", "Ambient light direct pass", 54),
    ('55', "Ambient light indirect", "Ambient light indirect pass", 55),
    ('56', "Sunlight direct", "Sunlight direct pass", 56),
    ('57', "Sunlight indirect", "Sunlight indirect pass", 57),
    ('58', "Light pass 1 direct", "Light pass 1 direct", 58),    
    ('59', "Light pass 2 direct", "Light pass 2 direct", 59),
    ('60', "Light pass 3 direct", "Light pass 3 direct", 60),
    ('61', "Light pass 4 direct", "Light pass 4 direct", 61),
    ('62', "Light pass 5 direct", "Light pass 5 direct", 62),
    ('63', "Light pass 6 direct", "Light pass 6 direct", 63),
    ('64', "Light pass 7 direct", "Light pass 7 direct", 64),
    ('65', "Light pass 8 direct", "Light pass 8 direct", 65),   
    ('66', "Light pass 1 indirect", "Light pass 1 indirect", 66),    
    ('67', "Light pass 2 indirect", "Light pass 2 indirect", 67),
    ('68', "Light pass 3 indirect", "Light pass 3 indirect", 68),
    ('69', "Light pass 4 indirect", "Light pass 4 indirect", 69),
    ('70', "Light pass 5 indirect", "Light pass 5 indirect", 70),
    ('71', "Light pass 6 indirect", "Light pass 6 indirect", 71),
    ('72', "Light pass 7 indirect", "Light pass 7 indirect", 72),
    ('73', "Light pass 8 indirect", "Light pass 8 indirect", 73),       

    ('1000', "Geometric normals", "Geometric normals pass", 1000),
    ('1001', "Shading normals", "Shading normals pass", 1001),
    ('1002', "Position", "Position pass", 1002),
    ('1003', "Z-depth", "Z-depth pass", 1003),
    ('1004', "Material id", "Material id pass", 1004),
    ('1005', "UV coordinates", "UV coordinates pass", 1005),
    ('1006', "Tangents", "Tangents pass", 1006),
    ('1007', "Wireframe", "Wireframe pass", 1007),
    ('1008', "Smooth normals", "Smooth normals pass", 1008),
    ('1009', "Object id", "Object id pass", 1009),    
    ('1010', "Ambient occlusion", "Ambient occlusion pass", 1010),
    ('1011', "Motion vector", "Motion vector pass", 1011),
    ('1012', "Render layer ID", "Colours objects on the same layer with the same color based on the render layer ID", 1012),
    ('1013', "Render layer mask", "Mask for geometry on the active render layer", 1013),
    ('1014', "Light pass ID", "Light pass ID pass", 1014),
    ('1015', "Tangent normals", "Tangent normals pass", 1015),
    ('1016', "Info Opacity", "Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry", 1016),
    ('1017', "Baking group ID", "Colours each distinct baking group in the scene with a colour based on it's ID", 1017),
    ('1018', "Info Roughness", "Material roughness at the camera ray's hit point", 1018),
    ('1019', "Info IOR", "Material index of refraction at the camera ray's hit point", 1019),
    ('1020', "Info DiffFilter", "The diffuse texture color of the diffuse and glossy material", 1020),
    ('1021', "Info ReflectFilter", "The reflection texture color of the specular and glossy material", 1021),
    ('1022', "Info RefractFilter", "The refraction texture color of the specular material", 1022),    
    ('1023', "Info TransmFilter", "The transmission texture color of the diffuse material", 1023),    
    ('1024', "Object layer color", "The color specified in the object layer node", 1024),

    ('2001', "Cryptomatte MaterialName", "Cryptomatte channels for material node names", 2001), 
    ('2006', "Cryptomatte MaterialNode", "Cryptomatte channels using distinct material nodes", 2006),    
    ('2002', "Cryptomatte MaterialPinName", "Cryptomatte channels for material pin names", 2002), 
    ('2003', "Cryptomatte ObjectName", "Cryptomatte channels for object layer node names", 2003), 
    ('2004', "Cryptomatte ObjectNode", "Cryptomatte channels using distinct object layer nodes", 2004),    
    ('2007', "Cryptomatte ObjectPinName", "Cryptomatte channels for object layer pin names", 2007), 
    
    ('2005', "Cryptomatte InstanceID", "Cryptomatte channels for instance IDs", 2005),    
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
    ('2', "Planetary", ""),
    )

environment_daylight_types = (
    ('0', "Direction", ""),
    ('1', "Daylight system", ""),
    )

environment_daylight_models = (
    ('0', "Old", ""),
    ('1', "New", ""),
    ('2', "Nishita", ""),
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

    ('3', "Diffuse", "Diffuse pass"),
    ('4', "Diffuse direct", "Diffuse direct pass"),
    ('5', "Diffuse indirect", "Diffuse indirect pass"),
    ('6', "Diffuse filter", "Diffuse filter pass"),

    ('7', "Reflection", "Reflection pass"),
    ('8', "Reflection direct", "Reflection direct pass"),
    ('9', "Reflection indirect", "Reflection indirect pass"),
    ('10', "Reflection filter", "Reflection filter pass"),

    ('11', "Refraction", "Refraction pass pass"),
    ('12', "Refraction filter", "Refraction filter pass pass"),
    ('13', "Transmission", "Transmission pass"),
    ('14', "Transmission filter", "Transmission filter pass"),

    ('15', "Subsurface scattering", "Subsurface scattering pass"),
    ('16', "Post processing", "Post processing pass"),

    ('17', "Layer shadows", "Layer shadows pass"),
    ('18', "Layer black shadows", "Layer black shadows pass"),
    ('20', "Layer reflections", "Layer reflections pass"),

    ('21', "Ambient light", "Ambient light pass"),
    ('22', "Sunlight", "Sunlight pass"),
    ('23', "Light pass 1", "Light pass 1"),
    ('24', "Light pass 2", "Light pass 2"),
    ('25', "Light pass 3", "Light pass 3"),
    ('26', "Light pass 4", "Light pass 4"),
    ('27', "Light pass 5", "Light pass 5"),
    ('28', "Light pass 6", "Light pass 6"),
    ('29', "Light pass 7", "Light pass 7"),
    ('30', "Light pass 8", "Light pass 8"),
    ('31', "Noise", "Noise pass"),
    ('32', "Shadow", "Shadow pass"),
    ('33', "Irradiance", "Irradiance pass"),
    ('34', "Light Direction", "Light Direction pass"),
    ('35', "Volume", "Volume pass"),
    ('36', "Volume Mask", "Volume Mask pass"),
    ('37', "Volume Emission", "Volume Emission pass"),
    ('38', "Volume Z-Depth Front", "Volume Z-Depth Front pass"),
    ('39', "Volume Z-Depth Back", "Volume Z-Depth Back pass"),

    ('43', "Denoiser Beauty", "Denoiser Beauty pass"),
    ('44', "Denoiser DiffDir", "Denoiser Diffuse Direct pass"),
    ('45', "Denoiser DiffIndir", "Denoiser Diffuse Indirect pass"),
    ('46', "Denoiser ReflectDir", "Denoiser Reflection Direct pass"),
    ('47', "Denoiser ReflectIndir", "Denoiser Reflection Indirect pass"),
    #('48', "Denoiser Refraction", "Denoiser Refraction pass"),
    ('49', "Denoiser Remainder", "Denoiser Remainder pass"),
    ('76', "Denoiser Emission", "Denoiser Emission pass"),
    ('74', "Denoiser Volume", "Denoiser Volume pass"),
    ('75', "Denoiser Volume Emission", "Denoiser Volume Emission pass"),

    ('54', "Ambient light direct", "Ambient light direct pass"),
    ('55', "Ambient light indirect", "Ambient light indirect pass"),
    ('56', "Sunlight direct", "Sunlight direct pass"),
    ('57', "Sunlight indirect", "Sunlight indirect pass"),
    ('58', "Light pass 1 direct", "Light pass 1 direct"),    
    ('59', "Light pass 2 direct", "Light pass 2 direct"),
    ('60', "Light pass 3 direct", "Light pass 3 direct"),
    ('61', "Light pass 4 direct", "Light pass 4 direct"),
    ('62', "Light pass 5 direct", "Light pass 5 direct"),
    ('63', "Light pass 6 direct", "Light pass 6 direct"),
    ('64', "Light pass 7 direct", "Light pass 7 direct"),
    ('65', "Light pass 8 direct", "Light pass 8 direct"),   
    ('66', "Light pass 1 indirect", "Light pass 1 indirect"),    
    ('67', "Light pass 2 indirect", "Light pass 2 indirect"),
    ('68', "Light pass 3 indirect", "Light pass 3 indirect"),
    ('69', "Light pass 4 indirect", "Light pass 4 indirect"),
    ('70', "Light pass 5 indirect", "Light pass 5 indirect"),
    ('71', "Light pass 6 indirect", "Light pass 6 indirect"),
    ('72', "Light pass 7 indirect", "Light pass 7 indirect"),
    ('73', "Light pass 8 indirect", "Light pass 8 indirect"),       

    ('1000', "Geometric normals", "Geometric normals pass"),
    ('1001', "Shading normals", "Shading normals pass"),
    ('1002', "Position", "Position pass"),
    ('1003', "Z-depth", "Z-depth pass"),
    ('1004', "Material id", "Material id pass"),
    ('1005', "UV coordinates", "UV coordinates pass"),
    ('1006', "Tangents", "Tangents pass"),
    ('1007', "Wireframe", "Wireframe pass"),
    ('1008', "Smooth normals", "Smooth normals pass"),
    ('1009', "Object id", "Object id pass"),    
    ('1010', "Ambient occlusion", "Ambient occlusion pass"),
    ('1011', "Motion vector", "Motion vector pass"),
    ('1012', "Render layer ID", "Colours objects on the same layer with the same color based on the render layer ID"),
    ('1013', "Render layer mask", "Mask for geometry on the active render layer"),
    ('1014', "Light pass ID", "Light pass ID pass"),
    ('1015', "Tangent normals", "Tangent normals pass"),
    ('1016', "Info Opacity", "Assigns a colour to the camera ray's hit point proportional to the opacity of the geometry"),
    ('1017', "Baking group ID", "Colours each distinct baking group in the scene with a colour based on it's ID"),
    ('1018', "Info Roughness", "Material roughness at the camera ray's hit point"),
    ('1019', "Info IOR", "Material index of refraction at the camera ray's hit point"),
    ('1020', "Info DiffFilter", "The diffuse texture color of the diffuse and glossy material"),
    ('1021', "Info ReflectFilter", "The reflection texture color of the specular and glossy material"),
    ('1022', "Info RefractFilter", "The refraction texture color of the specular material"),    
    ('1023', "Info TransmFilter", "The transmission texture color of the diffuse material"),    
    ('1024', "Object layer color", "The color specified in the object layer node"),

    ('2001', "Cryptomatte MaterialName", "Cryptomatte channels for material node names"), 
    ('2006', "Cryptomatte MaterialNode", "Cryptomatte channels using distinct material nodes"),    
    ('2002', "Cryptomatte MaterialPinName", "Cryptomatte channels for material pin names"), 
    ('2003', "Cryptomatte ObjectName", "Cryptomatte channels for object layer node names"), 
    ('2004', "Cryptomatte ObjectNode", "Cryptomatte channels using distinct object layer nodes"),    
    ('2007', "Cryptomatte ObjectPinName", "Cryptomatte channels for object layer pin names"), 
    
    ('2005', "Cryptomatte InstanceID", "Cryptomatte channels for instance IDs"),    
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

info_pass_sampling_modes = (
    ('0', "Distributed rays", ""),
    ('1', "Non-distributed with pixel filtering", ""),
    ('2', "Non-distributed without pixel filtering", ""),
    )

adaptive_group_pixels = (
    ('1', "None", ""),
    ('2', "2 x 2", ""),
    ('4', "4 x 4", ""),
    )

rotation_orders = (
    ('0', "XYZ", ""),
    ('1', "XZY", ""),
    ('2', "YXZ", ""),
    ('3', "YZX", ""),
    ('4', "ZXY", ""),
    ('5', "ZYX", ""),
    )

octane_preset_shaders = (
    ('None', "None", '', 0),
    ('Smoke', "Smoke", '', 1),
)

light_ids_action_type = (
    ('Disable', "Disable", '', 1),
    ('Enable', "Enable", '', 0),
)

clay_modes = (
    ('None', "None", "", 0),
    ('Grey', "Grey", "", 1),
    ('Color', "Color", "", 2),
)

priority_modes = (
    ('Low', "Low", "", 0),
    ('Medium', "Medium", "", 1),
    ('High', "High", "", 2),
)

cryptomatte_pass_channel_modes = (
    ('2', "2", "", 2),
    ('4', "4", "", 4),
    ('6', "6", "", 6),
    ('8', "8", "", 8),
    ('10', "10", "", 10),        
)

up_sample_modes = (
    ('No subsampling', "No subsampling", "", 1),
    ('2x2 upsampling', "2x2 upsampling", "", 2),
    ('4x4 upsampling', "4x4 upsampling", "", 4),    
)


def get_int_response_type(cls):
    return int(cls.response_type)

def sync_baking_transform(self, context):
    scene = bpy.context.scene
    oct_scene = scene.octane
    baking_layer_settings = oct_scene.baking_layer_settings  
    oct_cam = bpy.data.cameras['Camera'].octane    
    if baking_layer_settings._get_baking_layer_by_idx(oct_cam.baking_group_id) is None:
        baking_layer_settings._add_new_baking_layer(oct_cam.baking_group_id)
    for transform in baking_layer_settings.baking_layer_transform_collections.values():
        if transform.id == oct_cam.baking_group_id:
            oct_cam.baking_uvw_translation = transform.translation
            oct_cam.baking_uvw_rotation = transform.rotation
            oct_cam.baking_uvw_scale = transform.scale
            oct_cam.baking_uvw_rotation_order = transform.rotation_order


def update_octane_localdb_path():
    import _octane
    import os
    octane_localdb_path = ""
    try:
        cur_path = str(bpy.context.preferences.addons[__package__].preferences.octane_localdb_path)
        if len(cur_path):
            cur_path = str(bpy.path.abspath(cur_path))            
            if not cur_path.endswith(os.sep):
                cur_path += os.sep            
        octane_localdb_path = cur_path                          
    except:
        pass
    _octane.update_octane_localdb(octane_localdb_path)   


def update_octane_server_address():
    import _octane
    import os
    octane_server_address = ""
    enable_relese_octane_license_when_exiting = False
    try:
        octane_server_address = str(bpy.context.preferences.addons[__package__].preferences.octane_server_address)  
        enable_relese_octane_license_when_exiting = bool(bpy.context.preferences.addons[__package__].preferences.enable_relese_octane_license_when_exiting)
    except:
        pass
    _octane.update_octane_server_address(octane_server_address, enable_relese_octane_license_when_exiting)   


def update_octane_params():
    import _octane
    default_material_id = 0
    try:
        default_material_id = int(bpy.context.preferences.addons[__package__].preferences.default_material_id)  
    except:
        pass
    _octane.set_octane_params(default_material_id)      


def update_octane_vdb_helper(cls):
    cls.octane_vdb_helper = cls.is_octane_vdb and 'F$' in cls.imported_openvdb_file_path


def update_octane_data():
    update_octane_localdb_path()
    update_octane_server_address()
    update_octane_params()


class OctaneBakingLayerTransform(bpy.types.PropertyGroup):    
    id: IntProperty(
            name="Baking Layer ID",
            min=1, max=65535,
            default=1,                
            )   
    translation: FloatVectorProperty(
            name="Translation",                                
            subtype='TRANSLATION',
            )      
    rotation: FloatVectorProperty(
            name="Rotation",                             
            subtype='EULER',
            )    
    scale: FloatVectorProperty(
            name="Scale",                             
            subtype='XYZ',
            default=(1, 1, 1)
            )  
    rotation_order: EnumProperty(
            name="Rotation order",
            items=rotation_orders,
            default='2',
            )


def OctaneBakingLayerTransformCollection_update_cur_baking_layer_id(self, context):
    return self.update_cur_baking_layer_id(context)

def OctaneBakingLayerTransformCollection_update_cur_baking_layer_transform(self, context):
    return self.update_cur_baking_layer_transform(context)

class OctaneBakingLayerTransformCollection(bpy.types.PropertyGroup):    
    baking_layer_transform_collections: CollectionProperty(type=OctaneBakingLayerTransform)
    #init default baking layer
    cur_baking_layer_id: IntProperty(
            name="Baking Layer ID",
            description="ID of the baking layer",
            update=OctaneBakingLayerTransformCollection_update_cur_baking_layer_id,
            min=1, max=65535,
            default=1,
            )
    cur_baking_layer_translation: FloatVectorProperty(
            name="Translation",
            description="Translation that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",   
            update = OctaneBakingLayerTransformCollection_update_cur_baking_layer_transform,                             
            subtype='TRANSLATION',
            )      
    cur_baking_layer_rotation: FloatVectorProperty(
            name="Rotation",
            description="Rotation that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = OctaneBakingLayerTransformCollection_update_cur_baking_layer_transform,
            subtype='EULER',
            )    
    cur_baking_layer_scale: FloatVectorProperty(
            name="Scale",
            description="Scale that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = OctaneBakingLayerTransformCollection_update_cur_baking_layer_transform,
            subtype='XYZ',
            default=(1, 1, 1)
            )        
    cur_baking_layer_rotation_order: EnumProperty(
            name="Rotation order",
            description="Rotation order that affects the way the UVs from that object layer are projected into the UV space when rendered using the baking camera",                                
            update = OctaneBakingLayerTransformCollection_update_cur_baking_layer_transform,
            items=rotation_orders,
            default='2',
            )       

    @classmethod
    def register(cls):
        pass

    @classmethod
    def unregister(cls):
        pass

    def init(self):
        if not len(self.baking_layer_transform_collections):      
            next_new_baking_layer = self.baking_layer_transform_collections.add()
            next_new_baking_layer.id = 1

    def _add_new_baking_layer(self, idx):
        #print('_add_new_baking_layer', idx)
        next_new_baking_layer = self.baking_layer_transform_collections.add()
        next_new_baking_layer.id = idx

    def _get_baking_layer_by_idx(self, idx):
        #print('_get_baking_layer_by_idx', idx)
        for baking_layer_transform in self.baking_layer_transform_collections.values():
            if idx == baking_layer_transform.id:
                #print('Found', idx)
                return baking_layer_transform
        #print('return None')
        return None        

    def _debug_show_all_baking_layer_info(self):
        for baking_layer_transform in self.baking_layer_transform_collections.values():
            print("Baking Group ID: ", baking_layer_transform.id)
            print(baking_layer_transform.translation)
            print(baking_layer_transform.rotation)
            print(baking_layer_transform.scale)
            print("Rotation Order: ", baking_layer_transform.rotation_order)

    def _delay_init(self):
        if self._get_baking_layer_by_idx(1) is None:
            self._add_new_baking_layer(1)
            return False       
        if not self.__contains__('cur_baking_layer_translation') or not self.__contains__('cur_baking_layer_rotation') or not self.__contains__('cur_baking_layer_scale') or not self.__contains__('cur_baking_layer_rotation_order'):
            self['cur_baking_layer_translation'] = self.cur_baking_layer_translation
            self['cur_baking_layer_rotation'] = self.cur_baking_layer_rotation
            self['cur_baking_layer_scale'] = self.cur_baking_layer_scale
            self['cur_baking_layer_rotation_order'] = self.cur_baking_layer_rotation_order
        return True

    def update_cur_baking_layer_id(self, context):
        # print('update_cur_baking_layer_id: ', self.cur_baking_layer_id)                
        # print('Before: ')
        # self._debug_show_all_baking_layer_info()
        #make sure it is initialized
        if not self._delay_init():
            return
        if self._get_baking_layer_by_idx(self.cur_baking_layer_id) is None:
            self._add_new_baking_layer(self.cur_baking_layer_id)
        # print('After: ')
        self._debug_show_all_baking_layer_info()
        cur_baking_transform = self._get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            self['cur_baking_layer_id'] = cur_baking_transform.id
            self['cur_baking_layer_translation'] = cur_baking_transform.translation
            self['cur_baking_layer_rotation'] = cur_baking_transform.rotation
            self['cur_baking_layer_scale'] = cur_baking_transform.scale
            self['cur_baking_layer_rotation_order'] = cur_baking_transform.rotation_order
        sync_baking_transform()

    def update_cur_baking_layer_transform(self, context):
        #make sure it is initialized
        if not self._delay_init():
            return
        cur_baking_transform = self._get_baking_layer_by_idx(self.cur_baking_layer_id)
        if cur_baking_transform:
            cur_baking_transform.translation = self['cur_baking_layer_translation']
            cur_baking_transform.rotation = self['cur_baking_layer_rotation']
            cur_baking_transform.scale = self['cur_baking_layer_scale']
            cur_baking_transform.rotation_order = str(self['cur_baking_layer_rotation_order'])
        sync_baking_transform()



def OctaneSpecificNodeCollection_update_function(self, context):
    self.update_nodes(context)

class OctaneGeoNode(bpy.types.PropertyGroup):    
    name: StringProperty(name="Octane Geo Node Name")  

class OctaneGeoNodeCollection(bpy.types.PropertyGroup):    
    osl_geo_nodes: CollectionProperty(type=OctaneGeoNode)

    node_graph_tree: StringProperty(
            name="Node Graph",
            description="The node graph containing target osl geometric node",
            default="",
            update=OctaneSpecificNodeCollection_update_function,
            maxlen=512,
            )   

    osl_geo_node: StringProperty(
            name="Octane Geo Node",
            description="Octane Geo Node(Vectron or Geometric primitives)",
            default="",
            maxlen=512,
            ) 

    def update_nodes(self, context):  
        print('Update OSL GEO Nodes') 
        for i in range(0, len(self.osl_geo_nodes)):
            self.osl_geo_nodes.remove(0)  
        if bpy.data.materials:      
            for mat in bpy.data.materials.values():
                if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                    continue
                if mat.name != self.node_graph_tree:
                    continue
                for node in mat.node_tree.nodes.values():
                    if node.bl_idname in ('ShaderNodeOctVectron'):                        
                        self.osl_geo_nodes.add()
                        self.osl_geo_nodes[-1].name = node.name


class OctaneOSLCameraNode(bpy.types.PropertyGroup):    

    name: StringProperty(
            name="Node Name"          
            )   


def OctaneOSLCameraNodeCollection_update_nodes(self, context):
	return self.update_nodes(context)


class OctaneOSLCameraNodeCollection(bpy.types.PropertyGroup):    

    osl_camera_nodes: CollectionProperty(type=OctaneOSLCameraNode)

    osl_camera_material_tree: StringProperty(
            name="Material Node Graph",
            description="Material node graph containing target osl camera node",
            default="",
            update=OctaneOSLCameraNodeCollection_update_nodes,
            maxlen=512,
            )   

    osl_camera_node: StringProperty(
            name="OSL Camera",
            description="OSL Camera Node",
            default="",
            update=OctaneOSLCameraNodeCollection_update_nodes,
            maxlen=512,
            )   

    @classmethod
    def unregister(cls):
        pass

    def update_nodes(cls, context):   
        for i in range(0, len(cls.osl_camera_nodes)):
            cls.osl_camera_nodes.remove(0)  
        if bpy.data.materials:      
            for mat in bpy.data.materials.values():
                if not getattr(mat, 'node_tree', None) or not getattr(mat.node_tree, 'nodes', None):
                    continue
                if mat.name != cls.osl_camera_material_tree:
                    continue
                for node in mat.node_tree.nodes.values():
                    if node.bl_idname in ('ShaderNodeOctOSLCamera', 'ShaderNodeOctOSLBakingCamera'):                        
                        cls.osl_camera_nodes.add()
                        cls.osl_camera_nodes[-1].name = node.name


class OctaneAIUpSamplertSettings(bpy.types.PropertyGroup):
    sample_mode: EnumProperty(
        name="Sampling mode",
        description="The sub/up-sample mode that should be used for rendering",
        items=up_sample_modes,
        default='No subsampling',
    )
    enable_ai_up_sampling: BoolProperty(
        name="Enable AI up-sampling",
        description="Enables the AI up-sampling when the sampling mode is one of the up-samples, and this toggle is on. Otherwise we just trivially scale up the frame",
        default=True,
    )           
    up_sampling_on_completion: BoolProperty(
        name="Up-sampling on completion",
        description="If enabled, beauty passes will be up-sampled only once at the end of a render",
        default=True,
    )   
    min_up_sampler_samples: IntProperty(
        name="Min. up-sampler samples",
        description="Minimum number of samples per pixel until up-sampler kicks in. Only valid when the the sampling mode is any of up-sampling",
        min=1, max=100000,
        default=10,                
    )     
    max_up_sampler_interval: IntProperty(
        name="Max. up-sampler interval",
        description="Maximum interval between up-sampler runs (in seconds). Only valid when the the sampling mode is any of up-sampling",
        min=1, max=120,
        default=10,                
    )

    @classmethod
    def register(cls):
        bpy.types.Object.octane_ai_sampler = PointerProperty(
            name="Octane AI UpSampler Settings",
            description="Octane AI up-sampler settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane_ai_sampler


class OctanePreferences(bpy.types.AddonPreferences):
    bl_idname = __package__

    default_material_id: EnumProperty(
            name="Default Material Type",
            description="Material to use for default (rendering with Octane)",   
            items=default_material_orders,   
            default="7", # Universal
            )
    default_texture_node_layout_id: EnumProperty(
            name="Texture Node Menu Layout",
            description="Layout of texture node menus(reboot blender to take effect)",   
            items=texture_node_layouts,         
            )

    default_use_blender_builtin_render_layer: BoolProperty(
            name="Use Blender Built-in Render Layer",
            description="Whether to use blender built-in render layer system for default(reboot blender to take effect)",   
            default=False,         
            )

    enable_empty_gpus_automatically: BoolProperty(
                name="Empty GPUs After Render",
                description="Empty GPU resources after rendering automatically",
                default=False,
            )

    enable_generate_default_uvs: BoolProperty(
                name="Generate Default UVs",
                description="Generate a default UV map",
                default=False,
            )

    enable_node_graph_upload_opt: BoolProperty(
                name="Node Graph Upload Optimization",
                description="Do not upload nodes that are not used",
                default=False,
            )  
    enable_mesh_upload_optimization: BoolProperty(
                name="Optimized Mesh Generation Mode",
                description="Do not regenerate & upload meshes(except reshapble ones) which are already cached",
                default=True,
            )   
    octane_localdb_path: StringProperty(
                name="Octane LocalDB Path",
                description="Customize octane localDB path. Leave empty to use default settings",
                default='',
                subtype='FILE_PATH',
            )   
    enable_relese_octane_license_when_exiting: BoolProperty(
                name="Release Octane License After Exiting",
                description="Release Octane license after exiting blender",
                default=False,
            )       
    octane_server_address: StringProperty(
            name="Server address",
            description="Octane render-server address",
            default="127.0.0.1",
            maxlen=255,
            )                           

    def draw(self, context):
        layout = self.layout
        layout.row().prop(self, "octane_server_address", expand=False) 
        layout.row().prop(self, "enable_relese_octane_license_when_exiting", expand=False)   
        layout.row().prop(self, "octane_localdb_path", expand=False)               
        layout.row().prop(self, "default_material_id", expand=False)
        layout.row().prop(self, "default_texture_node_layout_id", expand=False)     
        # layout.row().prop(self, "enable_empty_gpus_automatically", expand=False)
        # layout.row().prop(self, "enable_generate_default_uvs", expand=False)
        # layout.row().prop(self, "enable_node_graph_upload_opt", expand=False)        
        # layout.row().prop(self, "enable_mesh_upload_optimization", expand=False)          
        import _octane
        # _octane.update_default_mat_id(int(self.default_material_id))        
        # _octane.update_generate_default_uvs(int(self.enable_generate_default_uvs))        
        # _octane.update_octane_upload_opt(int(self.enable_node_graph_upload_opt), int(self.enable_mesh_upload_optimization))
        update_octane_data()


class OctaneRenderSettings(bpy.types.PropertyGroup):

# ################################################################################################
# OCTANE BLENDER RENDER VERSION
# ################################################################################################        
    octane_blender_version: StringProperty(
        name="",
        description="",
        default="",
        maxlen=128,
    )  
# ################################################################################################
# OCTANE OPTIMIZATION
# ################################################################################################        
    octane_opt_mesh_generation: BoolProperty(
        name="Use Opt. Mesh Generation Mode in Preview",
        description="[PREVIEW MODE] Do not regenerate & upload meshes(except reshapble ones) which are already cached",
        default=False,
    )        
# ################################################################################################
# OCTANE RENDER PASSES
# ################################################################################################
    use_passes: BoolProperty(
            name="Render passes",
            description="",
            default=False,
            )

    info_pass_max_samples: IntProperty(
            name="Info pass max samples",
            description="The maximum number of samples for the info passes (excluding AO)",
            min=1, max=1024,
            default=128,
            )
    info_pass_sampling_mode: EnumProperty(
            name="Sampling mode",
            description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
                "'Distributed rays':"
                " Enables motion blur and DOF, and also enables pixel filtering.\n"
                "'Non-distributed with pixel filtering':"
                " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
                "'Non-distributed without pixel filtering':"
                " Disables motion blur and DOF, and disables pixel filtering for all render passes"
                " except for render layer mask and ambient occlusion\n",
            items=info_pass_sampling_modes,
            default='0',
            )
    info_pass_z_depth_max: FloatProperty(
            name="Z-depth max",
            description="Z-depth value mapped to white (0 is mapped to black)",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=5.0,
            step=10,
            precision=4,
            )
    info_pass_uv_max: FloatProperty(
            name="UV max",
            description="UV coordinate value mapped to maximum intensity",
            min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
            default=1.0,
            step=10,
            precision=5,
            )
    info_pass_uv_coordinate_selection: IntProperty(
            name="UV coordinate selection",
            description="Determines which set of UV coordinates to use",
            min=1, max=3,
            default=1,
            )        
    info_pass_max_speed: FloatProperty(
            name="Max speed",
            description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
            min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
            default=1.0,
            step=10,
            precision=5,
            )
    info_pass_ao_distance: FloatProperty(
            name="AO distance",
            description="Ambient occlusion distance",
            min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
            default=3.0,
            step=10,
            precision=2,
            )
    info_pass_alpha_shadows: BoolProperty(
            name="AO alpha shadows",
            description="Take into account alpha maps when calculating ambient occlusion",
            default=False,
            )
    pass_raw: BoolProperty(
            name="Raw",
            description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray",
            default=False,
            )
    pass_pp_env: BoolProperty(
            name="Include environment",
            description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled",
            default=False,
            )
    info_pass_bump: BoolProperty(
            name="Bump and normal mapping",
            description="Take bump and normal mapping into account for shading normal output and wireframe shading",
            default=True,
            )
    info_pass_opacity_threshold: FloatProperty(
            name="Opacity threshold",
            description="Geometry with opacity higher or equal to this value is treated as totally opaque",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    cryptomatte_pass_channels: EnumProperty(
            name="Channels",
            description="Amount of cryptomatte channels to render",
            items=cryptomatte_pass_channel_modes,
            default='2',
            )
    cryptomatte_seed_factor: IntProperty(
            name="Cryptomatte seed factor",
            description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. Low values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs",
            min=4, max=25,
            default=10,
            )   

    cur_pass_type: EnumProperty(
            name="Preview pass type",
            description="Pass used for preview rendering",
            items=pass_types,
            default='0',
            )

# ################################################################################################
# OCTANE BAKING LAYER TRANSFORMS
# ################################################################################################
    baking_layer_settings = PointerProperty(
        name="Octane Baking Layer Transforms",
        description="",
        type=OctaneBakingLayerTransformCollection,
    )

# ################################################################################################
# OCTANE LAYERS
# ################################################################################################
    layers_enable: BoolProperty(
            name="Enable",
            description="Tick to enable Octane render layers",
            default=False,
            )
    layers_current: IntProperty(
            name="Active layer ID",
            description="ID of the active render layer",
            min=1, max=255,
            default=1,
            )
    layers_invert: BoolProperty(
            name="Invert",
            description="All the non-active render layers become the active render layer and the active render layer becomes inactive",
            default=False,
            )
    layers_mode: EnumProperty(
            name="Mode",
            description="The render mode that should be used to render layers:\n"
                "\n"
                "'Normal':"
                " The beauty passes contain the active layer only and the render layer passes (shadows,"
                " reflections...) record the side-effects of the active render layer for those samples/pixels"
                " that are not obstructed by the active render layer.\n"
                "\n"
                "'Hide inactive layers':"
                " All geometry that is not on an active layer will be made invisible. No side effects"
                " will be recorded in the render layer passes, i.e. the render layer passes will be empty.\n"
                "\n"
                "'Only side effects':"
                " The active layer will be made invisible and the render layer passes (shadows, reflections...)"
                " record the side-effects of the active render layer. The beauty passes will be empty.\n"
                " This is useful to capture all side-effects without having the active layer obstructing those.\n"
                "\n"
                "'Hide from camera':"
                " Similar to 'Hide inactive layers' All geometry that is not on an active layer"
                " will be made invisible. But side effects(shadows, reflections...)will be recorded in the render layer passes\n"
                "\n",
            items=layer_modes,
            default='0',
            )                     


# ################################################################################################
# OCTANE OUT OF CORE
# ################################################################################################
    out_of_core_enable: BoolProperty(
            name="Enable out of core",
            description="Tick to enable Octane out of core",
            default=False,
            )
    out_of_core_limit: IntProperty(
            name="Out of core memory limit (MB)",
            description="Maximal amount of memory to be used for out-of-core textures",
            min=1,
            default=4096,
            )
    out_of_core_gpu_headroom: IntProperty(
            name="GPU headroom (MB)",
            description="To run the render kernels successfully, there needs to be some amount of free GPU memory. This setting determines how much GPU memory the render engine will leave available when uploading the images. The default value should work for most scenes",
            min=1,
            default=300,
            )

# ################################################################################################
# OCTANE COMMON
# ################################################################################################
    viewport_hide: BoolProperty(
            name="Viewport hide priority",
            description="Hide from final render objects hidden in viewport",
            default=False,
            )
    prefer_tonemap: BoolProperty(
            name="Prefer tonemap if applicable",
            description="Render as tonemapped image if applicable",
            default=True,
            )
    export_with_object_layers: BoolProperty(
            name="Export with object layers",
            description="Export with object layers properties. If disabled, all object layer properties will be removed and the whole scene will be put in a single object layer",
            default=True,
            )        
    meshes_type: EnumProperty(
            name="Render all meshes as",
            description="Override all meshes type by this type during rendering",
            items=meshes_render_types,
            default='4',
            )
    priority_mode: EnumProperty(
            name="Render Priority",
            description="Render priority that should be used for rendering",
            items=priority_modes,
            default='High',
            )        
    anim_mode: EnumProperty(
            name="Animation mode",
            description="Optimize animation rendering speed (use in conjunction with Octane mesh types, see the manual)",
            items=anim_modes,
            default='0',
            )
    devices: BoolVectorProperty(
            name="GPU",
            description="Devices to use for rendering",
            default=(True, False, False, False, False, False, False, False),
            size=8,
            )
    stand_login: StringProperty(
            name="Stand",
            description="Octane standalone login",
            default="",
            maxlen=128,
            )
    stand_pass: StringProperty(
            name="",
            description="Octane standalone password",
            default="",
            maxlen=128,
            )
    server_login: StringProperty(
            name="Plugin",
            description="Octane render-server login",
            default="",
            maxlen=128,
            )
    server_pass: StringProperty(
            name="",
            description="Octane render-server password",
            default="",
            maxlen=128,
            )

    mb_type: EnumProperty(
            name="Motion blur type",
            description="",
            items=mb_types,
            default='1',
            )
    mb_direction: EnumProperty(
            name="Shutter alignment",
            description="Specifies how the shutter interval is aligned to the current time",
            items=mb_directions,
            default='0',
            )
    shutter_time: FloatProperty(
            name="Shutter time",
            description="The shutter time percentage relative to the duration of a single frame",                
            default=20.0,                
            precision=0,
            min=0.0, soft_min=0.0, max=100000.0, soft_max=100.0,
            subtype='PERCENTAGE',
            )
    subframe_start: FloatProperty(
            name="Subframe start",
            description="Minimum sub-frame % time to sample",                
            default=0.0,
            precision=0,
            min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
            subtype='PERCENTAGE',
            )  
    subframe_end: FloatProperty(
            name="Subframe end",
            description="Maximum sub-frame % time to sample",                
            default=100.0,
            precision=0,
            min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
            subtype='PERCENTAGE',
            )                      


    kernel_type: EnumProperty(
            name="Kernel type",
            description="",
            items=kernel_types,
            default='1',
            )

    max_samples: IntProperty(
            name="Max. samples",
            description="Number of samples to render for each pixel",
            min=1, max=64000,
            default=500,
            )
    max_preview_samples: IntProperty(
            name="Max. preview samples",
            description="Number of samples to render for each pixel for preview",
            min=1, max=64000,
            default=100,
            )
    max_subdivision_level: IntProperty(
            name="Max. subdivision level",
            description="The Maximum subdivision level that should be applied on the geometries in the scene. Setting zero will disable the subdivision",
            min=0, max=10,
            default=10,
            )    
    filter_size: FloatProperty(
            name="Filter size",
            description="Film splatting width (to reduce aliasing)",
            min=1.0, soft_min=1.0, max=16.0, soft_max=16.0,
            default=1.2,
            step=10,
            precision=2,
            )
    ray_epsilon: FloatProperty(
            name="Ray epsilon",
            description="Shadow ray offset distance to avoid self-intersection",
            min=0.000001, soft_min=0.000001, max=0.1, soft_max=0.1,
            default=0.0001,
            step=10,
            precision=6,
            )
    alpha_channel: BoolProperty(
            name="Alpha channel",
            description="Enables a compositing alpha channel",
            default=False,
            )
    alpha_shadows: BoolProperty(
            name="Alpha shadows",
            description="Enables direct light through opacity maps. If disabled, ray tracing will be faster but renders incorrect shadows for alpha-mapped geometry or specular materials with \"fake shadows\" enabled",
            default=True,
            )
    keep_environment: BoolProperty(
            name="Keep environment",
            description="Keeps environment with enabled alpha channel",
            default=False,
            )
    irradiance_mode: BoolProperty(
            name="Irradiance mode",
            description="Render the first surface as a white diffuse material",
            default=False,
            )  
    ai_light_enable: BoolProperty(
            name="AI light",
            description="Enables AI light",
            default=False,
            )   
    ai_light_update: BoolProperty(
            name="AI light update",
            description="Enables dynamic AI light update",
            default=True,
            )    
    ai_light_strength: FloatProperty(
            name="AI light strength",
            description="The strength for dynamic AI light update",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.8,
            step=1,
            precision=3,
            )    
    light_ids_action: EnumProperty(
            name="Light IDs action",
            description="The action to be taken on selected lights IDs",
            items=light_ids_action_type,
            default='Disable',
            )    
    light_id_sunlight: BoolProperty(
            name="Sunlight",
            description="Sunlight",
            default=False,
            )           
    light_id_env: BoolProperty(
            name="Environment",
            description="Environment",
            default=False,
            )    
    light_id_pass_1: BoolProperty(
            name="Pass 1",
            description="Pass 1",
            default=False,
            ) 
    light_id_pass_2: BoolProperty(
            name="Pass 2",
            description="Pass 2",
            default=False,
            ) 
    light_id_pass_3: BoolProperty(
            name="Pass 3",
            description="Pass 3",
            default=False,
            ) 
    light_id_pass_4: BoolProperty(
            name="Pass 4",
            description="Pass 4",
            default=False,
            ) 
    light_id_pass_5: BoolProperty(
            name="Pass 5",
            description="Pass 5",
            default=False,
            ) 
    light_id_pass_6: BoolProperty(
            name="Pass 6",
            description="Pass 6",
            default=False,
            ) 
    light_id_pass_7: BoolProperty(
            name="Pass 7",
            description="Pass 7",
            default=False,
            ) 
    light_id_pass_8: BoolProperty(
            name="Pass 8",
            description="Pass 8",
            default=False,
            )            

    light_id_sunlight_invert: BoolProperty(
            name="Sunlight",
            description="Sunlight",
            default=False,
            )           
    light_id_env_invert: BoolProperty(
            name="Environment",
            description="Environment",
            default=False,
            )    
    light_id_pass_1_invert: BoolProperty(
            name="Pass 1",
            description="Pass 1",
            default=False,
            ) 
    light_id_pass_2_invert: BoolProperty(
            name="Pass 2",
            description="Pass 2",
            default=False,
            ) 
    light_id_pass_3_invert: BoolProperty(
            name="Pass 3",
            description="Pass 3",
            default=False,
            ) 
    light_id_pass_4_invert: BoolProperty(
            name="Pass 4",
            description="Pass 4",
            default=False,
            ) 
    light_id_pass_5_invert: BoolProperty(
            name="Pass 5",
            description="Pass 5",
            default=False,
            ) 
    light_id_pass_6_invert: BoolProperty(
            name="Pass 6",
            description="Pass 6",
            default=False,
            ) 
    light_id_pass_7_invert: BoolProperty(
            name="Pass 7",
            description="Pass 7",
            default=False,
            ) 
    light_id_pass_8_invert: BoolProperty(
            name="Pass 8",
            description="Pass 8",
            default=False,
            )                                                                                                                                                                  


    caustic_blur: FloatProperty(
            name="Caustic blur",
            description="Caustic blur for noise reduction",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=1,
            precision=3,
            )
    affect_roughness: FloatProperty(
            name="Affect roughness",
            description="The percentage of roughness affecting subsequent layers' roughness",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.2,
            step=1,
            precision=3,
            )       
    parallelism: IntProperty(
            name="Parallelism",
            description="Specifies the number of samples that are run in parallel. A small number means less parallel samples, less memory usage and it makes caustics visible faster, but renders probably slower. A large number means more memory usage, slower visible caustics and probably a higher speed",
            min=1, max=4,
            default=4,
            )

    specular_depth: IntProperty(
            name="Specular depth",
            description="The maximum path depth for which specular reflections/refractions are allowed",
            min=1, max=1024,
            default=5,
            )
    glossy_depth: IntProperty(
            name="Glossy depth",
            description="The maximum path depth for which glossy reflections are allowed",
            min=1, max=1024,
            default=2,
            )
    ao_dist: FloatProperty(
            name="AOdist",
            description="Maximum distance for environment ambient occlusion",
            min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
            default=3.0,
            step=1,
            precision=2,
            )
    ao_texture: StringProperty(
            name="AO ambient texture",
            description="Ambient occlusion environment texture, which is used for AO rays. If not specified, the environment will be used instead",
            default="",
            maxlen=512,
            )
    gi_mode: EnumProperty(
            name="GImode",
            description="Determines how global illumination is approximated",
            items=gi_modes,
            default='3',
            )
    clay_mode: EnumProperty(
            name="Clay Mode",
            description="The clay mode should be used in rendering",
            items=clay_modes,
            default='None',
            )        
    gi_clamp: FloatProperty(
            name="GI clamp",
            description="GI clamp reducing fireflies",
            min=0.001, soft_min=0.001, max=1000000.0, soft_max=1000000.0,
            default=1000000.0,
            step=1,
            precision=3,
            )
    diffuse_depth: IntProperty(
            name="Diffuse depth",
            description="The maximum path depth for which diffuse reflections are allowed",
            min=1, max=8,
            default=2,
            )
    max_diffuse_depth: IntProperty(
            name="Max. diffuse depth",
            description="The maximum path depth for which diffuse reflections are allowed",
            min=1, max=2048,
            default=8,
            )
    max_glossy_depth: IntProperty(
            name="Max. glossy depth",
            description="The maximum path depth for which specular reflections/refractions are allowed",
            min=1, max=2048,
            default=24,
            )
    max_scatter_depth: IntProperty(
            name="Max. scatter depth",
            description="The maximum path depth for which scattering is allowed",
            min=1, max=256,
            default=8,
            )                
    parallel_samples: IntProperty(
            name="Parallel samples",
            description="Specifies the number of samples that are run in parallel. A small number means less parallel samples and less memory usage, but potentially slower speed. A large number means more memory usage and potentially a higher speed",
            min=1, max=32,
            default=32,
            )
    max_tile_samples: IntProperty(
            name="Max. tile samples",
            description="The maximum samples we calculate until we switch to a new tile",
            min=1, max=64,
            default=64,
            )
    minimize_net_traffic: BoolProperty(
            name="Minimize net traffic",
            description="If enabled, the work is distributed to the network render slaves in such a way to minimize the amount of data that is sent to the network render master",
            default=True,
            )
    emulate_old_volume_behavior: BoolProperty(
            name="Emulate old volume behavior",
            description="Emulate the behavior of of emission and scattering of version 4.0 and earlier",
            default=False,
            )        
    deep_image: BoolProperty(
            name="Deep image",
            description="Render and save deep image file into output folder after frame render is finished",
            default=False,
            )
    deep_render_passes: BoolProperty(
            name="Deep image passes",
            description="Include render passes in deep pixels",
            default=False,
            )    
    max_depth_samples: IntProperty(
            name="Max. depth samples",
            description="Maximum number of depth samples per pixels",
            min=1, max=32,
            default=8,
            )
    depth_tolerance: FloatProperty(
            name="Depth tolerance",
            description="Depth samples whose relative depth difference falls below the tolerance value are merged together",
            min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
            default=0.05,
            step=1,
            precision=3,
            )
    work_chunk_size: IntProperty(
            name="Work chunk size",
            description="The number of work blocks (of 512K samples each) we do per kernel run. Increasing this value increases the memory usage on the system, but doesn't affect memory usage on the system and may increase render speed",
            min=1, max=32,
            default=8,
            )
    toon_shadow_ambient: FloatVectorProperty(
            name="Toon shadow ambient",
            description="The ambient modifier of toon shadowing",
            min=0.0, max=1.0,
            default=(0.5, 0.5, 0.5),
            subtype='COLOR',
            )     
    ao_alpha_shadows: BoolProperty(
            name="AO alpha shadows",
            description="Take into account alpha maps when calculating ambient occlusion",
            default=False,
            )
    opacity_threshold: FloatProperty(
            name="Opacity threshold",
            description="Geometry with opacity higher or equal to this value is treated as totally opaque",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=1,
            precision=3,
            )

    exploration: FloatProperty(
            name="Exploration strength",
            description="Effort on investigating good paths",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.7,
            step=10,
            precision=2,
            )
    direct_light_importance: FloatProperty(
            name="Direct light imp.",
            description="Computational effort on direct lighting",
            min=0.01, soft_min=0.01, max=1.0, soft_max=1.0,
            default=0.1,
            step=1,
            precision=2,
            )
    max_rejects: IntProperty(
            name="Max. rejects",
            description="Maximum number of consecutive rejects",
            min=100, max=10000,
            default=500,
            )

    info_channel_type: EnumProperty(
            name="Info-channel type",
            description="",
            items=info_channel_types,
            default='0',
            )
    zdepth_max: FloatProperty(
            name="Z-Depth max.",
            description="",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=5.0,
            step=100,
            precision=3,
            )
    uv_max: FloatProperty(
            name="UV max.",
            description="UV coordinate value mapped to maximum intensity",
            min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
            default=1.0,
            step=1,
            precision=5,
            )
    sampling_mode: EnumProperty(
            name="Sampling mode",
            description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
                "'Distributed rays':"
                " Enables motion blur and DOF, and also enables pixel filtering.\n"
                "'Non-distributed with pixel filtering':"
                " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
                "'Non-distributed without pixel filtering':"
                " Disables motion blur and DOF, and disables pixel filtering for all render passes"
                " except for render layer mask and ambient occlusion\n",
            items=info_pass_sampling_modes,
            default='0',
            )
    max_speed: FloatProperty(
            name="Max speed",
            description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
            min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
            default=1.0,
            step=100,
            precision=3,
            )

    bump_normal_mapping: BoolProperty(
            name="Bump and normal mapping",
            description="Take bump and normal mapping into account for shading normal output and wireframe shading",
            default=False,
            )
    wf_bkface_hl: BoolProperty(
            name="Wireframe backface highlighting",
            description="Show faces seen from the backside of the face normal in a different color in wireframe mode",
            default=False,
            )
    path_term_power: FloatProperty(
            name="Path term. power",
            description="Path may get terminated when ray power is less then this value",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.3,
            step=10,
            precision=2,
            )
    coherent_ratio: FloatProperty(
            name="Coherent ratio",
            description="Runs the kernel more coherently which makes it usually faster, but may require at least a few hundred samples/pixel to get rid of visible artifacts",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=2,
            )
    static_noise: BoolProperty(
            name="Static noise",
            description="If enabled, the noise patterns are kept stable between frames",
            default=False,
            )

    progressive: BoolProperty(
            name="Progressive",
            description="Use progressive sampling of lighting",
            default=True,
            )

    preview_pause: BoolProperty(
            name="Pause Preview",
            description="Pause viewport preview",
            default=False,
            )
    preview_active_layer: BoolProperty(
            name="Preview Active Layer",
            description="Preview active render layer in viewport",
            default=False,
            )
    hdr_tonemap_preview_enable: BoolProperty(
            name="Enable HDR tonemapping in Interactive Mode",
            description="Tick to enable Octane HDR tonemapping in interactive preview mode",
            default=False,
            )
    hdr_tonemap_render_enable: BoolProperty(
            name="Enable HDR tonemapping in Render Mode",
            description="Tick to enable Octane HDR tonemapping in render mode",
            default=False,
            )        
    use_preview_setting_for_camera_imager: BoolProperty(
            name="Override",
            description="If enabled, we use this setting in all cases(ignore what is set in octane cameras)",
            default=False,
            )  
    use_preview_post_process_setting: BoolProperty(
            name="Override",
            description="If enabled, we use this setting in all cases(ignore what is set in octane cameras)",
            default=False,
            )                     

    adaptive_sampling: BoolProperty(
            name="Adaptive sampling",
            description="If enabled, The Adaptive sampling stops rendering clean image parts and focuses on noisy image parts",
            default=False,
            )
    adaptive_noise_threshold: FloatProperty(
            name="Noise threshold",
            description="A pixel treated as noisy pixel if noise level is higher than this threshold. Only valid if the adaptive sampling or the noise render pass is enabled",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.03,
            step=3,
            precision=4,
            )
    adaptive_expected_exposure: FloatProperty(
            name="Expected exposure",
            description="The expected exposure should be approximately the same value as the exposure in the image or 0 to ignore these settings. Only valid if adaptive sampling is enabled",
            min=0.0, soft_min=0.0, max=10000, soft_max=4096.0,
            default=0.0,
            step=0.1,
            precision=4,
            )
    adaptive_min_samples: IntProperty(
            name="Min. adaptive samples",
            description="Minimum number of samples per pixel until adaptive sampling kicks inunto estimate initial noise level. Higher the value for high quality, but will increase render time. Only valid if adaptive sampling is enabled",
            min=2, soft_min=2, max=1000000, soft_max=1024,
            default=256,
            )
    adaptive_group_pixels: EnumProperty(
            name="Group pixels",
            description="Size of the pixel groups that are evaluated together to decide whether sampling should stop or not",
            items=adaptive_group_pixels,
            default='2',
            )

    #LEGACY COMPATIBILITY
    hdr_tonemap_enable: BoolProperty(
       name="Tonemapped HDR",
       description="",
       default=False,
    )    

    @classmethod
    def register(cls):
        bpy.types.Scene.octane = PointerProperty(
            name="Octane Render Settings",
            description="Octane render settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        pass


class OctaneCameraSettings(bpy.types.PropertyGroup):

    pan_mode: EnumProperty(
            name="Pan mode",
            description="The panoramic projection that should be used",
            items=camera_pan_modes,
            default='SPHERE',
            )
    fov_x: FloatProperty(
            name="FOV X",
            description="Horizontal field of view in degrees. Will be ignored if cube mapping is used",
            min=1.0, soft_min=1.0, max=360.0, soft_max=360.0,
            default=360.0,
            step=10,
            precision=3,
            )
    fov_y: FloatProperty(
            name="FOV Y",
            description="Vertical field of view in degrees. Will be ignored if cube mapping is used",
            min=1.0, soft_min=1.0, max=180.0, soft_max=180.0,
            default=360.0,
            step=10,
            precision=3,
            )
    persp_corr: BoolProperty(
            name="Persp. correction",
            description="Perspective correction keeps vertical lines parallel if up-vector is vertical",
            default=False,
            )
    stereo_mode: EnumProperty(
            name="Stereo mode",
            description="The modus operandi for stereo rendering",
            items=camera_stereo_modes,
            default='1',
            )
    stereo_out: EnumProperty(
            name="Stereo output",
            description="The output rendered in stereo mode",
            items=camera_stereo_outs,
            default='0',
            )
    stereo_dist: FloatProperty(
            name="Stereo distance",
            description="Distance between the left and right eye in stereo mode [m]",
            min=0.001, soft_min=0.001, max=2.0, soft_max=2.0,
            default=0.02,
            step=10,
            precision=3,
            )
    stereo_dist_falloff: FloatProperty(
            name="Stereo dist. falloff",
            description="Controls how quickly the eye distance gets reduced towards the poles. This is to reduce eye strain at the poles when the panorama is looked at in an HMD. A value of 1"
                " will reduce the eye distance more or less continuously from equator to the poles, which will create a relaxed viewing experience, but this will also cause flat surfaces"
                " to appear curved. A value smaller than 1 keeps the eye distance more or less constant for a larger latitude range above and below the horizon, but will then rapidly reduce"
                " the eye distance near the poles. This will keep flat surface flat, but cause more eye strain near the poles (which can be reduced again by setting the pano cutoff latitude"
                " to something < 90 degrees",
            min=0.001, soft_min=0.001, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    stereo_swap_eyes: BoolProperty(
            name="Swap eyes",
            description="Swaps left and right eye positions when stereo mode is showing both",
            default=False,
            )
    left_filter: FloatVectorProperty(
            name="Left filter",
            description="Left eye filter color",
            min=0.0, max=1.0,
            default=(1.0, 0.0, 0.812),
            subtype='COLOR',
            )
    right_filter: FloatVectorProperty(
            name="Right filter",
            description="Right eye filter color",
            min=0.0, max=1.0,
            default=(0.0, 1.0, 0.188),
            subtype='COLOR',
            )
    use_fstop: BoolProperty(
            name="Use F-Stop",
            description="Use F-Stop setting instead of aperture",
            default=False,
            )
    aperture: FloatProperty(
            name="Aperture",
            description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
            min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
            default=0.0,
            step=10,
            precision=2,
            )
    fstop: FloatProperty(
            name="F-Stop",
            description="Aperture to focal length ratio",
            min=0.5, soft_min=1.4, max=64.0, soft_max=16.0,
            default=2.8,
            step=10,
            precision=1,
            )
    aperture_edge: FloatProperty(
            name="Aperture edge",
            description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
            min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
            default=1.0,
            step=10,
            precision=2,
            )
    distortion: FloatProperty(
            name="Distortion",
            description="The amount of spherical distortion",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=2,
            )    
    autofocus: BoolProperty(
            name="Autofocus",
            description="If enabled, the focus will be kept on the closest visible surface at the center of the image",
            default=True,
            )
    pixel_aspect: FloatProperty(
            name="Pixel aspect",
            description="The X:Y aspect ratio of pixels",
            min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
            default=1.0,
            step=10,
            precision=2,
            )
    aperture_aspect: FloatProperty(
            name="Aperture aspect",
            description="The X:Y aspect ratio of the aperture",
            min=0.1, soft_min=0.1, max=10.0, soft_max=10.0,
            default=1.0,
            step=10,
            precision=2,
            )
    keep_upright: BoolProperty(
            name="Keep upright",
            description="If enabled, the panoramic camera is always oriented towards the horizon and the up-vector will stay (0, 1, 0), i.e. vertical",
            default=False,
            )
    blackout_lat: FloatProperty(
            name="Pano blackout lat.",
            description="The +/- latitude at which the panorama gets cut off, when stereo rendering is enabled. The area with higher latitudes will be blacked out. If set to 90, nothing will be"
                " blacked out. If set to 70, an angle of 2x20 degrees will be blacked out at both poles. If set to 0, everything will be blacked out",
            min=1.0, soft_min=1.0, max=90.0, soft_max=90.0,
            default=90.0,
            step=10,
            precision=3,
            )
    bokeh_rotation: FloatProperty(
            name="Bokeh rotation",
            description="The orientation of the bokeh shape",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    bokeh_roundedness: FloatProperty(
            name="Bokeh roundedness",
            description="The roundedness of the sides of the bokeh shapes",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    bokeh_sidecount: IntProperty(
            name="Bokeh side count",
            description="The number of edges making up the bokeh shape",
            min=3, soft_min=3, max=100, soft_max=12,
            default=6,
            )

    baking_camera: BoolProperty(
            name="Baking camera",
            description="Use as baking camera",
            default=False,
            )
    baking_revert: BoolProperty(
            name="Revert baking",
            description="If enabled, camera rays are flipped, which allows using the geometry as a lens",
            default=False,
            )
    baking_use_position: BoolProperty(
            name="Use baking position",
            description="Use the provided position for baking position-dependent artifacts",
            default=False,
            )
    baking_bkface_culling: BoolProperty(
            name="Backface culling",
            description="When using a baking position, tells whether to bake back geometry faces",
            default=True,
            )
    baking_tolerance: FloatProperty(
            name="Edge noise tolerance",
            description="Specifies the tolerance to either keep or discard edge noise",
            min=0.0, max=1.0,
            default=0.5,
            step=10,
            precision=2,
            )
    baking_uvbox_min_x: FloatProperty(
            name="UV box min. X",
            description="Coordinates in UV space of the the origin of the bounding region for baking",
            default=0.0,
            step=10,
            precision=2,
            )
    baking_uvbox_min_y: FloatProperty(
            name="UV box min. Y",
            description="Coordinates in UV space of the the origin of the bounding region for baking",
            default=0.0,
            step=10,
            precision=2,
            )
    baking_uvbox_size_x: FloatProperty(
            name="UV box size X",
            description="Size in UV space of the bounding region for baking",
            min=0.0001,
            default=1.0,
            step=10,
            precision=2,
            )
    baking_uvbox_size_y: FloatProperty(
            name="UV box size Y",
            description="Size in UV space of the bounding region for baking",
            min=0.0001,
            default=1.0,
            step=10,
            precision=2,
            )
    baking_group_id: IntProperty(
            name="Baking group ID",
            description="Specifies which baking group ID should be baked",
            min=1, max=65535,
            update=sync_baking_transform,
            default=1,
            )       
    baking_uvw_translation: FloatVectorProperty(
            name="Translation",                                
            subtype='TRANSLATION',
            )      
    baking_uvw_rotation: FloatVectorProperty(
            name="Rotation",                             
            subtype='EULER',
            )    
    baking_uvw_scale: FloatVectorProperty(
            name="Scale",                             
            subtype='XYZ',
            default=(1, 1, 1)
            )  
    baking_uvw_rotation_order: EnumProperty(
            name="Rotation order",
            items=rotation_orders,
            default='2',
            )
    baking_padding: IntProperty(
            name="Size",
            description="Number of pixels added to the UV map edges",
            min=0, max=16,
            default=4,
            )
    baking_uv_set: IntProperty(
            name="UV set",
            description="Determines which set of UV coordinates to use for baking camera",
            min=1, max=3,
            default=1,
            )
    
    osl_camera_node_collections: PointerProperty(
            name="Octane OSL Camera Nodes",
            description="",
            type=OctaneOSLCameraNodeCollection,
            ) 

    white_balance: FloatVectorProperty(
            name="White balance",
            description="White point color",
            min=0.0, max=1.0,
            default=(1.0, 1.0, 1.0),
            subtype='COLOR',
            )
    camera_imager_order: EnumProperty(
            name="Order",
            description="The order by which camera response curve, gamma and custom LUT are applied",
            items=camera_imager_orders,
            default='0',
            )        
    response_type: EnumProperty(
            name="Response type",
            description="Camera response curve",
            items=response_types,
            default='105',
            )        
    int_response_type: IntProperty(
            name="Int Response type",
            get=get_int_response_type,
            )        
    exposure: FloatProperty(
            name="Exposure",
            description="",
            min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
            default=1.0,
            step=10,
            precision=2,
            )
    gamma: FloatProperty(
            name="Gamma",
            description="Output gamma correction",
            min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
            default=1.0,
            step=10,
            precision=2,
            )
    vignetting: FloatProperty(
            name="Vignetting",
            description="Amount of lens vignetting",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.3,
            step=1,
            precision=2,
            )
    saturation: FloatProperty(
            name="Saturation",
            description="Amount of saturation",
            min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
            default=1.0,
            step=1,
            precision=2,
            )
    hot_pix: FloatProperty(
            name="Hotpixel removal",
            description="Luminance threshold for firefly reduction",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=1,
            precision=2,
            )
    premultiplied_alpha: BoolProperty(
            name="Premultiplied alpha",
            description="If enabled, we pre-multiply an alpha value",
            default=False,
            )
    min_display_samples: IntProperty(
            name="Min. display samples",
            description="Minumum number of samples before the first image is displayed",
            min=1, max=32,
            default=1,
            )
    dithering: BoolProperty(
            name="Dithering",
            description="Enables dithering to remove banding",
            default=False,
            )
    white_saturation: FloatProperty(
            name="White saturation",
            description="Controls if clipping is done per channel or not",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=1,
            precision=2,
            )
    highlight_compression: FloatProperty(
            name="Highlight compression",
            description="Reduces burned out highlights by compressing them and reducing their contrast",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=1,
            precision=2,
            )
    neutral_response: BoolProperty(
            name="Neutral response",
            description="If enabled, the camera response curve will not affect the colors",
            default=False,
            )
    max_tonemap_interval: IntProperty(
            name="Max. tonemap interval",
            description="Maximum interval between tonemaps (in seconds)",
            min=1, max=120,
            default=20,
            )
    disable_partial_alpha: BoolProperty(
            name="Disable partial alpha",
            description="Make pixels that are partially transparent (alpha > 0) fully opaque",
            default=False,
            )
    custom_lut: StringProperty(
            name="Custom LUT",
            description="If set the custom LUT is applied in the order as specified in 'Order'",
            default='',
            subtype='FILE_PATH',
            )                     
    lut_strength: FloatProperty(
            name="LUT Strength",
            description="",
            min=0, soft_min=0, max=1.0, soft_max=1.0,
            default=1.0,
            step=1,
            precision=3,  
            )   
    enable_denoising: BoolProperty(
            name="Enable Denoising",
            description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes",
            default=False,
            )
    denoise_volumes: BoolProperty(
            name="Denoise volumes",
            description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
            default=False,
            )            
    denoise_on_completion: BoolProperty(
            name="Denoise on completion",
            description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region",
            default=True,
            )        
    min_denoiser_samples: IntProperty(
            name="Min. denoiser samples",
            description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once option is false",
            min=1, max=100000,
            default=10, 
            )     
    max_denoiser_interval: IntProperty(
            name="Max. denoiser interval",
            description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is false",
            min=1, max=120,
            default=20, 
            )      
    denoiser_blend: FloatProperty(
            name="Blend",
            description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f results with fully denoised image and setting 1.f results with the original image. An intermediate value will produce a blend between the denoised image and the original image",
            min=0, max=1,
            step=0.1,
            precision=3,                
            default=0.0, 
            )                                          

    ai_up_sampler: PointerProperty(
            name="Octane AI Up-Sampler",
            description="",
            type=OctaneAIUpSamplertSettings,
            )  
    postprocess: BoolProperty(
            name="Postprocess",
            description="Enable post processing",
            default=False,
            )
    bloom_power: FloatProperty(
            name="Bloom power",
            description="",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=1.0,
            step=1,
            precision=3,
            )
    cut_off: FloatProperty(
            name="Cutoff",
            description="The minimum brightness of a pixel to have bloom and glare applied. The brightness measured after the application of the exposure. Increasing this value will decrease the overall brightness of bloom and glare, which can be compensated by increasing the bloom/glare power, but that's scene dependent",
            min=0.0, soft_min=0.0, max=1000.0, soft_max=1000.0,
            default=0.0,
            step=1,
            precision=3,
            )      
    glare_power: FloatProperty(
            name="Glare power",
            description="",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=0.01,
            step=1,
            precision=3,
            )
    glare_ray_count: IntProperty(
            name="Glare ray count",
            description="",
            min=1, max=8,
            default=3,
            )
    glare_angle: FloatProperty(
            name="Glare angle",
            description="",
            min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
            default=15.0,
            step=10,
            precision=1,
            )
    glare_blur: FloatProperty(
            name="Glare blur",
            description="",
            min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
            default=0.001,
            step=0.1,
            precision=3,
            )
    spectral_intencity: FloatProperty(
            name="Spectral intensity",
            description="",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    spectral_shift: FloatProperty(
            name="Spectral shift",
            description="",
            min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
            default=2.0,
            step=100,
            precision=3,
            )

    @classmethod
    def register(cls):
        bpy.types.Camera.octane = PointerProperty(
                name="OctaneRender Camera Settings",
                description="OctaneRender camera settings",
                type=cls,
                options={'HIDDEN'},
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Camera.octane


class OctaneSpaceDataSettings(bpy.types.PropertyGroup):

    use_fstop: BoolProperty(
            name="Use F-Stop",
            description="Use F-Stop setting instead of aperture",
            default=False,
            )
    aperture: FloatProperty(
            name="Aperture",
            description="Aperture (higher numbers give more defocus, lower numbers give a sharper image)",
            min=0.0, soft_min=0.0, max=100.0, soft_max=100.0,
            default=0.0,
            step=10,
            precision=2,
            )
    fstop: FloatProperty(
            name="F-Stop",
            description="Aperture to focal length ratio",
            min=0.5, soft_min=1.4, max=64.0, soft_max=16.0,
            default=2.8,
            step=10,
            precision=1,
            )
    aperture_edge: FloatProperty(
            name="Aperture edge",
            description="Modifies the bokeh of the DOF. A high value increases the contrast towards the edge",
            min=1.0, soft_min=1.0, max=3.0, soft_max=3.0,
            default=1.0,
            step=10,
            precision=2,
            )
    distortion: FloatProperty(
            name="Distortion",
            description="The amount of spherical distortion",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=2,
            )

    white_balance: FloatVectorProperty(
            name="White balance",
            description="White point color",
            min=0.0, max=1.0,
            default=(1.0, 1.0, 1.0),
            subtype='COLOR',
            )

    camera_imager_order: EnumProperty(
            name="Order",
            description="The order by which camera response curve, gamma and custom LUT are applied",
            items=camera_imager_orders,
            default='0',
            )        
    response_type: EnumProperty(
            name="Response type",
            description="Camera response curve",
            items=response_types,
            default='105',
            )
    int_response_type: IntProperty(
            name="Int Response type",
            get=get_int_response_type,
            )
    exposure: FloatProperty(
            name="Exposure",
            description="",
            min=0.001, soft_min=0.001, max=4096.0, soft_max=4096.0,
            default=1.0,
            step=10,
            precision=2,
            )
    gamma: FloatProperty(
            name="Gamma",
            description="Output gamma correction",
            min=0.1, soft_min=0.1, max=32.0, soft_max=32.0,
            default=1.0,
            step=10,
            precision=2,
            )
    vignetting: FloatProperty(
            name="Vignetting",
            description="Amount of lens vignetting",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.3,
            step=1,
            precision=2,
            )
    saturation: FloatProperty(
            name="Saturation",
            description="Amount of saturation",
            min=0.0, soft_min=0.0, max=4.0, soft_max=4.0,
            default=1.0,
            step=1,
            precision=2,
            )
    hot_pix: FloatProperty(
            name="Hotpixel removal",
            description="Luminance threshold for firefly reduction",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=1,
            precision=2,
            )
    premultiplied_alpha: BoolProperty(
            name="Premultiplied alpha",
            description="If enabled, we pre-multiply an alpha value",
            default=False,
            )
    min_display_samples: IntProperty(
            name="Min. display samples",
            description="Minumum number of samples before the first image is displayed",
            min=1, max=32,
            default=1,
            )
    dithering: BoolProperty(
            name="Dithering",
            description="Enables dithering to remove banding",
            default=False,
            )
    white_saturation: FloatProperty(
            name="White saturation",
            description="Controls if clipping is done per channel or not",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=1,
            precision=2,
            )
    highlight_compression: FloatProperty(
            name="Highlight compression",
            description="Reduces burned out highlights by compressing them and reducing their contrast",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=1,
            precision=2,
            )
    neutral_response: BoolProperty(
            name="Neutral response",
            description="If enabled, the camera response curve will not affect the colors",
            default=False,
            )
    max_tonemap_interval: IntProperty(
            name="Max. tonemap interval",
            description="Maximum interval between tonemaps (in seconds)",
            min=1, max=120,
            default=20,
            )
    disable_partial_alpha: BoolProperty(
            name="Disable partial alpha",
            description="Make pixels that are partially transparent (alpha > 0) fully opaque",
            default=False,
            )
    custom_lut: StringProperty(
            name="Custom LUT",
            description="If set the custom LUT is applied in the order as specified in 'Order'",
            default='',
            subtype='FILE_PATH',
            )       
    lut_strength: FloatProperty(
            name="LUT Strength",
            description="",
            min=0, soft_min=0, max=1.0, soft_max=1.0,
            default=1.0,
            step=1,
            precision=3,  
            )    
    enable_denoising: BoolProperty(
            name="Enable Denoising",
            description="Enables the spectral AI denoiser, which will denoise some beauty passes including the main beauty pass and writes the outputs into separate denoiser render passes",
            default=False,
            )
    denoise_volumes: BoolProperty(
            name="Denoise volumes",
            description="If enabled the spectral AI denoiser will denoise volumes in the scene otherwise not",
            default=False,
            )         
    denoise_on_completion: BoolProperty(
            name="Denoise on completion",
            description="If enabled, beauty passes will be denoised only once at the end of a render. This option should be disabled while rendering with an interactive region",
            default=True,
            )        
    min_denoiser_samples: IntProperty(
            name="Min. denoiser samples",
            description="Minimum number of samples per pixel until denoiser kicks in. Only valid when the denosie once option is false",
            min=1, max=100000,
            default=10, 
            )     
    max_denoiser_interval: IntProperty(
            name="Max. denoiser interval",
            description="Maximum interval between denoiser runs (in seconds). Only valid when the denosie once option is false",
            min=1, max=120,
            default=20, 
            )      
    denoiser_blend: FloatProperty(
            name="Blend",
            description="A value between 0.f to 1.f to blend the original image into the denoiser output. Setting 0.f results with fully denoised image and setting 1.f results with the original image. An intermediate value will produce a blend between the denoised image and the original image",
            min=0, max=1,
            step=0.1,
            precision=3,                
            default=0.0, 
            ) 

    ai_up_sampler: PointerProperty(
            name="Octane AI Up-Sampler",
            description="",
            type=OctaneAIUpSamplertSettings,
            )  
    postprocess: BoolProperty(
            name="Postprocess",
            description="Enable post processing",
            default=False,
            )
    bloom_power: FloatProperty(
            name="Bloom power",
            description="",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=1.0,
            step=1,
            precision=3,
            )
    cut_off: FloatProperty(
            name="Cutoff",
            description="",
            min=0.0, soft_min=0.0, max=1000.0, soft_max=1000.0,
            default=0.0,
            step=1,
            precision=3,
            )      
    glare_power: FloatProperty(
            name="Glare power",
            description="",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=0.01,
            step=1,
            precision=3,
            )
    glare_ray_count: IntProperty(
            name="Glare ray count",
            description="",
            min=1, max=8,
            default=3,
            )
    glare_angle: FloatProperty(
            name="Glare angle",
            description="",
            min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
            default=15.0,
            step=10,
            precision=1,
            )
    glare_blur: FloatProperty(
            name="Glare blur",
            description="",
            min=0.001, soft_min=0.001, max=0.2, soft_max=0.2,
            default=0.001,
            step=0.1,
            precision=3,
            )
    spectral_intencity: FloatProperty(
            name="Spectral intensity",
            description="",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    spectral_shift: FloatProperty(
            name="Spectral shift",
            description="",
            min=0.0, soft_min=0.0, max=6.0, soft_max=6.0,
            default=2.0,
            step=100,
            precision=3,
            )                                                   

    @classmethod
    def register(cls):
        bpy.types.Scene.oct_view_cam = PointerProperty(
                name="OctaneRender Camera Settings",
                description="OctaneRender camera settings",
                type=cls,
                options={'HIDDEN'},
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Scene.oct_view_cam


class OctaneWorldSettings(bpy.types.PropertyGroup):

    env_type: EnumProperty(
            name="Environment type",
            description="",
            items=environment_types,
            default='1',
            )
    #LEGACY COMPATIBILITY
    env_texture: StringProperty(
            name="Texture",
            description="LEGACY COMPATIBILITY",
            default="",
            maxlen=512,
            )        
    env_texture_ptr: PointerProperty(
            name="Texture",
            description="Environment texture pointer",
            type=bpy.types.Texture,                
            )

    env_power: FloatProperty(
            name="Power",
            description="Scale factor that is applied to the sun and sky",
            min=0, soft_min=0, max=1000.0, soft_max=1000.0,
            default=1.0,
            step=10,
            precision=3,
            )
    env_importance_sampling: BoolProperty(
            name="Importance sampling",
            description="Use importance sampling for image textures",
            default=True,
            )
    env_daylight_type: EnumProperty(
            name="Daylight type",
            description="",
            items=environment_daylight_types,
            default='1',
            )
    env_sundir_x: FloatProperty(
            name="Sun direction X",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    env_sundir_y: FloatProperty(
            name="Sun direction Y",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    env_sundir_z: FloatProperty(
            name="Sun direction Z",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=-0.0,
            step=10,
            precision=3,
            )
    env_turbidity: FloatProperty(
            name="Turbidity",
            description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light",
            min=2.0, soft_min=2.0, max=15.0, soft_max=15.0,
            default=2.2,
            step=10,
            precision=3,
            )
    env_northoffset: FloatProperty(
            name="North offset",
            description="Additional rotation offset on longitude",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    env_model: EnumProperty(
            name="Model",
            description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
            items=environment_daylight_models,
            default='1',
            )
    env_sky_color: FloatVectorProperty(
            name="Sky color",
            description="Base color of the sky, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.05, 0.3, 1.0),
            subtype='COLOR',
            )
    env_sunset_color: FloatVectorProperty(
            name="Sunset color",
            description="Color of the sky and sun at sunset, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.6, 0.12, 0.02),
            subtype='COLOR',
            )
    env_ground_color: FloatVectorProperty(
            name="Ground color",
            description="Base color of the ground, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.0, 0.0, 0.0),
            subtype='COLOR',
            )
    env_ground_start_angle: FloatProperty(
            name="Ground start angle",
            description="The angle (in degrees) below the horizon where the transition to the ground color starts",
            min=0.0, max=90.0,
            default=90.0,
            step=10,
            precision=4,
            )
    env_ground_blend_angle: FloatProperty(
            name="Ground blend angle",
            description="The angle over which the sky color transitions to the ground color",
            min=1.0, max=90.0,
            default=5.0,
            step=10,
            precision=4,
            )
    env_sun_size: FloatProperty(
            name="Sun size",
            description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
            min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
            default=1.0,
            step=10,
            precision=4,
            )
    env_longitude: FloatProperty(
            name="Longitude",
            description="Longitude of the location",
            min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
            default=4.4667,
            step=1,
            precision=4,
            )
    env_latitude: FloatProperty(
            name="Latitude",
            description="Latitude of the location",
            min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
            default=50.7667,
            step=1,
            precision=4,
            )
    env_day: IntProperty(
            name="Day",
            description="Day of the month of the time the sun direction should be calculated for",
            min=1, max=31,
            default=1,
            )
    env_month: IntProperty(
            name="Month",
            description="Month of the time the sun direction should be calculated for",
            min=1, max=12,
            default=3,
            )
    env_gmtoffset: IntProperty(
            name="GMT offset",
            description="The time zone as offset to GMT",
            min=-12, max=12,
            default=0,
            )
    env_hour: FloatProperty(
            name="Local time",
            description="The local time as hours since 0:00",
            min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
            default=14,
            step=100,
            precision=1,
            )
    env_med_radius: FloatProperty(
            name="Medium radius",
            description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius",
            min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
            default=1.0,
            step=3,
            precision=4,
            )
    #LEGACY COMPATIBILITY
    env_medium: StringProperty(
            name="Medium",
            description="LEGACY COMPATIBILITY",
            default="",
            maxlen=512,
            )        
    env_medium_ptr: PointerProperty(
            name="Medium",
            description="The medium in the environment (free space). Ignored when this environment is used as a the visible environment",
            type=bpy.types.Texture,                
            )        
    env_altitude: FloatProperty(
            name="Altitude",
            description="The camera altitude",
            min=0.1, soft_min=0.1, max=10000000000, soft_max=10000000000,
            default=1.0,
            step=3,
            precision=3,
            )
    env_star_field: PointerProperty(
            name="Star field",
            description="Star fields behind the planet",
            type=bpy.types.Texture,                
            )  
    env_ground_albedo: PointerProperty(
            name="Ground albedo",
            description="Surface texture map on the planet",
            type=bpy.types.Texture,
            )        
    env_ground_reflection: PointerProperty(
            name="Ground reflection",
            description="Specular texture map on the planet",
            type=bpy.types.Texture,                
            )   
    env_ground_glossiness: PointerProperty(
            name="Ground glossiness",
            description="The planetary glossiness",
            type=bpy.types.Texture,                
            )       
    env_ground_emission: PointerProperty(
            name="Ground emission",
            description="Surface texture map on the planet at night time",
            type=bpy.types.Texture,   
            )     
    env_ground_normal_map: PointerProperty(
            name="Ground normal map",
            description="Normal map on the planet",
            type=bpy.types.Texture,                
            ) 
    env_ground_elevation: PointerProperty(
            name="Ground elevation",
            description="Elevation map on the planet",
            type=bpy.types.Texture,                
            )  
    env_planetary_axis: FloatVectorProperty(
            name="Planetary axis",
            description="The rotational axis of the planet running through the North and South pole",
            min=-1.0, max=1.0,
            default=(0.0, 0.0, 1.0),
            subtype='XYZ',
            )   
    env_planetary_angle: FloatProperty(
            name="Planetary angle",
            description="The rotation around the planetary axis",
            min=-3.1415923, soft_min=-3.1415923, max=3.1415923, soft_max=3.1415923,
            default=0.0,
            step=4,
            precision=4,
            )        

    use_vis_env: BoolProperty(
            name="Use visible environment",
            description="",
            default=False,
            )
    env_vis_type: EnumProperty(
            name="Environment type",
            description="",
            items=environment_types,
            default='1',
            )
    #LEGACY COMPATIBILITY
    env_vis_texture: StringProperty(
            name="Texture",
            description="LEGACY COMPATIBILITY",
            default="",
            maxlen=512,
            )        
    env_vis_texture_ptr: PointerProperty(
            name="Texture",
            description="Environment texture",
            type=bpy.types.Texture,
            )             
    env_vis_power: FloatProperty(
            name="Power",
            description="Scale factor that is applied to the sun and sky",
            min=0, soft_min=0, max=1000.0, soft_max=1000.0,
            default=1.0,
            step=10,
            precision=3,
            )
    env_vis_importance_sampling: BoolProperty(
            name="Octane importance sampling",
            description="Use importance sampling for image textures",
            default=True,
            )
    env_vis_daylight_type: EnumProperty(
            name="Daylight type",
            description="",
            items=environment_daylight_types,
            default='1',
            )
    env_vis_sundir_x: FloatProperty(
            name="Sun direction X",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    env_vis_sundir_y: FloatProperty(
            name="Sun direction Y",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    env_vis_sundir_z: FloatProperty(
            name="Sun direction Z",
            description="",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=-0.0,
            step=10,
            precision=3,
            )
    env_vis_turbidity: FloatProperty(
            name="Turbidity",
            description="Sky turbidity, i.e. the amount of sun light that is scattered. A high value will reduce the contrast between objects in the shadow and in sun light",
            min=2.0, soft_min=2.0, max=6.0, soft_max=6.0,
            default=2.2,
            step=10,
            precision=3,
            )
    env_vis_northoffset: FloatProperty(
            name="North offset",
            description="Additional rotation offset on longitude",
            min=-1.0, soft_min=-1.0, max=1.0, soft_max=1.0,
            default=0.0,
            step=10,
            precision=3,
            )
    env_vis_model: EnumProperty(
            name="Model",
            description="The daylight model you want to use. Sky and sunset color apply only to the new daylight model",
            items=environment_daylight_models,
            default='1',
            )
    env_vis_sky_color: FloatVectorProperty(
            name="Sky color",
            description="Base color of the sky, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.05, 0.3, 1.0),
            subtype='COLOR',
            )
    env_vis_sunset_color: FloatVectorProperty(
            name="Sunset color",
            description="Color of the sky and sun at sunset, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.6, 0.12, 0.02),
            subtype='COLOR',
            )
    env_vis_ground_color: FloatVectorProperty(
            name="Ground color",
            description="Base color of the ground, which works only with the new daylight model",
            min=0.0, max=1.0,
            default=(0.0, 0.0, 0.0),
            subtype='COLOR',
            )
    env_vis_ground_start_angle: FloatProperty(
            name="Ground start angle",
            description="The angle (in degrees) below the horizon where the transition to the ground color starts",
            min=0.0, max=90.0,
            default=90.0,
            step=10,
            precision=4,
            )
    env_vis_ground_blend_angle: FloatProperty(
            name="Ground blend angle",
            description="The angle over which the sky color transitions to the ground color",
            min=1.0, max=90.0,
            default=5.0,
            step=10,
            precision=4,
            )
    env_vis_sun_size: FloatProperty(
            name="Sun size",
            description="Size of the sun given as a factor of the actual sun radius (which is ~0.5 degree)",
            min=0.1, soft_min=0.1, max=30.0, soft_max=30.0,
            default=1.0,
            step=10,
            precision=4,
            )
    env_vis_longitude: FloatProperty(
            name="Longitude",
            description="Longitude of the location",
            min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
            default=4.4667,
            step=1,
            precision=4,
            )
    env_vis_latitude: FloatProperty(
            name="Latitude",
            description="Latitude of the location",
            min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
            default=50.7667,
            step=1,
            precision=4,
            )
    env_vis_day: IntProperty(
            name="Day",
            description="Day of the month of the time the sun direction should be calculated for",
            min=1, max=31,
            default=1,
            )
    env_vis_month: IntProperty(
            name="Month",
            description="Month of the time the sun direction should be calculated for",
            min=1, max=12,
            default=3,
            )
    env_vis_gmtoffset: IntProperty(
            name="GMT offset",
            description="The time zone as offset to GMT",
            min=-12, max=12,
            default=0,
            )
    env_vis_hour: FloatProperty(
            name="Local time",
            description="The local time as hours since 0:00",
            min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
            default=14,
            step=100,
            precision=1,
            )
    env_vis_med_radius: FloatProperty(
            name="Medium radius",
            description="Radius of the environment medium. The environment medium acts as a sphere around the camera position with the specified radius",
            min=0.0001, soft_min=0.0001, max=10000000000, soft_max=10000000000,
            default=1.0,
            step=3,
            precision=4,
            )
    #LEGACY COMPATIBILITY
    env_vis_medium: StringProperty(
            name="Medium",
            description="LEGACY COMPATIBILITY",
            default="",
            maxlen=512,
            )        
    env_vis_medium_ptr: PointerProperty(
            name="Medium",
            description="The medium in the environment (free space). Ignored when this environment is used as a the visible environment",
            type=bpy.types.Texture,
            )    
    env_vis_altitude: FloatProperty(
            name="Altitude",
            description="The camera altitude",
            min=0.1, soft_min=0.1, max=10000000000, soft_max=10000000000,
            default=1.0,
            step=3,
            precision=3,
            )
    env_vis_star_field: PointerProperty(
            name="Star field",
            description="Star fields behind the planet",
            type=bpy.types.Texture,                
            )    
    env_vis_ground_albedo: PointerProperty(
            name="Ground albedo",
            description="Surface texture map on the planet",
            type=bpy.types.Texture,                
            )     
    env_vis_ground_reflection: PointerProperty(
            name="Ground reflection",
            description="Specular texture map on the planet",
            type=bpy.types.Texture,                
            )   
    env_vis_ground_glossiness: PointerProperty(
            name="Ground glossiness",
            description="The planetary glossiness",
            type=bpy.types.Texture,                
            )       
    env_vis_ground_emission: PointerProperty(
            name="Ground emission",
            description="Surface texture map on the planet at night time",
            type=bpy.types.Texture,   
            )     
    env_vis_ground_normal_map: PointerProperty(
            name="Ground normal map",
            description="Normal map on the planet",
            type=bpy.types.Texture,                
            ) 
    env_vis_ground_elevation: PointerProperty(
            name="Ground elevation",
            description="Elevation map on the planet",
            type=bpy.types.Texture,                
            )  
    env_vis_planetary_axis: FloatVectorProperty(
            name="Planetary axis",
            description="The rotational axis of the planet running through the North and South pole",
            min=-1.0, max=1.0,
            default=(0.0, 0.0, 1.0),
            subtype='XYZ',
            )   
    env_vis_planetary_angle: FloatProperty(
            name="Planetary angle",
            description="The rotation around the planetary axis",
            min=-3.1415923, soft_min=-3.1415923, max=3.1415923, soft_max=3.1415923,
            default=0.0,
            step=4,
            precision=4,
            )  

    env_vis_backplate: BoolProperty(
            name="Backplate",
            description="When used as a visible environment, this environment will behave as a backplate image",
            default=False,
            )
    env_vis_reflections: BoolProperty(
            name="Reflections",
            description="When used as a visible environment, this environment will be visible in reflections (specular and glossy materials)",
            default=False,
            )
    env_vis_refractions: BoolProperty(
            name="Refractions",
            description="When used as a visible environment, this environment will be visible in refractions",
            default=False,
            )

    @classmethod
    def register(cls):
        bpy.types.World.octane = PointerProperty(
                name="OctaneRender World Settings",
                description="OctaneRender world settings",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.World.octane


def OctaneMeshSettings_update_is_scatter_group_source(self, context):        
    if self.is_scatter_group_source:
        for name, mesh in bpy.data.meshes.items():
            if name != context.mesh.name and mesh.octane.scatter_group_id == self.scatter_group_id and mesh.octane.is_scatter_group_source:
                mesh.octane.is_scatter_group_source = False


class OctaneMeshSettings(bpy.types.PropertyGroup):

    winding_order: EnumProperty(
            name="Winding order",
            description="May be usable if you need to correct some Octane's triangulation artifacts. Alembic export requires clockwise order",
            items=winding_orders,
            default='0',
            )
    mesh_type: EnumProperty(
            name="Mesh type",
            description="Used for rendering speed optimization, see the manual",
            items=mesh_types,
            default='1',
            )
    is_scatter_group_source: BoolProperty(
            name="Used as source for current group",
            description="Use this object data(mesh and material) for current scatter group when rendering. If none of the meshes is set as source, a random source will be picked",
            update=OctaneMeshSettings_update_is_scatter_group_source,
            default=False,
            )
    scatter_group_id: IntProperty(
            name="Scatter group",
            description="Indicate which scatter group this mesh will be put in. Default -1 for independent group",
            min=-1, max=65535,
            default=-1,                
            )  
    scatter_instance_id: IntProperty(
            name="Scatter instance id",
            description="Indicate the instance id this mesh used",
            min=-1, max=65535,
            default=-1,                
            )                                      
    infinite_plane: BoolProperty(
            name="Infinite plane",
            description="Convert this mesh to infinite plane when rendering",
            default=False,
            )
    tessface_in_preview: BoolProperty(
            name="TessFace in Preview",
            description="Enable tessfaces(if available) in interactive rendering mode",
            default=False,
            )        
    open_subd_enable: BoolProperty(
            name="Enable OpenSubDiv",
            description="Subdivide mesh before rendering",
            default=False,
            )
    open_subd_scheme: EnumProperty(
            name="Scheme",
            description="",
            items=subd_scheme,
            default='1',
            )
    open_subd_level: IntProperty(
            name="Subd level",
            description="",
            min=0, max=10,
            default=0,
            )
    open_subd_sharpness: FloatProperty(
            name="Sharpness",
            description="",
            min=0.0, max=11.0, soft_max=11.0,
            default=0.0,
            )
    open_subd_bound_interp: EnumProperty(
            name="Boundary interp.",
            description="",
            items=bound_interp,
            default='3',
            )
    vis_general: FloatProperty(
            name="General visibility",
            description="",
            min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            )
    vis_cam: BoolProperty(
            name="Camera visibility",
            description="",
            default=True,
            )
    vis_shadow: BoolProperty(
            name="Shadow visibility",
            description="",
            default=True,
            )
    rand_color_seed: IntProperty(
            name="Random color seed",
            description="",
            min=0, max=65535,
            default=0,
            )
    layer_number: IntProperty(
            name="Layer number",
            description="Render layer number for current object. Will use the layer number from blender built-in render layer system if the value is 0",
            min=0, max=255,
            default=(0 if getattr(bpy.context.preferences.addons['octane'].preferences, 'default_use_blender_builtin_render_layer', True) else 1),
            )
    baking_group_id: IntProperty(
            name="Baking group",
            description="",
            min=1, max=65535,
            default=1,                
            )
    light_id_sunlight: BoolProperty(
            name="Sunlight",
            description="Sunlight",
            default=True,
            )           
    light_id_env: BoolProperty(
            name="Environment",
            description="Environment",
            default=True,
            )    
    light_id_pass_1: BoolProperty(
            name="Pass 1",
            description="Pass 1",
            default=True,
            ) 
    light_id_pass_2: BoolProperty(
            name="Pass 2",
            description="Pass 2",
            default=True,
            ) 
    light_id_pass_3: BoolProperty(
            name="Pass 3",
            description="Pass 3",
            default=True,
            ) 
    light_id_pass_4: BoolProperty(
            name="Pass 4",
            description="Pass 4",
            default=True,
            ) 
    light_id_pass_5: BoolProperty(
            name="Pass 5",
            description="Pass 5",
            default=True,
            ) 
    light_id_pass_6: BoolProperty(
            name="Pass 6",
            description="Pass 6",
            default=True,
            ) 
    light_id_pass_7: BoolProperty(
            name="Pass 7",
            description="Pass 7",
            default=True,
            ) 
    light_id_pass_8: BoolProperty(
            name="Pass 8",
            description="Pass 8",
            default=True,
            )                

    octane_vdb_helper: BoolProperty(
            default=False,
            )
    is_octane_vdb: BoolProperty(
            name="Used as Octane VDB",
            description="Will use the imported OpenVDB file as source",
            default=False,
            update= lambda cls, context : update_octane_vdb_helper(cls),
            )
    imported_openvdb_file_path: StringProperty(
            name="OpenVDB File",
            description="Import the OpenVDB file. Use '$F$' to label the frame parts in vdb file path. E.g. $F$. => (0, 1, ... 100 ...). E.g. $4F$. => (0000, 0001, ... 0100 ...)",
            default='',
            update= lambda cls, context : update_octane_vdb_helper(cls),
            subtype='FILE_PATH',
            )     
    openvdb_frame_speed_mutiplier: FloatProperty(
            name="Speed Multiplier",
            description="The speed multiplier will be used when filling vdb path with $F$ label. VDB_FRAME = CURRENT_FRAME * MULTIPLIER",
            min=0.0,
            default=1.0,
            )   
    openvdb_frame_start_playing_at: IntProperty(
            name="Start Playing at",
            description="In which specific frame on the general timeline it should start to show and play the OpenVDB sequence",
            default=1,
            )        
    openvdb_frame_start: IntProperty(
            name="Start",
            description="The start frame of vdb sequence",
            min=0,
            default=1,
            )
    openvdb_frame_end: IntProperty(
            name="End",
            description="The end frame of vdb sequence",
            min=0,
            default=250,
            )                                                              
    vdb_iso: FloatProperty(
            name="ISO",
            description="Isovalue used for when rendering openvdb level sets",
            min=0.0,
            default=0.04,
            )
    vdb_abs_scale: FloatProperty(
            name="Absorption scale",
            description="This scalar value scales the grid value used for absorption",
            min=0.0,
            default=1.0,
            )
    vdb_emiss_scale: FloatProperty(
            name="Emission scale",
            description="This scalar value scales the grid value used for temperature. Use this when temperature information in a grid is too low",
            min=0.0,
            default=1.0,
            )
    vdb_scatter_scale: FloatProperty(
            name="Scatter scale",
            description="This scalar value scales the grid value used for scattering",
            min=0.0,
            default=1.0,
            )
    vdb_vel_scale: FloatProperty(
            name="Velocity scale",
            description="This scalar value linearly scales velocity vectors in the velocity grid",
            min=0.0,
            default=1.0,
            )
    vdb_sdf: BoolProperty(
            name="SDF",
            description="SDF",
            default=False,
            )
    hair_interpolation: EnumProperty(
            name="Hair W interpolation",
            description="Specifies the hair interpolation type. If \"Use hair Ws\" is chosen - you need to explicitly set the hairs root/tip W coordinates in Octane's part of particle settings",
            items=hair_interpolations,
            default='0',
            )

    use_auto_smooth: BoolProperty(
            name="Auto smooth",
            description="Curves autosmooth",
            default=False,
            )
    auto_smooth_angle: FloatProperty(
            subtype='ANGLE',
            name="Angle",
            description="Curves autosmooth angle",
            min=0.0, max=3.141593,
            default=1.55,
            )
    force_load_vertex_normals: BoolProperty(
            name="Force load vertex normals",
            description="Force to use vertex normals",
            default=False,
            )                         
    #Vectron
    octane_geo_node_collections: PointerProperty(
            name="Used as Octane Geometric Node",
            description="",
            type=OctaneGeoNodeCollection,
            )
    #Orbx
    imported_orbx_file_path: StringProperty(
            name="Orbx File Path",
            description="Import the Orbx file",
            default='',
            subtype='FILE_PATH',
            )             

    @classmethod
    def register(cls):
        bpy.types.Mesh.octane = PointerProperty(
                name="OctaneRender Mesh Settings",
                description="",
                type=cls,
                )
        bpy.types.Curve.octane = PointerProperty(
                name="OctaneRender Curve Settings",
                description="",
                type=cls,
                )
        bpy.types.MetaBall.octane = PointerProperty(
                name="OctaneRender MetaBall Settings",
                description="",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Mesh.octane
        del bpy.types.Curve.octane
        del bpy.types.MetaBall.octane


class OctaneObjPropertiesSettings(bpy.types.PropertyGroup):

    visibility: BoolProperty(
            name="Visibility",
            description="Object visibility for OctaneRender",
            default=True,
            )
    overwrite_scatter_instance_id: IntProperty(
            name="Overwrite instance id",
            description="Indicate the instance id this object used",
            min=0, max=65535,
            default=0,                
            )             

    @classmethod
    def register(cls):
        bpy.types.Object.octane_properties = PointerProperty(
                name="OctaneRender Object Properties",
                description="OctaneRender object properties",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane_properties


class OctaneLightSettings(bpy.types.PropertyGroup):

    enable: BoolProperty(
            name="Enable",
            description="Lamp casts shadows",
            default=True,
            )
    camera_visibility: BoolProperty(
            name="Camera Visibility",
            description="",
            default=False
            )
    mesh_type: EnumProperty(
            name="Mesh type",
            description="",
            items=mesh_types,
            default='1',
            )
    texture: StringProperty(
            name="Texture",
            description="The emission texture (on the emitting surface)",
            default="",
            maxlen=512,
            )        
    power: FloatProperty(
           name="Power",
           description="Multiplier for light source's brightness",
           min=0.01, soft_min=0.01, max=100000.0, soft_max=100000.0,
           default=1.0,
           step=1,
           precision=3,
           )
    light_pass_id: IntProperty(
            name="Light pass ID",
            description="ID of the light pass that captures the contribution of this emitter",
            min=1, max=8,
            default=1,
            )   
    enable_light_object_direction: BoolProperty(
            name="Enable Light Object Direction",
            description="Use the directoin from the light object. If this option is disabled, Octane will use the direction vector or sun direction set in the ToonDirectionLight",
            default=True,
            )        
    sun_dir_enable: BoolProperty(
            name="Use Sun Direction",
            description="",
            default=True,
            )        
    sun_dir_longitude: FloatProperty(
            name="Longitude",
            description="Longitude of the location",
            min=-180.0, soft_min=-180.0, max=180.0, soft_max=180.0,
            default=4.4667,
            step=1,
            precision=4,
            )
    sun_dir_latitude: FloatProperty(
            name="Latitude",
            description="Latitude of the location",
            min=-90.0, soft_min=-90.0, max=90.0, soft_max=90.0,
            default=50.7667,
            step=1,
            precision=4,
            )
    sun_dir_day: IntProperty(
            name="Day",
            description="Day of the month of the time the sun direction should be calculated for",
            min=1, max=31,
            default=1,
            )
    sun_dir_month: IntProperty(
            name="Month",
            description="Month of the time the sun direction should be calculated for",
            min=1, max=12,
            default=3,
            )
    sun_dir_gmtoffset: IntProperty(
            name="GMT offset",
            description="The time zone as offset to GMT",
            min=-12, max=12,
            default=0,
            )
    sun_dir_hour: FloatProperty(
            name="Local time",
            description="The local time as hours since 0:00",
            min=0.0, soft_min=0.0, max=24.0, soft_max=24.0,
            default=14,
            step=10,
            precision=1,
            )
    light_mesh: PointerProperty(
            name="Light Mesh",
            description="Use this mesh with octane emission",
            type=bpy.types.Mesh,                
            )   
    use_external_mesh: BoolProperty(
            name="Use External Mesh",
            description="",
            default=False,
            )                     
    external_mesh_file: StringProperty(
            name="External Obj File",
            description="Use external mesh with octane emission",
            default='',
            subtype='FILE_PATH',
            )         

    @classmethod
    def register(cls):
        bpy.types.Light.octane = PointerProperty(
                name="OctaneRender Light Settings",
                description="OctaneRender Light settings",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Light.octane


class OctaneMaterialSettings(bpy.types.PropertyGroup):
    @classmethod
    def register(cls):
        bpy.types.Material.octane = PointerProperty(
                name="OctaneRender Material Settings",
                description="OctaneRender material settings",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.Material.octane


class OctaneRenderLayerSettings(bpy.types.PropertyGroup):
    use_passes: BoolProperty(
            name="Render passes",
            description="",
            default=False,
            )

    info_pass_max_samples: IntProperty(
            name="Info pass max samples",
            description="The maximum number of samples for the info passes (excluding AO)",
            min=1, max=1024,
            default=128,
            )
    info_pass_sampling_mode: EnumProperty(
            name="Sampling mode",
            description="Enables motion blur and depth of field, and sets pixel filtering modes.\n\n"
                "'Distributed rays':"
                " Enables motion blur and DOF, and also enables pixel filtering.\n"
                "'Non-distributed with pixel filtering':"
                " Disables motion blur and DOF, but leaves pixel filtering enabled.\n"
                "'Non-distributed without pixel filtering':"
                " Disables motion blur and DOF, and disables pixel filtering for all render passes"
                " except for render layer mask and ambient occlusion\n",
            items=info_pass_sampling_modes,
            default='0',
            )
    info_pass_z_depth_max: FloatProperty(
            name="Z-depth max",
            description="Z-depth value mapped to white (0 is mapped to black)",
            min=0.001, soft_min=0.001, max=100000.0, soft_max=100000.0,
            default=5.0,
            step=10,
            precision=4,
            )
    info_pass_uv_max: FloatProperty(
            name="UV max",
            description="UV coordinate value mapped to maximum intensity",
            min=0.00001, soft_min=0.00001, max=1000.0, soft_max=1000.0,
            default=1.0,
            step=10,
            precision=5,
            )
    info_pass_uv_coordinate_selection: IntProperty(
            name="UV coordinate selection",
            description="Determines which set of UV coordinates to use",
            min=1, max=3,
            default=1,
            )        
    info_pass_max_speed: FloatProperty(
            name="Max speed",
            description="Speed mapped to the maximum intensity in the motion vector channel. A value of 1 means a maximum movement of 1 screen width in the shutter interval",
            min=0.00001, soft_min=0.00001, max=10000.0, soft_max=10000.0,
            default=1.0,
            step=10,
            precision=5,
            )
    info_pass_ao_distance: FloatProperty(
            name="AO distance",
            description="Ambient occlusion distance",
            min=0.01, soft_min=0.01, max=1024.0, soft_max=1024.0,
            default=3.0,
            step=10,
            precision=2,
            )
    info_pass_alpha_shadows: BoolProperty(
            name="AO alpha shadows",
            description="Take into account alpha maps when calculating ambient occlusion",
            default=False,
            )
    pass_raw: BoolProperty(
            name="Raw",
            description="Make the beauty pass raw render passes by dividing out the color of the BxDF of the surface hit by the camera ray",
            default=False,
            )
    pass_pp_env: BoolProperty(
            name="Include environment",
            description="When enabled, the environment render pass is included when doing post-processing. This option only applies when the environment render pass and alpha channel are enabled",
            default=False,
            )
    info_pass_bump: BoolProperty(
            name="Bump and normal mapping",
            description="Take bump and normal mapping into account for shading normal output and wireframe shading",
            default=True,
            )
    info_pass_opacity_threshold: FloatProperty(
            name="Opacity threshold",
            description="Geometry with opacity higher or equal to this value is treated as totally opaque",
            min=0.0, soft_min=0.0, max=1.0, soft_max=1.0,
            default=1.0,
            step=10,
            precision=3,
            )
    cryptomatte_pass_channels: EnumProperty(
            name="Channels",
            description="Amount of cryptomatte channels to render",
            items=cryptomatte_pass_channel_modes,
            default='2',
            )
    cryptomatte_seed_factor: IntProperty(
            name="Cryptomatte seed factor",
            description="Amount of samples to use for seeding cryptomatte. This gets multiplied with the amount of bins. Low values result in pitting artefacts at feathered edges, while large values the values can result in artefacts in places with coverage for lots of different IDs",
            min=4, max=25,
            default=10,
            )   

    current_preview_pass_type: EnumProperty(
            name="Preview pass type",
            description="Pass used for preview rendering",
            items=octane_render_pass_types,
            default='0',
            )

    @classmethod
    def register(cls):
        bpy.types.ViewLayer.octane = PointerProperty(
            name="Octane ViewLayer Settings",
            description="Octane ViewLayer Settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.ViewLayer.octane


class OctaneObjectSettings(bpy.types.PropertyGroup):

    render_layer_id: IntProperty(
        name="Render layer ID",
        description="Render layer number for current object. Will use the layer number from blender built-in render layer system if the value is 0",
        min=1, max=255,
        default=1,
    )
    general_visibility: FloatProperty(
        name="General visibility",
        description="",
        min=0.0, max=1.0, soft_max=1.0,
        default=1.0,
    )    
    camera_visibility: BoolProperty(
        name="Camera Visibility",
        description="",
        default=True
    )
    shadow_visibility: BoolProperty(
        name="Shadow Visibility",
        description="",
        default=True
    )    
    random_color_seed: IntProperty(
        name="Random color seed",
        description="Random color seed",
        min=0, max=65535,
        default=0,
    )    
    color: FloatVectorProperty(
        name="Color",
        description="The color that is rendered in the object layer render pass",
        min=0.0, max=1.0,
        default=(1.0, 1.0, 1.0),
        subtype='COLOR',
    )
    light_id_sunlight: BoolProperty(
        name="Sunlight",
        description="Sunlight",
        default=True,
    )           
    light_id_env: BoolProperty(
        name="Environment",
        description="Environment",
        default=True,
    )    
    light_id_pass_1: BoolProperty(
        name="Pass 1",
        description="Pass 1",
        default=True,
    ) 
    light_id_pass_2: BoolProperty(
        name="Pass 2",
        description="Pass 2",
        default=True,
    ) 
    light_id_pass_3: BoolProperty(
        name="Pass 3",
        description="Pass 3",
        default=True,
    ) 
    light_id_pass_4: BoolProperty(
        name="Pass 4",
        description="Pass 4",
        default=True,
    ) 
    light_id_pass_5: BoolProperty(
        name="Pass 5",
        description="Pass 5",
        default=True,
    ) 
    light_id_pass_6: BoolProperty(
        name="Pass 6",
        description="Pass 6",
        default=True,
    ) 
    light_id_pass_7: BoolProperty(
        name="Pass 7",
        description="Pass 7",
        default=True,
    ) 
    light_id_pass_8: BoolProperty(
        name="Pass 8",
        description="Pass 8",
        default=True,
    )      

    baking_group_id: IntProperty(
        name="Baking group ID",
        description="",
        min=1, max=65535,
        default=1,                
    )
    baking_uv_transform_rz: FloatProperty(
        name="R.Z",
        description="Rotation Z",
        min=-360, max=360,
        default=0,                
    )
    baking_uv_transform_sx: FloatProperty(
        name="S.X",
        description="Scale X",
        min=-0.001, max=1000,
        default=1,                
    )    
    baking_uv_transform_sy: FloatProperty(
        name="S.Y",
        description="Scale Y",
        min=-0.001, max=1000,
        default=1,                
    )   
    baking_uv_transform_tx: FloatProperty(
        name="T.X",
        description="Translation X",
        default=0,                
    )    
    baking_uv_transform_ty: FloatProperty(
        name="T.Y",
        description="Translation Y",
        default=0,                
    )      

    use_motion_blur: BoolProperty(
        name="Use Motion Blur",
        description="Use motion blur for this object",
        default=False,
    )
    use_deform_motion: BoolProperty(
        name="Use Deformation Motion",
        description="Use deformation motion blur for this object",
        default=False,
    )
    motion_steps: IntProperty(
        name="Motion Steps",
        description="Control accuracy of motion blur, more steps gives more memory usage (actual number of steps is 2^(steps - 1))",
        min=1, soft_max=8,
        default=1,
    )   

    @classmethod
    def register(cls):
        bpy.types.Object.octane = PointerProperty(
            name="Octane Object Settings",
            description="Octane object settings",
            type=cls,
        )

    @classmethod
    def unregister(cls):
        del bpy.types.Object.octane


#LEGACY SYSTEM
class OctaneHairSettings(bpy.types.PropertyGroup):
    root_width: FloatProperty(
            name="Root thickness",
            description="Hair thickness at root",
            min=0.0, max=1000.0,
            default=0.001,
            )
    tip_width: FloatProperty(
            name="Tip thickness",
            description="Hair thickness at tip",
            min=0.0, max=1000.0,
            default=0.001,
            )
    min_curvature: FloatProperty(
            name="Minimal curvature (deg.)",
            description="Hair points having angle deviation from previous point less than this value will be skipped",
            min=0.0, max=180.0,
            default=0.0001,
            )
    w_min: FloatProperty(
            name="Min. W",
            description="W coordinate of the root of a hair: it represents a position on a color gradient for roots of all hairs of this particle system",
            min=0.0, max=1.0,
            default=0.0,
            )
    w_max: FloatProperty(
            name="Max. W",
            description="W coordinate of the tip of a hair: it represents a position on a color gradient for tips of all hairs of this particle system",
            min=0.0, max=1.0,
            default=1.0,
            )

    @classmethod
    def register(cls):
        bpy.types.ParticleSettings.octane = PointerProperty(
                name="Octane Hair Settings",
                description="Octane hair settings",
                type=cls,
                )

    @classmethod
    def unregister(cls):
        del bpy.types.ParticleSettings.octane



classes = (
    OctanePreferences,    
    OctaneAIUpSamplertSettings,
    OctaneBakingLayerTransform,
    OctaneBakingLayerTransformCollection,
	OctaneGeoNode,
	OctaneGeoNodeCollection,
	OctaneOSLCameraNode,
	OctaneOSLCameraNodeCollection,
    OctaneRenderSettings,
    OctaneCameraSettings,
    OctaneSpaceDataSettings,
    OctaneWorldSettings,
    OctaneMeshSettings,
    OctaneHairSettings,
    OctaneObjPropertiesSettings,
    OctaneLightSettings,
    OctaneMaterialSettings,
    OctaneRenderLayerSettings,
    OctaneObjectSettings
)

@persistent
def load_handler(dummy):
    try:
        import _octane
        from . import operators
        _octane.activate(True)  
    except:
        pass

def register():    
    from bpy.utils import register_class	
    for cls in classes:
        register_class(cls) 
    shader_node_categories = nodeitems_octane.shader_node_categories_based_functions
    nodeitems_utils.register_node_categories("OCT_SHADER", shader_node_categories)    
    texture_node_categories = nodeitems_octane.texture_node_categories_based_functions
    nodeitems_utils.register_node_categories("OCT_TEXTURE", texture_node_categories)
    update_octane_data()
    bpy.app.handlers.load_post.append(load_handler)


def unregister():
    from bpy.utils import unregister_class	
    for cls in classes:
        unregister_class(cls)
    nodeitems_utils.unregister_node_categories("OCT_SHADER")
    nodeitems_utils.unregister_node_categories("OCT_TEXTURE")        
    bpy.app.handlers.load_post.remove(load_handler)