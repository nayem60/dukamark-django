from django import template
from category.models import Brand
register=template.Library()




@register.filter
def brand(subcategoryId):
    brand=Brand.objects.select_related('subcategory').filter(subcategory__id=subcategoryId)
    for i in brand:
        if brand:
           return brand 
        else:
           return ""

    