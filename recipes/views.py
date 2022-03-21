from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')


def recipe(request, recipe_id):
    return render(request, 'recipes/pages/recipe-view.html')
