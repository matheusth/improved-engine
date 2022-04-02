from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeDetailViewTest(RecipeTestBase):
    def test_recipes_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)

    def test_recipes_recipe_detail_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:recipe', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_detail_view_template_loads_recipe(self):
        recipe = self.make_recipe(title='Needed title')
        response = self.client.get(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))
        recipe_detail = response.context['recipe']

        self.assertEqual(recipe, recipe_detail, "loaded recipe does not match the expected recipe.")

    def test_recipes_recipe_detail_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))

        self.assertEqual(404, response.status_code, "unpublished recipe loaded")
