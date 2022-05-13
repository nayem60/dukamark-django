from django.db import models
from category.models import *
from django.utils.text import slugify
from django.utils import timezone
from PIL import Image
from ckeditor.fields import RichTextField
#from sorl.thumbnail import ImageField, get_thumbnail
from django_resized import ResizedImageField



class Product(models.Model):
      STOCK=(
         ('In Stock','In Stock'),
         ('Out Stock','Out Stock')
      )
      STATUS=(
       ('Active','Active'),
       ('Inactive','Inactive')
      )
      
      category=models.ForeignKey(Category,on_delete=models.CASCADE, related_name="product")
      subcategory=models.ForeignKey(Subcategory,on_delete=models.CASCADE)
      subcategory_child=models.ForeignKey(Subcategory_child,on_delete=models.CASCADE, related_name="subChildProduct")
      brand=models.ForeignKey(Brand,on_delete=models.SET_NULL,null=True,blank=True)
      name=models.CharField(max_length=100)
      slug=models.SlugField(max_length=100, unique=True)
      sku=models.CharField(max_length=100)
      information=RichTextField(null=True)
      description=RichTextField(null=True)
      price=models.DecimalField(max_digits=12,decimal_places=2)
      regular_discount_price=models.DecimalField(max_digits=12,decimal_places=2,null=True,blank=True)
      delivery_charge=models.IntegerField(null=True,blank=True, verbose_name="Delivery Charge")
      quantity=models.IntegerField(default=1)
      stock_status=models.CharField(max_length=100,choices=STOCK,default="In Stock")
      image=models.ImageField(upload_to="product/image")
      free_shipping=models.BooleanField(default=False,verbose_name="Free Shipping")
      featured=models.BooleanField(default=False)
      status=models.CharField(max_length=100, choices=STATUS, default="Active")
      def __str__(self):
         return self.name 
         
      def save(self,*args,**kwargs):
          self.slug=slugify(self.name)
          super(Product,self).save(*args,**kwargs)
          img=Image.open(self.image.path)
          if img.width >350 or img.heigth >350:
             output_size=(350,350)
             img.save(self.image.path)
         
      
class SpecialPrice(models.Model):

    STATUS=(
       ('Active','Active'),
       ('Inactive','Inactive')
      )
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    special_price=models.DecimalField(max_digits=12,decimal_places=2)
    end_date=models.DateTimeField()
    status=models.CharField(max_length=100, choices=STATUS, default="Active")
    
class ImageGellary(models.Model):
      product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="image_gellery")
      images=models.ImageField(upload_to='product/images')
      def save(self,*args,**kwargs):
          img=Image.open(self.images.path)
          if img.width >350 or img.heigth>350:
             output_size=(350,350)
             img.save(self.images.path)
      
class ProductWarranty(models.Model):
      DURATION=(
        ('',''),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
        ('12','12'),
        
      )
      
      DATE=(
      ('',''),
      ('Day','Day'),
      ('Month','Month'),
      ('Year','Year')
      )
      
      TYPE=(
      ('',''),
      ('warranty','Warranty'),
      ('Guarantee','Guarantee')
      )
      
      product=models.ForeignKey(Product,on_delete=models.CASCADE)
      warranty_duration=models.CharField(max_length=100, choices=DURATION,default="")
      warranty_date=models.CharField(max_length=100, choices=DATE,default="")
      warranty_type=models.CharField(max_length=100, choices=TYPE,default="")
      
class FlashSale(models.Model):
     ACTIVE=(
     ('active','active'),
     ('unactive','unactive')
     )
     flash_date=models.DateTimeField(default=timezone.now)
     quantity=models.IntegerField(default=10)
     active=models.CharField(max_length=100,choices=ACTIVE, default='active')
     
      
      
class ProductSpecification(models.Model):
      product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="specification")
      attribute=models.CharField(max_length=10,verbose_name="Specification Name")
      value=models.CharField(max_length=10,verbose_name="Specification Value")
      
      

    