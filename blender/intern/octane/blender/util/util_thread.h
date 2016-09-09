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

#ifndef __UTIL_THREAD_H__
#define __UTIL_THREAD_H__

#ifdef WIN32
#   ifdef _DEBUG
#       pragma pack(push,_CRT_PACKING)
#       pragma push_macro("new")
#       undef new
#   endif
#endif

#if (__cplusplus > 199711L) || (defined(_MSC_VER) && _MSC_VER >= 1800)
#   include <thread>
#   include <mutex>
#   include <condition_variable>
#   include <functional>
#else
#   include <boost/thread.hpp>
#endif

#if (__cplusplus > 199711L) || (defined(_MSC_VER) && _MSC_VER >= 1800)
#   include <functional>
#else
#   include <boost/bind.hpp>
#   include <boost/function.hpp>
#endif

#ifdef WIN32
#   ifdef _DEBUG
#       pragma pop_macro("new")
#       pragma pack(pop)
#   endif
#endif

#include <pthread.h>
#include <queue>

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

#if (__cplusplus > 199711L) || (defined(_MSC_VER) && _MSC_VER >= 1800)
#   define function_bind std::bind
#   define function_null nullptr
    using std::function;
    using std::placeholders::_1;
    using std::placeholders::_2;
    using std::placeholders::_3;
    using std::placeholders::_4;
    using std::placeholders::_5;
    using std::placeholders::_6;
    using std::placeholders::_7;
    using std::placeholders::_8;
    using std::placeholders::_9;
#else
    using boost::function;
#   define function_bind boost::bind
#   define function_null NULL
#endif

#if (__cplusplus > 199711L) || (defined(_MSC_VER) && _MSC_VER >= 1800)
    typedef std::mutex thread_mutex;
    typedef std::unique_lock<std::mutex> thread_scoped_lock;
    typedef std::condition_variable thread_condition_variable;
#else
    /* use boost for mutexes */
    typedef boost::mutex thread_mutex;
    typedef boost::mutex::scoped_lock thread_scoped_lock;
    typedef boost::condition_variable thread_condition_variable;
#endif

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Own pthread based implementation, to avoid boost version conflicts with
// dynamically loaded blender plugins */
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class thread {
public:
	thread(function<void(void)> run_cb_) {
		joined = false;
		run_cb = run_cb_;

		pthread_create(&pthread_id, NULL, run, (void*)this);
	}

	~thread() {
		if(!joined) join();
	}

	static void *run(void *arg) {
		((thread*)arg)->run_cb();
		return NULL;
	}

	bool join() {
		return pthread_join(pthread_id, NULL) == 0;
	}

protected:
	function<void(void)>	    run_cb;
	pthread_t					pthread_id;
	bool						joined;
}; //thread

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Thread Local Storage
// Boost implementation is a bit slow, and Mac OS X __thread is not supported
// but the pthreads implementation is optimized, so we use these macros. */
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#ifdef __APPLE__
#   define tls_ptr(type, name) \
	    pthread_key_t name
#   define tls_set(name, value) \
	    pthread_setspecific(name, value)
#   define tls_get(type, name) \
	    ((type*)pthread_getspecific(name))
#   define tls_create(type, name) \
	    pthread_key_create(&name, NULL)
#   define tls_delete(type, name) \
	    pthread_key_delete(name);
#else
#   ifdef __WIN32
#       define __thread __declspec(thread)
#   endif

#   define tls_ptr(type, name)      __thread type *name
#   define tls_set(name, value)     name = value
#   define tls_get(type, name)      name
#   define tls_create(type, name)
#   define tls_delete(type, name)
#endif

OCT_NAMESPACE_END

#endif /* __UTIL_THREAD_H__ */

