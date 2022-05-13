from django.urls import path
from .views import *

urlpatterns=[
   path('category/',SubcategoryList.as_view()),
   path('subcategory/',SubcategoryChildList.as_view())

]