from django.contrib import admin
from .models import *
# Register your models here.

class VariantsModel(admin.ModelAdmin):
      list_display=['id','product','color','size','price']

class ColorModel(admin.ModelAdmin):
      list_display=['subcategory','name']
      class Media:
         js=("drop/brand.js",)

class SizeModel(admin.ModelAdmin):
      list_display=['subcategory','name']
      class Media:
         js=("drop/brand.js",)
      

admin.site.register(Variants,VariantsModel)
admin.site.register(Color,ColorModel)
admin.site.register(Size,SizeModel)

