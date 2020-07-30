from django.shortcuts import render
from .models import Fooddishes
from .models import Fooddishes1, Toprecipe

# Create your views here.

def home(request):
    dishes = Fooddishes.objects.all()
    dishes1 = Fooddishes1.objects.all()
    recipes = Toprecipe.objects.all()
    
    return render(request, "base.html", {'dishes' : dishes, 'dishes1' : dishes1 , 'recipes': recipes })


    

