from django.shortcuts import render
from .models import Recipe
from .forms import IngredientForm

def home(request):
    suggested_recipes = []
    form = IngredientForm()

    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            user_ingredients = form.cleaned_data['ingredients'].lower().split(',')

            all_recipes = Recipe.objects.all()
            for recipe in all_recipes:
                recipe_ingredients = recipe.ingredients.lower().split(',')
                if all(ingredient.strip() in recipe_ingredients for ingredient in user_ingredients):
                    suggested_recipes.append(recipe)

    return render(request, 'home.html', {'form': form, 'recipes': suggested_recipes})
