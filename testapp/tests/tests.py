import pytest
from testapp.models import Product
from django.urls import reverse


# to use database to test models any test to connect database must use this decorator
@pytest.mark.django_db 
def test_create_product():

    product = Product.objects.create(name="laptop", price=220.2, stock=3)

    assert product.name == "laptop"
    assert product.price == 220.2
    assert product.stock == 3

@pytest.mark.skip
def test_add():
    assert 2 == 2 
