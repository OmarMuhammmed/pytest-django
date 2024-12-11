import pytest
from testapp.models import Product
from django.urls import reverse


@pytest.mark.django_db # to use database to test models
def test_create_product():

    product = Product.objects.create(name="laptop", price=220.2, stock=3)

    assert product.name == "laptop"
    assert product.price == 220.2
    assert product.stock == 3

