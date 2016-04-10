from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'recipes/index.html')

def food(request, food_id):
    return HttpResponse("Food page: %d" % int(food_id))