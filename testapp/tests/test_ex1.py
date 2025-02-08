import pytest 



# @pytest.mark.django_db
# def test_new_user(user_factory):
    
#     user = user_factory.build()
#     print(user.username)
    
#     assert True

def test_product(product_factory):
    product = product_factory.build()
    print(product.title)
    assert True