from django.db import models

# Create your models here.
class Fooddishes(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Fooddishes1(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()

class Toprecipe(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()