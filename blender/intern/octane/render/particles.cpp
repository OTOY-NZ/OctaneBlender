/*
 * Copyright 2011-2013 Blender Foundation
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

#include "render/particles.h"
#include "render/scene.h"

OCT_NAMESPACE_BEGIN

/* Particle System */

ParticleSystem::ParticleSystem()
{
}

ParticleSystem::~ParticleSystem()
{
}

void ParticleSystem::tag_update(Scene *scene)
{
  scene->particle_system_manager->need_update = true;
}

/* Particle System Manager */

ParticleSystemManager::ParticleSystemManager()
{
  need_update = true;
}

ParticleSystemManager::~ParticleSystemManager()
{
}

void ParticleSystemManager::tag_update(Scene * /*scene*/)
{
  need_update = true;
}

OCT_NAMESPACE_END
