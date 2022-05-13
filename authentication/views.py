from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.
from django.db.models import Max,Count,Min,Sum
from category.models import Category,Subcategory_child
from product.models import Product


class Loging(TemplateView):
     def get(self, request):
         return render(request,'authentication/login.py')
     def post(self, request):
         username=request.POST.get('username')
         password=request.POST.get('password')

def Registration(request):
    if request.method=="post" or request.method=="POST":
       username=request.POST.get('username')
       email=request.POST.get('email')
       password1=request.POST.get('password1')
       password2=request.POST.get('password2')
       
       if User.objects.filter(username=username).exists():
          return HttpResponse("username Already Exists")
       if password1 != password2:
          return HttpResponse("Wong Password")
          
       user=User() 
       user.username=username 
       user.email=email 
       user.is_active=True 
       user.set_password(raw_password=password1)
       user.save()
       return HttpResponse('Registration Successful')


def category(request):
    category=Subcategory_child.objects.annotate(count=Count('subChildProduct')).order_by('-count')
    products=Product.objects.filter(orderItem__order__order_status='delivered').annotate(total=Sum('orderItem__quantity')).order_by('-total')
    context={
        'category':category,
         'products':products
    }
    return render(request,'text.py',context)

