from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.TextField(default='unknown')  # comma-separated list
    instructions = models.TextField(default='unknown')  # Add this line

    def __str__(self):
        return self.name

