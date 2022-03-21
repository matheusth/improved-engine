from django.shortcuts import render
from utils.recipes.recipes_generator import make_recipe


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'recipes': [make_recipe for _ in range(10)]
    })


def recipe(request, recipe_id):
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })
