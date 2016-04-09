from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200)
    unitValue = models.FloatField(default=0.0)
    unitName = models.CharField(max_length=200)
    calories = models.IntegerField(default=0)
    protein = models.DecimalField(default=0.0, max_digits=7, decimal_places=2)

class Ingredient(models.Model):
    fromRecipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    fromStep = models.ForeignKey("Step", on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    portion = models.FloatField(default=0.0)

class Step(models.Model):
    fromRecipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    instruction = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)

class Recipe(models.Model):
    pub_date = models.DateTimeField('date published')
    ingredients = models.ManyToManyField(Ingredient)
    steps = models.ManyToManyField(Step)