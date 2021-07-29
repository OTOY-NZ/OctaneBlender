/*
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
 */

/** \file
 * \ingroup nodes
 */

/* intentionally no include guard */

/* Keep aligned args for readability. */
/* clang-format off */

/* Empty definitions for undefined macros to avoid warnings */
#ifndef DefNode
#define DefNode(Category, ID, DefFunc, EnumName, StructName, UIName, UIDesc)
#endif

/* WARNING! If you edit those strings, please do the same in relevant nodes files (under blender/nodes/...)! */

/*       Tree type       Node ID                  RNA def function        Enum name         Struct name       UI Name              UI Description */
DefNode(Node,           NODE_FRAME,              def_frame,              "FRAME",          Frame,            "Frame",             ""              )
DefNode(Node,           NODE_GROUP,              def_group,              "GROUP",          Group,            "Group",             ""              )
DefNode(Node,           NODE_GROUP_INPUT,        def_group_input,        "GROUP_INPUT",    GroupInput,       "Group Input",       ""              )
DefNode(Node,           NODE_GROUP_OUTPUT,       def_group_output,       "GROUP_OUTPUT",   GroupOutput,      "Group Output",      ""              )
DefNode(Node,           NODE_REROUTE,            0,                      "REROUTE",        Reroute,          "Reroute",           ""              )

DefNode(ShaderNode,     SH_NODE_RGB,             0,                      "RGB",            RGB,              "RGB",               ""              )
DefNode(ShaderNode,     SH_NODE_VALUE,           0,                      "VALUE",          Value,            "Value",             ""              )
DefNode(ShaderNode,     SH_NODE_MIX_RGB,         def_mix_rgb,            "MIX_RGB",        MixRGB,           "MixRGB",            ""              )
DefNode(ShaderNode,     SH_NODE_VALTORGB,        def_colorramp,          "VALTORGB",       ValToRGB,         "ColorRamp",         ""              )
DefNode(ShaderNode,     SH_NODE_RGBTOBW,         0,                      "RGBTOBW",        RGBToBW,          "RGB to BW",         ""              )
DefNode(ShaderNode,     SH_NODE_SHADERTORGB,     0,                      "SHADERTORGB",    ShaderToRGB,      "Shader to RGB",     ""              )
DefNode(ShaderNode,     SH_NODE_NORMAL,          0,                      "NORMAL",         Normal,           "Normal",            ""              )
DefNode(ShaderNode,     SH_NODE_GAMMA,           0,                      "GAMMA",          Gamma,            "Gamma",             ""              )
DefNode(ShaderNode,     SH_NODE_BRIGHTCONTRAST,  0,                      "BRIGHTCONTRAST", BrightContrast,   "Bright Contrast",   ""              )
DefNode(ShaderNode,     SH_NODE_MAPPING,         def_sh_mapping,         "MAPPING",        Mapping,          "Mapping",           ""              )
DefNode(ShaderNode,     SH_NODE_CURVE_VEC,       def_vector_curve,       "CURVE_VEC",      VectorCurve,      "Vector Curves",     ""              )
DefNode(ShaderNode,     SH_NODE_CURVE_RGB,       def_rgb_curve,          "CURVE_RGB",      RGBCurve,         "RGB Curves",        ""              )
DefNode(ShaderNode,     SH_NODE_CAMERA,          0,                      "CAMERA",         CameraData,       "Camera Data",       ""              )
DefNode(ShaderNode,     SH_NODE_MAP_RANGE,       def_map_range,          "MAP_RANGE",      MapRange,         "Map Range",         ""              )
DefNode(ShaderNode,     SH_NODE_CLAMP,           def_clamp,              "CLAMP",          Clamp,            "Clamp",             ""              )
DefNode(ShaderNode,     SH_NODE_MATH,            def_math,               "MATH",           Math,             "Math",              ""              )
DefNode(ShaderNode,     SH_NODE_VECTOR_MATH,     def_vector_math,        "VECT_MATH",      VectorMath,       "Vector Math",       ""              )
DefNode(ShaderNode,     SH_NODE_SQUEEZE,         0,                      "SQUEEZE",        Squeeze,          "Squeeze Value",     ""              )
DefNode(ShaderNode,     SH_NODE_INVERT,          0,                      "INVERT",         Invert,           "Invert",            ""              )
DefNode(ShaderNode,     SH_NODE_SEPRGB,          0,                      "SEPRGB",         SeparateRGB,      "Separate RGB",      ""              )
DefNode(ShaderNode,     SH_NODE_COMBRGB,         0,                      "COMBRGB",        CombineRGB,       "Combine RGB",       ""              )
DefNode(ShaderNode,     SH_NODE_HUE_SAT,         0,                      "HUE_SAT",        HueSaturation,    "Hue/Saturation",    ""              )

