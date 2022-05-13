from django.db import models
from product.models import Product
from category.models import Category,Subcategory,Subcategory_child
from django.utils.safestring import mark_safe
from django_resized import ResizedImageField

# Create your models here.
 
class Color(models.Model):
      category=models.ForeignKey(Category,on_delete=models.CASCADE)
      subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="color")
      name=models.CharField(max_length=100)
      code=models.CharField(max_length=100,null=True,blank=True)
      
      def __str__(self):
          return self.name
      def color_tag(self):
          if self.code is not None:
             return mark_safe("<p style='background-color:{}'>Color</p".format(self.code))
          else:
            return ""
      
class Size(models.Model):
      category=models.ForeignKey(Category,on_delete=models.CASCADE)
      subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE, related_name="size")
      name=models.CharField(max_length=100)
      def __str__(self):
         return self.name
         
          

class Variants(models.Model):
      product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name="variant")
      color=models.ForeignKey(Color,on_delete=models.SET_NULL,null=True,blank=True)
      size=models.ForeignKey(Size,on_delete=models.SET_NULL,null=True,blank=True)
      sku=models.CharField(max_length=100)
      quantity=models.IntegerField(default=1) 
      price=models.DecimalField(max_digits=12,decimal_places=2)
      
   
      def __str__(self):
          return str(self.id)
          
      
             

