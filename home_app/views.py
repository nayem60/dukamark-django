from django.shortcuts import render
from product.models import *
from category.models import *
from variant.models import Variants
from banner.models import *
from django.http import HttpResponse,JsonResponse
from django.template.loader import render_to_string
from django.db.models import Q
from datetime import datetime
import json
from category.models import *
from django.contrib.auth.decorators import login_required


def home(request):
   product=Product.objects.all().reverse()
   slider=Slider.objects.all()
   footer_banner=FooterBanner.objects.filter(active=True)[:3]
   context={
       "product":product, 
       "slider":slider,
       'footer_banner':footer_banner,
   }
   try:
     flasSale=FlashSale.objects.get(flash_date__date__gte=datetime.now())
     flasProduct=Product.objects.filter(quantity__gte=flasSale.quantity)[:5]
     context.update({"flasSale":flasSale,"flasProduct":flasProduct})
   except:
     pass
   return render(request,'home.py', context)
  
  
def category_product(request,slug):
    sub_id=request.GET.get("id")
    min_price=request.GET.get("min")
    max_price=request.GET.get("max")
    brand=request.GET.get("brand")
    color=request.GET.getlist("color[]")
    category_product=Product.objects.all()
    if sub_id:
       print("=====",sub_id)
       category_product=Product.objects.filter(subcategory_child__id=sub_id)
    if min_price and max_price:
       category_product=Product.objects.filter(Q(subcategory__slug=slug) & Q(price__gte=min_price) & Q(price__lte=max_price))
   
    elif brand:
       category_product=Product.objects.filter(brand__id=brand)
       
    elif color:
         colors=[int(i) for i in color] 
         category_product=category_product.filter(variant__color__id__in=color)
         
             #category_product=Product.objects.filter(Q(subcategory__slug=slug) & Q(id=i.product.id))
    category_filter=Subcategory.objects.get(slug=slug)
    sub_child=Subcategory_child.objects.filter(subcategory=category_filter)
    category_banner=CategoryBanner.objects.filter(subcategory=category_filter,active=True).first()
    special_offer=SpecialPrice.objects.filter(end_date__date__gte=datetime.now(),status="Active")
    context={
        'category_product':category_product,
        'category_filter':category_filter,
        'sub_child':sub_child,
        'category_banner':category_banner,
        'brands':brand,
        'colorId':color,
        'special_offer':special_offer,
        'subId':sub_id,
        
    }
    return render(request,'shop.py',context)
    
    
    
def Filter(request,slug):    
    colors=request.GET.getlist('color[]')
    subcategory=request.GET.get('subId')
    sizes=request.GET.getlist('size[]')
    storage=request.GET.getlist('storage[]')
    ram=request.GET.getlist('ram[]')
    if len(colors)>0:
       variant_id=Variants.objects.filter(color__id__in=colors)
       for i in variant_id:
           product=Product.objects.filter(Q(subcategory__slug=slug) & Q(id=i.product.id))
           
    product=Product.objects.all()
    t=render_to_string('ajax_layouts/product-list.py',{'category_product':product})
    return JsonResponse({'data':t})
    
    
    
    