from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.
class UserProfile(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      phone=models.IntegerField(null=True)
      address=models.CharField(max_length=100,null=True)
      city=models.CharField(max_length=100,null=True,blank=True)
      country=models.CharField(max_length=100,null=True,blank=True)
      image=models.ImageField(upload_to='User/',null=True,blank=True)
      
      def __str__(self):
          return self.user.username
          
          
      def ImageTag(self):
          return mark_safe("<img src='{}'height='40'width='50'/>".format(self.image.url))