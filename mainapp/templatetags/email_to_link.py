from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def email_to_link(value):
    return mark_safe(f'<a href="mailto:{value}">{value}</a>')


@register.filter
def phone_to_link(value):
    return mark_safe(f'<a href="tel:{value}">{value}</a>')


# <a href="tel:+79070700777" class="phone_list_link">+7-907-070-0777</a>