DefNode(ShaderNode,     SH_NODE_OUTPUT_MATERIAL,    def_sh_output,          "OUTPUT_MATERIAL",    OutputMaterial,   "Material Output",   ""       )
DefNode(ShaderNode,     SH_NODE_EEVEE_SPECULAR,     0,                      "EEVEE_SPECULAR",     EeveeSpecular,    "Specular",          ""       )
DefNode(ShaderNode,     SH_NODE_OUTPUT_LIGHT,       def_sh_output,          "OUTPUT_LIGHT",       OutputLight,      "Light Output",      ""       )
DefNode(ShaderNode,     SH_NODE_OUTPUT_WORLD,       def_sh_output,          "OUTPUT_WORLD",       OutputWorld,      "World Output",      ""       )
DefNode(ShaderNode,     SH_NODE_OUTPUT_LINESTYLE,   def_sh_output_linestyle,"OUTPUT_LINESTYLE",   OutputLineStyle,  "Line Style Output", ""       )
DefNode(ShaderNode,     SH_NODE_FRESNEL,            0,                      "FRESNEL",            Fresnel,          "Fresnel",           ""       )
DefNode(ShaderNode,     SH_NODE_LAYER_WEIGHT,       0,                      "LAYER_WEIGHT",       LayerWeight,      "Layer Weight",      ""       )
DefNode(ShaderNode,     SH_NODE_MIX_SHADER,         0,                      "MIX_SHADER",         MixShader,        "Mix Shader",        ""       )
DefNode(ShaderNode,     SH_NODE_ADD_SHADER,         0,                      "ADD_SHADER",         AddShader,        "Add Shader",        ""       )
DefNode(ShaderNode,     SH_NODE_ATTRIBUTE,          def_sh_attribute,       "ATTRIBUTE",          Attribute,        "Attribute",         ""       )
DefNode(ShaderNode,     SH_NODE_AMBIENT_OCCLUSION,  def_sh_ambient_occlusion,"AMBIENT_OCCLUSION", AmbientOcclusion, "Ambient Occlusion", ""       )
DefNode(ShaderNode,     SH_NODE_BACKGROUND,         0,                      "BACKGROUND",         Background,       "Background",        ""       )
DefNode(ShaderNode,     SH_NODE_HOLDOUT,            0,                      "HOLDOUT",            Holdout,          "Holdout",           ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_ANISOTROPIC,   def_anisotropic,        "BSDF_ANISOTROPIC",   BsdfAnisotropic,  "Anisotropic BSDF",  ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_DIFFUSE,       0,                      "BSDF_DIFFUSE",       BsdfDiffuse,      "Diffuse BSDF",      ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_PRINCIPLED,    def_principled,         "BSDF_PRINCIPLED",    BsdfPrincipled,   "Principled BSDF",   ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_GLOSSY,        def_glossy,             "BSDF_GLOSSY",        BsdfGlossy,       "Glossy BSDF",       ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_GLASS,         def_glass,              "BSDF_GLASS",         BsdfGlass,        "Glass BSDF",        ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_REFRACTION,    def_refraction,         "BSDF_REFRACTION",    BsdfRefraction,   "Refraction BSDF",   ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_TRANSLUCENT,   0,                      "BSDF_TRANSLUCENT",   BsdfTranslucent,  "Translucent BSDF",  ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_TRANSPARENT,   0,                      "BSDF_TRANSPARENT",   BsdfTransparent,  "Transparent BSDF",  ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_VELVET,        0,                      "BSDF_VELVET",        BsdfVelvet,       "Velvet BSDF",       ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_TOON,          def_toon,               "BSDF_TOON",          BsdfToon,         "Toon BSDF",         ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_HAIR,          def_hair,               "BSDF_HAIR",          BsdfHair,         "Hair BSDF",         ""       )
DefNode(ShaderNode,     SH_NODE_BSDF_HAIR_PRINCIPLED,  def_hair_principled, "BSDF_HAIR_PRINCIPLED", BsdfHairPrincipled,  "Principled Hair BSDF", "")
DefNode(ShaderNode,     SH_NODE_SUBSURFACE_SCATTERING, def_sh_subsurface,   "SUBSURFACE_SCATTERING",SubsurfaceScattering,"Subsurface Scattering","")
DefNode(ShaderNode,     SH_NODE_VOLUME_ABSORPTION,  0,                      "VOLUME_ABSORPTION",  VolumeAbsorption, "Volume Absorption", ""       )
DefNode(ShaderNode,     SH_NODE_VOLUME_SCATTER,     0,                      "VOLUME_SCATTER",     VolumeScatter,    "Volume Scatter",    ""       )
DefNode(ShaderNode,     SH_NODE_VOLUME_PRINCIPLED,  0,                      "PRINCIPLED_VOLUME",  VolumePrincipled, "Principled Volume", ""       )
DefNode(ShaderNode,     SH_NODE_EMISSION,           0,                      "EMISSION",           Emission,         "Emission",          ""       )
DefNode(ShaderNode,     SH_NODE_NEW_GEOMETRY,       0,                      "NEW_GEOMETRY",       NewGeometry,      "Geometry",          ""       )
DefNode(ShaderNode,     SH_NODE_LIGHT_PATH,         0,                      "LIGHT_PATH",         LightPath,        "Light Path",        ""       )
DefNode(ShaderNode,     SH_NODE_LIGHT_FALLOFF,      0,                      "LIGHT_FALLOFF",      LightFalloff,     "Light Falloff",     ""       )
DefNode(ShaderNode,     SH_NODE_OBJECT_INFO,        0,                      "OBJECT_INFO",        ObjectInfo,       "Object Info",       ""       )
DefNode(ShaderNode,     SH_NODE_PARTICLE_INFO,      0,                      "PARTICLE_INFO",      ParticleInfo,     "Particle Info",     ""       )
DefNode(ShaderNode,     SH_NODE_HAIR_INFO,          0,                      "HAIR_INFO",          HairInfo,         "Hair Info",         ""       )
DefNode(ShaderNode,     SH_NODE_VOLUME_INFO,        0,                      "VOLUME_INFO",        VolumeInfo,       "Volume Info",       ""       )
DefNode(ShaderNode,     SH_NODE_WIREFRAME,          def_sh_tex_wireframe,   "WIREFRAME",          Wireframe,        "Wireframe",         ""       )
DefNode(ShaderNode,     SH_NODE_WAVELENGTH,         0,                      "WAVELENGTH",         Wavelength,       "Wavelength",        ""       )
DefNode(ShaderNode,     SH_NODE_BLACKBODY,          0,                      "BLACKBODY",          Blackbody,        "Blackbody",         ""       )
DefNode(ShaderNode,     SH_NODE_BUMP,               def_sh_bump,            "BUMP",               Bump,             "Bump",              ""       )
DefNode(ShaderNode,     SH_NODE_NORMAL_MAP,         def_sh_normal_map,      "NORMAL_MAP",         NormalMap,        "Normal Map",        ""       )
DefNode(ShaderNode,     SH_NODE_TANGENT,            def_sh_tangent,         "TANGENT",            Tangent,          "Tangent",           ""       )
DefNode(ShaderNode,     SH_NODE_SCRIPT,             def_sh_script,          "SCRIPT",             Script,           "Script",            ""       )
DefNode(ShaderNode,     SH_NODE_TEX_IMAGE,          def_sh_tex_image,       "TEX_IMAGE",          TexImage,         "Image Texture",     ""       )
DefNode(ShaderNode,     SH_NODE_TEX_ENVIRONMENT,    def_sh_tex_environment, "TEX_ENVIRONMENT",    TexEnvironment,   "Environment Texture",""      )
DefNode(ShaderNode,     SH_NODE_TEX_SKY,            def_sh_tex_sky,         "TEX_SKY",            TexSky,           "Sky Texture",       ""       )
DefNode(ShaderNode,     SH_NODE_TEX_GRADIENT,       def_sh_tex_gradient,    "TEX_GRADIENT",       TexGradient,      "Gradient Texture",  ""       )
DefNode(ShaderNode,     SH_NODE_TEX_NOISE,          def_sh_tex_noise,       "TEX_NOISE",          TexNoise,         "Noise Texture",     ""       )
DefNode(ShaderNode,     SH_NODE_TEX_MAGIC,          def_sh_tex_magic,       "TEX_MAGIC",          TexMagic,         "Magic Texture",     ""       )
DefNode(ShaderNode,     SH_NODE_TEX_WAVE,           def_sh_tex_wave,        "TEX_WAVE",           TexWave,          "Wave Texture",      ""       )
DefNode(ShaderNode,     SH_NODE_TEX_MUSGRAVE,       def_sh_tex_musgrave,    "TEX_MUSGRAVE",       TexMusgrave,      "Musgrave Texture",  ""       )
DefNode(ShaderNode,     SH_NODE_TEX_VORONOI,        def_sh_tex_voronoi,     "TEX_VORONOI",        TexVoronoi,       "Voronoi Texture",   ""       )
DefNode(ShaderNode,     SH_NODE_TEX_CHECKER,        def_sh_tex_checker,     "TEX_CHECKER",        TexChecker,       "Checker Texture",   ""       )
DefNode(ShaderNode,     SH_NODE_TEX_BRICK,          def_sh_tex_brick,       "TEX_BRICK",          TexBrick,         "Brick Texture",     ""       )
DefNode(ShaderNode,     SH_NODE_TEX_POINTDENSITY,   def_sh_tex_pointdensity,"TEX_POINTDENSITY",   TexPointDensity,  "Point Density",     ""       )
DefNode(ShaderNode,     SH_NODE_TEX_COORD,          def_sh_tex_coord,       "TEX_COORD",          TexCoord,         "Texture Coordinate",""       )
DefNode(ShaderNode,     SH_NODE_VECTOR_ROTATE,      def_sh_vector_rotate,   "VECTOR_ROTATE",      VectorRotate,     "Vector Rotate",     ""       )
DefNode(ShaderNode,     SH_NODE_VECT_TRANSFORM,     def_sh_vect_transform,  "VECT_TRANSFORM",     VectorTransform,  "Vector Transform",  ""       )
DefNode(ShaderNode,     SH_NODE_SEPHSV,             0,                      "SEPHSV",             SeparateHSV,      "Separate HSV",      ""       )
DefNode(ShaderNode,     SH_NODE_COMBHSV,            0,                      "COMBHSV",            CombineHSV,       "Combine HSV",       ""       )
DefNode(ShaderNode,     SH_NODE_UVMAP,              def_sh_uvmap,           "UVMAP",              UVMap,            "UV Map",            ""       )
DefNode(ShaderNode,     SH_NODE_VERTEX_COLOR,       def_sh_vertex_color,    "VERTEX_COLOR",       VertexColor,      "Vertex Color",      ""       )
DefNode(ShaderNode,     SH_NODE_UVALONGSTROKE,      def_sh_uvalongstroke,   "UVALONGSTROKE",      UVAlongStroke,    "UV Along Stroke",   ""       )
DefNode(ShaderNode,     SH_NODE_SEPXYZ,             0,                      "SEPXYZ",             SeparateXYZ,      "Separate XYZ",      ""       )
DefNode(ShaderNode,     SH_NODE_COMBXYZ,            0,                      "COMBXYZ",            CombineXYZ,       "Combine XYZ",       ""       )
DefNode(ShaderNode,     SH_NODE_BEVEL,              def_sh_bevel,           "BEVEL",              Bevel,            "Bevel",             ""       )
DefNode(ShaderNode,     SH_NODE_DISPLACEMENT,       def_sh_displacement,    "DISPLACEMENT",       Displacement,     "Displacement",      ""       )
DefNode(ShaderNode,     SH_NODE_VECTOR_DISPLACEMENT,def_sh_vector_displacement,"VECTOR_DISPLACEMENT",VectorDisplacement,"Vector Displacement",""  )
DefNode(ShaderNode,     SH_NODE_TEX_IES,            def_sh_tex_ies,         "TEX_IES",            TexIES,           "IES Texture",       ""       )
DefNode(ShaderNode,     SH_NODE_TEX_WHITE_NOISE,    def_sh_tex_white_noise, "TEX_WHITE_NOISE",    TexWhiteNoise,    "White Noise",       ""       )
DefNode(ShaderNode,     SH_NODE_OUTPUT_AOV,         def_sh_output_aov,      "OUTPUT_AOV",         OutputAOV,        "AOV Output",        ""       )

