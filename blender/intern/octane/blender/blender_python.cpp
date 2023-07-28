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
#include "BKE_global.h"

#include "blender/OCT_api.h"
#include <Python.h>

#include "blender/blender_client.h"
#include "blender/blender_session.h"

#include "util/util_debug.h"
#include "util/util_foreach.h"
#include "util/util_md5.h"
#include "util/util_opengl.h"
#include "util/util_path.h"
#include "util/util_string.h"
#include "util/util_types.h"

#include "render/common_d3d.hpp"

#include "render/osl.h"

#include "GPU_state.h"

OCT_NAMESPACE_BEGIN

void *pylong_as_voidptr_typesafe(PyObject *object)
{
  if (object == Py_None)
    return NULL;
  return PyLong_AsVoidPtr(object);
}

void python_thread_state_save(void **python_thread_state)
{
  *python_thread_state = (void *)PyEval_SaveThread();
}

void python_thread_state_restore(void **python_thread_state)
{
  PyEval_RestoreThread((PyThreadState *)*python_thread_state);
  *python_thread_state = NULL;
}

static const char *PyC_UnicodeAsByte(PyObject *py_str, PyObject **coerce)
{
  const char *result = _PyUnicode_AsString(py_str);
  if (result) {
    /* 99% of the time this is enough but we better support non unicode
     * chars since blender doesnt limit this.
     */
    return result;
  }
  else {
    PyErr_Clear();
    if (PyBytes_Check(py_str)) {
      return PyBytes_AS_STRING(py_str);
    }
    else if ((*coerce = PyUnicode_EncodeFSDefault(py_str))) {
      return PyBytes_AS_STRING(*coerce);
    }
    else {
      /* Clear the error, so Cycles can be at leadt used without
       * GPU and OSL support,
       */
      PyErr_Clear();
      return "";
    }
  }
}

static PyObject *py_init_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *path, *user_path;
  if (!PyArg_ParseTuple(args, "OO", &path, &user_path)) {
    Py_RETURN_FALSE;
  }
  PyObject *path_coerce = NULL, *user_path_coerce = NULL;
  path_init(PyC_UnicodeAsByte(path, &path_coerce),
            PyC_UnicodeAsByte(user_path, &user_path_coerce));
  Py_XDECREF(path_coerce);
  Py_XDECREF(user_path_coerce);
#if defined(WIN32)
  if (!G.background) {
    CommonD3D::InitD3D11();
  }
#endif
  Py_RETURN_TRUE;
}

static PyObject *py_exit_func(PyObject * /*self*/, PyObject * /*args*/)
{
#if defined(WIN32)
  CommonD3D::ReleaseD3D11();
#endif
  Py_RETURN_TRUE;
}

static PyObject *py_is_shared_surface_supported(PyObject * /*self*/, PyObject * /*args*/)
{
#if defined(WIN32)
  if (CommonD3D::IsD3DInited()) {
    Py_RETURN_TRUE;
  }
  {
    Py_RETURN_FALSE;
  }
#else
  Py_RETURN_FALSE;
#endif
}

static PyObject *create_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pyengine, *pypreferences, *pydata, *pyscreen, *pyregion, *pyv3d, *pyrv3d;
  PyObject *py_resource_list = NULL;

  if (!PyArg_ParseTuple(args,
                        "OOOOOOOO",
                        &pyengine,
                        &pypreferences,
                        &pydata,
                        &pyscreen,
                        &pyregion,
                        &pyv3d,
                        &pyrv3d,
                        &py_resource_list)) {
    return NULL;
  }

  /* RNA */
  ID *bScreen = (ID *)PyLong_AsVoidPtr(pyscreen);

  PointerRNA engineptr;
  RNA_pointer_create(NULL, &RNA_RenderEngine, (void *)PyLong_AsVoidPtr(pyengine), &engineptr);
  BL::RenderEngine engine(engineptr);

  PointerRNA preferencesptr;
  RNA_pointer_create(
      NULL, &RNA_Preferences, (void *)PyLong_AsVoidPtr(pypreferences), &preferencesptr);
  BL::Preferences preferences(preferencesptr);

  PointerRNA dataptr;
  RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  BL::BlendData data(dataptr);

  PointerRNA regionptr;
  RNA_pointer_create(bScreen, &RNA_Region, pylong_as_voidptr_typesafe(pyregion), &regionptr);
  BL::Region region(regionptr);

  PointerRNA v3dptr;
  RNA_pointer_create(bScreen, &RNA_SpaceView3D, pylong_as_voidptr_typesafe(pyv3d), &v3dptr);
  BL::SpaceView3D v3d(v3dptr);

  PointerRNA rv3dptr;
  RNA_pointer_create(bScreen, &RNA_RegionView3D, pylong_as_voidptr_typesafe(pyrv3d), &rv3dptr);
  BL::RegionView3D rv3d(rv3dptr);

  std::string export_path("");

  std::unordered_set<std::string> dirty_resources;
  if (py_resource_list && PyList_Size(py_resource_list)) {
    for (int i = 0; i < PyList_Size(py_resource_list); ++i) {
      PyObject *obj = PyList_GetItem(py_resource_list, i);
      PyObject *strObj = PyUnicode_AsUTF8String(obj);
      std::string str = std::string(PyBytes_AsString(strObj));
      Py_DECREF(strObj);
      dirty_resources.insert(str);
    }
  }

  /* create session */
  BlenderSession *session;

  if (rv3d) {
    /* interactive viewport session */
    int width = region.width();
    int height = region.height();

    session = new BlenderSession(engine,
                                 preferences,
                                 data,
                                 v3d,
                                 rv3d,
                                 width,
                                 height,
                                 BlenderSession::ExportType::NONE,
                                 export_path,
                                 dirty_resources);
  }
  else {
    /* offline session or preview render */
    session = new BlenderSession(
        engine, preferences, data, BlenderSession::ExportType::NONE, export_path, dirty_resources);
  }

  return PyLong_FromVoidPtr(session);
}

