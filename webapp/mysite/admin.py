from django.contrib import admin
from .models import Fooddishes,Fooddishes1, Toprecipe

# Register your models here.
mymodels = [Fooddishes,Fooddishes1, Toprecipe]
admin.site.register(mymodels)

