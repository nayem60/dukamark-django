from django.urls import path
from .views import *
urlpatterns=[
   path('add-cart/<int:pk>',Addcart,name='addcart'),
   path('cart-page',CartPage,name='cart_page'),
   path('increment/<int:pk>',Increment),
   path('remove/<int:pk>',Remove),

]