DefNode(CompositorNode, CMP_NODE_VIEWER,         def_cmp_viewer,         "VIEWER",         Viewer,           "Viewer",            ""              )
DefNode(CompositorNode, CMP_NODE_RGB,            0,                      "RGB",            RGB,              "RGB",               ""              )
DefNode(CompositorNode, CMP_NODE_VALUE,          0,                      "VALUE",          Value,            "Value",             ""              )
DefNode(CompositorNode, CMP_NODE_MIX_RGB,        def_mix_rgb,            "MIX_RGB",        MixRGB,           "Mix",               ""              )
DefNode(CompositorNode, CMP_NODE_VALTORGB,       def_colorramp,          "VALTORGB",       ValToRGB,         "ColorRamp",         ""              )
DefNode(CompositorNode, CMP_NODE_RGBTOBW,        0,                      "RGBTOBW",        RGBToBW,          "RGB to BW",         ""              )
DefNode(CompositorNode, CMP_NODE_NORMAL,         0,                      "NORMAL",         Normal,           "Normal",            ""              )
DefNode(CompositorNode, CMP_NODE_CURVE_VEC,      def_vector_curve,       "CURVE_VEC",      CurveVec,         "Vector Curves",     ""              )
DefNode(CompositorNode, CMP_NODE_CURVE_RGB,      def_rgb_curve,          "CURVE_RGB",      CurveRGB,         "RGB Curves",        ""              )
DefNode(CompositorNode, CMP_NODE_ALPHAOVER,      def_cmp_alpha_over,     "ALPHAOVER",      AlphaOver,        "Alpha Over",        ""              )
DefNode(CompositorNode, CMP_NODE_BLUR,           def_cmp_blur,           "BLUR",           Blur,             "Blur",              ""              )
DefNode(CompositorNode, CMP_NODE_FILTER,         def_cmp_filter,         "FILTER",         Filter,           "Filter",            ""              )
DefNode(CompositorNode, CMP_NODE_MAP_VALUE,      def_cmp_map_value,      "MAP_VALUE",      MapValue,         "Map Value",         ""              )
DefNode(CompositorNode, CMP_NODE_MAP_RANGE,      def_cmp_map_range,      "MAP_RANGE",      MapRange,         "Map Range",         ""              )
DefNode(CompositorNode, CMP_NODE_TIME,           def_time,               "TIME",           Time,             "Time",              ""              )
DefNode(CompositorNode, CMP_NODE_VECBLUR,        def_cmp_vector_blur,    "VECBLUR",        VecBlur,          "Vector Blur",       ""              )
DefNode(CompositorNode, CMP_NODE_SEPRGBA,        0,                      "SEPRGBA",        SepRGBA,          "Separate RGBA",     ""              )
DefNode(CompositorNode, CMP_NODE_SEPHSVA,        0,                      "SEPHSVA",        SepHSVA,          "Separate HSVA",     ""              )
DefNode(CompositorNode, CMP_NODE_SETALPHA,       def_cmp_set_alpha,      "SETALPHA",       SetAlpha,         "Set Alpha",         ""              )
DefNode(CompositorNode, CMP_NODE_HUE_SAT,        0,                      "HUE_SAT",        HueSat,           "Hue Saturation Value",""            )
DefNode(CompositorNode, CMP_NODE_IMAGE,          def_cmp_image,          "IMAGE",          Image,            "Image",             ""              )
DefNode(CompositorNode, CMP_NODE_R_LAYERS,       def_cmp_render_layers,  "R_LAYERS",       RLayers,          "Render Layers",     ""              )
DefNode(CompositorNode, CMP_NODE_COMPOSITE,      def_cmp_composite,      "COMPOSITE",      Composite,        "Composite",         ""              )
/* NB: OutputFile node has special rna setup function called in rna_nodetree.c */
DefNode(CompositorNode, CMP_NODE_OUTPUT_FILE,    0,                      "OUTPUT_FILE",    OutputFile,       "File Output",       ""              )
DefNode(CompositorNode, CMP_NODE_TEXTURE,        def_texture,            "TEXTURE",        Texture,          "Texture",           ""              )
DefNode(CompositorNode, CMP_NODE_TRANSLATE,      def_cmp_translate,      "TRANSLATE",      Translate,        "Translate",         ""              )
DefNode(CompositorNode, CMP_NODE_ZCOMBINE,       def_cmp_zcombine,       "ZCOMBINE",       Zcombine,         "Z Combine",         ""              )
DefNode(CompositorNode, CMP_NODE_COMBRGBA,       0,                      "COMBRGBA",       CombRGBA,         "Combine RGBA",      ""              )
DefNode(CompositorNode, CMP_NODE_DILATEERODE,    def_cmp_dilate_erode,   "DILATEERODE",    DilateErode,      "Dilate/Erode",      ""              )
DefNode(CompositorNode, CMP_NODE_INPAINT,        def_cmp_inpaint,        "INPAINT",        Inpaint,          "Inpaint",           ""              )
DefNode(CompositorNode, CMP_NODE_DESPECKLE,      def_cmp_despeckle,      "DESPECKLE",      Despeckle,        "Despeckle",         ""              )
DefNode(CompositorNode, CMP_NODE_ROTATE,         def_cmp_rotate,         "ROTATE",         Rotate,           "Rotate",            ""              )
DefNode(CompositorNode, CMP_NODE_SCALE,          def_cmp_scale,          "SCALE",          Scale,            "Scale",             ""              )
DefNode(CompositorNode, CMP_NODE_SEPYCCA,        def_cmp_ycc,            "SEPYCCA",        SepYCCA,          "Separate YCbCrA",   ""              )
DefNode(CompositorNode, CMP_NODE_COMBYCCA,       def_cmp_ycc,            "COMBYCCA",       CombYCCA,         "Combine YCbCrA",    ""              )
DefNode(CompositorNode, CMP_NODE_SEPYUVA,        0,                      "SEPYUVA",        SepYUVA,          "Separate YUVA",     ""              )
DefNode(CompositorNode, CMP_NODE_COMBYUVA,       0,                      "COMBYUVA",       CombYUVA,         "Combine YUVA",      ""              )
DefNode(CompositorNode, CMP_NODE_DIFF_MATTE,     def_cmp_diff_matte,     "DIFF_MATTE",     DiffMatte,        "Difference Key",    ""              )
DefNode(CompositorNode, CMP_NODE_COLOR_SPILL,    def_cmp_color_spill,    "COLOR_SPILL",    ColorSpill,       "Color Spill",       ""              )
DefNode(CompositorNode, CMP_NODE_CHROMA_MATTE,   def_cmp_chroma_matte,   "CHROMA_MATTE",   ChromaMatte,      "Chroma Key",        ""              )
DefNode(CompositorNode, CMP_NODE_CHANNEL_MATTE,  def_cmp_channel_matte,  "CHANNEL_MATTE",  ChannelMatte,     "Channel Key",       ""              )
DefNode(CompositorNode, CMP_NODE_FLIP,           def_cmp_flip,           "FLIP",           Flip,             "Flip",              ""              )
DefNode(CompositorNode, CMP_NODE_SPLITVIEWER,    def_cmp_splitviewer,    "SPLITVIEWER",    SplitViewer,      "Split Viewer",      ""              )
DefNode(CompositorNode, CMP_NODE_MAP_UV,         def_cmp_map_uv,         "MAP_UV",         MapUV,            "Map UV",            ""              )
DefNode(CompositorNode, CMP_NODE_ID_MASK,        def_cmp_id_mask,        "ID_MASK",        IDMask,           "ID Mask",           ""              )
DefNode(CompositorNode, CMP_NODE_DOUBLEEDGEMASK, def_cmp_double_edge_mask,"DOUBLEEDGEMASK", DoubleEdgeMask,  "Double Edge Mask",  ""              )
DefNode(CompositorNode, CMP_NODE_DEFOCUS,        def_cmp_defocus,        "DEFOCUS",        Defocus,          "Defocus",           ""              )
DefNode(CompositorNode, CMP_NODE_DISPLACE,       0,                      "DISPLACE",       Displace,         "Displace",          ""              )
DefNode(CompositorNode, CMP_NODE_COMBHSVA,       0,                      "COMBHSVA",       CombHSVA,         "Combine HSVA",      ""              )
DefNode(CompositorNode, CMP_NODE_MATH,           def_math,               "MATH",           Math,             "Math",              ""              )
DefNode(CompositorNode, CMP_NODE_LUMA_MATTE,     def_cmp_luma_matte,     "LUMA_MATTE",     LumaMatte,        "Luminance Key",     ""              )
DefNode(CompositorNode, CMP_NODE_BRIGHTCONTRAST, def_cmp_brightcontrast, "BRIGHTCONTRAST", BrightContrast,   "Bright/Contrast",   ""              )
DefNode(CompositorNode, CMP_NODE_GAMMA,          0,                      "GAMMA",          Gamma,            "Gamma",             ""              )
DefNode(CompositorNode, CMP_NODE_INVERT,         def_cmp_invert,         "INVERT",         Invert,           "Invert",            ""              )
DefNode(CompositorNode, CMP_NODE_NORMALIZE,      0,                      "NORMALIZE",      Normalize,        "Normalize",         ""              )
DefNode(CompositorNode, CMP_NODE_CROP,           def_cmp_crop,           "CROP",           Crop,             "Crop",              ""              )
DefNode(CompositorNode, CMP_NODE_DBLUR,          def_cmp_dblur,          "DBLUR",          DBlur,            "Directional Blur",  ""              )
DefNode(CompositorNode, CMP_NODE_BILATERALBLUR,  def_cmp_bilateral_blur, "BILATERALBLUR",  Bilateralblur,    "Bilateral Blur",    ""              )
DefNode(CompositorNode, CMP_NODE_PREMULKEY,      def_cmp_premul_key,     "PREMULKEY",      PremulKey,        "Alpha Convert",     ""              )
DefNode(CompositorNode, CMP_NODE_GLARE,          def_cmp_glare,          "GLARE",          Glare,            "Glare",             ""              )
DefNode(CompositorNode, CMP_NODE_TONEMAP,        def_cmp_tonemap,        "TONEMAP",        Tonemap,          "Tonemap",           ""              )
DefNode(CompositorNode, CMP_NODE_LENSDIST,       def_cmp_lensdist,       "LENSDIST",       Lensdist,         "Lens Distortion",   ""              )
DefNode(CompositorNode, CMP_NODE_VIEW_LEVELS,    def_cmp_levels,         "LEVELS",         Levels,           "Levels",            ""              )
DefNode(CompositorNode, CMP_NODE_COLOR_MATTE,    def_cmp_color_matte,    "COLOR_MATTE",    ColorMatte,       "Color Key",         ""              )
DefNode(CompositorNode, CMP_NODE_DIST_MATTE,     def_cmp_distance_matte, "DISTANCE_MATTE", DistanceMatte,    "Distance Key",      ""              )
DefNode(CompositorNode, CMP_NODE_COLORBALANCE,   def_cmp_colorbalance,   "COLORBALANCE",   ColorBalance,     "Color Balance",     ""              )
DefNode(CompositorNode, CMP_NODE_HUECORRECT,     def_cmp_huecorrect,     "HUECORRECT",     HueCorrect,       "Hue Correct",       ""              )
DefNode(CompositorNode, CMP_NODE_MOVIECLIP,      def_cmp_movieclip,      "MOVIECLIP",      MovieClip,        "Movie Clip",        ""              )
DefNode(CompositorNode, CMP_NODE_TRANSFORM,      dev_cmd_transform,      "TRANSFORM",      Transform,        "Transform",         ""              )
DefNode(CompositorNode, CMP_NODE_STABILIZE2D,    def_cmp_stabilize2d,    "STABILIZE2D",    Stabilize,        "Stabilize 2D",      ""              )
DefNode(CompositorNode, CMP_NODE_MOVIEDISTORTION,def_cmp_moviedistortion,"MOVIEDISTORTION",MovieDistortion,  "Movie Distortion",  ""              )
DefNode(CompositorNode, CMP_NODE_MASK_BOX,       def_cmp_boxmask,        "BOXMASK",        BoxMask,          "Box Mask",          ""              )
DefNode(CompositorNode, CMP_NODE_MASK_ELLIPSE,   def_cmp_ellipsemask,    "ELLIPSEMASK",    EllipseMask,      "Ellipse Mask",      ""              )
DefNode(CompositorNode, CMP_NODE_BOKEHIMAGE,     def_cmp_bokehimage,     "BOKEHIMAGE",     BokehImage,       "Bokeh Image",       ""              )
DefNode(CompositorNode, CMP_NODE_BOKEHBLUR,      def_cmp_bokehblur,      "BOKEHBLUR",      BokehBlur,        "Bokeh Blur",        ""              )
DefNode(CompositorNode, CMP_NODE_SWITCH,         def_cmp_switch,         "SWITCH",         Switch,           "Switch",            ""              )
DefNode(CompositorNode, CMP_NODE_SWITCH_VIEW,    def_cmp_switch_view,    "VIEWSWITCH",     SwitchView,       "View Switch",       ""              )
DefNode(CompositorNode, CMP_NODE_COLORCORRECTION,def_cmp_colorcorrection,"COLORCORRECTION",ColorCorrection,  "Color Correction",  ""              )
DefNode(CompositorNode, CMP_NODE_MASK,           def_cmp_mask,           "MASK",           Mask,             "Mask",              ""              )
DefNode(CompositorNode, CMP_NODE_KEYINGSCREEN,   def_cmp_keyingscreen,   "KEYINGSCREEN",   KeyingScreen,     "Keying Screen",     ""              )
DefNode(CompositorNode, CMP_NODE_KEYING,         def_cmp_keying,         "KEYING",         Keying,           "Keying",            ""              )
DefNode(CompositorNode, CMP_NODE_TRACKPOS,       def_cmp_trackpos,       "TRACKPOS",       TrackPos,         "Track Position",    ""              )
DefNode(CompositorNode, CMP_NODE_PIXELATE,       0,                      "PIXELATE",       Pixelate,         "Pixelate",          ""              )
DefNode(CompositorNode, CMP_NODE_PLANETRACKDEFORM,def_cmp_planetrackdeform,"PLANETRACKDEFORM",PlaneTrackDeform,"Plane Track Deform",""            )
DefNode(CompositorNode, CMP_NODE_CORNERPIN,      0,                      "CORNERPIN",      CornerPin,        "Corner Pin",        ""              )
DefNode(CompositorNode, CMP_NODE_SUNBEAMS,       def_cmp_sunbeams,       "SUNBEAMS",       SunBeams,         "Sun Beams",         ""              )
DefNode(CompositorNode, CMP_NODE_CRYPTOMATTE,    def_cmp_cryptomatte,    "CRYPTOMATTE_V2", CryptomatteV2,    "Cryptomatte",       ""              )
DefNode(CompositorNode, CMP_NODE_CRYPTOMATTE_LEGACY, def_cmp_cryptomatte_legacy, "CRYPTOMATTE", Cryptomatte, "Cryptomatte (Legacy)", ""           )
DefNode(CompositorNode, CMP_NODE_DENOISE,        def_cmp_denoise,        "DENOISE",        Denoise,          "Denoise",           ""              )
DefNode(CompositorNode, CMP_NODE_EXPOSURE,       0,                      "EXPOSURE",       Exposure,         "Exposure",          ""              )
DefNode(CompositorNode, CMP_NODE_ANTIALIASING,   def_cmp_antialiasing,   "ANTIALIASING",   AntiAliasing,     "Anti-Aliasing",     ""              )

