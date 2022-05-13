from django.urls import path
from .views import *

urlpatterns=[
    path('checkout',Checkout.as_view(),name="checkout"),
    path('paypal/',Paypal,name='paypal'),
    path('status',sslc_status,name='status'),
    path('payment/success/<val_id>/<tran_id>/',ssl_compeled,name='ssl_compeled'),
]