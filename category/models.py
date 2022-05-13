from django.db import models
from django_resized import ResizedImageField
# Create your models here.

class Category(models.Model):
      name=models.CharField(max_length=100)
      slug=models.SlugField(unique=True)
      is_active=models.BooleanField(default=True)
      create_at=models.DateTimeField(auto_now_add=True)
      def __str__(self):
         return self.name
         
class Subcategory(models.Model):
     category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name="subcategorys")
     name=models.CharField(max_length=100)
     slug=models.SlugField(unique=True)
     is_active=models.BooleanField(default=True)
     create_at=models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.name
        
        
class Subcategory_child(models.Model):
     subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="SubcategoryChild")
     name=models.CharField(max_length=100)
     slug=models.SlugField(unique=True)
     is_active=models.BooleanField(default=True)
     create_at=models.DateTimeField(auto_now_add=True)
     def __str__(self):
        return self.name
     class Meta:
          verbose_name_plural="Subcategory Child"
        
        
class Brand(models.Model):
     category=models.ForeignKey(Category,on_delete=models.CASCADE)
     subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE,related_name="brands")
     name=models.CharField(max_length=100)
     image=ResizedImageField(size=[170,40],upload_to='brand',null=True,blank=True)
     slug=models.SlugField(unique=True)
     is_active=models.BooleanField(default=True)
     create_at=models.DateTimeField(auto_now_add=True)
     def __str__(self):
       return self.name