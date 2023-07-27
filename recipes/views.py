from django.http import Http404
from django.shortcuts import render
from utils.recipes.recipe_factory import make_recipe

from recipes.models import Recipe


def home(request):
    # Retorna todas as receitas ordenando por id de forma decrescente
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })


def category(request, category_id):
    # Retorna todas as receitas ordenando por id de forma decrescente
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    # Verificar porque o Pylance não aceita a verificação abaixo e aceita a chamada de recipes.first().category
    # Desativando o python.analysis.typeCheckingMode por enquanto...
    if not recipes:
        raise Http404('Not found')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name}',
    })
