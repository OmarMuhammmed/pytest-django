import pytest 
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from pytest_factoryboy import register
from factories import UserFactory, ProductFactory, CategoryFactory

register(UserFactory)
register(ProductFactory)
register(CategoryFactory)



@pytest.fixture(scope="function")  
def browser():
   
    driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
    yield driver  # pass the driver object to the test 
    
    driver.quit()