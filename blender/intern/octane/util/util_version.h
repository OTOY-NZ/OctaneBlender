/*
 * Copyright 2011-2016 Blender Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __UTIL_VERSION_H__
#define __UTIL_VERSION_H__

/* Octane version number */

OCT_NAMESPACE_BEGIN

#define OCTANE_VERSION_MAJOR 20
#define OCTANE_VERSION_MINOR 0

#define OCTANE_MAKE_VERSION_STRING2(a, b) #a "." #b
#define OCTANE_MAKE_VERSION_STRING(a, b) OCTANE_MAKE_VERSION_STRING2(a, b)
#define OCTANE_VERSION_STRING \
  OCTANE_MAKE_VERSION_STRING(OCTANE_VERSION_MAJOR, OCTANE_VERSION_MINOR)

OCT_NAMESPACE_END

#endif /* __UTIL_VERSION_H__ */
