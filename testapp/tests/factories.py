import factory
from faker import Faker
from testapp.models import Category, Product
from django.contrib.auth.models import User 

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    username = fake.name()
    password = fake.password()
    email = fake.email()    


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category
    name = fake.name()   

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product
        
    title = fake.name()
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = fake.slug()
    regular_price = fake.random_number()
    discount_price = fake.random_number()
    is_active = fake.boolean()
    created_at = fake.date_time()
    updated_at = fake.date_time()