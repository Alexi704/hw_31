import factory.django

from ads.models import Ad, Category
from selections.models import Selection
from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker('word')


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker('name')
    email = factory.Faker('email')
    # birth_date = factory.Faker('date')
    birth_date = '2004-05-12'
    is_staff = True


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    category = factory.SubFactory(CategoryFactory)
    author = factory.SubFactory(UserFactory)
    price = 454


# class SelectionFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Selection
#
#     name = "Selection_Name"
#     owner_id = 1


