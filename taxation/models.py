from django.db import models
from django.conf import settings

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    tin_number = models.CharField(max_length=255)
   
    
class admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    

class Profile(models.Model):
    tin_number = models.IntegerField(null=True, blank=True)
    stock_type = models.CharField(max_length=255, null=True, blank=True)
    
        