static PyObject *free_func(PyObject * /*self*/, PyObject *value)
{
  delete (BlenderSession *)PyLong_AsVoidPtr(value);

  Py_RETURN_NONE;
}

static PyObject *render_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pysession, *pydepsgraph;

  if (!PyArg_ParseTuple(args, "OO", &pysession, &pydepsgraph))
    return NULL;

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, (ID *)PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);

  python_thread_state_save(&session->python_thread_state);

  session->render(b_depsgraph);

  python_thread_state_restore(&session->python_thread_state);

  Py_RETURN_NONE;
}

static PyObject *draw_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pysession, *pygraph, *pyv3d, *pyrv3d;

  if (!PyArg_ParseTuple(args, "OOOO", &pysession, &pygraph, &pyv3d, &pyrv3d))
    return NULL;

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  if (PyLong_AsVoidPtr(pyrv3d)) {
    /* 3d view drawing */
    int viewport[4];
    GPU_viewport_size_get_i(viewport);

    session->draw(viewport[2], viewport[3]);
  }

  Py_RETURN_NONE;
}

static PyObject *sync_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pysession, *pydepsgraph;

  if (!PyArg_ParseTuple(args, "OO", &pysession, &pydepsgraph))
    return NULL;

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);

  python_thread_state_save(&session->python_thread_state);

  session->synchronize(b_depsgraph);

  python_thread_state_restore(&session->python_thread_state);

  Py_RETURN_NONE;
}

static PyObject *reset_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pysession, *pydata, *pydepsgraph;

  if (!PyArg_ParseTuple(args, "OOO", &pysession, &pydata, &pydepsgraph))
    return NULL;

  BlenderSession *session = (BlenderSession *)PyLong_AsVoidPtr(pysession);

  PointerRNA dataptr;
  RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  BL::BlendData b_data(dataptr);

  PointerRNA depsgraphptr;
  RNA_pointer_create(NULL, &RNA_Depsgraph, PyLong_AsVoidPtr(pydepsgraph), &depsgraphptr);
  BL::Depsgraph b_depsgraph(depsgraphptr);

  python_thread_state_save(&session->python_thread_state);

  session->reset_session(b_data, b_depsgraph);

  python_thread_state_restore(&session->python_thread_state);

  Py_RETURN_NONE;
}

static PyObject *command_to_octane_func(PyObject *self, PyObject *args)
{
  int octane_cmd_type = 0;
  PyObject *py_int_list = NULL, *py_float_list = NULL, *py_str_list = NULL;
  if (PyArg_ParseTuple(args,
                       "i|O!O!O!",
                       &octane_cmd_type,
                       &PyList_Type,
                       &py_int_list,
                       &PyList_Type,
                       &py_float_list,
                       &PyList_Type,
                       &py_str_list)) {
    std::vector<int> int_params;
    std::vector<float> float_params;
    std::vector<std::string> str_params;
    if (py_int_list && PyList_Size(py_int_list)) {
      for (int i = 0; i < PyList_Size(py_int_list); ++i) {
        PyObject *obj = PyList_GetItem(py_int_list, i);
        if (PyLong_Check(obj)) {
          int_params.emplace_back(PyLong_AsLong(obj));
        }
      }
    }
    if (py_float_list && PyList_Size(py_float_list)) {
      for (int i = 0; i < PyList_Size(py_float_list); ++i) {
        PyObject *obj = PyList_GetItem(py_float_list, i);
        if (PyFloat_Check(obj)) {
          float_params.emplace_back(PyFloat_AsDouble(obj));
        }
      }
    }
    if (py_str_list && PyList_Size(py_str_list)) {
      for (int i = 0; i < PyList_Size(py_str_list); ++i) {
        PyObject *obj = PyList_GetItem(py_str_list, i);
        PyObject *strObj = PyUnicode_AsUTF8String(obj);
        std::string str = std::string(PyBytes_AsString(strObj));
        Py_DECREF(strObj);
        str_params.emplace_back(str);
      }
    }
    Py_BEGIN_ALLOW_THREADS;
    BlenderSession::command_to_octane(
        G.octane_server_address, octane_cmd_type, int_params, float_params, str_params);
    Py_END_ALLOW_THREADS;
  }
  Py_RETURN_NONE;
}

