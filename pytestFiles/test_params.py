from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


# @pytest.fixture(params=["chrome", "firefox"], scope="class")
# def init_driver(request):
#     global web_driver
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(ChromeDriverManager().install())
#     if request.param == "firefox":
#         web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()


@pytest.mark.usefixtures("init_driver")
class Base:
    pass


class Test_Google(Base):
    def test_title(self):
        self.driver.get("https://www.google.co.in/")
        assert self.driver.title == "Google"
