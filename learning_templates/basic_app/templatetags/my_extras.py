from django import template

register = template.Library()

@register.filter(name='cuti')
def cuti(value,arg):

	return value.replace(arg,'')

	