DefNode(TextureNode,    TEX_NODE_OUTPUT,         def_tex_output,         "OUTPUT",         Output,           "Output",            ""              )
DefNode(TextureNode,    TEX_NODE_CHECKER,        0,                      "CHECKER",        Checker,          "Checker",           ""              )
DefNode(TextureNode,    TEX_NODE_TEXTURE,        def_texture,            "TEXTURE",        Texture,          "Texture",           ""              )
DefNode(TextureNode,    TEX_NODE_BRICKS,         def_tex_bricks,         "BRICKS",         Bricks,           "Bricks",            ""              )
DefNode(TextureNode,    TEX_NODE_MATH,           def_math,               "MATH",           Math,             "Math",              ""              )
DefNode(TextureNode,    TEX_NODE_MIX_RGB,        def_mix_rgb,            "MIX_RGB",        MixRGB,           "Mix RGB",           ""              )
DefNode(TextureNode,    TEX_NODE_RGBTOBW,        0,                      "RGBTOBW",        RGBToBW,          "RGB to BW",         ""              )
DefNode(TextureNode,    TEX_NODE_VALTORGB,       def_colorramp,          "VALTORGB",       ValToRGB,         "ColorRamp",         ""              )
DefNode(TextureNode,    TEX_NODE_IMAGE,          def_tex_image,          "IMAGE",          Image,            "Image",             ""              )
DefNode(TextureNode,    TEX_NODE_CURVE_RGB,      def_rgb_curve,          "CURVE_RGB",      CurveRGB,         "RGB Curves",        ""              )
DefNode(TextureNode,    TEX_NODE_INVERT,         0,                      "INVERT",         Invert,           "Invert",            ""              )
DefNode(TextureNode,    TEX_NODE_HUE_SAT,        0,                      "HUE_SAT",        HueSaturation,    "Hue/Saturation",    ""              )
DefNode(TextureNode,    TEX_NODE_CURVE_TIME,     def_time,               "CURVE_TIME",     CurveTime,        "Curve Time",        ""              )
DefNode(TextureNode,    TEX_NODE_ROTATE,         0,                      "ROTATE",         Rotate,           "Rotate",            ""              )
DefNode(TextureNode,    TEX_NODE_VIEWER,         0,                      "VIEWER",         Viewer,           "Viewer",            ""              )
DefNode(TextureNode,    TEX_NODE_TRANSLATE,      0,                      "TRANSLATE",      Translate,        "Translate",         ""              )
DefNode(TextureNode,    TEX_NODE_COORD,          0,                      "COORD",          Coordinates,      "Coordinates",       ""              )
DefNode(TextureNode,    TEX_NODE_DISTANCE,       0,                      "DISTANCE",       Distance,         "Distance",          ""              )
DefNode(TextureNode,    TEX_NODE_COMPOSE,        0,                      "COMPOSE",        Compose,          "Combine RGBA",      ""              )
DefNode(TextureNode,    TEX_NODE_DECOMPOSE,      0,                      "DECOMPOSE",      Decompose,        "Separate RGBA",     ""              )
DefNode(TextureNode,    TEX_NODE_VALTONOR,       0,                      "VALTONOR",       ValToNor,         "Value to Normal",   ""              )
DefNode(TextureNode,    TEX_NODE_SCALE,          0,                      "SCALE",          Scale,            "Scale",             ""              )
DefNode(TextureNode,    TEX_NODE_AT,             0,                      "AT",             At,               "At",                ""              )
/* procedural textures */
DefNode(TextureNode,    TEX_NODE_PROC+TEX_VORONOI, 0,                    "TEX_VORONOI",    TexVoronoi,       "Voronoi",           ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_BLEND, 0,                      "TEX_BLEND",      TexBlend,         "Blend",             ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_MAGIC, 0,                      "TEX_MAGIC",      TexMagic,         "Magic",             ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_MARBLE, 0,                     "TEX_MARBLE",     TexMarble,        "Marble",            ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_CLOUDS, 0,                     "TEX_CLOUDS",     TexClouds,        "Clouds",            ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_WOOD, 0,                       "TEX_WOOD",       TexWood,          "Wood",              ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_MUSGRAVE, 0,                   "TEX_MUSGRAVE",   TexMusgrave,      "Musgrave",          ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_NOISE, 0,                      "TEX_NOISE",      TexNoise,         "Noise",             ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_STUCCI, 0,                     "TEX_STUCCI",     TexStucci,        "Stucci",            ""              )
DefNode(TextureNode,    TEX_NODE_PROC+TEX_DISTNOISE, 0,                  "TEX_DISTNOISE",  TexDistNoise,     "Distorted Noise",   ""              )

