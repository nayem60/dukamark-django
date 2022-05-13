from django.contrib import admin
from .models import *
# Register your models here.

class SliderModel(admin.ModelAdmin):
      list_display=['first_caption','last_captiop','action_text','action_url','image_tag']

class HeaderBannerModel(admin.ModelAdmin):
      list_display=['first_caption','last_captiop','action_text','action_url','image_tag']

class FooterBannerModel(admin.ModelAdmin):
      list_display=['first_caption','last_captiop','action_text','action_url','image_tag']

class CategoryBannerModel(admin.ModelAdmin):
      list_display=['first_caption','last_captiop','action_text','action_url','image_tag']
      class Media:
         js=("drop/brand.js",)


admin.site.register(Slider,SliderModel)
admin.site.register(HeaderBanner,HeaderBannerModel)
admin.site.register(FooterBanner,FooterBannerModel)
admin.site.register(CategoryBanner,CategoryBannerModel)