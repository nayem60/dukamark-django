from django.urls import path
from .views import *


urlpatterns =[
  path('',home,name="home"),
  path('category-product/<str:slug>', category_product,name="category_product"),
  path('filter-data/<str:slug>',Filter,name="filter"),
 
  ]