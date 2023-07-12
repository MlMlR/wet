from django import template
import random

register = template.Library()

@register.filter
def times(value, arg):
    return value * arg

@register.filter
def get_random_bright_color(value):
    return '#%06X' % (random.randint(0, 0xFFFFFF) | 0x808080)