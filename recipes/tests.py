from django.test import TestCase  # type: ignore
from django.urls import reverse, resolve  # type: ignore
from recipes import views


# Create your tests here.
class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_resolved_correctly(self):
        self.assertEqual('/', reverse('recipes:home'))

    def test_recipe_category_url_is_resolved_correctly(self):
        self.assertEqual('/recipes/category/1/',
                         reverse('recipes:category', kwargs={'category_id': 1}))

    def test_recipe_detail_url_is_resolved_correctly(self):
        self.assertEqual('/recipes/1/',
                         reverse('recipes:recipe', kwargs={'recipe_id': 1}))


class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', args=(1,)))
        self.assertIs(view.func, views.category)

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', args=(1,)))
        self.assertIs(view.func, views.recipe)
