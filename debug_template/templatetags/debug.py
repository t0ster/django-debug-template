from ipdb import set_trace
from django import template

register = template.Library()


@register.filter
def ipdb(element):
    set_trace()
    return element


@register.simple_tag(takes_context=True)
def ipdb_tag(context):
    set_trace()
