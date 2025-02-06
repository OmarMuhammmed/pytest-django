import pytest
from testapp.models import Product
from django.urls import reverse
from django.contrib.auth.models import User


# to use database to test models any test to connect database must use this decorator
# @pytest.mark.django_db 
# def test_create_product():

#     product = Product.objects.create(name="laptop", price=220.2, stock=3)

#     assert product.name == "laptop"
#     assert product.price == 220.2
#     assert product.stock == 3

# @pytest.mark.skip
# def test_add():
#     assert 2 == 2 


# @pytest.mark.parametrize("x, y, result",[ (7,3,10), (7,2,9), (5,5,10), (7,7,14) ])
# def test_addtion(x,y,result):
#     assert x+y == result 

@pytest.fixture
def fixture_1():
    print("run fixture 1")
    return 1


def test_example(fixture_1):
    assert fixture_1 == 1
      
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user(username="testuser", password="testpassword")
    count = User.objects.all().count()
    print (count)
    assert User.objects.count() == 1