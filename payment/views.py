from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.http import HttpResponse,HttpResponseRedirect
from django.utils.crypto import get_random_string
from .models import *
from  cart.models import Cart
import json
from django.conf import settings
from sslcommerz_python.payment import SSLCSession
from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt

# Create your views here.



class Checkout (TemplateView):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
           payment=request.GET.get('payment')
           context={
               'payment':payment,
           }
           return render(request,'checkout.py',context)
        else:
           return HttpResponse('please Login')
    def post(self, request,*args,**kwargs):
        ship_different=request.POST.get("ship_different")
 
        if ship_different == "1":
           return HttpResponse('1')
        else:
           first_name=request.POST.get('first_name')
           last_name=request.POST.get('last_name') 
           email=request.POST.get('email') 
           phone=request.POST.get('phone') 
           country=request.POST.get('country') 
           city=request.POST.get('city') 
           address=request.POST.get('address') 
           zipcode=request.POST.get('zipcode')
           order_note=request.POST.get('ordernote')
           payment=request.POST.get('payment')
           order=Order()
           order.first_name=first_name
           order.last_name=last_name
           order.email=email 
           order.mobile=phone 
           order.zipcode=zipcode 
           order.country=country 
           order.city=city 
           order.address=address 
           order.order_note=order_note 
           order.code=get_random_string(5).upper()
           order.user=request.user
           carts=Cart.objects.filter(user=request.user)
           totals=0
           for i in carts:
               if i.variant:
                  totals+=float(i.variant_price_total())
               else:
                  totals+=float(i.get_total())
           order.subtotal=totals 
           order.total=totals 
           #order.save()
           request.session['order_id']=order.id
           for i in carts:
               order_item=OrderItem()
               order_item.order=order 
               order_item.product=i.product 
               order_item.quantity=i.quantity 
               order_item.total=totals 
               #order_item.save()
           if payment == "cod":
              return HttpResponse('cod')
           if payment == "sslcommerz":
               store_id=settings.STORE_ID
               store_pass=settings.STORE_PASS
               mypayment = SSLCSession(sslc_is_sandbox=True, sslc_store_id=store_id, sslc_store_pass=store_pass)
               mypayment.set_product_integration(total_amount=Decimal(255575), currency='BDT', product_category='vbb', product_name='bbh', num_of_item=1, shipping_method='YES', product_profile='None')
               mypayment.set_customer_info(name='nayem', email='nayem@gmail.com', address1='keranigonjg', address2='', city='', postcode='', country='', phone='0196765557')
               mypayment.set_shipping_info(shipping_to='nayem', address='keranigonjg', city='dhaka', postcode='235', country='Bangladesh')
               status_url = request.build_absolute_uri(reverse('status'))
               mypayment.set_urls(success_url=status_url, fail_url=status_url, cancel_url=status_url, ipn_url=status_url)
               
               response_data = mypayment.init_payment()
               return redirect(response_data['GatewayPageURL'])
               
           if payment =="paypal":
              return redirect(reverse("checkout")+"?payment="+str("paypal"))
  

        return HttpResponse('insert Successful')


@csrf_exempt               
def sslc_status(request):
    if request.method=='post'or request.method=='POST':
       payment_data=request.POST
       status=payment_data['status']
       if status =='VALID':
          tran_id=payment_data['tran_id']
          val_id=payment_data['val_id']
          return HttpResponseRedirect(reverse('ssl_compeled',kwargs={'tran_id':tran_id,'val_id':val_id}))
    return HttpResponse('Successful')
    
def ssl_compeled(request,val_id,tran_id):
    if request.session.get('order_id'):
       payment_type=payment()
       payment_type.user=request.user
       payment_type.order_id=request.session['order_id']
       payment_type.orderid=val_id
       payment_type.payment_id=tran_id
       payment_type.payment_type="SSLcommerz"
       payment_type.status='Accepted'
       payment_type.save()
    return HttpResponse('Successful')
       

def Paypal(request):
    data=json.loads(request.body)
    order_id=data['order_id']
    payment_id=data['payment_id']
    status=data['status']
    
    if status =="COMPLETED":
       if request.user.is_authenticated:
         if request.session.get('order_id'):
            payment_type=payment()
            payment_type.user=request.user
            payment_type.order_id=request.session.get('order_id')
            payment_type.orderid=order_id
            payment_type.payment_id=payment_id
            payment_type.payment_type='PayPal'
            payment_type.status=status
            payment_type.save()
          
       else:
          pass
          
    return HttpResponse("Payment Successful");
          

        