static PyObject *osl_compile_func(PyObject *self, PyObject *args)
{
  PyObject *rets = PyTuple_New(2);
  std::string info;
  PyObject *py_osl_identifier = NULL, *pynodegroup = NULL, *pynode = NULL, *py_osl_path = NULL,
           *py_osl_code = NULL;
  if (PyArg_ParseTuple(
          args, "OOOOO", &py_osl_identifier, &pynodegroup, &pynode, &py_osl_path, &py_osl_code)) {
    /* RNA */
    PointerRNA nodeptr;
    RNA_pointer_create((ID *)PyLong_AsVoidPtr(pynodegroup),
                       &RNA_ShaderNode,
                       (void *)PyLong_AsVoidPtr(pynode),
                       &nodeptr);
    PyObject *path_coerce = NULL;
    std::string osl_identifier = PyC_UnicodeAsByte(py_osl_identifier, &path_coerce);
    std::string osl_path = PyC_UnicodeAsByte(py_osl_path, &path_coerce);
    std::string osl_code = PyC_UnicodeAsByte(py_osl_code, &path_coerce);
    Py_XDECREF(path_coerce);
    Py_BEGIN_ALLOW_THREADS;
    if (BlenderSession::osl_compile(
            G.octane_server_address, osl_identifier, nodeptr, osl_path, osl_code, info)) {
      PyTuple_SET_ITEM(rets, 0, Py_True);
    }
    else {
      PyTuple_SET_ITEM(rets, 0, Py_False);
    }
    Py_END_ALLOW_THREADS;
  }
  else {
    PyTuple_SET_ITEM(rets, 0, Py_False);
  }
  PyTuple_SET_ITEM(rets, 1, PyUnicode_FromString(info.c_str()));
  return rets;
}

