from django.contrib.auth.models import User  # type: ignore
from django.test import TestCase  # type: ignore
from recipes.models import Category, Recipe  # type: ignore


class RecipeTestBase(TestCase):
    def make_category(self, category_name='category'):
        return Category.objects.create(name=category_name)

    def make_author(self,
                    username='username',
                    password='username_password',
                    email='username@email.com',
                    first_name='First name',
                    last_name='Last name', ):
        return User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )

    def make_recipe(self,
                    category_data=None,
                    author_data=None,
                    title='Recipe title',
                    description='Recipe description',
                    slug='recipe-slug',
                    preparation_time=15,
                    preparation_time_unit='minutes',
                    servings=2,
                    servings_unit='porções',
                    preparation_steps='Grill it, Grill it, Grill it',
                    published=True,
                    preparation_steps_is_html=False,
                    cover='test.png'
                    ):
        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            category=self.make_category(**category_data),
            author=self.make_author(**author_data),
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            published=published,
            preparation_steps_is_html=preparation_steps_is_html,
            cover=cover
        )
