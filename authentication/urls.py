from django.urls import path
from .views import *

urlpatterns=[
    path('login',Loging.as_view(),name='login'),
    path('registration/',Registration,name='registration'),
    path('store/',category),
]