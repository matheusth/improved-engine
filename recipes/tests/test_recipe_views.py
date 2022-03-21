from django.test import TestCase  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from recipes import views  # type: ignore


# Create your tests here.


class RecipeViewsTest(TestCase):
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipes_home_view_returns_status_200(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_home_view_loads_expected_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/home.html')

    def test_recipes_home_view_shows_no_recipes_found(self):
        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        self.assertIn('não encontradas.', content)
        self.assertTemplateNotUsed(response, 'recipes/partials/recipe.html')

    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipes_category_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipes_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe', args=(1000,)))
        self.assertEqual(response.status_code, 404)
