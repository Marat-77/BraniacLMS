from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def email_to_link(value):
    return mark_safe(f'<a href="mailto:{value}">{value}</a>')


@register.filter
def phone_to_link(value):
    value2 = f'{value[:2]}-{value[2:5]}-{value[5:8]}-{value[8:]}'
    return mark_safe(f'<a href="tel:{value}">{value2}</a>')
