import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit

@pytest.fixture
def login_driver(driver):
    driver.get('http://selenium1py.pythonanywhere.com/ru/')





