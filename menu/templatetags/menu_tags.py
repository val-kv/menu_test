from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    items = MenuItem.objects.filter(menu_name=menu_name)

    def get_children(parent):
        return MenuItem.objects.filter(parent=parent)

    def render_menu(items, parent=None):
        result = '<ul>'
        for item in items.filter(parent=parent):
            result += '<li>'
            result += f'<a href="{item.url}">{item.title}</a>'
            children = get_children(item)
            if children.exists():
                result += render_menu(children, parent=item)
            result += '</li>'
        result += '</ul>'
        return result

    return render_menu(items, parent=None)
