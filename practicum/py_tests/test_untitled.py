import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    time.sleep(1)
    driver.quit()


def test_shadow(browser):
    browser.get("https://erikdark.github.io/SHADOM-DOM-SELENIUM-QA/?name=df&email=EFE%40MAIL.RU")

    shadow_host = browser.find_element(By.ID, "shadow-host")
    shadow_root = browser.execute_script("return arguments[0].shadowRoot", shadow_host)

    shadow_host_two = shadow_root.find_element(By.ID, "shadow-host-two")
    shadow_root_two = browser.execute_script("return arguments[0].shadowRoot", shadow_host_two)

    form = shadow_root_two.find_element(By.ID, "complex-form")

    name_input = form.find_element(By.ID, "name")
    email_input = form.find_element(By.ID, "email")

    name_input.send_keys("Ivan")
    email_input.send_keys("ivan@ex.com")

    time.sleep(2)

    submit_button = form.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()
