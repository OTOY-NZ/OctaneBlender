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

#ifndef __BLENDER_SYNC_H__
#define __BLENDER_SYNC_H__

#include "blender_util.h"
#include "blender_session.h"

#include "render/object.h"

OCT_NAMESPACE_BEGIN

class Camera;
class Light;
class Mesh;
class Scene;
class Shader;
class BlenderSync;
class BufferParams;
class SessionParams;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class objects_map {
public:
    objects_map(Scene* scene_, map<Mesh*, vector<Object*> > *scene_data_) : scene(scene_), scene_data(scene_data_) {}

	Object *find(const ObjectKey& key) {
        map<ObjectKey, Object*>::const_iterator it = b_map.find(key);
		if(it != b_map.end()) return it->second;
		else return NULL;
	}
	void set_recalc(BL::ID id) {
		b_recalc.insert(id.ptr.data);
	}
	bool has_recalc() {
		return !(b_recalc.empty());
	}
	void pre_sync() {
		used_set.clear();
	}
	bool sync(Object **r_data, BL::Object b_ob, BL::ID parent, const ObjectKey& key, BlenderSync* sync, vector<uint> &used_shaders, bool hide_tris);
    bool is_used(const ObjectKey& key) {
        Object *data = find(key);
        return (data) ? used_set.find(data) != used_set.end() : false;
    }
	void used(Object *data) {
		// Tag data as still in use
		used_set.insert(data);
	}
	bool post_sync(bool do_delete = true) {
		// Remove unused data
		map<Mesh*, vector<Object*> > new_scene_data;
		map<Mesh*, vector<Object*> >::iterator it;
		vector<Object*>::iterator ob_it;
		bool deleted = false;

		for(it = scene_data->begin(); it != scene_data->end(); it++) {
    		for(ob_it = it->second.begin(); ob_it != it->second.end(); ob_it++) {
			    Object *data = *ob_it;

			    if(do_delete && used_set.find(data) == used_set.end()) {
				    delete data;
				    deleted = true;
			    }
			    else new_scene_data[it->first].push_back(data);
            }
		}

		*scene_data = new_scene_data;

		// Update mapping
		map<ObjectKey, Object*> new_map;
		typedef pair<const ObjectKey, Object*> TMapPair;
		map<ObjectKey, Object*>::iterator jt;

		for(jt = b_map.begin(); jt != b_map.end(); jt++) {
			TMapPair& pair = *jt;

			if(used_set.find(pair.second) != used_set.end())
				new_map[pair.first] = pair.second;
		}

		used_set.clear();
		b_recalc.clear();
		b_map = new_map;

		return deleted;
	} //post_sync()

protected:
	map<Mesh*, vector<Object*> > *scene_data;
	map<ObjectKey, Object*>     b_map;
	set<Object*>                used_set;
	set<void*>                  b_recalc;
    Scene                       *scene;
}; //objects_map

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class lights_map {
public:
    lights_map(Scene* scene_, map<Light*, vector<Object*> > *scene_data_) : scene(scene_), scene_data(scene_data_) {}

	Object *find(const ObjectKey& key) {
        map<ObjectKey, Object*>::const_iterator it = b_map.find(key);
		if(it != b_map.end()) return it->second;
		else return NULL;
	}
	void set_recalc(BL::ID id) {
		b_recalc.insert(id.ptr.data);
	}
	bool has_recalc() {
		return !(b_recalc.empty());
	}
	void pre_sync() {
		used_set.clear();
	}
	bool sync(Object **r_data, BL::Object b_ob, BL::ID parent, const ObjectKey& key, BlenderSync* sync, Transform& tfm);
    bool is_used(const ObjectKey& key) {
        Object *data = find(key);
        return (data) ? used_set.find(data) != used_set.end() : false;
    }
	void used(Object *data) {
		// Tag data as still in use
		used_set.insert(data);
	}
	bool post_sync(bool do_delete = true) {
		// Remove unused data
		map<Light*, vector<Object*> > new_scene_data;
		map<Light*, vector<Object*> >::iterator it;
		vector<Object*>::iterator ob_it;
		bool deleted = false;

		for(it = scene_data->begin(); it != scene_data->end(); it++) {
    		for(ob_it = it->second.begin(); ob_it != it->second.end(); ob_it++) {
			    Object *data = *ob_it;

			    if(do_delete && used_set.find(data) == used_set.end()) {
				    delete data;
				    deleted = true;
			    }
			    else new_scene_data[it->first].push_back(data);
            }
		}

		*scene_data = new_scene_data;

		// Update mapping
		map<ObjectKey, Object*> new_map;
		typedef pair<const ObjectKey, Object*> TMapPair;
		map<ObjectKey, Object*>::iterator jt;

		for(jt = b_map.begin(); jt != b_map.end(); jt++) {
			TMapPair& pair = *jt;

			if(used_set.find(pair.second) != used_set.end())
				new_map[pair.first] = pair.second;
		}

		used_set.clear();
		b_recalc.clear();
		b_map = new_map;

		return deleted;
	} //post_sync()

protected:
	map<Light*, vector<Object*> >    *scene_data;
	map<ObjectKey, Object*>         b_map;
	set<Object*>                    used_set;
	set<void*>                      b_recalc;
    Scene                           *scene;
}; //lights_map


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class BlenderSync {
public:
	BlenderSync(BL::RenderEngine b_engine_, BL::BlendData b_data, BL::Scene b_scene, Scene *scene_, bool interactive_, Progress &progress_);
	~BlenderSync();

	bool sync_recalc();
	// Sync the Blender scene data to Octane
	void sync_data(PassType pass_type, BL::SpaceView3D b_v3d, BL::Object b_override, const char *layer = 0);
	void sync_kernel(PassType pass_type);
	void sync_camera(BL::Object b_override, int width, int height);
	void sync_view(BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height);
	int  get_layer_samples() { return render_layer.samples; }

    Mesh  *sync_mesh(BL::Object b_ob, vector<uint> &used_shaders, bool object_updated, bool hide_tris);
	Light *sync_light(BL::Object b_ob, Transform& tfm, bool object_updated);

	// Get parameters
	static SessionParams    get_session_params(BL::RenderEngine b_engine, BL::UserPreferences b_userpref, BL::Scene b_scene, bool background);
	static bool             get_session_pause_state(BL::Scene b_scene, bool background);
	static void             set_session_pause_state(BL::Scene b_scene, bool state);
	static BufferParams     get_display_buffer_params(Camera* cam, int width, int height);

private:
	void sync_lamps();
	void sync_materials();
	void sync_objects(BL::SpaceView3D b_v3d, int motion = 0);
	void sync_motion(BL::SpaceView3D b_v3d, BL::Object b_override);
	void sync_view();
	void sync_world();
	void sync_render_layers(BL::SpaceView3D b_v3d, const char *layer);
	void sync_shaders();
    void sync_curve_settings();

	void    sync_nodes(Shader *shader, BL::ShaderNodeTree b_ntree);
    void    sync_curves(Mesh *mesh, BL::Mesh b_mesh, BL::Object b_ob, bool object_updated);
    Object  *sync_object(BL::Object b_parent, int persistent_id[OBJECT_PERSISTENT_ID_SIZE], BL::DupliObject b_dupli_ob, Transform& tfm, uint layer_flag, int motion, bool hide_tris);
    void    sync_light_object(BL::Object b_parent, int persistent_id[OBJECT_PERSISTENT_ID_SIZE], BL::Object b_ob, Transform& tfm, BL::DupliObject b_dupli_ob, uint layer_flag);

    bool sync_dupli_particle(BL::Object b_ob, BL::DupliObject b_dup, Object *object);

	// Util
	void add_used_shader_index(BL::ID id, vector<uint>& used_shaders, int default_shader);
	bool BKE_object_is_modified(BL::Object b_ob);
	bool object_is_mesh(BL::Object b_ob);
	bool object_is_light(BL::Object b_ob);

    void load_camera_from_object(Camera* cam, BL::Object b_ob, int width, int height, float zoom, float2& offset, bool skip_panorama = false);

    void get_cam_settings(Camera* cam, PointerRNA &oct_camera, bool view = false);

    void load_camera_from_view(Camera* cam, BL::Scene b_scene, BL::SpaceView3D b_v3d, BL::RegionView3D b_rv3d, int width, int height, float2& offset, bool skip_panorama = false);
    void get_camera_sensor_size(Camera* cam, int width, int height, float *sensor_size);
    void calculate_ortho_scale(Camera* cam, float x_aspect, float y_aspect, float *ortho_scale);
    void get_camera_ortho_scale(Camera* cam, BL::Camera &b_camera, int width, int height, float *ortho_scale);
    void get_viewport_ortho_scale(Camera* cam, float view_distance, float lens, int width, int height, float *ortho_scale);

	// Variables
	BL::RenderEngine    b_engine;
	BL::BlendData       b_data;
	BL::Scene           b_scene;

	id_map<void*, Shader>   shader_map;
	objects_map             object_map;
	id_map<void*, Mesh>     mesh_map;
	lights_map              light_object_map;
	id_map<void*, Light>    light_map;
	set<Mesh*>              mesh_synced;
	set<Light*>             lights_synced;
	void                    *world_map;
	bool                    world_recalc;

	Scene                   *scene;
	bool                    interactive;

    // Layer Info structure
	struct RenderLayerInfo {
        RenderLayerInfo() :
		        scene_layer(0), layer(0), holdout_layer(0), exclude_layer(0),
		        material_override(PointerRNA_NULL),
		        use_background(true),
		        use_viewport_visibility(false),
		        samples(0), bound_samples(false)
		{}

		string          name;
		uint            scene_layer;
		uint            layer;
		uint            holdout_layer;
        uint            exclude_layer;
		BL::Material    material_override;
		bool            use_background;
		bool            use_viewport_visibility;
		bool            use_localview;
		int             samples;
        bool            bound_samples;
	} render_layer;

	Progress &progress;
}; //BlenderSync

OCT_NAMESPACE_END

#endif /* __BLENDER_SYNC_H__ */