static PyObject *osl_update_node_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pydata = NULL, *py_osl_identifier = NULL, *pynodegroup = NULL, *pynode = NULL;
  const char *osl_filepath = NULL;
  if (!PyArg_ParseTuple(args, "OOOO", &pydata, &py_osl_identifier, &pynodegroup, &pynode))
    return NULL;

  /* RNA */
  PointerRNA dataptr;
  RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  BL::BlendData b_data(dataptr);

  PyObject *path_coerce = NULL;
  std::string osl_identifier = PyC_UnicodeAsByte(py_osl_identifier, &path_coerce);
  Py_XDECREF(path_coerce);
  /* RNA */
  PointerRNA nodeptr;
  RNA_pointer_create((ID *)PyLong_AsVoidPtr(pynodegroup),
                     &RNA_ShaderNode,
                     (void *)PyLong_AsVoidPtr(pynode),
                     &nodeptr);
  BL::ShaderNode b_node(nodeptr);
  OctaneDataTransferObject::OSLNodeInfo oslNodeInfo;
  if (OSLManager::Instance().query_osl(osl_identifier, oslNodeInfo)) {
    /* add new sockets from parameters */
    set<void *> used_sockets;
    for (int i = 0; i < oslNodeInfo.mPinInfo.size(); ++i) {
      /* determine socket type */
      string socket_type;
      BL::NodeSocket::type_enum data_type = BL::NodeSocket::type_VALUE;
      float4 default_float4 = make_float4(0.0f, 0.0f, 0.0f, 1.0f);
      float default_float = 0.0f;
      int default_int = 0;
      int default_enum = 0;
      bool default_bool = false;
      string default_string = "";

      const OctaneDataTransferObject::ApiNodePinInfo &pinInfo = oslNodeInfo.mPinInfo.get_param(i);
      string socket_name = pinInfo.mLabelName;
      string identifier = pinInfo.mName;

      switch (pinInfo.mType) {
        case Octane::PT_TRANSFORM:
        case Octane::PT_PROJECTION:
          socket_type = "NodeSocketShader";
          data_type = BL::NodeSocket::type_SHADER;
          break;
        case Octane::PT_TEXTURE:
          socket_type = "NodeSocketFloat";
          data_type = BL::NodeSocket::type_VALUE;
          default_float = pinInfo.mFloatInfo.mDefaultValue.x;
          break;
        case Octane::PT_STRING:
          socket_type = "NodeSocketString";
          data_type = BL::NodeSocket::type_STRING;
          default_string = pinInfo.mStringInfo.mDefaultValue;
          break;
        case Octane::PT_BOOL:
          socket_type = "NodeSocketBool";
          data_type = BL::NodeSocket::type_BOOLEAN;
          default_bool = pinInfo.mBoolInfo.mDefaultValue;
          break;
        case Octane::PT_ENUM:
          socket_type = "NodeSocketInt";
          data_type = BL::NodeSocket::type_INT;
          default_enum = pinInfo.mEnumInfo.mDefaultValue;
          break;
        case Octane::PT_FLOAT:
          if (pinInfo.mFloatInfo.mIsColor) {
            socket_type = "NodeSocketColor";
            data_type = BL::NodeSocket::type_RGBA;
            default_float4[0] = pinInfo.mFloatInfo.mDefaultValue.x;
            default_float4[1] = pinInfo.mFloatInfo.mDefaultValue.y;
            default_float4[2] = pinInfo.mFloatInfo.mDefaultValue.z;
          }
          else if (pinInfo.mFloatInfo.mDimCount > 1) {
            socket_type = "NodeSocketVector";
            data_type = BL::NodeSocket::type_VECTOR;
            default_float4[0] = pinInfo.mFloatInfo.mDefaultValue.x;
            default_float4[1] = pinInfo.mFloatInfo.mDefaultValue.y;
            default_float4[2] = pinInfo.mFloatInfo.mDimCount > 2 ?
                                    pinInfo.mFloatInfo.mDefaultValue.z :
                                    0.f;
          }
          else {
            socket_type = "NodeSocketFloat";
            data_type = BL::NodeSocket::type_VALUE;
            default_float = pinInfo.mFloatInfo.mDefaultValue.x;
          }
          break;
        case Octane::PT_INT:
          if (pinInfo.mIntInfo.mIsColor) {
            socket_type = "NodeSocketColor";
            data_type = BL::NodeSocket::type_RGBA;
            default_float4[0] = pinInfo.mIntInfo.mDefaultValue.x;
            default_float4[1] = pinInfo.mIntInfo.mDefaultValue.y;
            default_float4[2] = pinInfo.mIntInfo.mDefaultValue.z;
          }
          else if (pinInfo.mIntInfo.mDimCount > 1) {
            socket_type = "NodeSocketVector";
            data_type = BL::NodeSocket::type_VECTOR;
            default_float4[0] = pinInfo.mIntInfo.mDefaultValue.x;
            default_float4[1] = pinInfo.mIntInfo.mDefaultValue.y;
            default_float4[2] = pinInfo.mIntInfo.mDefaultValue.z;
          }
          else {
            socket_type = "NodeSocketInt";
            data_type = BL::NodeSocket::type_INT;
            default_int = pinInfo.mIntInfo.mDefaultValue.x;
          }
          break;
        default:
          continue;
      }
      /* find socket socket */
      BL::NodeSocket b_sock(PointerRNA_NULL);
      if (pinInfo.mIsOutput) {
        b_sock = b_node.outputs[socket_name];
        // LEGACY ISSUES
        // Before 16.3.2, blender uses mName as socket name.
        // After 16.3.2, blender uses mLabelName as socket name.
        // To solve the backward compatibility issue, server send both
        // therefore, client can solve backward compatibility issues
        if (!b_sock) {
          b_sock = b_node.outputs[identifier];
          if (b_sock && socket_name.size() > 0) {
            b_sock.name(socket_name);
          }
        }
        /* remove if type no longer matches */
        if (b_sock && b_sock.bl_idname() != socket_type) {
          b_node.outputs.remove(b_data, b_sock);
          b_sock = BL::NodeSocket(PointerRNA_NULL);
        }
      }
      else {
        b_sock = b_node.inputs[socket_name];
        if (!b_sock) {
          b_sock = b_node.inputs[identifier];
          if (b_sock && socket_name.size() > 0) {
            b_sock.name(socket_name);
          }
        }
        /* remove if type no longer matches */
        if (b_sock && b_sock.bl_idname() != socket_type) {
          b_node.inputs.remove(b_data, b_sock);
          b_sock = BL::NodeSocket(PointerRNA_NULL);
        }
      }

      if (!b_sock) {
        /* create new socket */
        if (pinInfo.mIsOutput)
          b_sock = b_node.outputs.create(
              b_data, socket_type.c_str(), socket_name.c_str(), identifier.c_str());
        else
          b_sock = b_node.inputs.create(
              b_data, socket_type.c_str(), socket_name.c_str(), identifier.c_str());

        /* set default value */
        if (data_type == BL::NodeSocket::type_VALUE) {
          set_float(b_sock.ptr, "default_value", default_float);
        }
        else if (data_type == BL::NodeSocket::type_INT) {
          set_int(b_sock.ptr, "default_value", default_int);
        }
        else if (data_type == BL::NodeSocket::type_RGBA) {
          set_float4(b_sock.ptr, "default_value", default_float4);
        }
        else if (data_type == BL::NodeSocket::type_VECTOR) {
          set_float3(b_sock.ptr, "default_value", float4_to_float3(default_float4));
        }
        else if (data_type == BL::NodeSocket::type_STRING) {
          set_string(b_sock.ptr, "default_value", default_string);
        }
      }

      used_sockets.insert(b_sock.ptr.data);
    }

    /* remove unused parameters */
    bool removed;

    do {
      BL::Node::inputs_iterator b_input;
      BL::Node::outputs_iterator b_output;

      removed = false;

      for (b_node.inputs.begin(b_input); b_input != b_node.inputs.end(); ++b_input) {
        if (used_sockets.find(b_input->ptr.data) == used_sockets.end()) {
          b_node.inputs.remove(b_data, *b_input);
          removed = true;
          break;
        }
      }

    } while (removed);

    Py_RETURN_TRUE;
  }
  Py_RETURN_FALSE;
}

