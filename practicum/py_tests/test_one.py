import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def test_exection1():
    try:
        driver = webdriver.Chrome()
        driver.get('http://selenium1py.pythonanywhere.com/ru/')
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR,'button.btn')
            pytest.fail('Не должно быть кнопки')

    finally:
        driver.quit()


def test_exection2():
    try:
        driver = webdriver.Chrome()
        driver.get('http://selenium1py.pythonanywhere.com/ru/')
        with pytest.raises(NoSuchElementException):
            driver.find_element(By.CSS_SELECTOR,'no_such_button.btn')
            pytest.fail('Не должно быть кнопки')
   
    finally:
        driver.quit()
