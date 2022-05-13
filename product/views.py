from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,HttpResponseRedirect
from category.models import *
from .models import *
from variant.models import *
# Create your views here.

class SubcategoryChiled(APIView):
      def post(self,request,format=False):
          return HttpResponse('hi')
     
      
     
class BrandList(APIView):
      permission_classes=[IsAuthenticated,]
      def post(self,request,format=False):
          subcategory=request.data['subcategory']
          brand={}
          if subcategory:
             subcategories=Subcategory.objects.get(id=subcategory).brands.all()
             brand={p.name:p.id for p in subcategories}
             return JsonResponse(data=brand,safe=False)
             
             
             
             
def product_detail(request,slug):
    url = request.META.get('HTTP_REFERER')
    variant_id=None
    try:
       color_id=request.GET.get('color')
       color_id=int(color_id)
       variant_id=Variants.objects.get(id=color_id)
       #================size variant====
       size_id=request.GET.get('size')
       size_id=int(size_id)
       variant_id=Variants.objects.get(id=size_id)
    except:
       pass
    product=Product.objects.get(slug=slug)
    context={
        'product':product,
        'color_id':color_id,
        'size_id':size_id,
        'variant_id':variant_id
       
    }
    return render(request,'product_detail.py',context)
    
    
    
    
def product_detail2(request,slug): 
    product=Product.objects.get(slug=slug)
    context={
        'product':product,
    }
    return render(request,'product_details.py',context)
    
   