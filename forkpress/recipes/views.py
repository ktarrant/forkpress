from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect

from .forms import StepForm

def recipe(request):
    return render(request, 'recipes/recipe.html')

def index(request):
    form = StepForm()
    return render(request, 'recipes/index.html')

def food(request, food_id):
    return HttpResponse("Food page: %d" % int(food_id))