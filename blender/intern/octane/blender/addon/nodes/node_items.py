# <pep8 compliant>

import bpy
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem
# noinspection PyUnresolvedReferences
from bl_ui import space_node
from octane import core
from octane.utils import consts, utility


def check_pin_type_compatible(octane_pin_type1, octane_pin_type2):
    if octane_pin_type1 == consts.PinType.PT_UNKNOWN:
        return True
    elif octane_pin_type2 == consts.PinType.PT_UNKNOWN:
        return True
    elif octane_pin_type1 == octane_pin_type2:
        return True
    else:
        return False


def render_aov_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.RENDER_AOV)


def composite_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.COMPOSITE)


def camera_imager_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.CAMERA_IMAGER)


def kernel_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.KERNEL)


def render_aov_and_composite_poll(context):
    return render_aov_poll(context) or composite_poll(context)


def shader_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.BLENDER_SHADER)


def texture_poll(context):
    return context.scene.render.engine == consts.ENGINE_NAME and \
        (not hasattr(context.space_data,
                     "tree_type") or context.space_data.tree_type == consts.OctaneNodeTreeIDName.BLENDER_TEXTURE)


def object_shader_poll(context):
    return shader_poll(context) and getattr(context.space_data, "shader_type", None) == "OBJECT"


def world_shader_poll(context):
    return shader_poll(context) and getattr(context.space_data, "shader_type", None) == "WORLD"


class OctaneNodeItem(NodeItem):
    def __init__(self, nodetype, label=None, settings=None, poll=None, octane_pin_type=consts.PinType.PT_UNKNOWN,
                 octane_multiple_pin_types=None):
        super().__init__(nodetype, label=label, settings=settings, poll=poll)
        self.octane_pin_type = octane_pin_type
        self.octane_multiple_pin_types = octane_multiple_pin_types

    def is_pin_type_compatible(self, octane_pin_type):
        result = check_pin_type_compatible(self.octane_pin_type, octane_pin_type)
        if self.octane_multiple_pin_types is not None:
            for pin_type in self.octane_multiple_pin_types:
                result |= check_pin_type_compatible(pin_type, octane_pin_type)
        return result

    @staticmethod
    def draw(self, layout, _context):
        if _context.region.type == "HEADER":
            return NodeItem.draw(self, layout, _context)
        else:
            op = layout.operator("octane.add_default_node_helper", text=self.label, text_ctxt=self.translation_context)
            op.use_transform = True
            op.default_node_name = self.nodetype


class OctaneNodeItemSeperator(object):
    def __init__(self, label, icon="INFO"):
        self.label = label
        self.icon = icon

    @classmethod
    def poll(cls, _context):
        return True

    @staticmethod
    def draw(self, layout, _context):
        layout.label(text=self.label, icon=self.icon)


class OctaneNodeCategory(NodeCategory):
    NODE_TREE_ID_LIST = []

    def __init__(self, identifier, name, description="", items=None, octane_pin_type=consts.PinType.PT_UNKNOWN,
                 octane_multiple_pin_types=None):
        super().__init__(identifier, name, description=description, items=items)
        self.octane_pin_type = octane_pin_type
        self.octane_multiple_pin_types = octane_multiple_pin_types

    def is_pin_type_compatible(self, octane_pin_type):
        result = check_pin_type_compatible(self.octane_pin_type, octane_pin_type)
        if self.octane_multiple_pin_types is not None:
            for pin_type in self.octane_multiple_pin_types:
                result |= check_pin_type_compatible(pin_type, octane_pin_type)
        return result

    @classmethod
    def poll(cls, context):
        if context.scene.render.engine != consts.ENGINE_NAME:
            return False
        if not hasattr(context.space_data, "tree_type") or len(cls.NODE_TREE_ID_LIST) == 0:
            return True
        return context.space_data.tree_type in cls.NODE_TREE_ID_LIST


class OctaneGeneralNodeCategory(OctaneNodeCategory):
    pass


class OctaneOutputNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, consts.OctaneNodeTreeIDName.BLENDER_TEXTURE,
                         consts.OctaneNodeTreeIDName.COMPOSITE, consts.OctaneNodeTreeIDName.RENDER_AOV,
                         consts.OctaneNodeTreeIDName.CAMERA_IMAGER, consts.OctaneNodeTreeIDName.KERNEL, ]


class OctaneTextureNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, consts.OctaneNodeTreeIDName.BLENDER_TEXTURE,
                         consts.OctaneNodeTreeIDName.RENDER_AOV, consts.OctaneNodeTreeIDName.COMPOSITE,
                         consts.OctaneNodeTreeIDName.CAMERA_IMAGER, consts.OctaneNodeTreeIDName.KERNEL, ]


class OctaneTextureLayerNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, consts.OctaneNodeTreeIDName.BLENDER_TEXTURE,
                         consts.OctaneNodeTreeIDName.RENDER_AOV, consts.OctaneNodeTreeIDName.CAMERA_IMAGER,
                         consts.OctaneNodeTreeIDName.KERNEL, ]


class OctaneShaderNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.BLENDER_SHADER, ]


class OctaneCompositeNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.COMPOSITE, ]


class OctaneRenderAovNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.RENDER_AOV, ]


class OctaneCameraImagerNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.CAMERA_IMAGER, ]


class OctaneKernelNodeCategory(OctaneNodeCategory):
    NODE_TREE_ID_LIST = [consts.OctaneNodeTreeIDName.KERNEL, ]


