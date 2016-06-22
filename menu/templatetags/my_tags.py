from django import template
from menu.models import *

register = template.Library()


# @register.assignment_tag(takes_context=False)
# def load_menus(name):
#      try:
#          return Menu.objects.get_by_natural_key(name)
#      except Menu.DoesNotExist:
#          logger.critical("No such navigation menu %s", name)

@register.assignment_tag(takes_context=False)
def load_menus(menu_name):
    menu = Menu.objects.filter(menu_name=menu_name)

    if menu:
        return menu[0].menu_items.all()
    else:
        return None