from django.contrib import admin

# Register your models here.
from .models import Recipe, Food

admin.site.register(Recipe)
admin.site.register(Food)