DefNode(FunctionNode, FN_NODE_BOOLEAN_MATH,  def_boolean_math,  "BOOLEAN_MATH",  BooleanMath,  "Boolean Math", "")
DefNode(FunctionNode, FN_NODE_FLOAT_COMPARE, def_float_compare, "FLOAT_COMPARE", FloatCompare, "Float Compare", "")
DefNode(FunctionNode, FN_NODE_RANDOM_FLOAT, 0,                  "RANDOM_FLOAT", RandomFloat, "Random Float", "")
DefNode(FunctionNode, FN_NODE_INPUT_VECTOR, def_fn_input_vector, "INPUT_VECTOR", InputVector, "Vector", "")
DefNode(FunctionNode, FN_NODE_INPUT_STRING, def_fn_input_string, "INPUT_STRING", InputString, "String", "")

DefNode(GeometryNode, GEO_NODE_TRIANGULATE, def_geo_triangulate, "TRIANGULATE", Triangulate, "Triangulate", "")
DefNode(GeometryNode, GEO_NODE_EDGE_SPLIT, 0, "EDGE_SPLIT", EdgeSplit, "Edge Split", "")
DefNode(GeometryNode, GEO_NODE_TRANSFORM, 0, "TRANSFORM", Transform, "Transform", "")
DefNode(GeometryNode, GEO_NODE_SUBDIVISION_SURFACE, 0, "SUBDIVISION_SURFACE", SubdivisionSurface, "Subdivision Surface", "")
DefNode(GeometryNode, GEO_NODE_BOOLEAN, def_geo_boolean, "BOOLEAN", Boolean, "Boolean", "")
DefNode(GeometryNode, GEO_NODE_POINT_DISTRIBUTE, def_geo_point_distribute, "POINT_DISTRIBUTE", PointDistribute, "Point Distribute", "")
DefNode(GeometryNode, GEO_NODE_POINT_INSTANCE, def_geo_point_instance, "POINT_INSTANCE", PointInstance, "Point Instance", "")
DefNode(GeometryNode, GEO_NODE_OBJECT_INFO, def_geo_object_info, "OBJECT_INFO", ObjectInfo, "Object Info", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_RANDOMIZE, def_geo_attribute_randomize, "ATTRIBUTE_RANDOMIZE", AttributeRandomize, "Attribute Randomize", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_MATH, def_geo_attribute_math, "ATTRIBUTE_MATH", AttributeMath, "Attribute Math", "")
DefNode(GeometryNode, GEO_NODE_JOIN_GEOMETRY, 0, "JOIN_GEOMETRY", JoinGeometry, "Join Geometry", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_FILL, def_geo_attribute_fill, "ATTRIBUTE_FILL", AttributeFill, "Attribute Fill", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_MIX, def_geo_attribute_mix, "ATTRIBUTE_MIX", AttributeMix, "Attribute Mix", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_COLOR_RAMP, def_geo_attribute_color_ramp, "ATTRIBUTE_COLOR_RAMP", AttributeColorRamp, "Attribute Color Ramp", "")
DefNode(GeometryNode, GEO_NODE_POINT_SEPARATE, 0, "POINT_SEPARATE", PointSeparate, "Point Separate", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_COMPARE, def_geo_attribute_attribute_compare, "ATTRIBUTE_COMPARE", AttributeCompare, "Attribute Compare", "")
DefNode(GeometryNode, GEO_NODE_POINT_ROTATE, def_geo_point_rotate, "POINT_ROTATE", RotatePoints, "Point Rotate", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_VECTOR_MATH, def_geo_attribute_vector_math, "ATTRIBUTE_VECTOR_MATH", AttributeVectorMath, "Attribute Vector Math", "")
DefNode(GeometryNode, GEO_NODE_ALIGN_ROTATION_TO_VECTOR, def_geo_align_rotation_to_vector, "ALIGN_ROTATION_TO_VECTOR", AlignRotationToVector, "Align Rotation to Vector", "")
DefNode(GeometryNode, GEO_NODE_POINT_SCALE, def_geo_point_scale, "POINT_SCALE", PointScale, "Point Scale", "")
DefNode(GeometryNode, GEO_NODE_POINT_TRANSLATE, def_geo_point_translate, "POINT_TRANSLATE", PointTranslate, "Point Translate", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_SAMPLE_TEXTURE, def_geo_attribute_sample_texture, "ATTRIBUTE_SAMPLE_TEXTURE", AttributeSampleTexture, "Attribute Sample Texture", "")
DefNode(GeometryNode, GEO_NODE_POINTS_TO_VOLUME, def_geo_points_to_volume, "POINTS_TO_VOLUME", PointsToVolume, "Points to Volume", "")
DefNode(GeometryNode, GEO_NODE_COLLECTION_INFO, def_geo_collection_info, "COLLECTION_INFO", CollectionInfo, "Collection Info", "")
DefNode(GeometryNode, GEO_NODE_IS_VIEWPORT, 0, "IS_VIEWPORT", IsViewport, "Is Viewport", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_PROXIMITY, def_geo_attribute_proximity, "ATTRIBUTE_PROXIMITY", AttributeProximity, "Attribute Proximity", "")
DefNode(GeometryNode, GEO_NODE_VOLUME_TO_MESH, def_geo_volume_to_mesh, "VOLUME_TO_MESH", VolumeToMesh, "Volume to Mesh", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_COMBINE_XYZ, def_geo_attribute_combine_xyz, "ATTRIBUTE_COMBINE_XYZ", AttributeCombineXYZ, "Attribute Combine XYZ", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_SEPARATE_XYZ, def_geo_attribute_separate_xyz, "ATTRIBUTE_SEPARATE_XYZ", AttributeSeparateXYZ, "Attribute Separate XYZ", "")
DefNode(GeometryNode, GEO_NODE_SUBDIVIDE, 0, "SUBDIVIDE", Subdivide, "Subdivide", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_REMOVE, 0, "ATTRIBUTE_REMOVE", AttributeRemove, "Attribute Remove", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_CONVERT, def_geo_attribute_convert, "ATTRIBUTE_CONVERT", AttributeConvert, "Attribute Convert", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_CUBE, 0, "MESH_PRIMITIVE_CUBE", MeshCube, "Cube", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_CIRCLE, def_geo_mesh_circle, "MESH_PRIMITIVE_CIRCLE", MeshCircle, "Circle", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_UV_SPHERE, 0, "MESH_PRIMITIVE_UV_SPHERE", MeshUVSphere, "UV Sphere", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_CYLINDER, def_geo_mesh_cylinder, "MESH_PRIMITIVE_CYLINDER", MeshCylinder, "Cylinder", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_ICO_SPHERE, 0, "MESH_PRIMITIVE_ICO_SPHERE", MeshIcoSphere, "Ico Sphere", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_CONE, def_geo_mesh_cone, "MESH_PRIMITIVE_CONE", MeshCone, "Cone", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_LINE, def_geo_mesh_line, "MESH_PRIMITIVE_LINE", MeshLine, "Line", "")
DefNode(GeometryNode, GEO_NODE_MESH_PRIMITIVE_GRID, 0, "MESH_PRIMITIVE_GRID", MeshGrid, "Grid", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_MAP_RANGE, def_geo_attribute_map_range, "ATTRIBUTE_MAP_RANGE", AttributeMapRange, "Attribute Map Range", "")
DefNode(GeometryNode, GEO_NODE_ATTRIBUTE_CLAMP, def_geo_attribute_clamp, "ATTRIBUTE_CLAMP", AttributeClamp, "Attribute Clamp", "")
DefNode(GeometryNode, GEO_NODE_BOUNDING_BOX, 0, "BOUNDING_BOX", BoundBox, "Bounding Box", "")

