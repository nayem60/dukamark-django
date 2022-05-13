from cart.models import Cart
from coupon.models import Coupon
from django.utils import timezone
from .serializer import CouponSerializer
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
def CartPage(request):
    carts=Cart.objects.filter(user=request.user)
    cart_count=carts.count()
    totals=0
    for i in carts:
        if i.variant:
           totals+=float(i.variant_price_total())
        else:
           totals+=float(i.get_total())
   
    return {
        'cart':carts,
        'cart_count':cart_count,
        'totals':totals,
    }
     