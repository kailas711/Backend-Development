from django.db import models
from tomlkit import comment

# Create your models here.
class MenuItem(models.Model): # Each class has attributes and those attributes represent columns in the DB
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    

class reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)