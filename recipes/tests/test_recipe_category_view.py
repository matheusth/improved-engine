from django.urls import reverse, resolve  # type: ignore
from recipes import views  # type: ignore
from .test_recipe_base import RecipeTestBase


class RecipeCategoryViewTest(RecipeTestBase):
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipes_category_view_returns_status_404_if_no_recipes(self):
        response = self.client.get(reverse('recipes:category', args=(1000,)))
        self.assertEqual(response.status_code, 404)

    def test_recipes_category_view_template_loads_recipes(self):
        recipe = self.make_recipe(title='This is a category test')
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))
        recipes = response.context['recipes']

        self.assertIn(recipe, recipes, "recipe not loaded in the context variable of the view")

    def test_recipes_category_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)