from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from cart.models import Cart
from product.models import Product
from variant.models import Variants
from coupon.models import Coupon
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def Addcart(request,pk):
    url=request.META.get('HTTP_REFERER')
    product=get_object_or_404(Product,pk=pk)
    variantId=request.POST.get('variant')
    quantity=request.POST.get('quantity')
    check_variant=Variants.objects.filter(product=product)
    cart_variant=None
    if check_variant:
       cart_variant=Cart.objects.filter(user=request.user,variant=variantId)
       if cart_variant:
          control=1
       else:
         control=0
    else:
      cart_product=Cart.objects.filter(user=request.user,product=product)
      if cart_product:
         control=1
      else:
         control=0
    if request.method =="post" or request.method=="POST":
       if control==1:
          if cart_variant is None or cart_variant == 0:
             data=Cart.objects.get(user=request.user, product=product)
          else:
              data=Cart.objects.get(user=request.user, variant=variantId)
          data.quantity+=int(quantity)
          data.save()
       else:
           carts=Cart()
           carts.user=request.user
           carts.product=product
           carts.quantity +=int(quantity)
           carts.variant_id=variantId
           carts.save()
       return HttpResponse("add success")
    else:
       if control==1:
          cart=Cart.objects.get(user=request.user, product=product,variant=None)
          cart.quantity+=1
          cart.save()
          return HttpResponse('single quantity update')
       else:
          carts=Cart()
          carts.user=request.user
          carts.product=product
          carts.quantity +=1
          carts.variant_id=None
          carts.save()
       return HttpResponse(" single product add")
       
     
     
     
     
def CartPage(request):
    discount=0
    subtotal=0
    coupon={}
    carts=Cart.objects.filter(user=request.user).select_related('product','variant')
    coupon_code=request.GET.get('code')
    totals=0
    for i in carts:
        if i.variant:
           totals+=float(i.variant_price_total())
        else:
           totals+=float(i.get_total())
    check=Coupon.objects.filter(name=coupon_code,cart_value__lte=totals,exfail_date__gte=timezone.now()).first()
    if check:
       coupon['coupon']={
           'name':check.name,
           'type':check.coupon_type,
           'value':check.coupon_valu,
           'cart_value':check.cart_value,
       }
       request.session['coupon_data']=coupon
    else:
      print("========",'Coupon Not Found')
      print("========", request.session['coupon_data']['coupon']['type'])
      
       
    if 'coupon_data' in request.session:
       if request.session['coupon_data']['coupon']['type'] == 'fixed':
          discount=request.session['coupon_data']['coupon']['value']
       else:
          discount=totals*request.session['coupon_data']['coupon']['value']/100
       subtotal=totals-discount
     
    else:
       print ('=======','Not Found Cupon Session')
       
    context={
        'cart':carts,
        'totals':totals,
        'subtotal':subtotal,
        'discount':discount,
    }
    return render(request,'shopping_cart.py',context)
     
     
     
     
     
     
     
     
def Increment(request,pk):     
    check=Cart.objects.filter(user=request.user,id=pk)
    if check.exists():
       cart=check[0]
       if cart.quantity>=1:
          cart.quantity +=1
          cart.save()
       else:
          cart.delete()
       return HttpResponse('Increment Successful')
       
       
     
def Remove(request,pk):     
    if request.method=="post" or request.method=="POST":
       cart=get_object_or_404(Cart,pk=pk)
       Cart.objects.get(user=request.user,id=cart.id).delete()
       return HttpResponse('deleted')
       
    return HttpResponseRedirect('home')
    
 
     
     
     
       