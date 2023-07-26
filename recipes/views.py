from django.shortcuts import render
from utils.recipes.recipe_factory import make_recipe


def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)]
    })

def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'recipes': make_recipe(),
    })
