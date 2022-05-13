from django.contrib import admin
from .models import Coupon
# Register your models here.

class CouponModel(admin.ModelAdmin):
      list_display=['name','coupon_type','coupon_valu','cart_value','exfail_date','active']

admin.site.register(Coupon,CouponModel)