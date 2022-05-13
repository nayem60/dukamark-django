from django.db import models
from django.utils.safestring import mark_safe
from category.models import *
from django.utils.text import slugify
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill




class Slider(models.Model):
     TYPE=(
        ('New Deal','New Deal'),
        ('Hot Deal','Hot Deal'),
        ('New Arriavels','New Arriavels'),
     )
     first_caption=models.CharField(max_length=100,null=True, blank=True,verbose_name="Caption 1")
     last_captiop=models.CharField(max_length=100, null=True, blank=True,verbose_name="Caption 2")
     action_text=models.CharField(max_length=100, null=True, blank=True,verbose_name="Call To Action Text")
     action_url=models.CharField(max_length=100, verbose_name="Call To Action Url")
     image=models.ImageField(upload_to='product/banner/slider',null=True,blank=True)
     types=models.CharField(max_length=100, choices=TYPE,null=True,blank=True, default="")
     active=models.BooleanField(verbose_name="Open In Window")
     def image_tag(self):
         return mark_safe('<img src="{}" width="150px"; height=80px />'.format(self.image.url))
       
            
class HeaderBanner(models.Model):
     first_caption=models.CharField(max_length=100,null=True, blank=True,verbose_name="Caption 1")
     last_captiop=models.CharField(max_length=100, null=True, blank=True,verbose_name="Caption 2")
     action_text=models.CharField(max_length=100, null=True, blank=True,verbose_name="Call To Action Text")
     action_url=models.CharField(max_length=100, verbose_name="Call To Action Url")
     image=models.ImageField(upload_to="product/banner/header_banner")
     active=models.BooleanField(verbose_name="Open In Window")
     def image_tag(self):
         return mark_safe('<img src="{}" width="80px" />'.format(self.image.url))
      
     
class FooterBanner(models.Model):
     TYPE=(
        ('New Deal','New Deal'),
        ('Hot Deal','Hot Deal'),
        ('New Arriavels','New Arriavels'),
     )
     
     first_caption=models.CharField(max_length=100,null=True, blank=True,verbose_name="Caption 1")
     last_captiop=models.CharField(max_length=100, null=True, blank=True,verbose_name="Caption 2")
     action_text=models.CharField(max_length=100, null=True, blank=True,verbose_name="Call To Action Text")
     action_url=models.CharField(max_length=100, verbose_name="Call To Action Url")
     image=ProcessedImageField(upload_to='product/banner/footer_banner',processors=[ResizeToFill(100, 50)],format='JPEG',options={'quality': 60},null=True,blank=True)
     types=models.CharField(max_length=100, choices=TYPE,null=True,blank=True, default="")
     active=models.BooleanField(verbose_name="Open In Window")
     def image_tag(self):
         return mark_safe('<img src="{}" width="80px" />'.format(self.image.url))
     
     
            
            
class CategoryBanner(models.Model):
     category=models.ForeignKey(Category,on_delete=models.CASCADE)
     subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
     subcategory_child=models.ForeignKey(Subcategory_child,on_delete=models.SET_NULL,null=True,blank=True)
     first_caption=models.CharField(max_length=100,null=True, blank=True,verbose_name="Caption 1")
     last_captiop=models.CharField(max_length=100, null=True, blank=True,verbose_name="Caption 2")
     action_text=models.CharField(max_length=100, null=True, blank=True,verbose_name="Call To Action Text")
     action_url=models.CharField(max_length=100, verbose_name="Call To Action Url")
     image=ProcessedImageField(upload_to='product/banner/category_banner',null=True,blank=True,processors=[ResizeToFill(100, 50)],format='JPEG',options={'quality': 60})
     active=models.BooleanField(verbose_name="Open In Window")
     def image_tag(self):
         return mark_safe('<img src="{}" width="80px" />'.format(self.image.url))
         
     
          
          
          
          
class fav_icon(models.Model):
     image=models.ImageField(upload_to='FavIcon')
     active=models.BooleanField(default=True)
     create_at=models.DateTimeField(auto_now_add=True)
     def icon_image(self):
        return mark_safe("<img src='{}' width='50px' height='50px'/>".format(self.image.url))
        
        
        
class main_logo(models.Model):
     image=models.ImageField(upload_to='MainLogo')
     active=models.BooleanField(default=True)
     create_at=models.DateTimeField(auto_now_add=True)
     
     def __str__(self):
        return mark_safe("<img src='{}' width='50px' height='50px'/>".format(self.image.url))
     
          
         