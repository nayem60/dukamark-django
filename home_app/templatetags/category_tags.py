from django import template
from category.models import Category
register=template.Library()



@register.filter
def category(request):
    if request:
       category=Category.objects.all().prefetch_related('subcategorys')
       return category
    else:
      return ""
    
    