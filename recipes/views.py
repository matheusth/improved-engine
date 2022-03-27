from django.shortcuts import render, get_object_or_404, get_list_or_404
from recipes.models import Recipe
from django.http import Http404


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(published=True).order_by("-id")
    return render(request, 'recipes/home.html', context={
        'recipes': recipes,

    })


def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id,
                                                    published=True).order_by("-id"))

    return render(request, 'recipes/pages/category-view.html', context={
        'recipes': recipes,
        'category_name': recipes[0].category.name,
    })


def recipe(request, recipe_id):
    selected_recipe = get_object_or_404(Recipe, id=recipe_id, published=True)
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': selected_recipe,
        'is_detail_page': True,
    })


def search(request):
    return Http404()
