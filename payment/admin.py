from django.contrib import admin
from .models import *
# Register your models here.
class OrderItemAdmin(admin.ModelAdmin):
      list_display=['order','product','variant','quantity','price','r_statu']
      
class PaymentAdmin(admin.ModelAdmin):
      list_display=['user','order','payment_id','payment_type']
      
admin.site.register(Order)
admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(payment,PaymentAdmin)