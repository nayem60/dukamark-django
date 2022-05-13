from django.db import models
from product.models import Product
from django.contrib.auth.models import User
from variant.models import Variants
# Create your models here.
class Cart(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     product=models.ForeignKey(Product,on_delete=models.CASCADE, related_name="product")
     variant=models.ForeignKey(Variants,on_delete=models.SET_NULL,blank=True,null=True,related_name="variant")
     quantity=models.IntegerField(default=0)
     tax=models.IntegerField(null=True,blank=True)
     shipping_status=models.BooleanField(default=False)
     
     def __str__(self):
        return str(self.product)
     def get_total(self):
         total=self.product.price*self.quantity
         float_total=format(total,'0.2f')
         return float_total
     def variant_price_total(self):
         total=self.variant.price*self.quantity
         float_total=format(total,'0.2f')
         return float_total
         
     def totals(self):
         carts=Cart.objects.filter(user=self.user)
         total=0
         for i in carts:
           if i.variant:
             total+=float(i.variant_price_total())
           else:
             total+=float(i.get_total())
         return total
        
class wishlist(models.Model):
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     def __str__(self):
         return self.product