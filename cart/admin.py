from django.contrib import admin
from .models import *
# Register your models here.
class CartModel(admin.ModelAdmin):
      list_display=['user','product','variant','quantity','totals']
  
class WishlistModel(admin.ModelAdmin):
      list_display=['user','product']
  

admin.site.register(Cart,CartModel)
admin.site.register(wishlist,WishlistModel)
