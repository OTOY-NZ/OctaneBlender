# <pep8 compliant>
from bpy.types import Panel
from bpy.utils import register_class, unregister_class

from octane.uis.common import OctanePropertyPanel


class OCTANE_PARTICLE_PT_hair_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Hair Properties"
    bl_context = "particle"

    @classmethod
    def poll(cls, context):
        psys = context.particle_system
        return super().poll(context) and psys and psys.settings.type == 'HAIR'

    def draw(self, context):
        layout = self.layout
        psys = context.particle_settings
        psys_octane = psys.octane
        row = layout.row()
        row.prop(psys_octane, "min_curvature")
        layout.label(text="Thickness:")
        row = layout.row(align=True)
        row.prop(psys_octane, "root_width")
        row.prop(psys_octane, "tip_width")
        layout.label(text="W Coordinate:")
        row = layout.row(align=True)
        row.prop(psys_octane, "w_min")
        row.prop(psys_octane, "w_max")


class OCTANE_PARTICLE_PT_sphere_primitive_properties(OctanePropertyPanel, Panel):
    bl_label = "Octane Sphere Primitive Properties"
    bl_context = "particle"
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        psys = context.particle_system
        engine = context.engine
        if psys is None:
            return False
        return engine == "octane"

    def draw(self, context):
        layout = self.layout

        psys = context.particle_system
        particle_settings = context.particle_settings

        is_active = psys.settings.type != 'HAIR' and (psys.settings.render_type != 'OBJECT'
                                                      and psys.settings.render_type != 'COLLECTION')

        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "use_as_octane_sphere_primitive")
        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "octane_velocity_multiplier")
        row = layout.row()
        row.active = is_active
        row.prop(particle_settings, "octane_sphere_size_multiplier")


_CLASSES = [
    OCTANE_PARTICLE_PT_hair_properties,
    OCTANE_PARTICLE_PT_sphere_primitive_properties
]


def register():
    for cls in _CLASSES:
        register_class(cls)


def unregister():
    for cls in _CLASSES:
        unregister_class(cls)
