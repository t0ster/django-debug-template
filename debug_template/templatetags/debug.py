from django import template

register = template.Library()


@register.filter
def ipdb(element):
    import ipdb
    ipdb.set_trace()
    return element
