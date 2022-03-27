from django.core.exceptions import ValidationError  # type: ignore
from parameterized import parameterized  # type: ignore
from recipes.models import Recipe  # type: ignore
from .test_recipe_base import RecipeTestBase  # type: ignore


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_rises_error_if_has_more_max_chars_is_exceeded(self, field, max_length):
        setattr(self.recipe, field, "A" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_model_published_and_preparation_steps_is_html_default_to_false(self):
        local_recipe = Recipe.objects.create(
            category=self.make_category(),
            author=self.make_author(username="matheushti"),
            description="descricao",
            servings=2,
            servings_unit="porções",
            preparation_time=25,
            preparation_time_unit="minutos",
            preparation_steps="lorem ipsum dolor sit ammet"
        )

        self.assertIs(local_recipe.published, False, msg="published didn't default to false.")
        self.assertIs(local_recipe.published, False,
                      msg="preparation_steps_is_html didn't default to false.")

    def test_recipe_model_string_representation(self):
        self.recipe.title = "Teste"
        self.recipe.author = self.make_author(username="second", first_name="autor")
        self.recipe.full_clean()
        self.recipe.save()

        self.assertEqual(str(self.recipe), "Teste por second",
                         msg="Recipe string representation must be in the format '\
                         '<recipe-title> por <author-first-name>'")


class CategoryModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()

    def test_category_name_raises_exception_if_exceeds_65_chars(self):
        self.category.name = "A" * 66
        with self.assertRaises(ValidationError):
            self.category.full_clean()

    def test_category_representation_string_is_equal_category_name(self):
        self.category.name = "Teste"
        self.category.full_clean()
        self.category.save()
        self.assertEqual(str(self.category), "Teste")
