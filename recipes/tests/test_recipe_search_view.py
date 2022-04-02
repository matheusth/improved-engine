from django.urls import reverse, resolve  # type: ignore
from recipes import views  # type: ignore
from .test_recipe_base import RecipeTestBase


class RecipeViewsTest(RecipeTestBase):

    def test_recipes_search_is_calling_the_correct_view(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)

    def test_recipes_search_load_wanted_template(self):
        response = self.client.get(reverse('recipes:search'), data={'query': 'points'})

        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(404, response.status_code)

    def test_recipe_search_term_is_on_title_and_is_scaped(self):
        response = self.client.get(reverse('recipes:search'), data={'query': '<points>'})

        self.assertIn('Pesquisa por &quot;&lt;points&gt;&quot;', response.content.decode("utf-8"))