static PyObject *export_func(PyObject * /*self*/, PyObject *args)
{
  int octane_export_type;
  PyObject *pyscene, *pycontext, *pypreferences, *pydata, *py_path;

  if (!PyArg_ParseTuple(args,
                        "OOOOOi",
                        &pyscene,
                        &pycontext,
                        &pypreferences,
                        &pydata,
                        &py_path,
                        &octane_export_type)) {
    return NULL;
  }

  PointerRNA sceneptr;
  RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pyscene), &sceneptr);
  BL::Scene b_scene(sceneptr);

  bContext *context = (bContext *)PyLong_AsVoidPtr(pycontext);

  PointerRNA preferencesptr;
  RNA_pointer_create(
      NULL, &RNA_Preferences, (void *)PyLong_AsVoidPtr(pypreferences), &preferencesptr);
  BL::Preferences preferences(preferencesptr);

  PointerRNA dataptr;
  RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  BL::BlendData data(dataptr);

  PyObject *path_coerce = NULL;
  std::string path = PyC_UnicodeAsByte(py_path, &path_coerce);
  Py_XDECREF(path_coerce);

  Py_BEGIN_ALLOW_THREADS;
  BlenderSession::export_scene(b_scene,
                               context,
                               preferences,
                               data,
                               path,
                               static_cast<BlenderSession::ExportType>(octane_export_type));
  Py_END_ALLOW_THREADS;
  Py_RETURN_NONE;
}

static PyObject *export_localdb_func(PyObject * /*self*/, PyObject *args)
{
  PyObject *pyscene, *pycontext, *pypreferences, *pydata, *pymaterial;

  if (!PyArg_ParseTuple(
          args, "OOOOO", &pyscene, &pycontext, &pypreferences, &pydata, &pymaterial)) {
    return NULL;
  }

  PointerRNA sceneptr;
  RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pyscene), &sceneptr);
  BL::Scene b_scene(sceneptr);

  bContext *context = (bContext *)PyLong_AsVoidPtr(pycontext);

  PointerRNA preferencesptr;
  RNA_pointer_create(
      NULL, &RNA_Preferences, (void *)PyLong_AsVoidPtr(pypreferences), &preferencesptr);
  BL::Preferences preferences(preferencesptr);

  PointerRNA dataptr;
  RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
  BL::BlendData data(dataptr);

  PointerRNA matptr;
  RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pymaterial), &matptr);
  BL::Material material(matptr);

  Py_BEGIN_ALLOW_THREADS;
  BlenderSession::export_localdb(b_scene, context, preferences, data, material);
  Py_END_ALLOW_THREADS;
  Py_RETURN_NONE;
}

static PyObject *heart_beat_func(PyObject *self, PyObject *args)
{
  Py_RETURN_NONE;
}

static PyObject *get_octanedb_func(PyObject *self, PyObject *args)
{
  PyObject *pyscene = NULL, *pycontext = NULL;
  if (PyArg_ParseTuple(args, "OO", &pyscene, &pycontext)) {
    PointerRNA sceneptr;
    RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene b_scene(sceneptr);
    bContext *context = (bContext *)PyLong_AsVoidPtr(pycontext);
    Py_BEGIN_ALLOW_THREADS;
    BlenderSession::get_octanedb(context, G.octane_server_address);
    Py_END_ALLOW_THREADS;
  }
  Py_RETURN_NONE;
}

