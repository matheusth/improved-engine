from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_home_view_returns_status_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_loads_expected_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/home.html')

    def test_recipes_home_view_loads_recipes(self):
        recipe = self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']

        self.assertIn(recipe, recipes, "recipe not loaded in the context variable of the view")

    def test_recipes_home_view_shows_no_recipes_found(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('não encontradas.', content)
        self.assertTemplateNotUsed(response, 'recipes/partials/recipe.html')

    def test_recipes_home_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)

        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']

        self.assertNotIn(recipe, recipes)
