import pytest 

from pytest_factoryboy import register
from factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)

