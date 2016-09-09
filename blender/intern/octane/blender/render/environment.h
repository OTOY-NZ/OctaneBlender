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

#ifndef __ENVIRONMENT_H__
#define __ENVIRONMENT_H__

#include "util_types.h"
#include "util_string.h"

#include "memleaks_check.h"
#include "OctaneClient.h"

OCT_NAMESPACE_BEGIN

class Scene;

class Environment {
public:
	Environment();
	~Environment();

    inline Environment(Environment &other) {
        oct_node = new ::OctaneEngine::Environment;
        *oct_node = *other.oct_node;
        oct_vis_node = new ::OctaneEngine::Environment;
        *oct_vis_node = *other.oct_vis_node;

        use_vis_environment = other.use_vis_environment;
        use_background = other.use_background;
        transparent = other.transparent;
        need_update = other.need_update;
    }
    inline Environment(Environment &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;
        delete oct_vis_node;
        oct_vis_node = other.oct_vis_node;
        other.oct_vis_node = 0;

        use_vis_environment = other.use_vis_environment;
        use_background = other.use_background;
        transparent = other.transparent;
        need_update = other.need_update;
    }

    inline Environment& operator=(Environment &other) {
        *oct_node = *other.oct_node;
        *oct_vis_node = *other.oct_vis_node;

        use_vis_environment = other.use_vis_environment;
        use_background = other.use_background;
        transparent = other.transparent;
        need_update = other.need_update;
        return *this;
    }
    inline Environment& operator=(Environment &&other) {
        delete oct_node;
        oct_node = other.oct_node;
        other.oct_node = 0;
        delete oct_vis_node;
        oct_vis_node = other.oct_vis_node;
        other.oct_vis_node = 0;

        use_vis_environment = other.use_vis_environment;
        use_background = other.use_background;
        transparent = other.transparent;
        need_update = other.need_update;
        return *this;
    }

    void server_update(::OctaneEngine::OctaneClient *server, Scene *scene);

	bool modified(const Environment& background);
	void tag_update(Scene *scene);

    ::OctaneEngine::Environment *oct_node, *oct_vis_node;
    bool    use_vis_environment;

	bool    use_background;
	bool    transparent;
	bool    need_update;
}; //Environment

OCT_NAMESPACE_END

#endif /* __ENVIRONMENT_H__ */

