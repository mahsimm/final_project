from django import template
from accounts.enums import RoleCodes

register = template.Library()

@register.simple_tag
def is_admin(user):
    return user.is_admin()


@register.simple_tag
def is_normal(user):
    return user.is_normal()
