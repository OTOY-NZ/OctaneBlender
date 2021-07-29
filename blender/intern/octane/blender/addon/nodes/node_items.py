import bpy
from bpy.props import IntProperty, StringProperty
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem, NodeItemCustom
from ..utils import consts


class OctaneNodeItemSeperator(object):
    def __init__(self, label, icon="TEXTURE"):
        self.label = label
        self.icon = icon

    @classmethod
    def poll(cls, context):
        return True

    @staticmethod
    def draw(self, layout, context):
        layout.label(text=self.label, icon=self.icon)


def register_octane_node_categories(identifier, cat_list):
    _node_categories = nodeitems_utils._node_categories
    if identifier in _node_categories:
        raise KeyError("Node categories list '%s' already registered" % identifier)
        return

    # works as draw function for menus
    def draw_node_item(self, context):
        layout = self.layout
        col = layout.column()
        for item in self.category.items(context):
            if isinstance(item, NodeCategory):
                layout.menu("NODE_MT_category_%s" % item.identifier)
            else:
                item.draw(item, col, context)

    def draw_add_menu(self, context):
        layout = self.layout

        for cat in cat_list:
            if cat.poll(context):
                layout.menu("NODE_MT_category_%s" % cat.identifier)

    def register_octane_node_category(menu_types, cat):
        menu_type = type("NODE_MT_category_" + cat.identifier, (bpy.types.Menu,), {
            "bl_space_type": 'NODE_EDITOR',
            "bl_label": cat.name,
            "category": cat,
            "poll": cat.poll,
            "draw": draw_node_item,
        })
        menu_types.append(menu_type)
        bpy.utils.register_class(menu_type)


    def register_submenu(menu_types, sub_cat_list, cat):
        if not isinstance(cat, NodeCategory):
            return
        sub_cat_list.append(cat)
        register_octane_node_category(menu_types, cat)
        for item in cat.items(None):
            register_submenu(menu_types, sub_cat_list, item)

    menu_types = []
    sub_cat_list = []
    for cat in cat_list:
        register_submenu(menu_types, sub_cat_list, cat)

    # stores: (categories list, menu draw function, submenu types)
    final_cat_list = cat_list + sub_cat_list
    _node_categories[identifier] = (final_cat_list, draw_add_menu, menu_types)


def unregister_node_cat_types(cats):
    for mt in cats[2]:
        bpy.utils.unregister_class(mt)


def unregister_octane_node_categories(identifier=None):
    _node_categories = nodeitems_utils._node_categories
    # unregister existing UI classes
    if identifier:
        cat_types = _node_categories.get(identifier, None)
        if cat_types:
            unregister_node_cat_types(cat_types)
        del _node_categories[identifier]

    else:
        for cat_types in _node_categories.values():
            unregister_node_cat_types(cat_types)
        _node_categories.clear()


def register():
    pass


def unregister():
    pass