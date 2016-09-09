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

#ifndef __KERNEL_H__
#define __KERNEL_H__

#include "util_types.h"

#include "memleaks_check.h"
#include "OctaneClient.h"

OCT_NAMESPACE_BEGIN

class Scene;

class Kernel {
public:
	Kernel();
	~Kernel();

    inline Kernel(Kernel &other) {
        oct_node = new ::OctaneEngine::Kernel;
        *oct_node = *other.oct_node;

        uiGPUs = other.uiGPUs;
        need_update = other.need_update;
        need_update_GPUs = other.need_update_GPUs;
    }
    inline Kernel(Kernel &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;

        uiGPUs = other.uiGPUs;
        need_update = other.need_update;
        need_update_GPUs = other.need_update_GPUs;
    }

    inline Kernel& operator=(Kernel &other) {
        *oct_node = *other.oct_node;

        uiGPUs = other.uiGPUs;
        need_update = other.need_update;
        need_update_GPUs = other.need_update_GPUs;
        return *this;
    }
    inline Kernel& operator=(Kernel &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;

        uiGPUs = other.uiGPUs;
        need_update = other.need_update;
        need_update_GPUs = other.need_update_GPUs;
        return *this;
    }

	void server_update(::OctaneEngine::OctaneClient *server, Scene *scene, bool interactive);

	bool modified(const Kernel& kernel);
	void tag_update(void);
	void tag_updateGPUs(void);

    ::OctaneEngine::Kernel *oct_node;

    uint32_t    uiGPUs;

	bool        need_update;
	bool        need_update_GPUs;
}; //Kernel

OCT_NAMESPACE_END

#endif /* __KERNEL_H__ */

