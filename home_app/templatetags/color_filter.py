from django import template 
register=template.Library()


@register.filter
def CheckList(value,lists):
    lists=[int(i) for i in lists]
    if value in lists:
       return True 
    else:
       return False

