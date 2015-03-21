from django import template

register = template.Library()

@register.simple_tag(name="next_modulo")
def next_modulo(num, val):
        return (int(num) + 1) % int(val)

@register.simple_tag(name="modulo")
def modulo(num, val):
    return int(num) % int(val)

@register.simple_tag(name="quotient")
def next_quotient(num, val):
    return int(num) / int(val)

@register.simple_tag(name="next_quotient")
def next_quotient(num, val):
    return (int(num) + 1) / int(val)

@register.simple_tag(name="prev_quotient")
def prev_quotient(num, val):
    return (int(num) - 1) / int(val)

@register.simple_tag(name="prev_modulo")
def prev_modulo(num, val):
    return (int(num) + val - 1) % int(val)