def register_octane_node_categories(identifier, cat_list):
    # noinspection PyProtectedMember
    _node_categories = nodeitems_utils._node_categories
    if identifier in _node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)

    # works as draw function for menus
    def draw_node_item(self, context):
        octane_pin_type = getattr(self, "octane_pin_type", consts.PinType.PT_UNKNOWN)
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            if hasattr(item, "octane_pin_type"):
                if not item.is_pin_type_compatible(octane_pin_type):
                    continue
            if isinstance(item, NodeCategory):
                layout.menu("NODE_MT_category_%s" % item.identifier)
            else:
                item.draw(item, col, context)

    def draw_add_menu(self, context, octane_pin_type=consts.PinType.PT_UNKNOWN):
        layout = self.layout
        for cur_cat in cat_list:
            if cur_cat.poll(context):
                if isinstance(cur_cat, OctaneNodeCategory):
                    if cur_cat.is_pin_type_compatible(octane_pin_type):
                        layout.menu("NODE_MT_category_%s" % cur_cat.identifier)
                else:
                    layout.menu("NODE_MT_category_%s" % cur_cat.identifier)

    def register_octane_node_category(cur_menu_types, cur_cat):
        menu_type = type("NODE_MT_category_" + cur_cat.identifier, (bpy.types.Menu,), {
            "bl_space_type": 'NODE_EDITOR',
            "bl_label": cur_cat.name,
            "category": cur_cat,
            "poll": cur_cat.poll,
            "draw": draw_node_item,
        })
        cur_menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)

    def register_submenu(cur_menu_types, cur_sub_cat_list, cur_cat, octane_pin_type):
        if isinstance(cur_cat, OctaneNodeItem):
            if getattr(cur_cat, "octane_pin_type", consts.PinType.PT_UNKNOWN) == consts.PinType.PT_UNKNOWN:
                cur_cat.octane_pin_type = octane_pin_type
            return
        if isinstance(cur_cat, OctaneNodeItemSeperator):
            return
        cur_sub_cat_list.append(cur_cat)
        register_octane_node_category(cur_menu_types, cur_cat)
        for item in cur_cat.items(None):
            register_submenu(cur_menu_types, cur_sub_cat_list, item, cur_cat.octane_pin_type)

    menu_types = []
    sub_cat_list = []
    for cat in cat_list:
        register_submenu(menu_types, sub_cat_list, cat, cat.octane_pin_type)

    # stores: (categories list, menu draw function, submenu types)
    final_cat_list = []
    for cat in (cat_list + sub_cat_list):
        if cat not in final_cat_list:
            final_cat_list.append(cat)
    _node_categories[identifier] = (final_cat_list, draw_add_menu, menu_types)


def unregister_node_cat_types(cats):
    for mt in cats[2]:
        bpy.utils.unregister_class(mt)


def unregister_octane_node_categories(identifier=None):
    # noinspection PyProtectedMember
    _node_categories = nodeitems_utils._node_categories
    # unregister existing UI classes
    if identifier:
        cat_types = _node_categories.get(identifier, None)
        if cat_types:
            unregister_node_cat_types(cat_types)
        del _node_categories[identifier]

    else:
        for cat_types in _node_categories.values():
            unregister_node_cat_types(cat_types)
        _node_categories.clear()


def draw_octane_node_categories_menu(self, context, octane_pin_type=consts.PinType.PT_UNKNOWN):
    # noinspection PyProtectedMember
    _node_categories = nodeitems_utils._node_categories
    for cats in _node_categories.values():
        is_octane_node_category = False
        for cat in cats[0]:
            if isinstance(cat, OctaneNodeCategory):
                is_octane_node_category = True
                break
        if is_octane_node_category:
            for menu in cats[2]:
                menu.octane_pin_type = octane_pin_type
            cats[1](self, context, octane_pin_type)
        else:
            # Do not show Blender's menu under quick adding mode(octane_pin_type is assigned)
            if octane_pin_type == consts.PinType.PT_UNKNOWN:
                cats[1](self, context)


def octane_NODE_MT_add_draw(self, context):
    if not utility.is_octane_engine(context):
        # noinspection PyCallingNonCallable
        _blender_NODE_MT_add_draw(self, context)
        return
    import nodeitems_utils
    layout = self.layout
    layout.operator_context = "INVOKE_REGION_WIN"
    snode = context.space_data
    if snode.tree_type in ("GeometryNodeTree", "CompositorNodeTree"):
        # noinspection PyCallingNonCallable
        _blender_NODE_MT_add_draw(self, context)
        return
    elif nodeitems_utils.has_node_categories(context):
        props = layout.operator("octane.node_add_search", text="Search...", icon='VIEWZOOM')
        props.octane_pin_type = 0
        props.use_transform = True
        layout.separator()
        # actual node submenus are defined by draw functions from node categories
        nodeitems_utils.draw_node_categories_menu(self, context)
        layout.separator()
        layout.menu("NODE_MT_category_shader_group")
        layout.menu("NODE_MT_category_layout")


# Octane Nodes

