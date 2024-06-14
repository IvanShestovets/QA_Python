import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(3)
    driver.quit()

# browser = webdriver.Firefox()

def test_form(browser):
    browser.get("https://erikdark.github.io/dovod_repo_QA_form/")

    browser.find_element(By.ID, 'login').send_keys('admin123')
    browser.find_element(By.ID, 'password').send_keys('password123')
    browser.find_element(By.ID, 'database').send_keys('bd_dovod')
    browser.find_element(By.ID, 'host').send_keys('localhost')

    #  Продолжить
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = browser.switch_to.alert
    alert.accept()

    browser.find_element(By.ID, 'login').clear()
    browser.find_element(By.ID, 'password').clear()
    browser.find_element(By.ID, 'database').clear()
    browser.find_element(By.ID, 'host').clear()

    # форма регистрации
    browser.find_element(By.ID, 'login').send_keys(reversed('admin123'))
    browser.find_element(By.ID, 'password').send_keys(reversed('password123'))
    browser.find_element(By.ID, 'database').send_keys(reversed('bd_dovod'))
    browser.find_element(By.ID, 'host').send_keys(reversed('localhost'))

    #  Продолжить
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
