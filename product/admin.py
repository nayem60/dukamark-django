from django.contrib import admin
from .models import *
from variant.models import Variants
# Register your models here.

      
class ImageGellaryTable(admin.TabularInline):
      model=ImageGellary
      extra=3
      
class ProductWarrantyTable(admin.TabularInline):
      model=ProductWarranty
      extra=1
      
class ProductSpecificationTable (admin.TabularInline):
      model=ProductSpecification
      extra=2
      
class VariantsTable(admin.TabularInline):
      model=Variants
      extra=1
      
      
      
class ProductModel(admin.ModelAdmin):
      list_display=['name','slug','price','regular_discount_price','stock_status','quantity','featured']
      prepopulated_fields={'slug':('name',)}
      inlines=[ImageGellaryTable,ProductWarrantyTable,ProductSpecificationTable,VariantsTable]
      class Media:
         js=("drop/product.js",)
      
class FlashSaleModel(admin.ModelAdmin):
      list_display=['flash_date','quantity','active']

admin.site.register(Product,ProductModel)
admin.site.register(FlashSale,FlashSaleModel)
