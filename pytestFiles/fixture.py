from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


driver = None


@pytest.fixture(scope="module")
def init_driver():
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.google.co.in/")
    yield
    driver.quit()

@pytest.mark.usefixtures("init_driver")
def test_title():
    assert driver.title == "Google"


