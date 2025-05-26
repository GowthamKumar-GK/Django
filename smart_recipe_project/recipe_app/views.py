from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import IngredientForm
from .models import Recipe

def home(request):
    form = IngredientForm()
    recipes = None
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            selected_ingredients = form.cleaned_data['ingredients']
            recipes = Recipe.objects.all()
            for ingredient in selected_ingredients:
                recipes = recipes.filter(ingredients=ingredient)
    return render(request, 'home.html', {'form': form, 'recipes': recipes})

