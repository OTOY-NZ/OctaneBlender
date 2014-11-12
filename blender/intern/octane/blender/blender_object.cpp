/*
 * Copyright 2011, Blender Foundation.
 *
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

#include "object.h"
#include "camera.h"
#include "light.h"
#include "mesh.h"
#include "scene.h"

#include "blender_sync.h"
#include "blender_util.h"

#include "util_hash.h"
#include "util_types.h"
#include "util_progress.h"

#ifdef WIN32
#   include "BLI_winstuff.h"
#endif

OCT_NAMESPACE_BEGIN

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test if modificators are applied to object for certain mode (Render or Realtime, depends on "preview" member flag)
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::BKE_object_is_modified(BL::Object b_ob) {
	// Test if we can instance or if the object is modified
	if(oct::BKE_object_is_modified(b_ob, b_scene, interactive))
		return true;
	else {
		// Object level material links
		BL::Object::material_slots_iterator slot;
		for(b_ob.material_slots.begin(slot); slot != b_ob.material_slots.end(); ++slot)
			if(slot->link() == BL::MaterialSlot::link_OBJECT)
				return true;
	}
	return false;
} //BKE_object_is_modified()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test if the Blender Object is Mesh
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::object_is_mesh(BL::Object b_ob) {
	BL::ID b_ob_data = b_ob.data();

	return (b_ob_data && (b_ob_data.is_a(&RNA_Mesh)
            || b_ob_data.is_a(&RNA_Curve)
            || b_ob_data.is_a(&RNA_MetaBall)));
} //object_is_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test if the Blender Object is Light
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool BlenderSync::object_is_light(BL::Object b_ob) {
	BL::ID b_ob_data = b_ob.data();
	return (b_ob_data && b_ob_data.is_a(&RNA_Lamp));
} //object_is_light()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Test object's Octane visibility
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool object_ray_visibility(BL::Object b_ob) {
	PointerRNA oct_properties = RNA_pointer_get(&b_ob.ptr, "octane_properties");
	return get_boolean(oct_properties, "visibility");
} //object_ray_visibility()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_light_object(BL::Object b_parent, int persistent_id[OBJECT_PERSISTENT_ID_SIZE], BL::Object b_ob, Transform& tfm, BL::DupliObject b_dupli_ob, uint layer_flag) {
	// Key to lookup object
	ObjectKey   key(b_parent, persistent_id, b_ob);
	Object      *light_object;

	// Test if we need to sync
	bool object_updated;
	if(light_object_map.sync(&light_object, b_ob, b_parent, key, this, tfm)) object_updated = true;
    else object_updated = false;

	bool use_holdout = (layer_flag & render_layer.holdout_layer) != 0;
	
	// Light sync
	light_object->light = sync_light(b_ob, tfm, object_updated);

	// Special case not tracked by object update flags
	if(use_holdout != light_object->use_holdout) {
		light_object->use_holdout = use_holdout;
		scene->light_manager->tag_update(scene);
		object_updated = true;
	}

    // Object sync
	// Transform comparison should not be needed, but duplis don't work perfect
	// in the depsgraph and may not signal changes, so this is a workaround
	if(object_updated || (light_object->light && light_object->light->need_update) || tfm != light_object->tfm) {
        if(!light_object->name.length()) {
		    light_object->name = b_ob.name().c_str();
        }
		light_object->pass_id   = b_ob.pass_index();
		light_object->tfm       = tfm;

		// Random number
		light_object->random_id = hash_string(light_object->name.c_str());

		if(persistent_id) {
			for(int i = 0; i < OBJECT_PERSISTENT_ID_SIZE; i++)
				light_object->random_id = hash_int_2d(light_object->random_id, persistent_id[i]);
		}
		else light_object->random_id = hash_int_2d(light_object->random_id, 0);

		// Visibility flags for both parent
		light_object->visibility = object_ray_visibility(b_ob);
		if(b_parent.ptr.data != b_ob.ptr.data) {
            if(!object_ray_visibility(b_parent) && light_object->visibility) light_object->visibility = false;
			light_object->random_id ^= hash_int(hash_string(b_parent.name().c_str()));
		}

		// Make holdout objects on excluded layer invisible for non-camera rays
		if(use_holdout && (layer_flag & render_layer.exclude_layer)) light_object->visibility = false;

		if (b_dupli_ob) {
			light_object->dupli_generated   = get_float3(b_dupli_ob.orco());
			light_object->dupli_uv          = get_float2(b_dupli_ob.uv());
		}
		else {
			light_object->dupli_generated   = make_float3(0.0f, 0.0f, 0.0f);
			light_object->dupli_uv          = make_float2(0.0f, 0.0f);
		}

		light_object->tag_update(scene);
	} //if(object_updated || (light_object->light && light_object->light->need_update) || tfm != light_object->tfm)
	return;
} //sync_light_object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Syncronise Light
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Light* BlenderSync::sync_light(BL::Object b_ob, Transform& tfm, bool object_updated) {
	Light *light;
	//ObjectKey key(b_parent, persistent_id, b_ob);
	BL::ID b_ob_data = b_ob.data();
	BL::ID key = b_ob_data;

	if(!light_map.sync(&light, key) && !object_updated) return light;

	// Ensure we only sync instanced meshes once
	if(lights_synced.find(light) != lights_synced.end()) return light;
	lights_synced.insert(light);

    if(!light->mesh) light->mesh = new Mesh;
	
	BL::Lamp b_lamp(b_ob.data());
    light->nice_name = b_ob_data.name().c_str();
    if(BKE_object_is_modified(b_ob)) {
        char szName[128];
        snprintf(szName, 128, "%s.%s", b_ob.name().c_str(), b_ob_data.name().c_str());
        light->name = szName;
    }
    else
        light->name = b_ob_data.name().c_str();

	PointerRNA oct_lamp     = RNA_pointer_get(&b_lamp.ptr, "octane");
	light->enable           = get_boolean(oct_lamp, "enable");
    light->mesh->mesh_type  = static_cast<Mesh::MeshType>(RNA_enum_get(&oct_lamp, "mesh_type"));

    // Type
	switch(b_lamp.type()) {
		case BL::Lamp::type_POINT: {
			BL::PointLamp b_point_lamp(b_lamp);
			light->size = b_point_lamp.shadow_soft_size();
            light->type = Light::LIGHT_POINT;
            if(light->enable) light->enable = false;
			break;
		}
		case BL::Lamp::type_SPOT: {
			BL::SpotLamp b_spot_lamp(b_lamp);
			light->size         = b_spot_lamp.shadow_soft_size();
			light->type         = Light::LIGHT_SPOT;
			light->spot_angle   = b_spot_lamp.spot_size();
			light->spot_smooth  = b_spot_lamp.spot_blend();
            if(light->enable) light->enable = false;
			break;
		}
		case BL::Lamp::type_HEMI: {
			light->type = Light::LIGHT_DISTANT;
			light->size = 0.0f;
            if(light->enable) light->enable = false;
			break;
		}
		case BL::Lamp::type_SUN: {
			BL::SunLamp b_sun_lamp(b_lamp);
			light->size = b_sun_lamp.shadow_soft_size();
			light->type = Light::LIGHT_DISTANT;
            if(light->enable) light->enable = false;
			break;
		}
		case BL::Lamp::type_AREA: {
			BL::AreaLamp b_area_lamp(b_lamp);
			light->size = 1.0f;
			light->sizeu = b_area_lamp.size();
			if(b_area_lamp.shape() == BL::AreaLamp::shape_RECTANGLE)
				light->sizev = b_area_lamp.size_y();
			else
				light->sizev = light->sizeu;
			light->type = Light::LIGHT_AREA;

            // Light mesh
            light->mesh->clear();

            float3 cur_normal = make_float3(0, 0, -1.0f);

            light->mesh->points.push_back(make_float3(light->sizeu/2, -light->sizev/2, 0));
            light->mesh->normals.push_back(cur_normal);

            light->mesh->points.push_back(make_float3(-light->sizeu/2, -light->sizev/2, 0));
            light->mesh->normals.push_back(cur_normal);

            light->mesh->points.push_back(make_float3(-light->sizeu/2, light->sizev/2, 0));
            light->mesh->normals.push_back(cur_normal);

            light->mesh->points.push_back(make_float3(light->sizeu/2, light->sizev/2, 0));
            light->mesh->normals.push_back(cur_normal);

            light->mesh->uvs.push_back(make_float3(0, 0, 0));

            light->mesh->points_indices.push_back(0);
            light->mesh->points_indices.push_back(1);
            light->mesh->points_indices.push_back(2);
            light->mesh->points_indices.push_back(3);

            light->mesh->uv_indices.push_back(0);
            light->mesh->uv_indices.push_back(0);
            light->mesh->uv_indices.push_back(0);
            light->mesh->uv_indices.push_back(0);

            light->mesh->vert_per_poly.push_back(4);
            light->mesh->poly_mat_index.push_back(0);
			break;
		} //case BL::Lamp::type_AREA
	} //switch(b_lamp.type())

	// Shader
	//vector<uint> used_shaders;
	//add_used_shader_index(b_lamp, used_shaders, scene->default_light);
	//if(used_shaders.size() == 0) used_shaders.push_back(scene->default_light);
	//light->shader = used_shaders[0];

	light->tag_update(scene);
    return light;
} //sync_light()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Syncronise the Mesh Object
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Object *BlenderSync::sync_object(BL::Object b_parent, int persistent_id[OBJECT_PERSISTENT_ID_SIZE], BL::DupliObject b_dupli_ob, Transform& tfm, uint layer_flag, int motion, bool hide_tris) {
	BL::Object b_ob = (b_dupli_ob ? b_dupli_ob.object() : b_parent);
	
	// Light is handled separately
	if(object_is_light(b_ob)) {
		if(!motion) sync_light_object(b_parent, persistent_id, b_ob, tfm, b_dupli_ob, layer_flag);
		return NULL;
	}

	// Only interested in object that we can create meshes from
	if(!object_is_mesh(b_ob)) return NULL;

	// Key to lookup object
	ObjectKey   key(b_parent, persistent_id, b_ob);
	Object      *object;

	// Find shader indices
	BL::Material material_override = render_layer.material_override;
	vector<uint> used_shaders;
	BL::Object::material_slots_iterator slot;
	for(b_ob.material_slots.begin(slot); slot != b_ob.material_slots.end(); ++slot) {
		if(material_override)
			add_used_shader_index(material_override, used_shaders, scene->default_surface);
		else
			add_used_shader_index(slot->material(), used_shaders, scene->default_surface);
	}
	if(used_shaders.size() == 0) {
		if(material_override)
			add_used_shader_index(material_override, used_shaders, scene->default_surface);
		else
			used_shaders.push_back(scene->default_surface);
	}

	// Test if we need to sync
	bool object_updated;
	if(object_map.sync(&object, b_ob, b_parent, key, this, used_shaders, hide_tris)) object_updated = true;
    else object_updated = false;
	
	bool use_holdout = (layer_flag & render_layer.holdout_layer) != 0;
	
	// Special case not tracked by object update flags
	if(use_holdout != object->use_holdout) {
		object->use_holdout = use_holdout;
		scene->object_manager->tag_update(scene);
		object_updated = true;
	}

	// Object sync
	// Transform comparison should not be needed, but duplis don't work perfect
	// in the depsgraph and may not signal changes, so this is a workaround
	if(object_updated || (object->mesh && object->mesh->need_update) || object->used_shaders != used_shaders || tfm != object->tfm) {
        if(!object->name.length()) {
		    object->name = b_ob.name().c_str();
        }
		object->pass_id = b_ob.pass_index();
		object->tfm = tfm;
    	object->used_shaders.swap(used_shaders);

		// Random number
		object->random_id = hash_string(object->name.c_str());

		if(persistent_id) {
			for(int i = 0; i < OBJECT_PERSISTENT_ID_SIZE; i++)
				object->random_id = hash_int_2d(object->random_id, persistent_id[i]);
		}
		else
			object->random_id = hash_int_2d(object->random_id, 0);

		// Visibility flags for both parent
		object->visibility = object_ray_visibility(b_ob);
		if(b_parent.ptr.data != b_ob.ptr.data) {
            if(!object_ray_visibility(b_parent) && object->visibility)
			    object->visibility = false;
			object->random_id ^= hash_int(hash_string(b_parent.name().c_str()));
		}

		// Make holdout objects on excluded layer invisible for non-camera rays
		if(use_holdout && (layer_flag & render_layer.exclude_layer))
			object->visibility = false;

		if (b_dupli_ob) {
			object->dupli_generated = get_float3(b_dupli_ob.orco());
			object->dupli_uv = get_float2(b_dupli_ob.uv());
		}
		else {
			object->dupli_generated = make_float3(0.0f, 0.0f, 0.0f);
			object->dupli_uv = make_float2(0.0f, 0.0f);
		}

		object->tag_update(scene);
	}
	return object;
} //sync_object()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool object_render_hide_original(BL::Object::dupli_type_enum dupli_type) {
	return (dupli_type == BL::Object::dupli_type_VERTS ||
	        dupli_type == BL::Object::dupli_type_FACES ||
	        dupli_type == BL::Object::dupli_type_FRAMES);
} //object_render_hide_original()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool object_render_hide(BL::Object b_ob, bool top_level, bool parent_hide, bool& hide_triangles) {
	// Check if we should render or hide particle emitter
	BL::Object::particle_systems_iterator b_psys;

	bool hair_present = false;
	bool show_emitter = false;
	bool hide = false;

	for(b_ob.particle_systems.begin(b_psys); b_psys != b_ob.particle_systems.end(); ++b_psys) {
		if((b_psys->settings().render_type() == BL::ParticleSettings::render_type_PATH) &&
		   (b_psys->settings().type() == BL::ParticleSettings::type_HAIR))
			hair_present = true;

		if(b_psys->settings().use_render_emitter()) {
			hide = false;
			show_emitter = true;
		}
	}

	// Duplicators hidden by default, except dupliframes which duplicate self
	if(b_ob.is_duplicator())
		if(top_level || b_ob.dupli_type() != BL::Object::dupli_type_FRAMES)
			hide = true;

	// Hide original object for duplis
	BL::Object parent = b_ob.parent();
	if(parent && object_render_hide_original(parent.dupli_type()))
		if(parent_hide)
			hide = true;

	hide_triangles = (hair_present && !show_emitter);
	return hide && !show_emitter;
} //object_render_hide()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool object_render_hide_duplis(BL::Object b_ob) {
	BL::Object parent = b_ob.parent();
	return (parent && object_render_hide_original(parent.dupli_type()));
}

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Object Loop
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void BlenderSync::sync_objects(BL::SpaceView3D b_v3d, int motion) {
	// Layer data
	uint scene_layer = render_layer.scene_layer;
	
	if(!motion) {
		// Prepare for sync
		light_map.pre_sync();
		mesh_map.pre_sync();
		object_map.pre_sync();
		light_object_map.pre_sync();
		mesh_synced.clear();
		lights_synced.clear();
	}

	// Object loop
	BL::Scene::objects_iterator b_ob;
	BL::Scene b_sce = b_scene;

	// Global particle index counter
	int particle_id = 1;

	bool cancel = false;
	for(; b_sce && !cancel; b_sce = b_sce.background_set()) {
		for(b_sce.objects.begin(b_ob); b_ob != b_sce.objects.end() && !cancel; ++b_ob) {
			bool hide       = (render_layer.use_viewport_visibility) ? b_ob->hide() : b_ob->hide_render();
			uint ob_layer   = get_layer(b_ob->layers(), b_ob->layers_local_view(), render_layer.use_localview, object_is_light(*b_ob));
			hide            = hide || !(ob_layer & scene_layer);

			if(!hide) {
				progress.set_sync_status("Synchronizing object", (*b_ob).name());

                if(b_ob->is_duplicator() && !object_render_hide_duplis(*b_ob)) {
					// Dupli objects
					b_ob->dupli_list_create(b_scene, 2);

					BL::Object::dupli_list_iterator b_dup;
					for(b_ob->dupli_list.begin(b_dup); b_dup != b_ob->dupli_list.end(); ++b_dup) {
						Transform   tfm             = scene->matrix * get_transform(b_dup->matrix());
						BL::Object  b_dup_ob        = b_dup->object();
                        bool        dup_hide        = (b_v3d) ? b_dup_ob.hide() : (scene->use_viewport_hide ? b_dup_ob.hide() : b_dup_ob.hide_render());
						bool        in_dupli_group  = (b_dup->type() == BL::DupliObject::type_GROUP);
						bool        hide_tris;

						if(!(b_dup->hide() || dup_hide || object_render_hide(b_dup_ob, false, in_dupli_group, hide_tris))) {
							// The persistent_id allows us to match dupli objects between frames and updates
							BL::Array<int, OBJECT_PERSISTENT_ID_SIZE> persistent_id = b_dup->persistent_id();

							// Sync object and mesh or light data
							Object *object = sync_object(*b_ob, persistent_id.data, *b_dup, tfm, ob_layer, motion, hide_tris);

							// Sync possible particle data, note particle_id starts counting at 1, first is dummy particle
                            if(!motion && object) {
								if(particle_id != object->particle_id) {
									object->particle_id = particle_id;
									scene->object_manager->tag_update(scene);
								}
								particle_id++;
							}
						} //if(!(b_dup->hide() || dup_hide || object_render_hide(b_dup_ob, false, in_dupli_group, hide_tris)))
					} //for(b_ob->dupli_list.begin(b_dup); b_dup != b_ob->dupli_list.end(); ++b_dup)
					b_ob->dupli_list_clear();
				} //if(b_ob->is_duplicator() && !object_render_hide_duplis(*b_ob))

				// Test if object needs to be hidden
				bool hide_tris;
				if(!object_render_hide(*b_ob, true, true, hide_tris)) {
                    std::string sTmp = (*b_ob).name();
					// Object itself
                    Transform tfm;
			        tfm = scene->matrix * get_transform(b_ob->matrix_world());
					sync_object(*b_ob, NULL, PointerRNA_NULL, tfm, ob_layer, motion, hide_tris);
				}
			}
			cancel = progress.get_cancel();
		} //for(b_sce.objects.begin(b_ob); b_ob != b_sce.objects.end() && !cancel; ++b_ob)
	} //for(; b_sce && !cancel; b_sce = b_sce.background_set())

	progress.set_sync_status("");

	if(!cancel && !motion) {
		// Handle removed data and modified pointers
		if(light_map.post_sync())
			scene->light_manager->tag_update(scene);
		if(object_map.post_sync())
			scene->object_manager->tag_update(scene);
		if(light_object_map.post_sync())
			scene->object_manager->tag_update(scene);
		if(mesh_map.post_sync())
			scene->mesh_manager->tag_update(scene);
		mesh_synced.clear();
		lights_synced.clear();
	}
} //sync_objects()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool objects_map::sync(Object **r_data, BL::Object b_ob, BL::ID parent, const ObjectKey& key, BlenderSync* sync, vector<uint> &used_shaders, bool hide_tris) {
    BL::ID  id      = b_ob;
	Object  *data   = find(key);
	bool    recalc;

	if(!data) {
		// Add data if it didn't exist yet
		data = new Object(scene);
    	data->mesh = sync->sync_mesh(b_ob, used_shaders, true, hide_tris);

        (*scene_data)[data->mesh->name].push_back(data);
		b_map[key] = data;
		recalc = true;
	}
	else {
		recalc = (b_recalc.find(id.ptr.data) != b_recalc.end());
		if(parent.ptr.data)
			recalc = recalc || (b_recalc.find(parent.ptr.data) != b_recalc.end());

    	Mesh *mesh = sync->sync_mesh(b_ob, used_shaders, recalc, hide_tris);
        if(mesh != data->mesh) {
            vector<Object*> &objects = (*scene_data)[data->mesh->name];
            if(!objects.size()) (*scene_data).erase(data->mesh->name);
            //FIXME: Rework this to normal fast search
            for(vector<Object*>::iterator it = objects.begin(); it != objects.end(); ++it) {
                if(*it == data) {
                    if(objects.size() == 1) (*scene_data).erase(data->mesh->name);
                    else objects.erase(it);
                    break;
                }
            }
            (*scene_data)[mesh->name].push_back(data);
            data->mesh = mesh;
        }
    }
	used(data);
	*r_data = data;

    return recalc;
} //objects_map::sync()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
bool lights_map::sync(Object **r_data, BL::Object b_ob, BL::ID parent, const ObjectKey& key, BlenderSync* sync, Transform& tfm) {
    BL::ID  id      = b_ob;
	Object  *data   = find(key);
	bool    recalc;

	if(!data) {
		// Add data if it didn't exist yet
		data = new Object(scene);
    	data->light = sync->sync_light(b_ob, tfm, true);

        (*scene_data)[data->light->name].push_back(data);
		b_map[key] = data;
		recalc = true;
	}
	else {
		recalc = (b_recalc.find(id.ptr.data) != b_recalc.end());
		if(parent.ptr.data)
			recalc = recalc || (b_recalc.find(parent.ptr.data) != b_recalc.end());

    	data->light = sync->sync_light(b_ob, tfm, recalc);
    }
	used(data);
	*r_data = data;

    return recalc;
} //lights_map::sync()

OCT_NAMESPACE_END

