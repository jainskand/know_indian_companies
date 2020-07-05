from django import template

register =  template.Library()

@register.filter(name = 'parsedate')
def cut(value):
    print(value,type(value))
    d = str(value).split(' ')
    return ''.join(d)

#register.filter('cuting',cut)
