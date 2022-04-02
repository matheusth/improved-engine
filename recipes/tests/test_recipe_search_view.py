from django.urls import reverse, resolve  # type: ignore
from recipes import views  # type: ignore
from .test_recipe_base import RecipeTestBase


class RecipeSearchViewTest(RecipeTestBase):

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

    def test_recipe_search_can_find_recipes_by_title(self):
        title_one = 'This is recipe one'
        title_two = 'This is recipe two'
        recipe_one = self.make_recipe(
            slug='recipe-one', title=title_one, author_data={'username': 'user_one'}
        )
        recipe_two = self.make_recipe(
            slug='recipe-two', title=title_two, author_data={'username': 'user_two'}
        )
        url = reverse('recipes:search')
        response_one = self.client.get(url, data={'query': title_one})
        response_two = self.client.get(url, data={'query': title_two})
        response_both = self.client.get(url, data={'query': 'This is'})

        self.assertIn(recipe_one, response_one.context['recipes'],
                      msg="recipe one should be in response one")
        self.assertIn(recipe_two, response_two.context['recipes'],
                      msg="recipe two should be in response two")

        self.assertNotIn(recipe_one, response_two.context['recipes'],
                         msg="recipe one should not be in response two")
        self.assertNotIn(recipe_two, response_one.context['recipes'],
                         msg="recipe two should not be in response one")

        self.assertIn(recipe_one, response_both.context['recipes'],
                      msg="recipe one should not be in response both")
        self.assertIn(recipe_two, response_both.context['recipes'],
                      msg="recipe two should not be in response both")