DefNode( ShaderNode,	 SH_NODE_OCT_DIFFUSE_MAT,			def_oct_diffuse,						"OCT_DIFFUSE_MAT",			OctDiffuseMat,			"Diffuse Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_GLOSSY_MAT,			def_oct_glossy,			"OCT_GLOSSY_MAT",			OctGlossyMat,			"Glossy Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_SPECULAR_MAT,			def_oct_specular,		"OCT_SPECULAR_MAT",			OctSpecularMat,			"Specular Material",	"");
DefNode( ShaderNode,	 SH_NODE_OCT_MIX_MAT,				def_oct_mix,						"OCT_MIX_MAT",				OctMixMat,				"Mix Material",			"");
DefNode( ShaderNode,	 SH_NODE_OCT_PORTAL_MAT,			0,						"OCT_PORTAL_MAT",			OctPortalMat,			"Portal Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_TOON_MAT,				def_oct_toon,			"OCT_TOON_MAT",				OctToonMat,				"Toon Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_METAL_MAT,				def_oct_metal,			"OCT_METAL_MAT",			OctMetalMat,			"Metal Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_UNIVERSAL_MAT,			def_oct_universal,		"OCT_UNIVERSAL_MAT",		OctUniversalMat,		"Universal Material",	"");
DefNode( ShaderNode,   SH_NODE_OCT_SHADOW_CATCHER_MAT,     def_oct_shadow_catcher,              "OCT_SHADOW_CATCHER_MAT", OctShadowCatcherMat, "ShadowCatcher Material",""   );
DefNode( ShaderNode,   SH_NODE_OCT_LAYERED_MAT,     def_oct_layered_mat,	 "OCT_LAYERED_MAT",		OctLayeredMat,	"Layered Material",""   );
DefNode( ShaderNode,   SH_NODE_OCT_COMPOSITE_MAT,   def_oct_composite_mat, "OCT_COMPOSITE_MAT",	OctCompositeMat,	"Composite Material",""   );
DefNode( ShaderNode,	 SH_NODE_OCT_HAIR_MAT,				def_oct_hair,			"OCT_HAIR_MAT",			OctHairMat,			"Hair Material",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_NULL_MAT,				0,			"OCT_NULL_MAT",			OctNullMat,			"Null Material",		"");
DefNode( ShaderNode, SH_NODE_OCT_CLIPPING_MAT, 0, "OCT_CLIPPING_MAT", OctClippingMat, "Clipping Material", "");

DefNode( ShaderNode,   SH_NODE_OCT_GROUP_LAYER,   def_oct_group_layer,	"OCT_GROUP_LAYER",		OctGroupLayer,	"Group Layer",""   );
DefNode( ShaderNode,   SH_NODE_OCT_DIFFUSE_LAYER, def_oct_diffuse_layer,	"OCT_DIFFUSE_LAYER",	OctDiffuseLayer, "Diffuse Layer",""   );
DefNode( ShaderNode,   SH_NODE_OCT_METALLIC_LAYER, def_oct_metal,			"OCT_METALLIC_LAYER",	OctMetallicLayer, "Metallic Layer",""   );
DefNode( ShaderNode,   SH_NODE_OCT_SHEEN_LAYER,	0,	"OCT_SHEEN_LAYER",	OctSheenLayer, "Sheen Layer",""   );
DefNode( ShaderNode,   SH_NODE_OCT_SPECULAR_LAYER, def_oct_specular,	"OCT_SPECULAR_LAYER",	OctSpecularLayer, "Specular Layer",""   );


DefNode( ShaderNode,	 SH_NODE_OCT_IMAGE_TEX,				def_oct_tex_image,		"OCT_IMAGE_TEX",			OctImageTex,			"Image Tex",			"");
DefNode( ShaderNode,	 SH_NODE_OCT_FLOAT_IMAGE_TEX,		def_oct_tex_image,		"OCT_FIMAGE_TEX",			OctFloatImageTex,		"Float Image Tex",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_ALPHA_IMAGE_TEX,		def_oct_tex_image,		"OCT_AIMAGE_TEX",			OctAlphaImageTex,		"Alpha Image Tex",		"");
DefNode( ShaderNode,	 SH_NODE_OCT_INSTANCE_COLOR_TEX,	def_oct_tex_image,		"OCT_INSTANCE_COLOR_TEX",	OctInstanceColorTex,	"Instance Color Tex",	"");

DefNode( ShaderNode, SH_NODE_OCT_FLOAT_TEX, 0, "OCT_FLOAT_TEX", OctFloatTex, "Grayscale Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RGB_SPECTRUM_TEX, 0, "OCT_RGBSPECTRUM_TEX", OctRGBSpectrumTex, "RGBSpectrum Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_GAUSSIAN_SPECTRUM_TEX, 0, "OCT_GAUSSSPECTRUM_TEX", OctGaussSpectrumTex, "Gaussian Spectrum Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CHECKS_TEX, 0, "OCT_CHECKS_TEX", OctChecksTex, "Checks Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_MARBLE_TEX, 0, "OCT_MARBLE_TEX", OctMarbleTex, "Marble Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RIDGED_FRACTAL_TEX, 0, "OCT_RDGFRACTAL_TEX", OctRidgedFractalTex, "Ridged Fractal Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SAW_WAVE_TEX, 0, "OCT_SAWWAVE_TEX", OctSawWaveTex, "Saw Wave Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SINE_WAVE_TEX, 0, "OCT_SINEWAVE_TEX", OctSineWaveTex, "Sine Wave Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_TRIANGLE_WAVE_TEX, 0, "OCT_TRIWAVE_TEX", OctTriWaveTex, "Triangle Wave Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_TURBULENCE_TEX, 0, "OCT_TURBULENCE_TEX", OctTurbulenceTex, "Turbulence Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CLAMP_TEX, 0, "OCT_CLAMP_TEX", OctClampTex, "Clamp Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COSINE_MIX_TEX, 0, "OCT_COSMIX_TEX", OctCosineMixTex, "Cosine Mix Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_INVERT_TEX, 0, "OCT_INVERT_TEX", OctInvertTex, "Invert Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_MIX_TEX, 0, "OCT_MIX_TEX", OctMixTex, "Mix Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_MULTIPLY_TEX, 0, "OCT_MULTIPLY_TEX", OctMultiplyTex, "Multiply Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_ADD_TEX, 0, "OCT_ADD_TEX", OctAddTex, "Add Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SUBTRACT_TEX, 0, "OCT_SUBTRACT_TEX", OctSubtractTex, "Subtract Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COMPARE_TEX, 0, "OCT_COMPARE_TEX", OctCompareTex, "Compare Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_TRIPLANAR_TEX, def_oct_triplanar_coordinate_space_mode, "OCT_TRIPLANAR_TEX", OctTriplanarTex, "Triplanar Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_FALLOFF_TEX, def_oct_falloff_map_tex, "OCT_FALLOFF_TEX", OctFalloffTex, "Falloff Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COLOR_CORRECT_TEX, 0, "OCT_CCORRECT_TEX", OctColorCorrectTex, "Color Correct Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CHAOS_TEX, 0, "OCT_CHAOS_TEX", OctChaosTex, "Chaos Tex", "");

DefNode( ShaderNode, SH_NODE_OCT_DIRT_TEX, def_oct_texture_dirt, "OCT_DIRT_TEX", OctDirtTex, "Dirt Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_GRADIENT_TEX, def_oct_colorramp, "OCT_GRADIENT_TEX", OctGradientTex, "Gradient Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RANDOM_COLOR_TEX, 0, "OCT_RANDOM_COLOR_TEX", OctRandomColorTex, "Random Color Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_DISPLACEMENT_TEX, def_oct_displacement_tex, "OCT_DISPLACEMENT_TEX", OctDisplacementTex, "Texture Displacement", "");
DefNode( ShaderNode, SH_NODE_OCT_VERTEX_DISPLACEMENT_TEX,def_oct_vertex_displacement_tex, "OCT_VERTEX_DISPLACEMENT_TEX",  OctVertexDisplacementTex,  "Vertex Displacement",          ""    );
DefNode( ShaderNode, SH_NODE_OCT_VERTEX_DISPLACEMENT_MIXER_TEX,def_oct_vertex_displacement_mixer_tex, "OCT_VERTEX_DISPLACEMENT_MIXER_TEX",  OctVertexDisplacementMixerTex,  "Vertex Displacement Mixer",          ""    );
DefNode( ShaderNode, SH_NODE_OCT_POLYGON_SIDE_TEX, 0, "OCT_POLYGON_SIDE_TEX", OctPolygonSideTex, "Polygon Side Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_NOISE_TEX, def_oct_noise_tex, "OCT_NOISE_TEX", OctNoiseTex, "Noise Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CINEMA4D_NOISE_TEX, def_oct_cinema4d_noise_tex, "OCT_CINEMA4D_NOISE_TEX", OctCinema4DNoiseTex, "Cinema4D Noise Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_VOLUME_RAMP_TEX, def_oct_colorramp, "OCT_VOLUME_RAMP_TEX", OctVolumeRampTex, "Volume Ramp Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_W_TEX, 0, "OCT_W_TEX", OctWTex, "W Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_BAKING_TEX, def_oct_baking_tex, "OCT_BAKING_TEX", OctBakingTex, "Baking Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_UVW_TRANSFORM_TEX, 0, "OCT_UVW_TRANSFORM_TEX", OctUVWTransformTex, "UVW Transform Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_INSTANCE_RANGE_TEX, 0, "OCT_INSTANCE_RANGE_TEX", OctInstanceRangeTex, "Instance Range Tex", "");

DefNode( ShaderNode, SH_NODE_OCT_OSL_TEX, def_sh_script, "OCT_OSL_TEX", OctOSLTex, "OSL Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_TOON_RAMP_TEX, def_oct_colorramp, "OCT_TOON_RAMP_TEX", OctToonRampTex, "Toon Ramp Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_IMAGE_TILE_TEX, def_oct_tex_image_tile, "OCT_IMAGE_TILE_TEX", OctImageTileTex, "Image Tile Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_FLOAT_VERTEX_TEX, 0, "OCT_FLOAT_VERTEX_TEX", OctFloatVertexTex, "Float Vertex Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COLOR_VERTEX_TEX, 0, "OCT_COLOR_VERTEX_TEX", OctColorVertexTex, "Color Vertex Tex", "");

DefNode( ShaderNode, SH_NODE_OCT_BBODY_EMI, 0, "OCT_BBODY_EMI", OctBlackBodyEmission, "Black Body Emission", "");
DefNode( ShaderNode, SH_NODE_OCT_TEXTURE_EMI, 0, "OCT_TEXT_EMI", OctTextureEmission, "Texture Emission", "");
DefNode( ShaderNode, SH_NODE_OCT_TOON_DIRECTION_LIGHT, def_oct_toon_direction_light, "OCT_TOON_DIRECTION_LIGHT", OctToonDirectionLight, "Toon Directional Light", "");
DefNode( ShaderNode, SH_NODE_OCT_TOON_POINT_LIGHT, 0, "OCT_TOON_POINT_LIGHT", OctToonPointLight, "Toon Point Light", "");

DefNode( ShaderNode, SH_NODE_OCT_SCALE_TRN, 0, "OCT_SCALE_TRN", OctScaleTransform, "Scale Transform", "");
DefNode( ShaderNode, SH_NODE_OCT_ROTATE_TRN, def_oct_rotation_order, "OCT_ROTATE_TRN", OctRotateTransform, "Rotate Transform", "");
DefNode( ShaderNode, SH_NODE_OCT_FULL_TRN, def_oct_rotation_order, "OCT_FULL_TRN", OctFullTransform, "Full Transform", "");
DefNode( ShaderNode, SH_NODE_OCT_2D_TRN, 0, "OCT_2D_TRN", Oct2DTransform, "2D Transform", "");
DefNode( ShaderNode, SH_NODE_OCT_3D_TRN, def_oct_rotation_order, "OCT_3D_TRN", Oct3DTransform, "3D Transform", "");

DefNode( ShaderNode, SH_NODE_OCT_ABSORP_MED, def_oct_medium, "OCT_ABSORP_MED", OctAbsorptionMedium, "Absorption Medium", "");
DefNode( ShaderNode, SH_NODE_OCT_SCATTER_MED, def_oct_medium, "OCT_SCATTER_MED", OctScatteringMedium, "Scatter Medium", "");
DefNode( ShaderNode, SH_NODE_OCT_VOLUME_MED, def_oct_medium, "OCT_VOLUME_MED", OctVolumeMedium, "Volume Medium", "");
DefNode( ShaderNode, SH_NODE_OCT_RANDOMWALK_MED, def_oct_medium, "OCT_RANDOMWALK_MED", OctRandomWalkMedium, "RandomWalk Medium", "");

DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_XYZ, def_oct_coordinate_space_mode, "OCT_XYZ_PROJ", OctXYZProjection, "XYZ Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_BOX, def_oct_coordinate_space_mode, "OCT_BOX_PROJ", OctBoxProjection, "Box Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_CYL, def_oct_coordinate_space_mode, "OCT_CYL_PROJ", OctCylProjection, "Cylindrical Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_PERSP, def_oct_coordinate_space_mode, "OCT_PERSP_PROJ", OctPerspProjection, "Perspective Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_SPHERICAL, def_oct_coordinate_space_mode, "OCT_SPHERICAL_PROJ", OctSphericalProjection, "Spherical Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_UVW, 0, "OCT_UVW_PROJ", OctUVWProjection, "UVW Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_TRIPLANAR, 0, "OCT_TRIPLANAR_PROJ", OctTriplanarProjection, "Triplanar Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_OSL_UV, 0, "OCT_OSL_UV_PROJ", OctOSLUVProjection, "OSL delayed UV Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_OSL, def_sh_script, "OCT_OSL_PROJ", OctOSLProjection, "OSL Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_SAMPLE_POS_TO_UV, 0, "OCT_SAMPLE_POS_TO_UV_PROJ", OctSamplePosToUVProjection, "Sample pos. to UV Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_MAT_CAP, 0, "OCT_MAT_CAP_PROJ", OctMatCapProjection, "MatCap Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_COLOR_TO_UVW, 0, "OCT_COLOR_TO_UVW_PROJ", OctColorToUVWProjection, "Color to UVW Projection", "");
DefNode( ShaderNode, SH_NODE_OCT_PROJECTION_DISTORTED_MESH_UV, 0, "OCT_DISTORTED_MESH_UV_PROJ", OctDistortedMeshUVProjection, "Distorted mesh UV Projection", "");

DefNode( ShaderNode, SH_NODE_OCT_VALUE_FLOAT, 0, "OCT_FLOAT_VAL", OctFloatValue, "Float Value", "");
DefNode( ShaderNode, SH_NODE_OCT_VALUE_INT, 0, "OCT_INT_VAL", OctIntValue, "Int Value", "");
DefNode( ShaderNode, SH_NODE_OCT_VALUE_SUN_DIRECTION, 0, "OCT_SUN_DIRECTION", OctSunDirectionValue, "Sun Direction", "");
DefNode( ShaderNode, SH_NODE_OCT_VALUE_TEXTURE_REFERENCE, def_oct_texture_reference, "OCT_TEXTURE_REFERENCE", OctTextureReferenceValue, "Texture Reference", "");

DefNode( ShaderNode, SH_NODE_OCT_OSL_CAMERA, def_sh_script, "OCT_OSL_CAMERA", OctOSLCamera, "OSL Camera", "");
DefNode( ShaderNode, SH_NODE_OCT_OSL_BAKING_CAMERA, def_sh_script, "OCT_OSL_BAKING_CAMERA", OctOSLBakingCamera, "OSL Baking Camera", "");

DefNode( ShaderNode, SH_NODE_OCT_VECTRON, def_sh_script, "OCT_VECTRON", OctVectron, "Vectron", "");
DefNode( ShaderNode, SH_NODE_OCT_SCATTER_TOOL_SURFACE, def_oct_scatter_tool_surface, "OCT_SCATTER_TOOL_SURFACE", OctScatterToolSurface, "Scatter on Surface", "");
DefNode( ShaderNode, SH_NODE_OCT_SCATTER_TOOL_VOLUME, def_oct_scatter_tool_volume, "OCT_SCATTER_TOOL_VOLUME", OctScatterToolVolume, "Scatter in Volume", "");

DefNode( ShaderNode, SH_NODE_OCT_ROUNDEDGES, def_oct_round_edges, "OCT_ROUND_EDGES", OctRoundEdges, "Round Edges", "");

DefNode( ShaderNode, SH_NODE_OCT_OBJECT_DATA, def_oct_object_data, "OCT_OBJECT_DATA", OctObjectData, "Octane Object Data", "");

DefNode( ShaderNode, SH_NODE_OCT_TEXTURE_ENVIRONMENT, 0, "OCT_TEXTURE_ENVIRONMENT", OctTextureEnvironment, "Texture Environment", "");
DefNode( ShaderNode, SH_NODE_OCT_DAYLIGHT_ENVIRONMENT, def_oct_daylight_environment, "OCT_DAYLIGHT_ENVIRONMENT", OctDaylightEnvironment, "Daylight Environment", "");
DefNode( ShaderNode, SH_NODE_OCT_PLANETARY_ENVIRONMENT, 0, "OCT_PLANETARY_ENVIRONMENT", OctPlanetaryEnvironment, "Planetary Environment", "");

DefNode( ShaderNode, SH_NODE_OCT_CHANNEL_INVERTER_TEX, 0, "OCT_CHANNEL_INVERTER_TEX", OctChannelInverterTex, "Channel Inverter Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CHANNEL_MAPPER_TEX, 0, "OCT_CHANNEL_MAPPER_TEX", OctChannelMapperTex, "Channel Mapper Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CHANNEL_MERGER_TEX, 0, "OCT_CHANNEL_MERGER_TEX", OctChannelMergerTex, "Channel Merger Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CHANNEL_PICKER_TEX, def_oct_channel_picker, "OCT_CHANNEL_PICKER_TEX", OctChannelPickerTex, "Channel Picker Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RAY_SWITCH_TEX, 0, "OCT_RAY_SWITCH_TEX", OctRaySwitchTex, "Ray Switch Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SPOTLIGHT_TEX, def_oct_spotlight, "OCT_SPOTLIGHT_TEX", OctSpotlightTex, "Spotlight Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COMPOSITE_TEX, def_oct_composite_tex, "OCT_COMPOSITE_TEX", OctCompositeTex, "Composite Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_COMPOSITE_LAYER_TEX, def_oct_composite_layer_tex, "OCT_COMPOSITE_LAYER_TEX", OctCompositeLayerTex, "Composite Layer Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_READ_VDB_TEX, def_oct_read_vdb, "OCT_READ_VDB_TEX", OctReadVDBTex, "Read VDB Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_FLOAT_TO_GREYSCALE, 0, "OCT_FLOAT_TO_GREYSCALE_TEX", OctFloatToGreyscaleTex, "Float to greyscale Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_FLOAT3_TO_COLOR, 0, "OCT_FLOAT3_TO_COLOR_TEX", OctFloat3ToColorTex, "Float3 to color Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_FLOATS_TO_COLOR, 0, "OCT_FLOATS_TO_COLOR_TEX", OctFloatsToColorTex, "Floats to color Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SURFACE_TANGENT_DPDV, 0, "OCT_SURFACE_TANGENT_DPDV_TEX", OctSurfaceTangentDPdvTex, "Surface tangent dPdv Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SURFACE_TANGENT_DPDU, 0, "OCT_SURFACE_TANGENT_DPDU_TEX", OctSurfaceTangentDPduTex, "Surface tangent dPdu Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_UV_COORDINATE, 0, "OCT_UV_COORDINATE_TEX", OctUVCoordinateTex, "UV coordinate Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_SAMPLE_POSITION, 0, "OCT_SAMPLE_POSITION_TEX", OctSamplePositionTex, "Sample position Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_Z_DEPTH, 0, "OCT_Z_DEPTH_TEX", OctZDepthTex, "Z depth Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_BINARY_MATH_OPERATION, def_oct_binary_math_operation_tex, "OCT_BINARY_MATH_OPERATION", OctBinaryMathOperationTex, "Binary math operation Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_UNARY_MATH_OPERATION, def_oct_unary_math_operation_tex, "OCT_UNARY_MATH_OPERATION_TEX", OctUnaryMathOperationTex, "Unary math operation Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_GRADIENT_GENERATOR, def_oct_gradient_generator_tex, "OCT_GRADIENT_GENERATOR_TEX", OctGradientGeneratorTex, "Gradient generator Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_CAPTURE_TO_CUSTOM_AOV, def_oct_capture_to_custom_aov_tex, "OCT_CAPTURE_TO_CUSTOM_AOV", OctCaptureToCustomAOVTex, "Capture to custom AOV Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_POSITION, def_oct_position_tex, "OCT_POSITION_TEX", OctPositionTex, "Position Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RELATIVE_DISTANCE, def_oct_relative_distance_tex, "OCT_RELATIVE_DISTANCE_TEX", OctRelativeDistanceTex, "Relative distance Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_NORMAL, def_oct_normal_tex, "OCT_NORMAL_TEX", OctNormalTex, "Normal Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RANGE, def_oct_range_tex, "OCT_RANGE_TEX", OctRangeTex, "Range Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RANDOM_MAP, def_oct_random_map_tex, "OCT_RANDOM_MAP_TEX", OctRandomMapTex, "Random map Tex", "");
DefNode( ShaderNode, SH_NODE_OCT_RAY_DIRECTION, def_oct_ray_direction_tex, "OCT_RAY_DIRECTION_TEX", OctRayDirectionTex, "Ray direction Tex", "");

DefNode( ShaderNode, SH_NODE_OCT_AOV_OUTPUT_GROUP, def_oct_aov_output_group, "OCT_AOV_OUTPUT_GROUP", OctAovOutputGroup, "AOV Output Group", "");
DefNode( ShaderNode, SH_NODE_OCT_COLOR_AOV_OUTPUT, 0, "OCT_COLOR_AOV_OUTPUT", OctColorAovOutput, "Color AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_COMPOSITE_AOV_OUTPUT, def_oct_composite_aov_output, "OCT_COMPOSITE_AOV_OUTPUT", OctCompositeAovOutput, "Composite AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_COMPOSITE_AOV_OUTPUT_LAYER, def_oct_composite_aov_output_layer, "OCT_COMPOSITE_AOV_OUTPUT_LAYER", OctCompositeAovOutputLayer, "Composite AOV Output Layer", "");
DefNode( ShaderNode, SH_NODE_OCT_RENDER_AOV_OUTPUT, def_oct_render_aov_output, "OCT_RENDER_AOV_OUTPUT", OctRenderAovOutput, "Render AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_IMAGE_AOV_OUTPUT, def_oct_image_aov_output, "OCT_IMAGE_AOV_OUTPUT", OctImageAovOutput, "Image AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_CLAMP_AOV_OUTPUT, def_oct_clamp_aov_output, "OCT_CLAMP_AOV_OUTPUT", OctClampAovOutput, "Clamp AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_COLOR_CORRECTION_AOV_OUTPUT, 0, "OCT_COLOR_CORRECTION_AOV_OUTPUT", OctColorCorrectionAovOutput, "Color correction AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_MAP_RANGE_AOV_OUTPUT, def_oct_map_range_aov_output, "OCT_MAP_RANGE_AOV_OUTPUT", OctMapRangeAovOutput, "Map range AOV Output", "");
DefNode( ShaderNode, SH_NODE_OCT_LIGHT_MIXING_AOV_OUTPUT, 0, "OCT_LIGHT_MIXING_AOV_OUTPUT", OctLightMixingAovOutput, "Light mixing AOV Output", "");

/* undefine macros */
#undef DefNode

/* clang-format on */
