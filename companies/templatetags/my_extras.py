from django import template
from datetime import datetime
register =  template.Library()

@register.filter(name = 'parsedata')
def parsedata(value):
    if value==None:
        return ''
    return value
#register.filter('cuting',cut)

@register.filter(name = 'parsedate')
def parsedate(value):
    if value==None:
        return ''
    return value.strftime("%d/%m/%Y")