static PyObject *update_octane_localdb_func(PyObject *self, PyObject *args)
{
  PyObject *path;
  if (!PyArg_ParseTuple(args, "O", &path)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string cur_path = PyC_UnicodeAsByte(path, &path_coerce);
  Py_XDECREF(path_coerce);

  std::strcpy(G.octane_localdb_path, cur_path.c_str());
  Py_RETURN_NONE;
}

static PyObject *update_octane_texture_cache_func(PyObject *self, PyObject *args)
{
  PyObject *path;
  if (!PyArg_ParseTuple(args, "O", &path)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string cur_path = PyC_UnicodeAsByte(path, &path_coerce);
  Py_XDECREF(path_coerce);

  std::strcpy(G.octane_texture_cache_path, cur_path.c_str());
  Py_RETURN_NONE;
}

static PyObject *set_octane_params_func(PyObject *self, PyObject *args)
{
  int octane_default_mat_type = 0;
  if (PyArg_ParseTuple(args, "i", &octane_default_mat_type)) {
    G.octane_default_mat_type = octane_default_mat_type;
  }
  Py_RETURN_NONE;
}

static PyObject *update_octane_server_address_func(PyObject *self, PyObject *args)
{
  PyObject *address;
  int release_octane_license_after_exiting;
  if (!PyArg_ParseTuple(args, "Oi", &address, &release_octane_license_after_exiting)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string cur_addr = PyC_UnicodeAsByte(address, &path_coerce);
  Py_XDECREF(path_coerce);

  std::strcpy(G.octane_server_address, cur_addr.c_str());
  G.release_octane_license_after_exiting = release_octane_license_after_exiting;
  Py_RETURN_NONE;
}

static PyObject *activate_func(PyObject *self, PyObject *args)
{
  int activate;
  if (!PyArg_ParseTuple(args, "i", &activate)) {
    return PyBool_FromLong(0);
  }
  BlenderSession::activate_license(activate);
  Py_RETURN_NONE;
}

static PyObject *update_vdb_info_func(PyObject *self, PyObject *args)
{
  std::vector<std::string> float_grid_ids;
  std::vector<std::string> vector_grid_ids;
  PyObject *pydata, *pyscene, *pyobject;
  if (PyArg_ParseTuple(args, "OOO", &pyobject, &pydata, &pyscene)) {

    PointerRNA dataptr;
    RNA_main_pointer_create((Main *)PyLong_AsVoidPtr(pydata), &dataptr);
    BL::BlendData b_data(dataptr);

    PointerRNA sceneptr;
    RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pyscene), &sceneptr);
    BL::Scene b_scene(sceneptr);

    PointerRNA objectptr;
    RNA_id_pointer_create((ID *)PyLong_AsVoidPtr(pyobject), &objectptr);
    BL::Object b_object(objectptr);
    BL::ID b_ob_data = b_object.data();
    PointerRNA oct_mesh = RNA_pointer_get(&b_ob_data.ptr, "octane");

    Py_BEGIN_ALLOW_THREADS;
    BlenderSession::resolve_octane_vdb_info(
        G.octane_server_address, oct_mesh, b_data, b_scene, float_grid_ids, vector_grid_ids);
    Py_END_ALLOW_THREADS;
  }
  PyObject *rets = PyTuple_New(2);
  PyObject *float_grid_return_values = PyTuple_New(float_grid_ids.size());
  for (int i = 0; i < float_grid_ids.size(); ++i) {
    PyTuple_SET_ITEM(float_grid_return_values, i, PyUnicode_FromString(float_grid_ids[i].c_str()));
  }
  PyObject *vector_grid_return_values = PyTuple_New(vector_grid_ids.size());
  for (int i = 0; i < vector_grid_ids.size(); ++i) {
    PyTuple_SET_ITEM(
        vector_grid_return_values, i, PyUnicode_FromString(vector_grid_ids[i].c_str()));
  }
  PyTuple_SET_ITEM(rets, 0, float_grid_return_values);
  PyTuple_SET_ITEM(rets, 1, vector_grid_return_values);
  return rets;
}

static PyObject *update_ocio_info_func(PyObject *self, PyObject *args)
{
  std::vector<std::vector<std::string>> results;
  int use_other_config, use_automatic, intermediate_color_space_octane;
  PyObject *py_path, *py_intermediate_color_space_ocio_name;
  if (!PyArg_ParseTuple(args,
                        "OiiiO",
                        &py_path,
                        &use_other_config,
                        &use_automatic,
                        &intermediate_color_space_octane,
                        &py_intermediate_color_space_ocio_name)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string path = PyC_UnicodeAsByte(py_path, &path_coerce);
  std::string intermediate_color_space_ocio_name = PyC_UnicodeAsByte(
      py_intermediate_color_space_ocio_name, &path_coerce);
  Py_XDECREF(path_coerce);

  Py_BEGIN_ALLOW_THREADS;
  BlenderSession::resolve_octane_ocio_info(G.octane_server_address,
                                           path,
                                           use_other_config,
                                           use_automatic,
                                           intermediate_color_space_octane,
                                           intermediate_color_space_ocio_name,
                                           results);
  Py_END_ALLOW_THREADS;

  PyObject *rets = PyTuple_New(results.size());
  for (int i = 0; i < results.size(); ++i) {
    PyObject *ret = PyTuple_New(results[i].size());
    for (int j = 0; j < results[i].size(); ++j) {
      PyTuple_SET_ITEM(ret, j, PyUnicode_FromString(results[i][j].c_str()));
    }
    PyTuple_SET_ITEM(rets, i, ret);
  }
  return rets;
}

static PyObject *orbx_preview_func(PyObject *self, PyObject *args)
{
  PyObject *abc_path_obj, *orbx_path_obj;
  float fps;
  int release_octane_license_after_exiting;
  if (!PyArg_ParseTuple(args, "OOf", &orbx_path_obj, &abc_path_obj, &fps)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string orbx_path = PyC_UnicodeAsByte(orbx_path_obj, &path_coerce);
  std::string abc_path = PyC_UnicodeAsByte(abc_path_obj, &path_coerce);
  Py_XDECREF(path_coerce);

  Py_BEGIN_ALLOW_THREADS;
  BlenderSession::generate_orbx_proxy_preview(G.octane_server_address, orbx_path, abc_path, fps);
  Py_END_ALLOW_THREADS;

  Py_RETURN_NONE;
}

static PyObject *update_octane_custom_node(PyObject *self, PyObject *args)
{
  PyObject *py_command, *py_data;
  if (!PyArg_ParseTuple(args, "OO", &py_command, &py_data)) {
    return PyBool_FromLong(0);
  }

  PyObject *path_coerce = NULL;
  std::string command = PyC_UnicodeAsByte(py_command, &path_coerce);
  std::string data = PyC_UnicodeAsByte(py_data, &path_coerce);
  Py_XDECREF(path_coerce);

  std::string result_data;
  Py_BEGIN_ALLOW_THREADS;
  BlenderSession::update_octane_custom_node(G.octane_server_address, command, data, result_data);
  Py_END_ALLOW_THREADS;

  PyObject *ret = PyUnicode_FromString(result_data.c_str());
  return ret;
}

static PyObject *py_add_node_name(PyObject *self, PyObject *args)
{
  int32_t node_type;
  PyObject *py_node_name;
  if (!PyArg_ParseTuple(args, "iO", &node_type, &py_node_name)) {
    Py_RETURN_FALSE;
  }
  PyObject *py_coerce = NULL;
  std::string node_name = PyC_UnicodeAsByte(py_node_name, &py_coerce);
  Py_XDECREF(py_coerce);
  OctaneInfo::instance().add_node_name(node_type, node_name);
  Py_RETURN_TRUE;
}

static PyObject *py_set_static_pin_count(PyObject *self, PyObject *args)
{
  int32_t nodeType, pinCount;
  if (!PyArg_ParseTuple(args, "ii", &nodeType, &pinCount)) {
    Py_RETURN_FALSE;
  }
  OctaneInfo::instance().set_static_pin_count(nodeType, pinCount);
  Py_RETURN_TRUE;
}

static PyObject *py_add_attribute_info(PyObject *self, PyObject *args)
{
  int32_t nodeType, attributeId, attributeType;
  PyObject *pyBlenderName, *pyAttributeName;
  if (!PyArg_ParseTuple(args,
                        "iOiOi",
                        &nodeType,
                        &pyBlenderName,
                        &attributeId,
                        &pyAttributeName,
                        &attributeType)) {
    Py_RETURN_FALSE;
  }
  PyObject *pyCoerce = NULL;
  std::string blenderName = PyC_UnicodeAsByte(pyBlenderName, &pyCoerce);
  std::string attributeName = PyC_UnicodeAsByte(pyAttributeName, &pyCoerce);
  Py_XDECREF(pyCoerce);
  OctaneInfo::instance().add_attribute_info(
      nodeType, blenderName, attributeId, attributeName, attributeType);
  Py_RETURN_TRUE;
}

static PyObject *py_add_pin_info(PyObject *self, PyObject *args)
{
  int32_t nodeType, pinId, pinIndex, pinType, socketType, defaultNodeType;
  PyObject *pyBlenderName, *pyPinName, *pyDefaultNodeName;
  if (!PyArg_ParseTuple(args,
                        "iOiOiiiiO",
                        &nodeType,
                        &pyBlenderName,
                        &pinId,
                        &pyPinName,
                        &pinIndex,
                        &pinType,
                        &socketType,
                        &defaultNodeType,
                        &pyDefaultNodeName)) {
    Py_RETURN_FALSE;
  }
  PyObject *pyCoerce = NULL;
  std::string blenderName = PyC_UnicodeAsByte(pyBlenderName, &pyCoerce);
  std::string pinName = PyC_UnicodeAsByte(pyPinName, &pyCoerce);
  std::string defaultNodeName = PyC_UnicodeAsByte(pyDefaultNodeName, &pyCoerce);
  Py_XDECREF(pyCoerce);
  OctaneInfo::instance().add_pin_info(nodeType,
                                      blenderName,
                                      pinId,
                                      pinName,
                                      pinIndex,
                                      pinType,
                                      socketType,
                                      defaultNodeType,
                                      defaultNodeName);
  Py_RETURN_TRUE;
}

static PyObject *py_add_legacy_data_info(PyObject *self, PyObject *args)
{
  int32_t node_type, is_socket, data_type, is_pin, octane_type, is_internal_data,
      internal_data_is_pin, internal_data_octane_type;
  PyObject *py_name;
  if (!PyArg_ParseTuple(args,
                        "iOiiiiiii",
                        &node_type,
                        &py_name,
                        &is_socket,
                        &data_type,
                        &is_pin,
                        &octane_type,
                        &is_internal_data,
                        &internal_data_is_pin,
                        &internal_data_octane_type)) {
    Py_RETURN_FALSE;
  }
  PyObject *pyCoerce = NULL;
  std::string name = PyC_UnicodeAsByte(py_name, &pyCoerce);
  Py_XDECREF(pyCoerce);
  OctaneInfo::instance().add_legacy_data_info(node_type,
                                              name,
                                              is_socket,
                                              data_type,
                                              is_pin,
                                              octane_type,
                                              is_internal_data,
                                              internal_data_is_pin,
                                              internal_data_octane_type);
  Py_RETURN_TRUE;
}

static PyObject *py_start_utils_client(PyObject *self, PyObject *args)
{
  PyObject *py_client_name;
  if (!PyArg_ParseTuple(args, "O", &py_client_name)) {
    Py_RETURN_FALSE;
  }
  PyObject *py_coerce = NULL;
  std::string client_name = PyC_UnicodeAsByte(py_client_name, &py_coerce);
  Py_XDECREF(py_coerce);
  bool result = OctaneClientManager::instance().start_utils_client(client_name);
  Py_RETURN_TRUE;
}

static PyObject *py_stop_utils_client(PyObject *self, PyObject *args)
{
  PyObject *py_client_name;
  if (!PyArg_ParseTuple(args, "O", &py_client_name)) {
    Py_RETURN_FALSE;
  }
  PyObject *py_coerce = NULL;
  std::string client_name = PyC_UnicodeAsByte(py_client_name, &py_coerce);
  Py_XDECREF(py_coerce);
  bool result = OctaneClientManager::instance().stop_utils_client(client_name);
  Py_RETURN_TRUE;
}

static PyObject *py_utils_function(PyObject *self, PyObject *args)
{
  std::string result_data;
  int32_t command_type;
  PyObject *py_client_name, *py_command_data;
  if (!PyArg_ParseTuple(args, "iOO", &command_type, &py_command_data, &py_client_name)) {
    Py_RETURN_FALSE;
  }
  PyObject *py_coerce = NULL;
  std::string command_data = PyC_UnicodeAsByte(py_command_data, &py_coerce);
  std::string client_name = PyC_UnicodeAsByte(py_client_name, &py_coerce);
  Py_XDECREF(py_coerce);
  result_data = OctaneClientManager::instance().utils_function(
      command_type, command_data, client_name);
  PyObject *ret = PyUnicode_FromString(result_data.c_str());
  return ret;
}

static PyObject *py_copy_color_ramp(PyObject *self, PyObject *args)
{
  size_t from_addr, to_addr;
  if (!PyArg_ParseTuple(args, "LL", &from_addr, &to_addr)) {
    Py_RETURN_FALSE;
  }
  ColorBand *from_color_band = reinterpret_cast<ColorBand *>(from_addr);
  ColorBand *to_color_band = reinterpret_cast<ColorBand *>(to_addr);
  for (int32_t i = 0; i < 32; ++i) {
    to_color_band->data[i].r = from_color_band->data[i].r;
    to_color_band->data[i].g = from_color_band->data[i].g;
    to_color_band->data[i].b = from_color_band->data[i].b;
    to_color_band->data[i].a = from_color_band->data[i].a;
    to_color_band->data[i].pos = from_color_band->data[i].pos;
    to_color_band->data[i].cur = from_color_band->data[i].cur;
  }
  to_color_band->tot = from_color_band->tot;
  to_color_band->cur = from_color_band->cur;
  to_color_band->ipotype = from_color_band->ipotype;
  to_color_band->ipotype_hue = from_color_band->ipotype_hue;
  to_color_band->color_mode = from_color_band->color_mode;
  Py_RETURN_TRUE;
}

static PyMethodDef methods[] = {
    {"init", py_init_func, METH_VARARGS, ""},
    {"exit", py_exit_func, METH_VARARGS, ""},
    {"is_shared_surface_supported", py_is_shared_surface_supported, METH_VARARGS, ""},
    {"create", create_func, METH_VARARGS, ""},
    {"free", free_func, METH_O, ""},
    {"render", render_func, METH_VARARGS, ""},
    //{"bake", bake_func, METH_VARARGS, ""},
    {"draw", draw_func, METH_VARARGS, ""},
    {"sync", sync_func, METH_VARARGS, ""},
    {"reset", reset_func, METH_VARARGS, ""},
    {"update_octane_localdb", update_octane_localdb_func, METH_VARARGS, ""},
    {"update_octane_texture_cache", update_octane_texture_cache_func, METH_VARARGS, ""},
    {"update_octane_server_address", update_octane_server_address_func, METH_VARARGS, ""},
    {"activate", activate_func, METH_VARARGS, ""},
    {"command_to_octane", command_to_octane_func, METH_VARARGS, ""},
    {"osl_compile", osl_compile_func, METH_VARARGS, ""},
    {"osl_update_node", osl_update_node_func, METH_VARARGS, ""},
    {"export", export_func, METH_VARARGS, ""},
    {"export_localdb", export_localdb_func, METH_VARARGS, ""},
    {"heart_beat", heart_beat_func, METH_VARARGS, ""},
    {"get_octanedb", get_octanedb_func, METH_VARARGS, ""},
    {"set_octane_params", set_octane_params_func, METH_VARARGS, ""},
    {"update_vdb_info", update_vdb_info_func, METH_VARARGS, ""},
    {"orbx_preview", orbx_preview_func, METH_VARARGS, ""},
    {"update_ocio_info", update_ocio_info_func, METH_VARARGS, ""},
    {"update_octane_custom_node", update_octane_custom_node, METH_VARARGS, ""},
    {"add_node_name", py_add_node_name, METH_VARARGS, ""},
    {"set_static_pin_count", py_set_static_pin_count, METH_VARARGS, ""},
    {"add_attribute_info", py_add_attribute_info, METH_VARARGS, ""},
    {"add_pin_info", py_add_pin_info, METH_VARARGS, ""},
    {"add_legacy_data_info", py_add_legacy_data_info, METH_VARARGS, ""},
    {"start_utils_client", py_start_utils_client, METH_VARARGS, ""},
    {"stop_utils_client", py_stop_utils_client, METH_VARARGS, ""},
    {"utils_function", py_utils_function, METH_VARARGS, ""},
    {"copy_color_ramp", py_copy_color_ramp, METH_VARARGS, ""},
    {NULL, NULL, 0, NULL},
};

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
//
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
static struct PyModuleDef module = {
    PyModuleDef_HEAD_INIT, "_octane", "OctaneBlender", -1, methods, NULL, NULL, NULL, NULL};

OCT_NAMESPACE_END

void *OCT_python_module_init()
{
  PyObject *mod = PyModule_Create(&oct::module);
  return (void *)mod;
}

void OCT_Rlease_API()
{
  if (G.release_octane_license_after_exiting) {
    oct::BlenderSession::activate_license(false);
  }
}

void OCT_get_octanedb(void *C)
{
  oct::BlenderSession::get_octanedb((bContext *)C, G.octane_server_address);
}