from django import template
from variant.models import *
register=template.Library()


@register.filter(name="variant")
def ColorVariant(productId):
    color_variant=Variants.objects.filter(product__id=productId)
    for i in color_variant:
       if i.color:
          return True
       else:
          return False


@register.filter(name="size")
def SizeVariant(productId):
    size_variant=Variants.objects.filter(product__id=productId)
    for i in size_variant:
        if i.size:
           return True
        else:
           return False

@register.filter(name="ram")
def RamVariant(productId):
    ram_variant=Variants.objects.filter(product__id=productId)
    for i in ram_variant:
       if i.ram:
          return True
       else:
          return False

