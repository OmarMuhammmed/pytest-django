import time 
import pytest
import os
from django.test import LiveServerTestCase
from selenium import webdriver

def take_screenshot(driver, name):
    time.sleep(10)
    os.makedirs(os.path.join (os.path.dirname(__file__), "screenshots"), exist_ok=True)
    driver.save_screenshot(os.path.join(os.path.dirname(__file__), "screenshots", name))



def test_example(live_server):
    driver = webdriver.Edge()
    driver.get("%s%s" % (live_server.url, "/admin/"))
    take_screenshot(driver, "admin.png")
    assert "Django" in driver.title
    driver.quit()


