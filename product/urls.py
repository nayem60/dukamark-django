from django.urls import path
from .views import *

urlpatterns=[
   path('subcategory-child/',SubcategoryChiled.as_view()),
   path('brand/',BrandList.as_view()),
   path('product-detail/<str:slug>',product_detail2,name='product_detail'),

]
