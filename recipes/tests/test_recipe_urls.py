from django.test import TestCase  # type: ignore
from django.urls import reverse  # type: ignore


class RecipeURLsTest(TestCase):
    def test_recipe_home_url_is_resolved_correctly(self):
        self.assertEqual('/', reverse('recipes:home'))

    def test_recipe_category_url_is_resolved_correctly(self):
        self.assertEqual('/recipes/category/1/',
                         reverse('recipes:category', kwargs={'category_id': 1}))

    def test_recipe_detail_url_is_resolved_correctly(self):
        self.assertEqual('/recipes/1/',
                         reverse('recipes:recipe', kwargs={'recipe_id': 1}))
