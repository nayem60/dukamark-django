from django import template
from cart.models import Cart
register=template.Library()

@register.filter
def cart_items(user):
    if user.is_authenticated:
       carts=Cart.objects.filter(user=user)
       return carts
    else:
      return ""
      
      
      
@register.filter
def cart_count(user):
    if user.is_authenticated:
       carts=Cart.objects.filter(user=user).count()
       return carts
    else:
       return "0"
       

@register.filter
def cart_totals(user):
    if user.is_authenticated:
       carts=Cart.objects.filter(user=user)
       total=0
       for i in carts:
          if i.variant:
             total+=float(i.variant_price_total())
          else:
             total+=float(i.get_total())
       return total
    else:
       return "0"
       
       
def add_cart(id):
    pass
    #Cart.objects.filter()
    
