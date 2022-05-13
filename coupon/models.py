from django.db import models

# Create your models here.


class Coupon (models.Model):
      TYPE=(
        ('fixed','fixed'),
        ('percent','percent')
      )
      name=models.CharField(max_length=100)
      coupon_type=models.CharField(max_length=100,choices=TYPE)
      coupon_valu=models.IntegerField()
      cart_value=models.IntegerField(null=True,blank=True)
      exfail_date=models.DateTimeField(verbose_name="Coupon Exfail Date")
      active=models.BooleanField(default=True)
      
      def __str__(self):
          return self.name