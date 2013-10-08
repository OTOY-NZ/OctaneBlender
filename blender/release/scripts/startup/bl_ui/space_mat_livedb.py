# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# <pep8 compliant>
import bpy
from bpy.types import Header, Menu


class MAT_LIVEDB_HT_header(Header):
    bl_space_type = 'MAT_LIVEDB'

    def draw(self, context):
        layout = self.layout

        space = context.space_data
        scene = context.scene
        mat = context.scene.objects.active.active_material

        row = layout.row(align=True)
        row.template_header()

        if context.area.show_menus:
            sub = row.row(align=True)
            sub.menu("MAT_LIVEDB_MT_view")
            sub.menu("MAT_LIVEDB_MT_search")

        layout.prop(space, "filter_text", icon='VIEWZOOM', text="")

        if mat:
            layout.separator()
            row = layout.row(align=False)
            row.label(text=mat.name, icon='MATERIAL')

        layout.separator()
        layout.prop(space, "server_address", icon='WORLD', text="")


class MAT_LIVEDB_MT_view(Menu):
    bl_label = "View"

    def draw(self, context):
        layout = self.layout

        space = context.space_data

#        if space.display_mode not in {'DATABLOCKS', 'USER_PREFERENCES', 'KEYMAPS'}:
#            layout.prop(space, "show_restrict_columns")
#            layout.separator()
#            layout.operator("mat_livedb.show_active")

        layout.operator("mat_livedb.show_one_level")
        layout.operator("mat_livedb.hide_one_level")

        layout.separator()

        layout.operator("screen.area_dupli")
        layout.operator("screen.screen_full_area")


class MAT_LIVEDB_MT_search(Menu):
    bl_label = "Search"

    def draw(self, context):
        layout = self.layout

        space = context.space_data

        layout.prop(space, "use_filter_case_sensitive")
        layout.prop(space, "use_filter_complete")


class MAT_LIVEDB_MT_edit_datablocks(Menu):
    bl_label = "Edit"

    def draw(self, context):
        layout = self.layout

        layout.operator("mat_livedb.keyingset_add_selected")
        layout.operator("mat_livedb.keyingset_remove_selected")

        layout.separator()

        layout.operator("mat_livedb.drivers_add_selected")
        layout.operator("mat_livedb.drivers_delete_selected")

if __name__ == "__main__":  # only for live edit.
    bpy.utils.register_module(__name__)
