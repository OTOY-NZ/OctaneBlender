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

#include <Python.h>

#include "OCT_api.h"

#include "OctaneClient.h"
#include "blender_sync.h"
#include "blender_session.h"

#include "util_opengl.h"
#include "util_path.h"

#include <atomic>
#include <string>

#include "BKE_scene.h"
#include "BKE_global.h"
#include "BKE_main.h"
#include "BLI_utildefines.h"
#include "BKE_context.h"
#include "RE_pipeline.h"
#include "BLI_fileops.h"
#include "render_types.h"

#include "WM_types.h"
#include "WM_api.h"

OCT_NAMESPACE_BEGIN

static std::atomic_flag export_busy = ATOMIC_FLAG_INIT;

struct OctExportJobData {
    BL::RenderEngine    b_engine;
    BL::Scene           b_scene;
    BL::BlendData       b_data;
    BL::UserPreferences b_userpref;

    bContext            *cont;
    wmTimer             *timer;
    int                 export_type;
    
    char                filename[1024];

    short *stop;
    short *do_update;
    float *progress;

    bool was_canceled;
}; //struct OctExportJobData


//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static const char *PyC_UnicodeAsByte(PyObject *py_str, PyObject **coerce) {
    const char *result = _PyUnicode_AsString(py_str);
    if(result) {
        // 99% of the time this is enough but we better support non unicode chars since blender doesnt limit this.
        return result;
    }
    else {
        PyErr_Clear();
        if(PyBytes_Check(py_str)) {
            return PyBytes_AS_STRING(py_str);
        }
        else if((*coerce = PyUnicode_EncodeFSDefault(py_str))) {
            return PyBytes_AS_STRING(*coerce);
        }
        else {
            // Clear the error, so Cycles can be at leadt used without GPU and OSL support
            PyErr_Clear();
            return "";
        }
    }
} //PyC_UnicodeAsByte()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void export_startjob(void *customdata, short *stop, short *do_update, float *progress) {
    OctExportJobData *data = static_cast<OctExportJobData *>(customdata);

    data->stop = stop;
    data->do_update = do_update;
    data->progress = progress;

    data->b_engine.update_progress(0.0000001f);

    // XXX annoying hack: needed to prevent data corruption when changing
    // scene frame in separate threads
    G.is_rendering = true;
    BKE_spacedata_draw_locks(true);

    G.is_break = false;

    int cur_frame = data->b_scene.frame_current();
    int first_frame = data->b_scene.frame_start();
    int last_frame = data->b_scene.frame_end();

    ::Scene *m_scene = (::Scene*)data->b_scene.ptr.data;
    if(!G.is_break) {
        m_scene->r.cfra = first_frame;
        m_scene->r.subframe = first_frame - m_scene->r.cfra;
        BKE_scene_update_for_newframe(CTX_data_main(data->cont)->eval_ctx, CTX_data_main(data->cont), m_scene, m_scene->lay);
        BKE_scene_camera_switch_update(m_scene);

        // Create session
        std::string export_path(data->filename);
        BlenderSession *session = newnt BlenderSession(data->b_engine, data->b_userpref, data->b_data, data->b_scene, (::OctaneEngine::OctaneClient::SceneExportTypes::SceneExportTypesEnum)data->export_type, export_path);

        if(session) {
            if(first_frame != last_frame) data->b_engine.update_progress(0.5f / (last_frame - first_frame + 1));

            for(int f = first_frame; f <= last_frame; ++f) {
                if(G.is_break) {
                    data->was_canceled = true;
                    break;
                }

                if(f > first_frame) {
                    m_scene->r.cfra = f;
                    m_scene->r.subframe = f - m_scene->r.cfra;
                    BKE_scene_update_for_newframe(CTX_data_main(data->cont)->eval_ctx, CTX_data_main(data->cont), m_scene, m_scene->lay);
                    BKE_scene_camera_switch_update(m_scene);

                    data->b_engine.update_progress(((float)(f - first_frame + 1) - 0.5f) / (last_frame - first_frame + 1));
                }

                if(G.is_break) {
                    data->was_canceled = true;
                    break;
                }

                session->sync->sync_recalc();
                session->render();

                if(f != last_frame) data->b_engine.update_progress((float)(f - first_frame + 1) / (last_frame - first_frame + 1));
            }
            delete session;
        }
        else fprintf(stderr, "Octane: ERROR creating session\n");
    }
    else data->was_canceled = true;

    if(cur_frame != data->b_scene.frame_current()) {
        m_scene->r.cfra = cur_frame;
        m_scene->r.subframe = cur_frame - m_scene->r.cfra;
        BKE_scene_update_for_newframe(CTX_data_main(data->cont)->eval_ctx, CTX_data_main(data->cont), m_scene, m_scene->lay);
        BKE_scene_camera_switch_update(m_scene);
    }
} //export_startjob()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void export_endjob(void *customdata) {
    OctExportJobData *data = static_cast<OctExportJobData *>(customdata);

    // Delete produced file
    if(data->was_canceled) {
        if(data->export_type == ::OctaneEngine::OctaneClient::SceneExportTypes::ORBX)
            strcat(data->filename, ".orbx");
        else
            strcat(data->filename, ".abc");

        if(BLI_exists(data->filename)) BLI_delete(data->filename, false, false);
    }
    else data->b_engine.update_progress(1.0f);

    G.is_rendering = false;
    BKE_spacedata_draw_locks(false);

    if(data->timer) WM_event_timer_sleep(CTX_wm_manager(data->cont), CTX_wm_window(data->cont), data->timer, false);
    export_busy.clear(std::memory_order_release);
} //export_endjob()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static void render_progress_update(void *rjv, float progress) {
    OctExportJobData *rj = (OctExportJobData*)rjv;
    
    if (rj->progress && *rj->progress != progress) {
        *rj->progress = progress;
        // make jobs timer to send notifier
        *(rj->do_update) = true;
    }
} //render_progress_update()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// INIT
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *init_func(PyObject *self, PyObject *args) {
    const char *path, *user_path;
    if(!PyArg_ParseTuple(args, "ss", &path, &user_path)) return NULL;
    
    path_init(path, user_path);

    Py_RETURN_NONE;
} //init_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Check if export is finished
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *export_ready_func(PyObject *self, PyObject *args) {
    if(export_busy.test_and_set(std::memory_order_acquire)) return PyBool_FromLong(0);
    else {
        export_busy.clear(std::memory_order_release);
        return PyBool_FromLong(1);
    }
} //export_ready_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Start the export job
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *export_func(PyObject *self, PyObject *args) {
    if(export_busy.test_and_set(std::memory_order_acquire)) return PyBool_FromLong(0);

    PyObject *pyscene, *pycontext, *pytimer, *pyuserpref, *pydata, *path;
    int export_type;

    if(!PyArg_ParseTuple(args, "OOOOOiO", &pyscene, &pycontext, &pytimer, &pyuserpref, &pydata, &export_type, &path)) {
        export_busy.clear(std::memory_order_release);
        return PyBool_FromLong(0);
    }

    if(export_type == ::OctaneEngine::OctaneClient::SceneExportTypes::NONE) {
        fprintf(stderr, "Octane: export ERROR: export type is not set\n");
        export_busy.clear(std::memory_order_release);
        return PyBool_FromLong(0);
    }

    PyObject *path_coerce = NULL;
    std::string cur_path = PyC_UnicodeAsByte(path, &path_coerce);
    Py_XDECREF(path_coerce);

    bContext *cont = (bContext*)PyLong_AsVoidPtr(pycontext);
    wmTimer *timer = (wmTimer*)PyLong_AsVoidPtr(pytimer);

    if(timer) WM_event_timer_sleep(CTX_wm_manager(cont), CTX_wm_window(cont), timer, true);

    PointerRNA sceneptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene b_scene(sceneptr);

    if(b_scene.frame_start() > b_scene.frame_end()) {
        fprintf(stderr, "Octane: export ERROR: the start frame is behind the end frame\n");
        export_busy.clear(std::memory_order_release);
        return PyBool_FromLong(0);
    }

    PointerRNA userprefptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyuserpref), &userprefptr);
    BL::UserPreferences b_userpref(userprefptr);

    PointerRNA dataptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pydata), &dataptr);
    BL::BlendData b_data(dataptr);

    // Create engine
    PointerRNA engineptr;
    BL::RenderSettings rs = b_scene.render();

    Render *re = RE_NewRender(b_scene.name().c_str());
    re->main    = G.main;
    re->scene   = (::Scene*)b_scene.ptr.data;
    re->lay     = re->scene->lay;
    //re->r.scemode = (resc->r.scemode & ~R_EXR_CACHE_FILE) | (re->r.scemode & R_EXR_CACHE_FILE);
    re->scene_color_manage = BKE_scene_check_color_management_enabled(re->scene);
    //RE_SetReports(re, op->reports);

    RenderEngineType *type = RE_engines_find("octane");
    RenderEngine *engine = RE_engine_create(type);
    engine->re              = re;
    engine->flag            |= RE_ENGINE_RENDERING | RE_ENGINE_ANIMATION;
    engine->camera_override = nullptr;
    engine->layer_override  = 0;
    engine->resolution_x    = rs.resolution_x() * rs.resolution_percentage() / 100;
    engine->resolution_y    = rs.resolution_y() * rs.resolution_percentage() / 100;
    //engine->tile_x = re->partx;
    //engine->tile_y = re->party;

    RNA_pointer_create(NULL, &RNA_RenderEngine, engine, &engineptr);
    BL::RenderEngine b_engine(engineptr);

    // Setup job data
    OctExportJobData *data = static_cast<OctExportJobData*>(MEM_mallocN(sizeof(OctExportJobData), "OctExportJobData"));
    data->was_canceled  = false;
    data->b_engine      = b_engine;
    data->b_scene       = b_scene;
    data->cont          = cont;
    data->timer         = timer;
    data->b_userpref    = b_userpref;
    data->b_data        = b_data;
    data->export_type   = export_type;
    strcpy(data->filename, cur_path.c_str());

    Py_BEGIN_ALLOW_THREADS
        
    wmJob *wm_job = WM_jobs_get(CTX_wm_manager(cont), CTX_wm_window(cont), (::Scene*)b_scene.ptr.data, export_type == ::OctaneEngine::OctaneClient::SceneExportTypes::ORBX ? "Octane ORBX export" : "Octane alembic export", WM_JOB_PROGRESS, WM_JOB_TYPE_RENDER);
    WM_jobs_customdata_set(wm_job, data, MEM_freeN);
    WM_jobs_timer(wm_job, 0.1, NC_SCENE | ND_FRAME, NC_SCENE | ND_FRAME);
    WM_jobs_callbacks(wm_job, export_startjob, NULL, NULL, export_endjob);
    RE_progress_cb(re, data, render_progress_update);
    WM_jobs_start(CTX_wm_manager(cont), wm_job);

    Py_END_ALLOW_THREADS

    return PyBool_FromLong(1);
} //export_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *create_func(PyObject *self, PyObject *args) {
    PyObject *pyengine, *pyuserpref, *pydata, *pyscene, *pyregion, *pyv3d, *pyrv3d;

    if(!PyArg_ParseTuple(args, "OOOOOOO", &pyengine, &pyuserpref, &pydata, &pyscene, &pyregion, &pyv3d, &pyrv3d))
        return NULL;

    PointerRNA userprefptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyuserpref), &userprefptr);
    BL::UserPreferences userpref(userprefptr);

    PointerRNA dataptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pydata), &dataptr);
    BL::BlendData data(dataptr);

    PointerRNA sceneptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene scene(sceneptr);

    PointerRNA regionptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyregion), &regionptr);
    BL::Region region(regionptr);

    PointerRNA v3dptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyv3d), &v3dptr);
    BL::SpaceView3D v3d(v3dptr);

    PointerRNA rv3dptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyrv3d), &rv3dptr);
    BL::RegionView3D rv3d(rv3dptr);

    PointerRNA engineptr;
    RNA_pointer_create(NULL, &RNA_RenderEngine, (void*)PyLong_AsVoidPtr(pyengine), &engineptr);
    BL::RenderEngine b_engine(engineptr);

    // Create session
    BlenderSession *session;

    Py_BEGIN_ALLOW_THREADS

    std::string export_path("");
    if(rv3d) {
        // Interactive session
        int width   = region.width();
        int height  = region.height();

        session = new BlenderSession(b_engine, userpref, data, scene, ::OctaneEngine::OctaneClient::SceneExportTypes::SceneExportTypesEnum::NONE, export_path, v3d, rv3d, width, height);
    }
    else {
        // Offline session
        session = new BlenderSession(b_engine, userpref, data, scene, ::OctaneEngine::OctaneClient::SceneExportTypes::SceneExportTypesEnum::NONE, export_path);
    }

    Py_END_ALLOW_THREADS

    return PyLong_FromVoidPtr(session);
} //create_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *free_func(PyObject *self, PyObject *value) {
    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(value);
    if(session) delete session;

    Py_RETURN_NONE;
} //free_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *render_func(PyObject *self, PyObject *value) {
    Py_BEGIN_ALLOW_THREADS

    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(value);
    if(session) session->render();

    Py_END_ALLOW_THREADS

    Py_RETURN_NONE;
} //render_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *draw_func(PyObject *self, PyObject *args) {
    PyObject *pysession, *pyv3d, *pyrv3d;

    if(!PyArg_ParseTuple(args, "OOO", &pysession, &pyv3d, &pyrv3d)) return NULL;
    
    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(pysession);

    if(session && PyLong_AsVoidPtr(pyrv3d)) {
        // 3d view drawing 
        int viewport[4];
        glGetIntegerv(GL_VIEWPORT, viewport);

        session->draw(viewport[2], viewport[3]);
    }

    Py_RETURN_NONE;
} //draw_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *reset_func(PyObject *self, PyObject *args) {
    PyObject *pysession, *pydata, *pyscene;

    //BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(value);
    if(!PyArg_ParseTuple(args, "OOO", &pysession, &pydata, &pyscene))
        return NULL;

    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(pysession);

    PointerRNA dataptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pydata), &dataptr);
    BL::BlendData b_data(dataptr);

    PointerRNA sceneptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene b_scene(sceneptr);

    Py_BEGIN_ALLOW_THREADS

    if(session) {
        session->reset_session(b_data, b_scene);
        delete session;
    }

    Py_END_ALLOW_THREADS

    Py_RETURN_NONE;
} //reset_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *reload_func(PyObject *self, PyObject *value) {
    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(value);

    Py_BEGIN_ALLOW_THREADS

    if(session) session->reload_session();

    Py_END_ALLOW_THREADS

    Py_RETURN_NONE;
} //reload_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *sync_func(PyObject *self, PyObject *value) {
    Py_BEGIN_ALLOW_THREADS

    BlenderSession *session = (BlenderSession*)PyLong_AsVoidPtr(value);
    if(session) session->synchronize();

    Py_END_ALLOW_THREADS

    Py_RETURN_NONE;
} //sync_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *octane_devices_func(PyObject */*self*/, PyObject *args) {
    static std::string sCurrentServerAddress;
    static ::OctaneEngine::OctaneClient::RenderServerInfo serverInfo;

    PyObject *ret;

    PyObject *pyscene;
    if(!PyArg_ParseTuple(args, "O", &pyscene)) {
        ret = PyTuple_New(0);
        return ret;
    }

    PointerRNA sceneptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene b_scene(sceneptr);

    if(b_scene) {
        PointerRNA oct_scene = RNA_pointer_get(&b_scene.ptr, "octane");
        string server_addr = get_string(oct_scene, "server_address");
        if(server_addr != sCurrentServerAddress) {
            sCurrentServerAddress = server_addr;

            if(!server_addr.length()) {
                ret = PyTuple_New(0);
                serverInfo.gpuNames.clear();
            }
            else {
                ::OctaneEngine::OctaneClient *server = newnt ::OctaneEngine::OctaneClient;
                if(server) {
                    if(!server->connectToServer(server_addr.c_str())) {
                        ret = PyTuple_New(0);
                        serverInfo.gpuNames.clear();
                    }
                    else {
                        serverInfo = server->getServerInfo();
                        size_t num_gpus = serverInfo.gpuNames.size();
                        ret = PyTuple_New(num_gpus);
                        if(num_gpus) {
                            std::string *cur_name = &serverInfo.gpuNames[0];
                            for(size_t i = 0; i < num_gpus; ++i) PyTuple_SET_ITEM(ret, i, PyUnicode_FromString(cur_name[i].c_str()));
                        }
                    }
                    delete server;
                }
                else {
                    ret = PyTuple_New(0);
                    serverInfo.gpuNames.clear();
                }
            }
        }
        else {
            size_t num_gpus = serverInfo.gpuNames.size();
            ret = PyTuple_New(num_gpus);
            if(num_gpus) {
                std::string *cur_name = &serverInfo.gpuNames[0];
                for(size_t i = 0; i < num_gpus; ++i) PyTuple_SET_ITEM(ret, i, PyUnicode_FromString(cur_name[i].c_str()));
            }
        }
    }
    else ret = PyTuple_New(0);

    return ret;
} //octane_devices_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static bool object_is_mesh(BL::Object &b_ob) {
    BL::ID b_ob_data = b_ob.data();

    return (b_ob_data && (b_ob_data.is_a(&RNA_Mesh)
            || b_ob_data.is_a(&RNA_Curve)
            || b_ob_data.is_a(&RNA_MetaBall)));
} //object_is_mesh()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *set_meshes_type_func(PyObject *self, PyObject *args) {
    PyObject *pydata, *pytype;

    if(!PyArg_ParseTuple(args, "OO", &pydata, &pytype)) return NULL;

    PointerRNA dataptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pydata), &dataptr);
    BL::BlendData b_data(dataptr);

    long int type = PyLong_AsLong(pytype);

    Py_BEGIN_ALLOW_THREADS

    BL::BlendData::objects_iterator b_ob;
    for(b_data.objects.begin(b_ob); b_ob != b_data.objects.end(); ++b_ob) {
        BL::Object cur_object(*b_ob);
        if(object_is_mesh(cur_object)) {
            if(cur_object.select()) {
                BL::Mesh cur_mesh(cur_object.data());
                PointerRNA oct_mesh = RNA_pointer_get(&cur_mesh.ptr, "octane");
                RNA_enum_set(&oct_mesh, "mesh_type", type);
            }
        }
        //else if(object_is_light(*b_ob)) {
        //}
    }

    Py_END_ALLOW_THREADS

    Py_RETURN_NONE;
} //set_meshes_type_func()

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *activate_func(PyObject *self, PyObject *args) {
    PyObject *pyscene;

    if(!PyArg_ParseTuple(args, "O", &pyscene))
        return PyBool_FromLong(0);

    // RNA
    PointerRNA sceneptr;
    RNA_id_pointer_create((ID*)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene scene(sceneptr);

    bool ret;

    Py_BEGIN_ALLOW_THREADS

    ret = BlenderSession::activate(scene);

    Py_END_ALLOW_THREADS

    return PyBool_FromLong(ret ? 1 : 0);
} //activate_func()



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyMethodDef methods[] = {
    {"init",                init_func,              METH_VARARGS,   ""},
    {"create",              create_func,            METH_VARARGS,   ""},
    {"export_ready",        export_ready_func,      METH_NOARGS,    ""},
    {"export",              export_func,            METH_VARARGS,   ""},
    {"free",                free_func,              METH_O,         ""},
    {"render",              render_func,            METH_O,         ""},
    {"draw",                draw_func,              METH_VARARGS,   ""},
    {"sync",                sync_func,              METH_O,         ""},
    {"reset",               reset_func,             METH_VARARGS,   ""},
    {"reload",              reload_func,            METH_O,         ""},
    {"octane_devices",      octane_devices_func,    METH_VARARGS,   ""},
    {"set_meshes_type",     set_meshes_type_func,   METH_VARARGS,   ""},
    {"activate",            activate_func,          METH_VARARGS,   ""},
    {NULL, NULL, 0, NULL},
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT,
    "_octane",
    "Blender OctaneRender integration",
    -1,
    methods,
    NULL, NULL, NULL, NULL
};


OCT_NAMESPACE_END

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void *OCT_python_module_init() {
    PyObject *mod = PyModule_Create(&oct::module);
    return (void*)mod;
}

