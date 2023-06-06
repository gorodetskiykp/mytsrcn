from django import template
from app.models import Menu

register = template.Library()


@register.simple_tag
def main_menu(filter=None):
    return Menu.objects.filter(parent=filter)