_octane_node_items = {
    "OCTANE_OUTPUT": [
        OctaneOutputNodeCategory(
            "OCTANE_OUTPUT", "Octane Output",
            octane_pin_type=consts.PinType.PT_BLENDER_OUTPUT,
            items=[
                OctaneNodeItem("ShaderNodeOutputMaterial", poll=object_shader_poll),
                OctaneNodeItem("OctaneEditorTextureOutputNode", poll=texture_poll),
                OctaneNodeItem("OctaneEditorWorldOutputNode", poll=world_shader_poll),
                OctaneNodeItem("OctaneOutputAOVGroupOutputNode", poll=composite_poll),
                OctaneNodeItem("OctaneRenderAOVOutputNode", poll=render_aov_poll),
                OctaneNodeItem("OctaneImagerOutputNode", poll=camera_imager_poll),
                OctaneNodeItem("OctaneKernelOutputNode", poll=kernel_poll),
            ]
        ),
    ],
    "OCTANE_TOOL": [
        OctaneGeneralNodeCategory(
            "OCTANE_TOOL", "Octane Advanced Tools",
            octane_pin_type=consts.PinType.PT_BLENDER_UTILITY,
            octane_multiple_pin_types=[
                consts.PinType.PT_GEOMETRY,
                consts.PinType.PT_TRANSFORM,
            ],
            items=[
                OctaneNodeItem("OctaneCameraData"),
                OctaneNodeItem("OctaneObjectData", octane_multiple_pin_types=[
                    consts.PinType.PT_GEOMETRY,
                    consts.PinType.PT_TRANSFORM,
                ]),
                OctaneNodeItem("OctaneScriptGraph"),
                OctaneNodeItem("OctaneProxy"),
            ]
        ),
    ],
    "OCTANE_RENDER_SETTINGS": [
        OctaneGeneralNodeCategory(
            "OCTANE_RENDER_SETTINGS", "Octane Render Settings",
            octane_pin_type=consts.PinType.PT_BLENDER_VALUES,
            items=[
                # OctaneNodeItem("OctaneImager", octane_pin_type=consts.PinType.PT_IMAGER),
                OctaneNodeItem("OctaneOCIOColorSpace",
                               octane_pin_type=consts.PinType.PT_OCIO_COLOR_SPACE),
            ]
        ),
    ],
    "OCTANE_VALUE": [
        OctaneGeneralNodeCategory(
            "OCTANE_VALUE", "Octane Values",
            octane_pin_type=consts.PinType.PT_BLENDER_VALUES,
            items=[
                OctaneNodeItem("OctaneBoolValue", octane_pin_type=consts.PinType.PT_BOOL),
                OctaneNodeItem("OctaneIntValue", octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneFloatValue", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneStringValue", octane_pin_type=consts.PinType.PT_STRING),
                OctaneNodeItem("OctaneLightIDBitValue",
                               octane_pin_type=consts.PinType.PT_BIT_MASK),
                OctaneNodeItem("OctaneSunDirection", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItemSeperator("Converters"),
                OctaneNodeItem("OctaneConverterFloatToInt",
                               octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneConverterIntToFloat",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItemSeperator("Operators"),
                OctaneNodeItem("OctaneOperatorBinaryMathOperation",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneOperatorBooleanLogicOperator",
                               octane_pin_type=consts.PinType.PT_BOOL),
                OctaneNodeItem("OctaneOperatorFloatRelationalOperator",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneOperatorIntRelationalOperator",
                               octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneOperatorRange", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneOperatorRotate", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneOperatorUnaryMathOperation",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneBoolSwitch", octane_pin_type=consts.PinType.PT_BOOL),
                OctaneNodeItem("OctaneFloatSwitch", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneIntSwitch", octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneStringSwitch", octane_pin_type=consts.PinType.PT_STRING),
                OctaneNodeItem("OctaneUtilityFloatComponentPicker",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneUtilityFloatIf", octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneUtilityFloatMerger",
                               octane_pin_type=consts.PinType.PT_FLOAT),
                OctaneNodeItem("OctaneUtilityIntComponentPicker",
                               octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneUtilityIntIf", octane_pin_type=consts.PinType.PT_INT),
                OctaneNodeItem("OctaneUtilityIntMerger", octane_pin_type=consts.PinType.PT_INT),
            ]
        ),
    ],
    "OCTANE_DISPLACEMENT": [
        OctaneShaderNodeCategory(
            "OCTANE_DISPLACEMENT", "Octane Displacement",
            octane_pin_type=consts.PinType.PT_DISPLACEMENT,
            items=[
                OctaneNodeItem("OctaneTextureDisplacement"),
                OctaneNodeItem("OctaneVertexDisplacement"),
                OctaneNodeItem("OctaneVertexDisplacementMixer"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneDisplacementSwitch"),
            ]
        ),
    ],
    "OCTANE_PROJECTION": [
        OctaneGeneralNodeCategory(
            "OCTANE_PROJECTION", "Octane Projection",
            octane_pin_type=consts.PinType.PT_PROJECTION,
            items=[
                OctaneNodeItem("OctaneBox"),
                OctaneNodeItem("OctaneColorToUVW"),
                OctaneNodeItem("OctaneCylindrical"),
                OctaneNodeItem("OctaneDistortedMeshUV"),
                OctaneNodeItem("OctaneInstancePosition"),
                OctaneNodeItem("OctaneMatCap"),
                OctaneNodeItem("OctaneMeshUVProjection"),
                OctaneNodeItem("OctaneOSLDelayedUV"),
                OctaneNodeItem("OctaneOSLProjection"),
                OctaneNodeItem("OctanePerspective"),
                OctaneNodeItem("OctaneSamplePosToUV"),
                OctaneNodeItem("OctaneSpherical"),
                OctaneNodeItem("OctaneTriplanar"),
                OctaneNodeItem("OctaneXYZToUVW"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneProjectionSwitch"),
            ]
        ),
    ],
    "OCTANE_TRANSFORM": [
        OctaneGeneralNodeCategory(
            "OCTANE_TRANSFORM", "Octane Transform",
            octane_pin_type=consts.PinType.PT_TRANSFORM,
            items=[
                OctaneNodeItem("Octane2DTransformation"),
                OctaneNodeItem("Octane3DTransformation"),
                OctaneNodeItem("OctaneConverterLookAtTransform"),
                OctaneNodeItem("OctaneRotation"),
                OctaneNodeItem("OctaneScale"),
                OctaneNodeItem("OctaneTransformValue"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneTransformSwitch"),
            ]
        ),
    ],
    "OCTANE_KERNEL": [
        OctaneKernelNodeCategory(
            "OCTANE_KERNEL", "Octane Kernel",
            octane_pin_type=consts.PinType.PT_KERNEL,
            items=[
                OctaneNodeItem("OctaneDirectLightingKernel"),
                OctaneNodeItem("OctaneInfoChannelsKernel"),
                OctaneNodeItem("OctanePMCKernel"),
                OctaneNodeItem("OctanePathTracingKernel"),
                OctaneNodeItem("OctanePhotonTracingKernel"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneKernelSwitch"),
            ]
        ),
    ],
    "OCTANE_COMPOSITE": [
        OctaneCompositeNodeCategory(
            "OCTANE_COMPOSITE", "Octane Compositor",
            items=[
                OctaneNodeItem("OctaneBlendingSettings",
                               octane_pin_type=consts.PinType.PT_BLENDING_SETTINGS),
                OctaneNodeItem("OctaneOutputAOVsOutputAOV",
                               octane_pin_type=consts.PinType.PT_OUTPUT_AOV),
                OctaneNodeItem("OctaneOutputAOVsOutputAOVGroup",
                               octane_pin_type=consts.PinType.PT_OUTPUT_AOV_GROUP),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_BLEND", "Blend",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsImageFile"),
                        OctaneNodeItem("OctaneOutputAOVsLayerGroup"),
                        OctaneNodeItem("OctaneOutputAOVsLightMixer"),
                        OctaneNodeItem("OctaneOutputAOVsRenderAOV"),
                        OctaneNodeItem("OctaneOutputAOVsSolidColor"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_CHECKPOINTS", "Checkpoints",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsDiscardCheckpoint"),
                        OctaneNodeItem("OctaneOutputAOVsLoadCheckpoint"),
                        OctaneNodeItem("OctaneOutputAOVsSaveCheckpoint"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_EFFECTS_COLOR", "Effects - color",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsAdjustBrightness"),
                        OctaneNodeItem("OctaneOutputAOVsAdjustContrastSDROnly"),
                        OctaneNodeItem("OctaneOutputAOVsAdjustHue"),
                        OctaneNodeItem("OctaneOutputAOVsAdjustSaturation"),
                        OctaneNodeItem("OctaneOutputAOVsAdjustWhiteBalance"),
                        OctaneNodeItem("OctaneOutputAOVsApplyCameraResponseCurveSDROnly"),
                        OctaneNodeItem("OctaneOutputAOVsApplyCustomCurve"),
                        OctaneNodeItem("OctaneOutputAOVsApplyGammaCurveSDROnly"),
                        OctaneNodeItem("OctaneOutputAOVsApplyLUT"),
                        OctaneNodeItem("OctaneOutputAOVsApplyOCIOLook"),
                        OctaneNodeItem("OctaneOutputAOVsChannelClamp"),
                        OctaneNodeItem("OctaneOutputAOVsChannelInvertSDROnly"),
                        OctaneNodeItem("OctaneOutputAOVsChannelMapRange"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_EFFECTS_DISPLAY",
                    "Effects - display",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsConvertForSDRDisplayACES"),
                        OctaneNodeItem("OctaneOutputAOVsConvertForSDRDisplayAgX"),
                        OctaneNodeItem("OctaneOutputAOVsConvertForSDRDisplayBasic"),
                        OctaneNodeItem("OctaneOutputAOVsConvertForSDRDisplayOCIO"),
                        OctaneNodeItem("OctaneOutputAOVsConvertForSDRDisplaySmooth"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_EFFECTS_OPACITY",
                    "Effects - opacity",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsAdjustOpacity"),
                        OctaneNodeItem("OctaneOutputAOVsMaskWithCryptomatte"),
                        OctaneNodeItem("OctaneOutputAOVsMaskWithLayerGroup"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_EFFECTS_PROCESSING",
                    "Effects - processing",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneOutputAOVsAddBloom"),
                        OctaneNodeItem("OctaneOutputAOVsAddChromaticAberration"),
                        OctaneNodeItem("OctaneOutputAOVsAddGlare"),
                        OctaneNodeItem("OctaneOutputAOVsAddLensFlare"),
                        OctaneNodeItem("OctaneOutputAOVsAddVignette"),
                        OctaneNodeItem("OctaneOutputAOVsBlur"),
                        OctaneNodeItem("OctaneOutputAOVsRemoveHotPixels"),
                        OctaneNodeItem("OctaneOutputAOVsSharpen"),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_LEGACY", "Legacy",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneLegacyOutputAOV",
                                       octane_pin_type=consts.PinType.PT_OUTPUT_AOV),
                    ]
                ),
                OctaneCompositeNodeCategory(
                    "OCTANE_COMPOSITE_UTILITY", "Utility",
                    octane_pin_type=consts.PinType.PT_OUTPUT_AOV_LAYER,
                    items=[
                        OctaneNodeItem("OctaneBlendingSettingsSwitch"),
                        OctaneNodeItem("OctaneOutputAOVGroupSwitch"),
                        OctaneNodeItem("OctaneOutputAOVLayerSwitch"),
                        OctaneNodeItem("OctaneOutputAOVSwitch"),
                        OctaneNodeItem("OctaneOutputAOVsLayerGroupPassThrough"),
                    ]
                ),
            ]
        ),
    ],
    "OCTANE_RENDER_AOV": [
        OctaneRenderAovNodeCategory(
            "OCTANE_RENDER_AOV", "Octane Render AOV",
            octane_pin_type=consts.PinType.PT_RENDER_PASSES,
            items=[
                OctaneNodeItem("OctaneRenderAOVGroup"),
                OctaneNodeItem("OctaneRenderAOVSwitch"),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_AUXILIARY", "Auxiliary",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneCryptomatteAOV"),
                        OctaneNodeItem("OctaneIrradianceAOV"),
                        OctaneNodeItem("OctaneLightDirectionAOV"),
                        OctaneNodeItem("OctaneNoiseAOV"),
                        OctaneNodeItem("OctanePostProcessingAOV"),
                        OctaneNodeItem("OctanePostfxMediaAOV"),
                        OctaneNodeItem("OctaneShadowAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_BEAUTY_SURFACES",
                    "Beauty - surfaces",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneDiffuseAOV"),
                        OctaneNodeItem("OctaneDiffuseDirectAOV"),
                        OctaneNodeItem("OctaneDiffuseFilterBeautyAOV"),
                        OctaneNodeItem("OctaneDiffuseIndirectAOV"),
                        OctaneNodeItem("OctaneEmittersAOV"),
                        OctaneNodeItem("OctaneEnvironmentAOV"),
                        OctaneNodeItem("OctaneReflectionAOV"),
                        OctaneNodeItem("OctaneReflectionDirectAOV"),
                        OctaneNodeItem("OctaneReflectionFilterBeautyAOV"),
                        OctaneNodeItem("OctaneReflectionIndirectAOV"),
                        OctaneNodeItem("OctaneRefractionAOV"),
                        OctaneNodeItem("OctaneRefractionFilterBeautyAOV"),
                        OctaneNodeItem("OctaneSubsurfaceScatteringAOV"),
                        OctaneNodeItem("OctaneTransmissionAOV"),
                        OctaneNodeItem("OctaneTransmissionFilterBeautyAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_BEAUTY_VOLUMES",
                    "Beauty - volumes",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneVolumeAOV"),
                        OctaneNodeItem("OctaneVolumeEmissionAOV"),
                        OctaneNodeItem("OctaneVolumeMaskAOV"),
                        OctaneNodeItem("OctaneVolumeZDepthBackAOV"),
                        OctaneNodeItem("OctaneVolumeZDepthFrontAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_CUSTOM", "Custom",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneCustomAOV"),
                        OctaneNodeItem("OctaneGlobalTextureAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_DENOISED", "Denoised",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneDenoisedDiffuseDirectAOV"),
                        OctaneNodeItem("OctaneDenoisedDiffuseIndirectAOV"),
                        OctaneNodeItem("OctaneDenoisedEmissionAOV"),
                        OctaneNodeItem("OctaneDenoisedReflectionDirectAOV"),
                        OctaneNodeItem("OctaneDenoisedReflectionIndirectAOV"),
                        OctaneNodeItem("OctaneDenoisedRemainderAOV"),
                        OctaneNodeItem("OctaneDenoisedVolumeAOV"),
                        OctaneNodeItem("OctaneDenoisedVolumeEmissionAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_INFO", "Info",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneAmbientOcclusionAOV"),
                        OctaneNodeItem("OctaneBakingGroupIDAOV"),
                        OctaneNodeItem("OctaneDiffuseFilterInfoAOV"),
                        OctaneNodeItem("OctaneIndexOfRefractionAOV"),
                        OctaneNodeItem("OctaneLightPassIDAOV"),
                        OctaneNodeItem("OctaneMaterialIDAOV"),
                        OctaneNodeItem("OctaneMotionVectorAOV"),
                        OctaneNodeItem("OctaneNormalGeometricAOV"),
                        OctaneNodeItem("OctaneNormalShadingAOV"),
                        OctaneNodeItem("OctaneNormalSmoothAOV"),
                        OctaneNodeItem("OctaneNormalTangentAOV"),
                        OctaneNodeItem("OctaneObjectIDAOV"),
                        OctaneNodeItem("OctaneObjectLayerColorAOV"),
                        OctaneNodeItem("OctaneOpacityAOV"),
                        OctaneNodeItem("OctanePositionAOV"),
                        OctaneNodeItem("OctaneReflectionFilterInfoAOV"),
                        OctaneNodeItem("OctaneRefractionFilterInfoAOV"),
                        OctaneNodeItem("OctaneRenderLayerIDAOV"),
                        OctaneNodeItem("OctaneRenderLayerMaskAOV"),
                        OctaneNodeItem("OctaneRoughnessAOV"),
                        OctaneNodeItem("OctaneTextureTangentAOV"),
                        OctaneNodeItem("OctaneTransmissionFilterInfoAOV"),
                        OctaneNodeItem("OctaneUVCoordinatesAOV"),
                        OctaneNodeItem("OctaneWireframeAOV"),
                        OctaneNodeItem("OctaneZDepthAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_LIGHT", "Light",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneLightAOV"),
                        OctaneNodeItem("OctaneLightDirectAOV"),
                        OctaneNodeItem("OctaneLightIndirectAOV"),
                    ]
                ),
                OctaneRenderAovNodeCategory(
                    "OCTANE_RENDER_AOV_RENDER_LAYER", "Render layer",
                    octane_pin_type=consts.PinType.PT_RENDER_PASSES,
                    items=[
                        OctaneNodeItem("OctaneBlackLayerShadowsAOV"),
                        OctaneNodeItem("OctaneLayerReflectionsAOV"),
                        OctaneNodeItem("OctaneLayerShadowsAOV"),
                    ]
                ),
            ]
        ),
    ],
    "OCTANE_SHADER": [
        OctaneShaderNodeCategory(
            "OCTANE_SHADER", "Octane Material",
            octane_pin_type=consts.PinType.PT_MATERIAL,
            items=[
                OctaneNodeItem("OctaneClippingMaterial"),
                OctaneNodeItem("OctaneCompositeMaterial"),
                OctaneNodeItem("OctaneDiffuseMaterial"),
                OctaneNodeItem("OctaneGlossyMaterial"),
                OctaneNodeItem("OctaneHairMaterial"),
                OctaneNodeItem("OctaneLayeredMaterial"),
                OctaneNodeItem("OctaneMetallicMaterial"),
                OctaneNodeItem("OctaneMixMaterial"),
                OctaneNodeItem("OctaneNullMaterial"),
                OctaneNodeItem("OctanePortalMaterial"),
                OctaneNodeItem("OctaneShadowCatcherMaterial"),
                OctaneNodeItem("OctaneSpecularMaterial"),
                OctaneNodeItem("OctaneStandardSurfaceMaterial"),
                OctaneNodeItem("OctaneToonMaterial"),
                OctaneNodeItem("OctaneToonRamp" if utility.use_new_addon_nodes() else "ShaderNodeOctToonRampTex",
                               octane_pin_type=consts.PinType.PT_TOON_RAMP),
                OctaneNodeItem("OctaneUniversalMaterial"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneMaterialSwitch"),
                OctaneNodeItem("OctaneToonRampSwitch"),
            ]
        ),
    ],
    "OCTANE_LAYER": [
        OctaneShaderNodeCategory(
            "OCTANE_MATERIAL_LAYER", "Octane Material Layer",
            octane_pin_type=consts.PinType.PT_MATERIAL_LAYER,
            items=[
                OctaneNodeItem("OctaneDiffuseLayer"),
                OctaneNodeItem("OctaneMaterialLayerGroup"),
                OctaneNodeItem("OctaneMetallicLayer"),
                OctaneNodeItem("OctaneSheenLayer"),
                OctaneNodeItem("OctaneSpecularLayer"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneMaterialLayerSwitch"),
            ]
        ),
    ],
    "OCTANE_MEDIUM": [
        OctaneShaderNodeCategory(
            "OCTANE_MEDIUM", "Octane Medium",
            octane_pin_type=consts.PinType.PT_MEDIUM,
            items=[
                OctaneNodeItem("OctaneAbsorption"),
                OctaneNodeItem("OctaneRandomWalk"),
                OctaneNodeItem("OctaneScattering"),
                OctaneNodeItem("OctaneSchlick", octane_pin_type=consts.PinType.PT_PHASEFUNCTION),
                OctaneNodeItem("OctaneStandardVolumeMedium"),
                OctaneNodeItem(
                    "OctaneVolumeGradient" if utility.use_new_addon_nodes() else "ShaderNodeOctVolumeRampTex",
                    octane_pin_type=consts.PinType.PT_VOLUME_RAMP),
                OctaneNodeItem("OctaneVolumeMedium"),
                OctaneNodeItemSeperator("Utility"),
                OctaneNodeItem("OctaneMediumSwitch"),
                OctaneNodeItem("OctanePhaseFunctionSwitch"),
                OctaneNodeItem("OctaneVolumeRampSwitch"),
            ]
        ),
    ],
    "OCTANE_EMISSION": [
        OctaneShaderNodeCategory(
            "OCTANE_EMISSION", "Octane Emission",
            octane_pin_type=consts.PinType.PT_EMISSION,
            items=[
                OctaneNodeItem("OctaneBlackBodyEmission"),
                OctaneNodeItem("OctaneTextureEmission"),
                OctaneNodeItem("OctaneEmissionSwitch"),
            ] if core.ENABLE_OCTANE_ADDON_CLIENT else [
                OctaneNodeItem("OctaneBlackBodyEmission"),
                OctaneNodeItem("OctaneTextureEmission"),
                OctaneNodeItem("OctaneEmissionSwitch"),
                OctaneNodeItem("ShaderNodeOctToonDirectionLight",
                               octane_pin_type=consts.PinType.PT_GEOMETRY),
                OctaneNodeItem("ShaderNodeOctToonPointLight",
                               octane_pin_type=consts.PinType.PT_GEOMETRY),
            ]
        ),
    ],
    "OCTANE_ENVIRONMENT": [
        OctaneShaderNodeCategory(
            "OCTANE_ENVIRONMENT", "Octane Environment",
            octane_pin_type=consts.PinType.PT_ENVIRONMENT,
            items=[
                OctaneNodeItem("OctaneDaylightEnvironment"),
                OctaneNodeItem("OctanePlanetaryEnvironment"),
                OctaneNodeItem("OctaneTextureEnvironment"),
                OctaneNodeItem("OctaneEnvironmentSwitch"),
            ]
        ),
    ],
    "OCTANE_CAMERA": [
        OctaneShaderNodeCategory(
            "OCTANE_CAMERA", "Octane Camera",
            octane_pin_type=consts.PinType.PT_CAMERA,
            items=[
                OctaneNodeItem("OctaneOSLCamera"),
                OctaneNodeItem("OctaneOSLBakingCamera"),
            ]
        ),
    ],
    "OCTANE_ROUND_EDGE": [
        OctaneShaderNodeCategory(
            "OCTANE_ROUND_EDGE", "Octane Round Edge",
            octane_pin_type=consts.PinType.PT_ROUND_EDGES,
            items=[
                OctaneNodeItem("OctaneRoundEdges"),
                OctaneNodeItem("OctaneRoundEdgesSwitch"),
            ]
        ),
    ],
    "OCTANE_GEOMETRY": [
        OctaneShaderNodeCategory(
            "OCTANE_GEOMETRY", "Octane Geometry",
            octane_pin_type=consts.PinType.PT_GEOMETRY,
            items=[
                OctaneNodeItem("OctaneVectron" if utility.use_new_addon_nodes() else "ShaderNodeOctVectron"),
                OctaneNodeItemSeperator("Scatter Tools"),
                OctaneNodeItem("OctaneScatterOnSurface"),
                OctaneNodeItem("OctaneScatterInVolume"),
                OctaneNodeItemSeperator("Vectron Operators"),
                OctaneNodeItem("OctaneSDFClip"),
                OctaneNodeItem("OctaneSDFDomainTransform"),
                OctaneNodeItem("OctaneSDFInk"),
                OctaneNodeItem("OctaneSDFInset"),
                OctaneNodeItem("OctaneSDFIntersect"),
                OctaneNodeItem("OctaneSDFOffset"),
                OctaneNodeItem("OctaneSDFSubtract"),
                OctaneNodeItem("OctaneSDFUnion"),
                OctaneNodeItemSeperator("Vectron Primitives"),
                OctaneNodeItem("OctaneSDFBox"),
                OctaneNodeItem("OctaneSDFCapsule"),
                OctaneNodeItem("OctaneSDFCylinder"),
                OctaneNodeItem("OctaneSDFPrism"),
                OctaneNodeItem("OctaneSDFSphere"),
                OctaneNodeItem("OctaneSDFTorus"),
                OctaneNodeItem("OctaneSDFTube"),
            ]
        ),
    ],
    "OCTANE_TEXTURE_LAYER": [
        OctaneTextureLayerNodeCategory(
            "OCTANE_TEXTURE_LAYER", "Octane Texture Layer",
            octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
            items=[
                OctaneTextureLayerNodeCategory("OCTANE_TEXTURE_LAYER_BLEND", "Blend",
                                               octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
                                               items=[
                                                   OctaneNodeItem("OctaneTexLayerLayerGroup"),
                                                   OctaneNodeItem("OctaneTexLayerTexture"),
                                               ]
                                               ),
                OctaneTextureLayerNodeCategory("OCTANE_TEXTURE_LAYER_EFFECTS_COLOR",
                                               "Effects - color",
                                               octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
                                               items=[
                                                   OctaneNodeItem("OctaneTexLayerAdjustBrightness"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustColorBalance"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustContrast"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustExposure"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustHue"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustLightness"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustSaturation"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustSaturationHSL"),
                                                   OctaneNodeItem("OctaneTexLayerAdjustWhiteBalance"),
                                                   OctaneNodeItem("OctaneTexLayerApplyGammaCurve"),
                                                   OctaneNodeItem("OctaneTexLayerApplyGradientMap"),
                                                   OctaneNodeItem("OctaneTexLayerConvertToGreyscale"),
                                               ]
                                               ),
                OctaneTextureLayerNodeCategory("OCTANE_TEXTURE_LAYER_EFFECTS_OPACITY",
                                               "Effects - opacity",
                                               octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
                                               items=[
                                                   OctaneNodeItem("OctaneTexLayerMaskWithLayerGroup"),
                                               ]
                                               ),
                OctaneTextureLayerNodeCategory("OCTANE_TEXTURE_LAYER_OPERATORS", "Operators",
                                               octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
                                               items=[
                                                   OctaneNodeItem("OctaneTexLayerChannelMixer"),
                                                   OctaneNodeItem("OctaneTexLayerClamp"),
                                                   OctaneNodeItem("OctaneTexLayerComparison"),
                                                   OctaneNodeItem("OctaneTexLayerMapRange"),
                                                   OctaneNodeItem("OctaneTexLayerMathBinary"),
                                                   OctaneNodeItem("OctaneTexLayerMathUnary"),
                                                   OctaneNodeItem("OctaneTexLayerThreshold"),
                                               ]
                                               ),
                OctaneTextureLayerNodeCategory("OCTANE_TEXTURE_LAYER_UTILITY", "Utility",
                                               octane_pin_type=consts.PinType.PT_TEX_COMPOSITE_LAYER,
                                               items=[
                                                   OctaneNodeItem("OctaneTextureLayerSwitch"),
                                               ]
                                               ),
            ]
        ),
    ],
    "OCTANE_TEXTURE": [
        OctaneTextureNodeCategory(
            "OCTANE_TEXTURE", "Octane Texture",
            octane_pin_type=consts.PinType.PT_TEXTURE,
            items=[
                OctaneNodeItem("OctaneGaussianSpectrum"),
                OctaneNodeItem("OctaneGreyscaleColor"),
                OctaneNodeItem("OctaneOSLTexture"),
                OctaneNodeItem("OctaneRGBColor"),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_CONVERTERS", "Converters",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneFloat3ToColor"),
                        OctaneNodeItem("OctaneFloatToGreyscale"),
                        OctaneNodeItem("OctaneFloatsToColor"),
                        OctaneNodeItem("OctaneVolumeToTexture"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_FIELDS", "Fields",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneAngularField"),
                        OctaneNodeItem("OctanePlanarField"),
                        OctaneNodeItem("OctaneShapeField"),
                        OctaneNodeItem("OctaneSphericalField"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_GEOMETRICS", "Geometric",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneColorVertexAttribute"),
                        OctaneNodeItem("OctaneCurvatureTexture"),
                        OctaneNodeItem("OctaneDirtTexture"),
                        OctaneNodeItem("OctaneFalloffMap"),
                        OctaneNodeItem("OctaneGreyscaleVertexAttribute"),
                        OctaneNodeItem("OctaneInstanceColor"),
                        OctaneNodeItem("OctaneInstanceHighlight"),
                        OctaneNodeItem("OctaneInstanceRange"),
                        OctaneNodeItem("OctaneNormal"),
                        OctaneNodeItem("OctaneObjectLayerColor"),
                        OctaneNodeItem("OctanePolygonSide"),
                        OctaneNodeItem("OctanePosition"),
                        OctaneNodeItem("OctaneRandomColorTexture"),
                        OctaneNodeItem("OctaneRayDirection"),
                        OctaneNodeItem("OctaneRelativeDistance"),
                        OctaneNodeItem("OctaneSamplePosition"),
                        OctaneNodeItem("OctaneSurfaceTangentDPdu"),
                        OctaneNodeItem("OctaneSurfaceTangentDPdv"),
                        OctaneNodeItem("OctaneUVCoordinate"),
                        OctaneNodeItem("OctaneWCoordinate"),
                        OctaneNodeItem("OctaneZDepth"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_IMAGE", "Image",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneAlphaImage"),
                        OctaneNodeItem("OctaneGreyscaleImage"),
                        OctaneNodeItem("OctaneImageTiles"),
                        OctaneNodeItem("OctaneRGBImage"),
                        OctaneNodeItem("OctaneBakingTexture"),
                    ] if utility.use_new_addon_nodes() else [
                        OctaneNodeItem("ShaderNodeOctAlphaImageTex"),
                        OctaneNodeItem("ShaderNodeOctFloatImageTex"),
                        OctaneNodeItem("ShaderNodeOctImageTileTex"),
                        OctaneNodeItem("ShaderNodeOctImageTex"),
                        OctaneNodeItem("ShaderNodeOctBakingTex"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_MAPPING", "Mapping",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneChaosTexture"),
                        OctaneNodeItem("OctaneTriplanarMap"),
                        OctaneNodeItem("OctaneUVWTransform"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_OPERATORS", "Operators",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneAddTexture"),
                        OctaneNodeItem("OctaneBinaryMathOperation"),
                        OctaneNodeItem("OctaneClampTexture"),
                        OctaneNodeItem("OctaneColorCorrection"),
                        OctaneNodeItem("OctaneColorKey"),
                        OctaneNodeItem("OctaneColorSpaceConversion"),
                        OctaneNodeItem("OctaneComparison"),
                        OctaneNodeItem("OctaneCosineMixTexture"),
                        OctaneNodeItem("OctaneGradientMap"
                                       if utility.use_new_addon_nodes()
                                       else "ShaderNodeOctGradientTex"),
                        OctaneNodeItem("OctaneImageAdjustment"),
                        OctaneNodeItem("OctaneInvertTexture"),
                        OctaneNodeItem("OctaneJitteredColorCorrection"),
                        OctaneNodeItem("OctaneMixTexture"),
                        OctaneNodeItem("OctaneMultiplyTexture"),
                        OctaneNodeItem("OctaneRandomMap"),
                        OctaneNodeItem("OctaneRange"),
                        OctaneNodeItem("OctaneSubtractTexture"),
                        OctaneNodeItem("OctaneUnaryMathOperation"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_PROCEDURAL", "Procedural",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneCellNoise"),
                        OctaneNodeItem("OctaneChainmail"),
                        OctaneNodeItem("OctaneChecksTexture"),
                        OctaneNodeItem("OctaneCinema4DNoise"),
                        OctaneNodeItem("OctaneCircleSpiral"),
                        OctaneNodeItem("OctaneColorSquares"),
                        OctaneNodeItem("OctaneDigits"),
                        OctaneNodeItem("OctaneFBMFlowNoise"),
                        OctaneNodeItem("OctaneFBMNoise"),
                        OctaneNodeItem("OctaneFanSpiral"),
                        OctaneNodeItem("OctaneFlakes"),
                        OctaneNodeItem("OctaneFractalFlowNoise"),
                        OctaneNodeItem("OctaneFractalNoise"),
                        OctaneNodeItem("OctaneGlowingCircle"),
                        OctaneNodeItem("OctaneGradientGenerator"),
                        OctaneNodeItem("OctaneHagelslag"),
                        OctaneNodeItem("OctaneIridescent"),
                        OctaneNodeItem("OctaneMandelbulb"),
                        OctaneNodeItem("OctaneMarbleTexture"),
                        OctaneNodeItem("OctaneMatrixEffect"),
                        OctaneNodeItem("OctaneMoireMosaic"),
                        OctaneNodeItem("OctaneNoiseTexture"),
                        OctaneNodeItem("OctanePixelFlow"),
                        OctaneNodeItem("OctaneProceduralEffects"),
                        OctaneNodeItem("OctaneRainBump"),
                        OctaneNodeItem("OctaneRidgedFractalTexture"),
                        OctaneNodeItem("OctaneRotFractal"),
                        OctaneNodeItem("OctaneSawWaveTexture"),
                        OctaneNodeItem("OctaneScratches"),
                        OctaneNodeItem("OctaneSineWaveFan"),
                        OctaneNodeItem("OctaneSineWaveTexture"),
                        OctaneNodeItem("OctaneSmoothVoronoiContours"),
                        OctaneNodeItem("OctaneSnowEffect"),
                        OctaneNodeItem("OctaneStarField"),
                        OctaneNodeItem("OctaneStripes"),
                        OctaneNodeItem("OctaneTilePatterns"),
                        OctaneNodeItem("OctaneTriangleWaveTexture"),
                        OctaneNodeItem("OctaneTripper"),
                        OctaneNodeItem("OctaneTurbulenceTexture"),
                        OctaneNodeItem("OctaneVolumeCloud"),
                        OctaneNodeItem("OctaneWavePattern"),
                        OctaneNodeItem("OctaneWoodgrain"),
                    ]
                ),
                OctaneTextureNodeCategory(
                    "OCTANE_TEXTURE_UTILITY", "Utility",
                    octane_pin_type=consts.PinType.PT_TEXTURE,
                    items=[
                        OctaneNodeItem("OctaneCaptureToCustomAOV"),
                        OctaneNodeItem("OctaneChannelInverter"),
                        OctaneNodeItem("OctaneChannelMapper"),
                        OctaneNodeItem("OctaneChannelMerger"),
                        OctaneNodeItem("OctaneChannelPicker"),
                        OctaneNodeItem("OctaneCompositeTexture"),

                        OctaneNodeItem("OctaneRaySwitch"),
                        OctaneNodeItem("OctaneSpotlight"),
                        OctaneNodeItem("OctaneTextureSwitch"),
                    ]
                ),
            ]
        ),
    ],
}

_draw_node_categories_menu = None
_octane_node_enum_items = None
_blender_NODE_MT_add_draw = None


def init_octane_node_enum_items():
    global _octane_node_enum_items
    if _octane_node_enum_items is not None:
        return
    # setup _octane_node_enum_items
    _octane_node_enum_items = {}
    data_headings = {}
    data_items = {}

    def add_octane_node_item(node_item, sub_type_name, octane_pin_type):
        if isinstance(node_item, OctaneNodeCategory):
            if octane_pin_type == consts.PinType.PT_UNKNOWN:
                octane_pin_type = node_item.octane_pin_type
            sub_type_name = getattr(node_item, "name", "")
            for cur_item in node_item.items(None):
                add_octane_node_item(cur_item, sub_type_name, octane_pin_type)
        elif isinstance(node_item, OctaneNodeItemSeperator):
            pass
        else:
            if node_item.octane_pin_type != consts.PinType.PT_UNKNOWN:
                octane_pin_type = node_item.octane_pin_type
            if octane_pin_type not in data_headings:
                data_headings[octane_pin_type] = []
            if octane_pin_type not in data_items:
                data_items[octane_pin_type] = {}
            if sub_type_name not in data_headings[octane_pin_type]:
                data_headings[octane_pin_type].append(sub_type_name)
            if sub_type_name not in data_items[octane_pin_type]:
                data_items[octane_pin_type][sub_type_name] = []
            data_items[octane_pin_type][sub_type_name].append((node_item.nodetype, node_item.label, ""))

    for _id, category in _octane_node_items.items():
        for _item in category:
            add_octane_node_item(_item, "", _item.octane_pin_type)
    for pin_type, categories in data_items.items():
        _octane_node_enum_items[pin_type] = []
        for heading in data_headings[pin_type]:
            if len(heading):
                _octane_node_enum_items[pin_type].append(("", heading, ""))
            for _item in categories[heading]:
                _octane_node_enum_items[pin_type].append(_item)
    for pin_type, enum_items in _octane_node_enum_items.items():
        _octane_node_enum_items[pin_type].extend(consts.LINK_UTILITY_MENU)


# noinspection PyUnresolvedReferences
def get_octane_node_enum_items(octane_pin_type):
    init_octane_node_enum_items()
    if octane_pin_type in _octane_node_enum_items:
        return _octane_node_enum_items[octane_pin_type]
    return []


def register():
    global _draw_node_categories_menu
    _draw_node_categories_menu = nodeitems_utils.draw_node_categories_menu
    nodeitems_utils.draw_node_categories_menu = draw_octane_node_categories_menu
    global _blender_NODE_MT_add_draw
    _blender_NODE_MT_add_draw = space_node.NODE_MT_add.draw
    space_node.NODE_MT_add.draw = octane_NODE_MT_add_draw
    for _id, _items in _octane_node_items.items():
        register_octane_node_categories(_id, _items)


def unregister():
    nodeitems_utils.draw_node_categories_menu = _draw_node_categories_menu
    space_node.NODE_MT_add.draw = _blender_NODE_MT_add_draw
    for _id, _items in _octane_node_items.items():
        unregister_octane_node_categories(_id)
