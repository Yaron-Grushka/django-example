from django import template

register = template.Library()

@register.filter(name='cutting')
def cutting(value,arg):
    """
    doc...
    """
    return value.replace(arg,'')

# register.filter('cutting',cutting)
