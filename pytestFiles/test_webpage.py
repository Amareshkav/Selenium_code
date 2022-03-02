from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest


def test_insta():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.instagram.com/accounts/login/?hl=en")
    title = driver.title
    assert title == "Login • Instagram"


def test_rediff():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
    title = driver.title
    assert title == "Rediffmail"
