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

#include "server.h"
#include "blender_sync.h"
#include "blender_session.h"

#include "util_opengl.h"
#include "util_path.h"

OCT_NAMESPACE_BEGIN

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
// 
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static PyObject *create_func(PyObject *self, PyObject *args) {
	PyObject *pyengine, *pyuserpref, *pydata, *pyscene, *pyregion, *pyv3d, *pyrv3d;

	if(!PyArg_ParseTuple(args, "OOOOOOO", &pyengine, &pyuserpref, &pydata, &pyscene, &pyregion, &pyv3d, &pyrv3d))
		return NULL;

	// RNA
	PointerRNA engineptr;
	RNA_pointer_create(NULL, &RNA_RenderEngine, (void*)PyLong_AsVoidPtr(pyengine), &engineptr);
	BL::RenderEngine engine(engineptr);

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

	// Create session
	BlenderSession *session;

	Py_BEGIN_ALLOW_THREADS

	if(rv3d) {
		// Interactive session
		int width   = region.width();
		int height  = region.height();

		session = new BlenderSession(engine, userpref, data, scene, v3d, rv3d, width, height);
	}
	else {
		// Offline session
		session = new BlenderSession(engine, userpref, data, scene);
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
static PyObject *server_info_func(PyObject *self, PyObject *args) {
	oct::RenderServerInfo& server = oct::RenderServer::get_info();
	PyObject *ret = PyTuple_New(1);

    PyTuple_SET_ITEM(ret, 0, PyUnicode_FromString(server.net_address));

	return ret;
} //server_info_func()

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
static PyMethodDef methods[] = {
	{"init",            init_func,              METH_VARARGS,   ""},
	{"create",          create_func,            METH_VARARGS,   ""},
	{"free",            free_func,              METH_O,         ""},
	{"render",          render_func,            METH_O,         ""},
	{"draw",            draw_func,              METH_VARARGS,   ""},
	{"sync",            sync_func,              METH_O,         ""},
    {"reset",           reset_func,             METH_VARARGS,   ""},
    {"reload",          reload_func,            METH_O,         ""},
	{"server_info",     server_info_func,       METH_NOARGS,    ""},
	{"set_meshes_type", set_meshes_type_func,   METH_VARARGS,   ""},
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

