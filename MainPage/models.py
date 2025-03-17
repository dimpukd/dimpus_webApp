from django.db import models

# Create your models here.
class food(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.TextField()
    offer = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

class wine(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.TextField()
    offer = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

class other_products(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.TextField()
    offer = models.BooleanField(default=False)
    available = models.BooleanField(default=False)
    
