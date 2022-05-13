from django.db import models
from django.contrib.auth.models import User
from product.models import Product 
from variant.models import Variants

class Order(models.Model):
     STATUS = (
        ('processing', 'processing'),
        ('Accepted', 'Accepted'),
        ('OnShipping', 'OnShipping'),
        ('delivered', 'delivered'),
        ('canceled', 'canceled'),
     )
     order_status=models.CharField(max_length=10,choices=STATUS,default='processing')
     code = models.CharField(max_length=5, editable=False,)
     user=models.ForeignKey(User,on_delete=models.CASCADE)
     tax=models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
     subtotal=models.DecimalField(max_digits=12, decimal_places=2)
     discount=models.DecimalField(max_digits=12, decimal_places=2,null=True,blank=True)
     total=models.DecimalField(max_digits=12, decimal_places=2)
     first_name=models.CharField(max_length=100)
     last_name=models.CharField(max_length=100)
     mobile=models.CharField(max_length=100)
     email=models.EmailField(max_length=100)
     country=models.CharField( max_length=20)
     address=models.CharField(max_length=150)
     city=models.CharField(max_length=20)
     zipcode=models.CharField(max_length=50)
     order_note=models.TextField(max_length=100,null=True,blank=True)
     shipping_defferent= models.BooleanField(default=False)
     create_at=models.DateTimeField(auto_now_add=True)
     update_at=models.DateTimeField(auto_now=True)
     
     def __str__(self):
         return str(self.id)

class OrderItem(models.Model):
      order = models.ForeignKey(Order, on_delete=models.CASCADE)
      product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="orderItem")
      variant=models.ForeignKey(Variants,on_delete=models.SET_NULL,null=True,blank=True)
      quantity = models.IntegerField()
      price = models.DecimalField(max_digits=12, decimal_places=2)
      status=models.BooleanField(default=False)
      create_at = models.DateTimeField(auto_now_add=True)
      update_at = models.DateTimeField(auto_now=True)
      
      def r_statu(self,*args,**kwargs):
          #order=self.order.order_status=='delivered'
          if self.order.order_status == 'delivered':
             r_status=self.status=True
            # r_status.update(*args,**kwargs)
             return r_status
          
          else:
             r_status=self.status=False
             
          return r_status
          
          
          
class payment(models.Model):
     PAYMENT_TYPE=(
     ('Cash On Delivery','Cash On Delivery'),
     ('PayPal','PayPal'),
     ('SSLcomerz','SSLcomerz'),
     )
     STATUS = (
        ('pending payment', 'pending payment'),
        ('On Hold','On Hold'),
        ('Accepted', 'Accepted'),
        ('Canceled', 'Canceled'),
    )
     user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
     order= models.ForeignKey(Order, on_delete=models.CASCADE)
     orderid=models.CharField(max_length=100,null=True,blank=True)
     payment_id=models.CharField(max_length=100,null=True,blank=True)
     payment_type=models.CharField(max_length=100,choices=PAYMENT_TYPE, default='Cash On Delivery')
     status=models.CharField(max_length=100,choices=STATUS,default="pending")   
     create_at=models.DateTimeField(auto_now_add=True)
     

