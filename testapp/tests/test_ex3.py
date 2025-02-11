import pytest 
from django.test import LiveServerTestCase  
from selenium import webdriver

class TestBrowser1(LiveServerTestCase):
    def test_example(self):
        driver = webdriver.Edge()
        driver.get(self.live_server_url)
        assert "Django" in driver.title
        driver.quit()