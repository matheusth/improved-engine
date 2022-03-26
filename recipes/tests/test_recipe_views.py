from django.urls import reverse, resolve  # type: ignore
from recipes import views  # type: ignore
from .test_recipe_base import RecipeTestBase
from ..models import Recipe


class RecipeViewsTest(RecipeTestBase):

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

    def test_recipes_home_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)

        response = self.client.get(reverse('recipes:home'))
        recipes = response.context['recipes']

        self.assertNotIn(recipe, recipes)

    def test_recipes_category_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': recipe.category.id}))

        self.assertEqual(response.status_code, 404)

    def test_recipes_recipe_detail_view_dont_load_unpublished_recipe(self):
        recipe = self.make_recipe(published=False)
        response = self.client.get(reverse('recipes:recipe', kwargs={'recipe_id': recipe.id}))

        self.assertEqual(404, response.status_code, "unpublished recipe loaded")
