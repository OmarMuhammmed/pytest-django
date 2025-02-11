import time


def test_homepage_title(browser):
   
    browser.get("https://www.example.com")
    
    
    time.sleep(30)

    assert "Example" in browser.title