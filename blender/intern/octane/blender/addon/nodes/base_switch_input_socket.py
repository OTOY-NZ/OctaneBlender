# <pep8 compliant>

# BEGIN OCTANE GENERATED CODE BLOCK #
import bpy  # noqa
from bpy.props import IntProperty  # noqa
from octane.utils import consts, runtime_globals, utility  # noqa
from octane.nodes.base_socket import OctaneBaseSocket, OctaneSwitchInput  # noqa


class OctaneBoolSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneBoolSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Bool
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BOOL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneFloatSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneFloatSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Float
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FLOAT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneIntSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneIntSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Int
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_INT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneTransformSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneTransformSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Transform
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TRANSFORM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneTextureSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneTextureSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Texture
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEXTURE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneEmissionSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneEmissionSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Emission
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_EMISSION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneMaterialSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneMaterialSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Material
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneCameraSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneCameraSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Camera
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_CAMERA)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneEnvironmentSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneEnvironmentSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Environment
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENVIRONMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneImagerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneImagerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Imager
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_IMAGER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneKernelSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneKernelSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Kernel
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_KERNEL)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneGeometrySwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneGeometrySwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Geometry
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_GEOMETRY)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneMediumSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneMediumSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Medium
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MEDIUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctanePhaseFunctionSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctanePhaseFunctionSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.PhaseFunction
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PHASEFUNCTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneFilmSettingsSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneFilmSettingsSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.FilmSettings
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_FILM_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneEnumSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneEnumSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Enum
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ENUM)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneObjectLayerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneObjectLayerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.ObjectLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OBJECTLAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctanePostProcessingSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctanePostProcessingSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.PostProcessing
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POSTPROCESSING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRenderTargetSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneRenderTargetSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.RenderTarget
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDERTARGET)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneProjectionSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneProjectionSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Projection
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_PROJECTION)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneDisplacementSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneDisplacementSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.Displacement
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_DISPLACEMENT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneStringSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneStringSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.String
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_STRING)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRenderAOVSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneRenderAOVSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.RenderAOV
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_PASSES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRenderLayerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneRenderLayerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.RenderLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneVolumeRampSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneVolumeRampSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.VolumeRamp
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_VOLUME_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneAnimationSettingsSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneAnimationSettingsSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.AnimationSettings
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ANIMATION_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneLUTSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneLUTSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.LUT
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_LUT)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRenderJobSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneRenderJobSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.RenderJob
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_RENDER_JOB)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneToonRampSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneToonRampSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.ToonRamp
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TOON_RAMP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneBitMaskSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneBitMaskSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.BitMask
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BIT_MASK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneRoundEdgesSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneRoundEdgesSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.RoundEdges
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_ROUND_EDGES)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneMaterialLayerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneMaterialLayerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.MaterialLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_MATERIAL_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOCIOViewSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOCIOViewSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OCIOView
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_VIEW)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOCIOLookSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOCIOLookSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OCIOLook
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_LOOK)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOCIOColorSpaceSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOCIOColorSpaceSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OCIOColorSpace
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OCIO_COLOR_SPACE)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOutputAOVGroupSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOutputAOVGroupSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OutputAOVGroup
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_GROUP)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOutputAOVSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOutputAOVSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OutputAOV
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneTextureLayerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneTextureLayerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.TextureLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_TEX_COMPOSITE_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneOutputAOVLayerSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneOutputAOVLayerSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.OutputAOVLayer
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_OUTPUT_AOV_LAYER)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctaneBlendingSettingsSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctaneBlendingSettingsSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.BlendingSettings
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_BLENDING_SETTINGS)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


class OctanePostVolumeSwitchInputSocket(OctaneSwitchInput):
    bl_idname = "OctanePostVolumeSwitchInputSocket"
    bl_label = "Input"
    octane_movable_input_count_attribute_name = "a_option_count"
    octane_input_pattern = r"Input (\d+)"
    octane_input_format_pattern = "Input {}"
    color = consts.OctanePinColor.PostVolume
    octane_default_node_type = consts.NodeType.NT_UNKNOWN
    octane_pin_type: IntProperty(name="Octane Pin Type", default=consts.PinType.PT_POST_VOLUME)
    octane_socket_type: IntProperty(name="Socket Type", default=consts.SocketType.ST_LINK)


_CLASSES = [
    OctaneBoolSwitchInputSocket,
    OctaneFloatSwitchInputSocket,
    OctaneIntSwitchInputSocket,
    OctaneTransformSwitchInputSocket,
    OctaneTextureSwitchInputSocket,
    OctaneEmissionSwitchInputSocket,
    OctaneMaterialSwitchInputSocket,
    OctaneCameraSwitchInputSocket,
    OctaneEnvironmentSwitchInputSocket,
    OctaneImagerSwitchInputSocket,
    OctaneKernelSwitchInputSocket,
    OctaneGeometrySwitchInputSocket,
    OctaneMediumSwitchInputSocket,
    OctanePhaseFunctionSwitchInputSocket,
    OctaneFilmSettingsSwitchInputSocket,
    OctaneEnumSwitchInputSocket,
    OctaneObjectLayerSwitchInputSocket,
    OctanePostProcessingSwitchInputSocket,
    OctaneRenderTargetSwitchInputSocket,
    OctaneProjectionSwitchInputSocket,
    OctaneDisplacementSwitchInputSocket,
    OctaneStringSwitchInputSocket,
    OctaneRenderAOVSwitchInputSocket,
    OctaneRenderLayerSwitchInputSocket,
    OctaneVolumeRampSwitchInputSocket,
    OctaneAnimationSettingsSwitchInputSocket,
    OctaneLUTSwitchInputSocket,
    OctaneRenderJobSwitchInputSocket,
    OctaneToonRampSwitchInputSocket,
    OctaneBitMaskSwitchInputSocket,
    OctaneRoundEdgesSwitchInputSocket,
    OctaneMaterialLayerSwitchInputSocket,
    OctaneOCIOViewSwitchInputSocket,
    OctaneOCIOLookSwitchInputSocket,
    OctaneOCIOColorSpaceSwitchInputSocket,
    OctaneOutputAOVGroupSwitchInputSocket,
    OctaneOutputAOVSwitchInputSocket,
    OctaneTextureLayerSwitchInputSocket,
    OctaneOutputAOVLayerSwitchInputSocket,
    OctaneBlendingSettingsSwitchInputSocket,
    OctanePostVolumeSwitchInputSocket,
]


_SOCKET_INTERFACE_CLASSES = []


def register():
    utility.octane_register_class(_CLASSES)
    utility.octane_register_interface_class(_CLASSES, _SOCKET_INTERFACE_CLASSES)


def unregister():
    utility.octane_unregister_interface_class(_SOCKET_INTERFACE_CLASSES)
    utility.octane_unregister_class(reversed(_CLASSES))


# END OCTANE GENERATED CODE BLOCK #
