from django.shortcuts import render, get_object_or_404
from recipes.models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(published=True).order_by("-id")
    return render(request, 'recipes/home.html', context={
        'recipes': recipes
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        published=True
    ).order_by("-id")

    return render(request, 'recipes/home.html', context={
        'recipes': recipes
    })


def recipe(request, recipe_id):
    selected_recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': selected_recipe,
        'is_detail_page': True,
    })
