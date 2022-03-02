from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="class")
def init_driver(request):

    ch_driver = webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver = ch_driver
#    driver.get("https://www.google.co.in/")
    yield
    ch_driver.quit()


@pytest.mark.usefixtures("init_driver")
class Base_Chrome:
    pass

class Test_chrome(Base_Chrome):

    def test_title(self):
        self.driver.get("https://www.google.co.in/")
        assert self.driver.title == "Google"
