import bpy

SEPERATOR = "."
OBJECT_TAG = "[Object]"
OBJECT_DATA_TAG = "[ObjData]"
MESH_TAG = "[Mesh]"
INFINITE_PLANE_TAG = "[InfPlane]"
CURVE_TAG = "[Curve]"
CURVES_TAG = "[Curves]"
META_TAG = "[Meta]"
VOLUME_SDF_TAG = "[VolSDF]"
VOLUME_TAG = "[Volume]"
LIGHT_TAG = "[Light]"
COLLECTION_TAG = "[Collection]"
SCATTER_TAG = "[Scatter]"
OBJECTLAYER_TAG = "[ObjLayer]"
OBJECTLAYER_MAP_TAG = "[ObjLM]"
MATERIAL_MAP_TAG = "[MatMap]"

def resolve_octane_name(id_data, type_tag, modifier_tag=""):
    if getattr(id_data, "library", None) is not None:
        lib_tag = id_data.library.name + SEPERATOR
    else:
        lib_tag = ""
    if modifier_tag != "":
        modifier_tag = modifier_tag + SEPERATOR
    id_data_name = id_data.name
    return "{lib_tag}{modifier_tag}{id_data_name}{type_tag}".format(lib_tag=lib_tag, \
        modifier_tag=modifier_tag, id_data_name=id_data_name, type_tag=type_tag)

def resolve_object_octane_name(_object, scene, is_viewport):
    return resolve_octane_name(_object, OBJECT_TAG, "")

def resolve_object_data_octane_name(_object, scene, is_viewport):
    is_modified = _object.is_modified(scene, "PREVIEW" if is_viewport else "RENDER")
    modifier_tag = _object.name if is_modified else ""
    ob_data = _object.data
    object_data_name = ""
    type_tag = OBJECT_DATA_TAG
    if ob_data is not None:
        if _object.mode == "EDIT":
            object_data_name = resolve_octane_name(_object.original.data, "", modifier_tag)
        else:
            object_data_name = resolve_octane_name(ob_data, "", modifier_tag)
        if _object.type == "MESH":
            octane_property = getattr(_object.original.data, "octane", None)
            is_infinite_plane = getattr(octane_property, "infinite_plane", False)
            octane_geo_property = getattr(octane_property, "octane_geo_node_collections", None)
            is_octane_geo = octane_geo_property.is_octane_geo_used() if octane_geo_property is not None else False
            if is_infinite_plane:
                type_tag = INFINITE_PLANE_TAG
            elif is_octane_geo:
                object_data_name = octane_geo_property.get_octane_geo_name()
                type_tag = ""
            else:
                type_tag = MESH_TAG
        elif _object.type == "CURVE":
            type_tag = CURVE_TAG
        elif _object.type == "CURVES":
            type_tag = CURVES_TAG
        elif _object.type == "META":
            type_tag = META_TAG
        elif _object.type == "LIGHT":
            type_tag = LIGHT_TAG
        elif _object.type == "VOLUME":
            octane_property = getattr(_object.original.data, "octane", None)
            vdb_sdf = getattr(octane_property, "vdb_sdf", False)
            if vdb_sdf:
                type_tag = VOLUME_SDF_TAG
            else:
                type_tag = VOLUME_TAG
    return "{object_data_name}{type_tag}".format(object_data_name=object_data_name, type_tag=type_tag)

def resolve_scatter_octane_name(instance_object, scene, is_viewport):
    parent_tag = getattr(getattr(instance_object, "parent", None), "name", "")
    if parent_tag != "":
        parent_tag = "{parent_tag}.".format(parent_tag=parent_tag)
    _object = instance_object.object
    object_data_tag = getattr(_object.data, "name", "")
    original_object_data_tag = getattr(_object.original.data, "name", "")
    if not instance_object.is_instance:
        object_data_tag = original_object_data_tag
    if object_data_tag != "":
        object_data_tag = ".{object_data_tag}.".format(object_data_tag=object_data_tag)
    object_name = resolve_octane_name(_object, "", "")
    return "{parent_tag}{object_name}{object_data_tag}{type_tag}".format(parent_tag=parent_tag, object_name=object_name, object_data_tag=object_data_tag, type_tag=SCATTER_TAG)

def resolve_objectlayer_octane_name(scatter_name):
    return "{scatter_name}{type_tag}".format(scatter_name=scatter_name, type_tag=OBJECTLAYER_TAG)

def resolve_objectlayer_map_octane_name(scatter_name):
    return "{scatter_name}{type_tag}".format(scatter_name=scatter_name, type_tag=OBJECTLAYER_MAP_TAG)

def resolve_material_map_octane_name(scatter_name):
    return "{scatter_name}{type_tag}".format(scatter_name=scatter_name, type_tag=MATERIAL_MAP_TAG)