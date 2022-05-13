from django.urls import path
from .views import Coupon

urlpatterns=[
   path('coupon',Coupon,name='coupon'),

]