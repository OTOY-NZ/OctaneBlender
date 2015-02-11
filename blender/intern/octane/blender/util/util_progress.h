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

#ifndef __UTIL_PROGRESS_H__
#define __UTIL_PROGRESS_H__

/* Progress
 *
 * Simple class to communicate progress status messages, timing information,
 * update notifications from a job running in another thread. All methods
 * except for the constructor/destructor are thread safe. */

#include "util_string.h"
#include "util_time.h"
#include "util_thread.h"

#include "memleaks_check.h"

OCT_NAMESPACE_BEGIN

class BlenderSession;

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
// Progress class
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class Progress {
public:
	Progress();
	Progress(Progress& progress);

	Progress& operator=(Progress& progress);

	// Cancel
	void    set_cancel(const string& cancel_message_);
	bool    get_cancel();
	string  get_cancel_message();

	void set_start_time(double start_time_);
    void refresh_cur_info();
	void get_time(double& total_time_);
	void reset_cur_samples();
	void set_cur_samples(unsigned long cur_samples_);
	int  get_cur_samples();

	// Status messages
	void set_status(const string& status_, const string& substatus_ = "");
	void set_substatus(const string& substatus_);
	void set_sync_status(const string& status_, const string& substatus_ = "");
	void set_sync_substatus(const string& substatus_);
	void get_status(string& status_, string& substatus_);

	void set_update();
	void set_blender_session(BlenderSession* const session);

protected:
	thread_mutex    progress_mutex;
	thread_mutex    update_mutex;
    BlenderSession* blender_session;

	int cur_samples;

	double start_time;
	double total_time;

	string status;
	string substatus;

	string sync_status;
	string sync_substatus;

	volatile bool cancel;
	string cancel_message;
}; //Progress

OCT_NAMESPACE_END

#endif /* __UTIL_PROGRESS_H__ */

