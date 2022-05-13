from django.contrib import admin
from .models import *
# Register your models here.
class SubcategoryTable(admin.TabularInline):
      model=Subcategory
      prepopulated_fields={'slug':('name',)}
      extra=3
      
class SubcategoryChildTable(admin.TabularInline):
      model=Subcategory_child
      prepopulated_fields={'slug':('name',)}
      extra=3
      
class BrandTable(admin.TabularInline):
      model=Brand
      prepopulated_fields={'slug':('name',)}
      extra=3
      
      
      
      
      
class CategoryModel(admin.ModelAdmin):
      list_display=['name','slug','is_active']
      prepopulated_fields={'slug':('name',)}
      inlines=[SubcategoryTable]
      
class SubcategoryModel(admin.ModelAdmin):
      list_display=['category','name','slug','is_active']
      prepopulated_fields={'slug':('name',)}
      inlines=[SubcategoryChildTable]
      
class SubategoryChildModel(admin.ModelAdmin):
      list_display=['subcategory','name','slug','is_active']
      prepopulated_fields={'slug':('name',)}
      
class BrandModel(admin.ModelAdmin):
      list_display=['subcategory','name','slug','is_active']
      prepopulated_fields={'slug':('name',)}
      class Media:
         js=("drop/brand.js",)
      
      
      
      

admin.site.register(Category,CategoryModel)
admin.site.register(Subcategory,SubcategoryModel)
admin.site.register(Subcategory_child,SubategoryChildModel)
admin.site.register(Brand,BrandModel)
