from django.db import models

# Create your models here.

class Setting(models.Model):
      logo=models.ImageField(upload_to="logo")
      favIcon=models.ImageField(upload_to="FavIcon")
      email=models.EmailField(max_length=200,null=True,blank=True)
      phone=models.CharField(max_length=200,null=True,blank=True)
      phone2=models.CharField(max_length=200,null=True,blank=True)
      address=models.TextField(max_length=200,null=True,blank=True)
      maps=models.CharField(max_length=200,null=True,blank=True,verbose_name="google map")
      twitter=models.URLField(max_length=200,null=True,blank=True)
      facebook=models.URLField(max_length=200,null=True,blank=True)
      youtoube=models.URLField(max_length=200,null=True,blank=True)
      instagram=models.URLField(max_length=200,null=True,blank=True)
      pinterest=models.URLField(max_length=200,null=True,blank=True)