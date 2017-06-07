from django import template

register = template.Library()

# You can also register those functions using decorators
# since I am passing a function in what is a function call
@register.filter(name='cut')
def cut(value, arg):
    """
        This cuts all of values of "arg" from the string!
    """
    return value.replace(arg,'')

# register.filter('cut', # Aliasing the functiont cut as "cut"
#                 cut)   # The function itselft that I want to pass
